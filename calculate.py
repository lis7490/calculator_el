import tkinter as tk
from tkinter import ttk, messagebox
import math


class CurrentCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор инженера проектировщика.v2.1")
        self.root.geometry("800x600")

        # Создание вкладок
        self.tab_control = ttk.Notebook(root)

        # Вкладка главного меню
        self.tab_main = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_main, text='Главное меню')

        # Вкладка однофазного тока
        self.tab_single_phase = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_single_phase, text='Однофазный ток')

        # Вкладка трехфазного тока
        self.tab_three_phase = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_three_phase, text='Трехфазный ток')

        # Общий косинус
        self.tab_cosinus = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_cosinus, text='Общий косинус')

        # Удельная расчетная электрическая нагрузка электроприемников квартир жилых зданий, кВт/квартиру на ГАЗЕ
        self.tab_ppg = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_ppg, text='Нагрузка квартир (ГАЗ)')

        # Удельная расчетная электрическая нагрузка электроприемников квартир жилых зданий, кВт/квартиру на ЭЛЕКТРИЧЕСТВЕ
        self.tab_ppe = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_ppe, text='Нагрузка квартир (ЭЛ)')

        # Удельная расчетная электрическая нагрузка электроприемников квартир жилых зданий, кВт/квартиру ПОВЫШЕННОЙ КОМФОРТНОСТИ
        self.tab_ppp = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_ppp, text='Нагрузка квартир (ПК)')

        self.tab_control.pack(expand=1, fill='both')

        self.setup_main_tab()
        self.setup_single_phase_tab()
        self.setup_three_phase_tab()
        self.setup_cosinus_tab()
        self.setup_ppg_tab()
        self.setup_ppe_tab()
        self.setup_ppp_tab()

    def setup_main_tab(self):
        """Настройка главной вкладки с кнопками"""
        label = tk.Label(self.tab_main, text="Выберите тип расчета:",
                         font=("Arial", 14))
        label.pack(pady=20)

        # Кнопка для однофазного тока
        btn_single = tk.Button(self.tab_main, text="Расчет однофазного тока",
                               command=self.show_single_phase,
                               font=("Arial", 12), width=25, height=2)
        btn_single.pack(pady=10)

        # Кнопка для трехфазного тока
        btn_three = tk.Button(self.tab_main, text="Расчет трехфазного тока",
                              command=self.show_three_phase,
                              font=("Arial", 12), width=25, height=2)
        btn_three.pack(pady=10)

        # Кнопка для косинуса
        btn_cos = tk.Button(self.tab_main, text="Расчет общего косинуса",
                            command=self.show_cosinus,
                            font=("Arial", 12), width=25, height=2)
        btn_cos.pack(pady=10)

         # Кнопка для Рр на ГАЗУ
        btn_ppg = tk.Button(self.tab_main, text="Расчет нагрузки\n квартир (ГАЗ)",
                            command=self.show_ppg,
                            font=("Arial", 12), width=25, height=2)
        btn_ppg.pack(pady=10)

        # Кнопка для Рр на ЭЛЕКТРИЧЕСТВЕ
        btn_ppe = tk.Button(self.tab_main, text="Расчет нагрузки\n квартир (ЭЛЕКТРИЧЕСТВО)",
                            command=self.show_ppg,
                            font=("Arial", 12), width=25, height=2)
        btn_ppe.pack(pady=10)

        # Кнопка для Рр повышенной комфортности
        btn_ppp = tk.Button(self.tab_main, text="Расчет нагрузки\n квартир (КОМФОРТ)",
                            command=self.show_ppp,
                            font=("Arial", 12), width=25, height=2)
        btn_ppp.pack(pady=10)

        # Информация о программе
        info_label = tk.Label(self.tab_main,
                              text="Помощь проектировщику электрику\n"
                                   "Разработчик: Ступников Дмитрий",
                              font=("Arial", 10), fg="black")
        info_label.pack(side=tk.BOTTOM, pady=10)

    def setup_single_phase_tab(self):
        """Настройка вкладки для однофазного тока"""
        # Заголовок
        title_label = tk.Label(self.tab_single_phase,
                               text="Расчет однофазного тока",
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Формула
        formula_label = tk.Label(self.tab_single_phase,
                                 text="Формула: I = P / (U × cos(φ))",
                                 font=("Arial", 12), fg="blue")
        formula_label.pack(pady=5)

        # Поля ввода
        input_frame = tk.Frame(self.tab_single_phase)
        input_frame.pack(pady=20)

        # Мощность
        tk.Label(input_frame, text="Мощность P (Вт):", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
        self.power_single = tk.Entry(input_frame, font=("Arial", 10), width=15)
        self.power_single.grid(row=0, column=1, pady=5, padx=10)
        tk.Label(input_frame, text="Вт").grid(row=0, column=2, sticky="w", pady=5)

        # Напряжение
        tk.Label(input_frame, text="Напряжение U (В):", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
        self.voltage_single = tk.Entry(input_frame, font=("Arial", 10), width=15)
        self.voltage_single.insert(0, "220")
        self.voltage_single.grid(row=1, column=1, pady=5, padx=10)
        tk.Label(input_frame, text="В").grid(row=1, column=2, sticky="w", pady=5)

        # Косинус фи
        tk.Label(input_frame, text="cos(φ):", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
        self.cos_phi_single = tk.Entry(input_frame, font=("Arial", 10), width=15)
        self.cos_phi_single.insert(0, "0.8")
        self.cos_phi_single.grid(row=2, column=1, pady=5, padx=10)

        # Фрейм для кнопок
        button_frame = tk.Frame(self.tab_single_phase)
        button_frame.pack(pady=10)

        # Кнопка расчета
        calc_btn = tk.Button(button_frame, text="Рассчитать ток",
                             command=self.calculate_single_phase,
                             font=("Arial", 12), bg="lightblue", width=15)
        calc_btn.grid(row=0, column=0, padx=10)

        # Кнопка сброса
        reset_btn = tk.Button(button_frame, text="Сброс",
                              command=self.reset_single_phase,
                              font=("Arial", 12), bg="lightcoral", width=15)
        reset_btn.grid(row=0, column=1, padx=10)

        # Поле результата
        self.result_single = tk.Label(self.tab_single_phase, text="Результат: ",
                                      font=("Arial", 12, "bold"), fg="green")
        self.result_single.pack(pady=10)

        # Кнопка возврата
        back_btn = tk.Button(self.tab_single_phase, text="Назад в меню",
                             command=self.show_main,
                             font=("Arial", 10))
        back_btn.pack(side=tk.BOTTOM, pady=10)

    def setup_three_phase_tab(self):
        """Настройка вкладки для трехфазного тока"""
        # Заголовок
        title_label = tk.Label(self.tab_three_phase,
                               text="Расчет трехфазного тока",
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Формула
        formula_label = tk.Label(self.tab_three_phase,
                                 text="Формула: I = P / (√3 × U × cos(φ))",
                                 font=("Arial", 12), fg="blue")
        formula_label.pack(pady=5)

        # Поля ввода
        input_frame = tk.Frame(self.tab_three_phase)
        input_frame.pack(pady=20)

        # Мощность
        tk.Label(input_frame, text="Мощность P (Вт):", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
        self.power_three = tk.Entry(input_frame, font=("Arial", 10), width=15)
        self.power_three.grid(row=0, column=1, pady=5, padx=10)
        tk.Label(input_frame, text="Вт").grid(row=0, column=2, sticky="w", pady=5)

        # Напряжение
        tk.Label(input_frame, text="Напряжение U (В):", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
        self.voltage_three = tk.Entry(input_frame, font=("Arial", 10), width=15)
        self.voltage_three.insert(0, "380")
        self.voltage_three.grid(row=1, column=1, pady=5, padx=10)
        tk.Label(input_frame, text="В").grid(row=1, column=2, sticky="w", pady=5)

        # Косинус фи
        tk.Label(input_frame, text="cos(φ):", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
        self.cos_phi_three = tk.Entry(input_frame, font=("Arial", 10), width=15)
        self.cos_phi_three.insert(0, "0.8")
        self.cos_phi_three.grid(row=2, column=1, pady=5, padx=10)

        # Фрейм для кнопок
        button_frame = tk.Frame(self.tab_three_phase)
        button_frame.pack(pady=10)

        # Кнопка расчета
        calc_btn = tk.Button(button_frame, text="Рассчитать ток",
                             command=self.calculate_three_phase,
                             font=("Arial", 12), bg="lightgreen", width=15)
        calc_btn.grid(row=0, column=0, padx=10)

        # Кнопка сброса
        reset_btn = tk.Button(button_frame, text="Сброс",
                              command=self.reset_three_phase,
                              font=("Arial", 12), bg="lightcoral", width=15)
        reset_btn.grid(row=0, column=1, padx=10)

        # Поле результата
        self.result_three = tk.Label(self.tab_three_phase, text="Результат: ",
                                     font=("Arial", 12, "bold"), fg="green")
        self.result_three.pack(pady=10)

        # Кнопка возврата
        back_btn = tk.Button(self.tab_three_phase, text="Назад в меню",
                             command=self.show_main,
                             font=("Arial", 10))
        back_btn.pack(side=tk.BOTTOM, pady=10)

    def setup_cosinus_tab(self):
        """Настройка вкладки для расчета общего косинуса"""
        # Заголовок
        title_label = tk.Label(self.tab_cosinus,
                               text="Расчет общего косинуса",
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Формула
        formula_label = tk.Label(self.tab_cosinus,
                                 text="Формула: cos(φ)общ = P∑ / √(P∑² + Q∑²)",
                                 font=("Arial", 12), fg="blue")
        formula_label.pack(pady=5)

        # Поля ввода
        input_frame = tk.Frame(self.tab_cosinus)
        input_frame.pack(pady=20)

        # Создаем 8 пар полей ввода
        self.power_entries = []
        self.cos_entries = []

        for i in range(8):
            row = i

            # Мощность
            tk.Label(input_frame, text=f"ЭП {i + 1} P(кВт):",
                     font=("Arial", 10)).grid(row=row, column=0, sticky="w", pady=2)

            power_entry = tk.Entry(input_frame, font=("Arial", 10), width=8)
            power_entry.insert(0, '0')
            power_entry.grid(row=row, column=1, pady=2, padx=5)
            self.power_entries.append(power_entry)

            # Косинус фи
            tk.Label(input_frame, text="cos(φ):", font=("Arial", 10)).grid(row=row, column=2, sticky="w", pady=2)

            cos_entry = tk.Entry(input_frame, font=("Arial", 10), width=8)
            cos_entry.insert(0, "0")
            cos_entry.grid(row=row, column=3, pady=2, padx=5)
            self.cos_entries.append(cos_entry)

        # Фрейм для кнопок
        button_frame = tk.Frame(self.tab_cosinus)
        button_frame.pack(pady=10)

        # Кнопка расчета
        calc_btn = tk.Button(button_frame, text="Рассчитать",
                             command=self.calculate_cosinus,
                             font=("Arial", 12), bg="lightgreen", width=15)
        calc_btn.grid(row=0, column=0, padx=5)

        # Кнопка сброса
        reset_btn = tk.Button(button_frame, text="Сброс",
                              command=self.reset_cosinus,
                              font=("Arial", 12), bg="lightcoral", width=15)
        reset_btn.grid(row=0, column=1, padx=5)

        # Поле результата
        self.result_cos = tk.Label(self.tab_cosinus, text="Результат: ",
                                   font=("Arial", 12, "bold"), fg="green")
        self.result_cos.pack(pady=10)

        # Кнопка возврата
        back_btn = tk.Button(self.tab_cosinus, text="Назад в меню",
                             command=self.show_main,
                             font=("Arial", 10))
        back_btn.pack(side=tk.BOTTOM, pady=10)

    def setup_ppg_tab(self):
        """Настройка вкладки для расчета нагрузки квартир на ГАЗЕ"""
        # Заголовок
        title_label = tk.Label(self.tab_ppg,
                               text="Расчет нагрузки квартир с плитами на ГАЗЕ",
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Ссылка на СП
        sp_label = tk.Label(self.tab_ppg,
                            text="СП 256.1325800.2016, таблица 7.1",
                            font=("Arial", 12), fg="green")
        sp_label.pack(pady=5)

        # Формула
        formula_label = tk.Label(self.tab_ppg,
                                 text="Формула: Pкв = Pкв.уд × n",
                                 font=("Arial", 12), fg="blue")
        formula_label.pack(pady=5)

        # Поля ввода
        input_frame = tk.Frame(self.tab_ppg)
        input_frame.pack(pady=10)

        # Количество квартир с плитами на газе
        tk.Label(input_frame, text="Количество квартир с плитами на природном газе, шт.", wraplength=150, font=("Arial", 10)).grid(row=0, column=0, pady=5, padx=20)
        self.pgaz = tk.Entry(input_frame, font=("Arial", 10), width=15)
        self.pgaz.grid(row=1, column=0, pady=5, padx=10)
        
        # Фрейм для кнопок
        button_frame = tk.Frame(self.tab_ppg)
        button_frame.pack(pady=10)

        # Кнопка расчета
        calc_btn = tk.Button(button_frame, text="Рассчитать мощность",
                             command=self.calculate_ppg,
                             font=("Arial", 12), bg="lightgreen", width=25)
        calc_btn.grid(row=0, column=0, pady=20)

        # Кнопка сброса
        reset_btn = tk.Button(button_frame, text="Сброс",
                              command=self.reset_ppg,
                              font=("Arial", 12), bg="lightcoral", width=15)
        reset_btn.grid(row=1, column=0)

        # Поле результата
        self.result_ppg = tk.Label(self.tab_ppg, text="Результат:",
                                   font=("Arial", 12, "bold"), fg="green")
        self.result_ppg.pack(pady=10)

        # Кнопка возврата
        back_btn = tk.Button(self.tab_ppg, text="Назад в меню",
                             command=self.show_main,
                             font=("Arial", 10))
        back_btn.pack(side=tk.BOTTOM, pady=10)

    def setup_ppe_tab(self):
        """Настройка вкладки для расчета нагрузки квартир на Электричестве"""
        # Заголовок
        title_label = tk.Label(self.tab_ppe,
                               text="Расчет нагрузки квартир с плитами на ЭЛЕКТРИЧЕСТВЕ",
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Ссылка на СП
        sp_label = tk.Label(self.tab_ppe,
                            text="СП 256.1325800.2016, таблица 7.1",
                            font=("Arial", 12), fg="green")
        sp_label.pack(pady=5)

        # Формула
        formula_label = tk.Label(self.tab_ppe,
                                 text="Формула: Pкв = Pкв.уд × n",
                                 font=("Arial", 12), fg="blue")
        formula_label.pack(pady=5)

        # Поля ввода
        input_frame = tk.Frame(self.tab_ppe)
        input_frame.pack(pady=10)

        # Количество квартир с плитами на электричестве
        tk.Label(input_frame, text="Количество квартир с электрическими плитами, шт.", wraplength=150,
                 font=("Arial", 10)).grid(row=0, column=0, pady=5, padx=20)
        self.pel = tk.Entry(input_frame, font=("Arial", 10), width=15)
        self.pel.grid(row=1, column=0, pady=5, padx=10)

        # Фрейм для кнопок
        button_frame = tk.Frame(self.tab_ppe)
        button_frame.pack(pady=10)

        # Кнопка расчета
        calc_btn = tk.Button(button_frame, text="Рассчитать мощность",
                             command=self.calculate_ppe,
                             font=("Arial", 12), bg="lightgreen", width=25)
        calc_btn.grid(row=0, column=0, pady=20)

        # Кнопка сброса
        reset_btn = tk.Button(button_frame, text="Сброс",
                              command=self.reset_ppe,
                              font=("Arial", 12), bg="lightcoral", width=15)
        reset_btn.grid(row=1, column=0)

        # Поле результата
        self.result_ppe = tk.Label(self.tab_ppe, text="Результат:",
                                   font=("Arial", 12, "bold"), fg="green")
        self.result_ppe.pack(pady=10)

        # Кнопка возврата
        back_btn = tk.Button(self.tab_ppe, text="Назад в меню",
                             command=self.show_main,
                             font=("Arial", 10))
        back_btn.pack(side=tk.BOTTOM, pady=10)

    def setup_ppp_tab(self):
        """Настройка вкладки для расчета нагрузки квартир ПОВЫШЕННОЙ КОМФОРТНОСТИ"""
        # Заголовок
        title_label = tk.Label(self.tab_ppp,
                               text="Расчет нагрузки квартир ПОВЫШЕННОЙ КОМФОРТНОСТИ",
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Ссылка на СП
        sp_label = tk.Label(self.tab_ppp,
                            text="СП 256.1325800.2016, таблица 7.2, 7.3",
                            font=("Arial", 12), fg="green")
        sp_label.pack(pady=5)

        # Формула
        formula_label = tk.Label(self.tab_ppp,
                                 text="Формула: Pp.кв = Pкв × n × Ko",
                                 font=("Arial", 12), fg="blue")
        formula_label.pack(pady=5)

        # Поля ввода
        input_frame = tk.Frame(self.tab_ppp)
        input_frame.pack(pady=10)

        # Заявленная мощность, кВт
        tk.Label(input_frame, text="Заявленная мощность, кВт", wraplength=200,
                 font=("Arial", 10)).grid(row=0, column=0, pady=5, padx=20)
        self.pu = tk.Entry(input_frame, font=("Arial", 10), width=15)
        self.pu.grid(row=1, column=0, pady=5, padx=10)

        # Количество квартир, шт.
        tk.Label(input_frame, text="Количество квартир повышенной комфортности, шт.", wraplength=200,
                 font=("Arial", 10)).grid(row=2, column=0, pady=5, padx=20)
        self.pn = tk.Entry(input_frame, font=("Arial", 10), width=15)
        self.pn.grid(row=3, column=0, pady=5, padx=5)


        # Фрейм для кнопок
        button_frame = tk.Frame(self.tab_ppp)
        button_frame.pack(pady=5)

        # Кнопка расчета
        calc_btn = tk.Button(button_frame, text="Рассчитать мощность",
                             command=self.calculate_ppp,
                             font=("Arial", 12), bg="lightgreen", width=25)
        calc_btn.grid(row=0, column=0, pady=20)

        # Кнопка сброса
        reset_btn = tk.Button(button_frame, text="Сброс",
                              command=self.reset_ppp,
                              font=("Arial", 12), bg="lightcoral", width=15)
        reset_btn.grid(row=1, column=0)

        # Поле результата
        self.result_ppp = tk.Label(self.tab_ppp, text="Результат:",
                                   font=("Arial", 12, "bold"), fg="green")
        self.result_ppp.pack(pady=10)

        # Кнопка возврата
        back_btn = tk.Button(self.tab_ppp, text="Назад в меню",
                             command=self.show_main,
                             font=("Arial", 10))
        back_btn.pack(side=tk.BOTTOM, pady=10)

    def show_main(self):
        """Показать главную вкладку"""
        self.tab_control.select(0)

    def show_single_phase(self):
        """Показать вкладку однофазного тока"""
        self.tab_control.select(1)

    def show_three_phase(self):
        """Показать вкладку трехфазного тока"""
        self.tab_control.select(2)

    def show_cosinus(self):
        """Показать вкладку косинуса"""
        self.tab_control.select(3)
    
    def show_ppg(self):
        """Показать вкладку расчета нагрузки квартир на ГАЗЕ"""
        self.tab_control.select(4)

    def show_ppe(self):
        """Показать вкладку расчета нагрузки квартир на ЭЛЕКТРИЧЕСТВЕ"""
        self.tab_control.select(5)

    def show_ppp(self):
        """Показать вкладку расчета нагрузки квартир ПП"""
        self.tab_control.select(6)

    def calculate_single_phase(self):
        """Расчет однофазного тока"""
        try:
            P = float(self.power_single.get())
            U = float(self.voltage_single.get())
            cos_phi = float(self.cos_phi_single.get())

            if P <= 0 or U <= 0 or cos_phi <= 0 or cos_phi > 1:
                raise ValueError("Некорректные значения")

            I = P / (U * cos_phi)
            self.result_single.config(text=f"Результат: I = {I:.2f} А")

        except ValueError as e:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения")

    def calculate_three_phase(self):
        """Расчет трехфазного тока"""
        try:
            P = float(self.power_three.get())
            U = float(self.voltage_three.get())
            cos_phi = float(self.cos_phi_three.get())

            if P <= 0 or U <= 0 or cos_phi <= 0 or cos_phi > 1:
                raise ValueError("Некорректные значения")

            I = P / (1.732 * U * cos_phi)  # 1.732 = √3
            self.result_three.config(text=f"Результат: I = {I:.2f} А")

        except ValueError as e:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения")

    def calculate_cosinus(self):
        """Расчет общего косинуса"""
        try:
            P_total = 0
            Q_total = 0

            # Суммируем мощности всех электроприемников
            for i in range(8):
                P = float(self.power_entries[i].get())
                cos_phi = float(self.cos_entries[i].get())

                if cos_phi < 0 or cos_phi > 1:
                    raise ValueError("Косинус должен быть от 0 до 1")

                # Вычисляем реактивную мощность
                if cos_phi > 0:
                    Q = P * math.tan(math.acos(cos_phi))
                else:
                    Q = 0

                P_total += P
                Q_total += Q

            # Вычисляем общий косинус
            if P_total > 0:
                S_total = math.sqrt(P_total ** 2 + Q_total ** 2)  # Полная мощность
                cos_total = P_total / S_total

                self.result_cos.config(text=f"cos(φ)общ = {cos_total:.3f}\n"
                                            f"P∑ = {P_total:.1f} кВт\n"
                                            f"Q∑ = {Q_total:.1f} кВАр")
            else:
                self.result_cos.config(text="Введите мощности электроприемников")

        except ValueError:
            messagebox.showerror("Ошибка", "Проверьте правильность введенных данных")

    def calculate_ppg(self):
        """Расчет нагрузок квартир на ГАЗЕ"""
       
        one_five = 4.5
        six = 2.8
        nine = 2.3
        twelw = 2
        fifteen = 1.8
        eighteen = 1.65
        twentyfour = 1.4
        forty = 1.2
        sixty = 1.05
        onehundred = 0.85
        twohundred = 0.77
        fourhundred = 0.71
        sixhundred = 0.69
        onethousand = 0.67
        try:
            Ppg = 0
            ng = float(self.pgaz.get())

            if ng < 0 or ng > 1000:
                raise ValueError("Некорректные значения")

            if ng in range(1, 6):
                Ppg = one_five*ng
            elif ng == 6:
                Ppg = six*ng
            elif ng > 6 and ng < 9:
                Ppg = ((nine-six)/(9-6)*(ng-6)+six)*ng
            elif ng == 9:
                Ppg = nine*ng
            elif ng > 9 and ng < 12:
                Ppg = ((twelw-nine)/(12-9)*(ng-9)+nine)*ng
            elif ng == 12:
                Ppg = twelw*ng
            elif ng > 12 and ng < 15:
                Ppg = ((fifteen-twelw)/(15-12)*(ng-12)+twelw)*ng
            elif ng == 15:
                Ppg = fifteen*ng
            elif ng > 15 and ng < 18:
                Ppg = ((eighteen-fifteen)/(18-15)*(ng-15)+fifteen)*ng
            elif ng == 18:
                Ppg = eighteen*ng
            elif ng > 18 and ng < 24:
                Ppg = ((twentyfour-eighteen)/(24-18)*(ng-18)+eighteen)*ng
            elif ng == 24:
                Ppg = twentyfour*ng
            elif ng > 24 and ng < 40:
                Ppg = ((forty-twentyfour)/(40-24)*(ng-24)+twentyfour)*ng
            elif ng == 40 :
                Ppg = forty*ng
            elif ng > 40 and ng < 60:
                Ppg = ((sixty-forty)/(60-40)*(ng-40)+forty)*ng
            elif ng == 60:
                Ppg = sixty*ng
            elif ng > 60 and ng < 100:
                Ppg = ((onehundred-sixty)/(100-60)*(ng-60)+sixty)*ng
            elif ng == 100:
                Ppg = onehundred*ng
            elif ng > 100 and ng < 200:
                Ppg = ((twohundred-onehundred)/(200-100)*(ng-100)+onehundred)*ng
            elif ng == 200:
                Ppg = twohundred*ng
            elif ng > 200 and ng < 400:
                Ppg = ((fourhundred-twohundred)/(400-200)*(ng-200)+twohundred)*ng
            elif ng == 400:
                Ppg = fourhundred*ng
            elif ng > 400 and ng < 600:
                Ppg = ((sixhundred-fourhundred)/(600-400)*(ng-400)+fourhundred)*ng
            elif ng == 600:
                Ppg = sixhundred*ng
            elif ng > 600 and ng < 1000:
                Ppg = ((onethousand-sixhundred)/(1000-600)*(ng-600)+sixhundred)*ng
            elif ng == 1000:
                Ppg = onethousand*ng

            self.result_ppg.config(text=f"Результат:\n\nPкв.уд = {Ppg / ng:.3f} кВт/кв.\n\nPкв = {Ppg:.2f} кВт")

        except ValueError as e:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения")

    def calculate_ppe(self):
        """Расчет нагрузок квартир на ""ЭЛЕКТРИЧЕСТВЕ"""""

        one_five = 10
        sixe = 5.1
        ninee = 3.8
        twelwe = 3.2
        fifteene = 2.8
        eighteene = 2.6
        twentyfoure = 2.2
        fortye = 1.95
        sixtye = 1.7
        onehundrede = 1.5
        twohundrede = 1.36
        fourhundrede = 1.27
        sixhundrede = 1.23
        onethousande = 1.19
        try:
            Ppe = 0
            ne = float(self.pel.get())

            if ne < 0 or ne > 1000:
                raise ValueError("Некорректные значения")

            if ne in range(1, 6):
                Ppe = one_five * ne
            elif ne == 6:
                Ppe = sixe * ne
            elif ne > 6 and ne < 9:
                Ppe = ((ninee - sixe) / (9 - 6) * (ne - 6) + sixe) * ne
            elif ne == 9:
                Ppe = ninee * ne
            elif ne > 9 and ne < 12:
                Ppe = ((twelwe - ninee) / (12 - 9) * (ne - 9) + ninee) * ne
            elif ne == 12:
                Ppe = twelwe * ne
            elif ne > 12 and ne < 15:
                Ppe = ((fifteene - twelwe) / (15 - 12) * (ne - 12) + twelwe) * ne
            elif ne == 15:
                Ppe = fifteene * ne
            elif ne > 15 and ne < 18:
                Ppe = ((eighteene - fifteene) / (18 - 15) * (ne - 15) + fifteene) * ne
            elif ne == 18:
                Ppe = eighteene * ne
            elif ne > 18 and ne < 24:
                Ppe = ((twentyfoure - eighteene) / (24 - 18) * (ne - 18) + eighteene) * ne
            elif ne == 24:
                Ppe = twentyfoure * ne
            elif ne > 24 and ne < 40:
                Ppe = ((fortye - twentyfoure) / (40 - 24) * (ne - 24) + twentyfoure) * ne
            elif ne == 40:
                Ppe = fortye * ne
            elif ne > 40 and ne < 60:
                Ppe = ((sixtye - fortye) / (60 - 40) * (ne - 40) + fortye) * ne
            elif ne == 60:
                Ppe = sixtye * ne
            elif ne > 60 and ne < 100:
                Ppe = ((onehundrede - sixtye) / (100 - 60) * (ne - 60) + sixtye) * ne
            elif ne == 100:
                Ppe = onehundrede * ne
            elif ne > 100 and ne < 200:
                Ppe = ((twohundrede - onehundrede) / (200 - 100) * (ne - 100) + onehundrede) * ne
            elif ne == 200:
                Ppe = twohundrede * ne
            elif ne > 200 and ne < 400:
                Ppe = ((fourhundrede - twohundrede) / (400 - 200) * (ne - 200) + twohundrede) * ne
            elif ne == 400:
                Ppe = fourhundrede * ne
            elif ne > 400 and ne < 600:
                Ppe = ((sixhundrede - fourhundrede) / (600 - 400) * (ne - 400) + fourhundrede) * ne
            elif ne == 600:
                Ppe = sixhundrede * ne
            elif ne > 600 and ne < 1000:
                Ppe = ((onethousande - sixhundrede) / (1000 - 600) * (ne - 600) + sixhundrede) * ne
            elif ne == 1000:
                Ppe = onethousande * ne

            self.result_ppe.config(text=f"Результат:\n\nPкв.уд = {Ppe / ne:.3f} кВт/кв.\n\nPкв = {Ppe:.2f} кВт")

        except ValueError as e:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения")

    def calculate_ppp(self):
        """Расчет нагрузок квартир ПК"""

        one_14 = 0.8
        twentyp = 0.65
        thirtyp = 0.6
        fortyp = 0.55
        fiftyp = 0.5
        sixtyp = 0.48
        seventyp = 0.45

        one_5k = 1
        sixk = 0.51
        ninek = 0.38
        twelvek = 0.32
        fifteenk = 0.29
        eighteenk = 0.26
        twentyfourk = 0.24
        fortyk = 0.2
        sixtyk = 0.18
        hundredk = 0.16
        twohundredk = 0.14
        fourhundredk = 0.13
        sixhundredk = 0.11

        try:
            Ppu = 0
            Ppk = 0
            Ko = 0
            nu = float(self.pu.get())
            nk = float(self.pn.get())

            if nu < 0 or nk < 0 or Ko < 0:
                raise ValueError("Некорректные значения")

            if nu in range(1, 15):
                Ppu = one_14 * nu
            elif nu in range(15, 20):
                Ppu = ((twentyp - one_14) / (20 - 14) * (nu - 14) + one_14) * nu
            elif nu in range(20, 30):
                Ppu = ((thirtyp - twentyp) / (30 - 20) * (nu - 20) + twentyp) * nu
            elif nu in range(30, 40):
                Ppu = ((fortyp - thirtyp) / (40 - 30) * (nu - 30) + thirtyp) * nu
            elif nu in range(40, 50):
                Ppu = ((fiftyp - fortyp) / (50 - 40) * (nu - 40) + fortyp) * nu
            elif nu in range(50, 60):
                Ppu = ((sixtyp - fiftyp) / (60 - 50) * (nu - 50) + fiftyp) * nu
            elif nu in range(60, 70):
                Ppu = ((seventyp - sixtyp) / (70 - 60) * (nu - 60) + sixtyp) * nu
            else:
                Ppu = seventyp * nu

            if nk in range(1, 6):
                Ppk = Ppu * nk * one_5k
            elif nk in range(6, 9):
                Ppk = ((ninek - sixk) / (9 - 6) * (nk - 6) + sixk) * nk * Ppu
            elif nk in range(9, 12):
                Ppk = ((twelvek - ninek) / (12 - 9) * (nk - 9) + ninek) * nk * Ppu
            elif nk in range(12, 15):
                Ppk = ((fifteenk - twelvek) / (15 - 12) * (nk - 12) + twelvek) * nk * Ppu
            elif nk in range(15, 18):
                Ppk = ((eighteenk - fifteenk) / (18 - 15) * (nk - 15) + fifteenk) * nk * Ppu
            elif nk in range(18, 24):
                Ppk = ((twentyfourk - eighteenk) / (24 - 18) * (nk - 18) + eighteenk) * nk * Ppu
            elif nk in range(24, 40):
                Ppk = ((fortyk - twentyfourk) / (40 - 24) * (nk - 24) + twentyfourk) * nk * Ppu
            elif nk in range(40, 60):
                Ppk = ((sixtyk - fortyk) / (60 - 40) * (nk - 40) + fortyk) * nk * Ppu
            elif nk in range(60, 100):
                Ppk = ((hundredk - sixtyk) / (100 - 60) * (nk - 60) + sixtyk) * nk * Ppu
            elif nk in range(100, 200):
                Ppk = ((twohundredk - hundredk) / (200 - 100) * (nk - 100) + hundredk) * nk * Ppu
            elif nk in range(200, 400):
                Ppk = ((fourhundredk - twohundredk) / (400 - 200) * (nk - 200) + twohundredk) * nk * Ppu
            elif nk in range(400, 600):
                Ppk = ((sixhundredk - fourhundredk) / (600 - 400) * (nk - 400) + fourhundredk) * nk * Ppu
            else:
                Ppk = Ppu * nk * sixhundredk
            if nu > 0 and nk > 0:
                self.result_ppp.config(text=f"Kc = {Ppu/nu:.3f}\n\nKo = {Ppk/(nk*Ppu):.3f}\n\nPp.кв = {Ppk:.2f} кВт")
            else:
                self.result_ppp.config(
                    text=f"Введите исходные данные")
        except ValueError as e:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения")

    def reset_single_phase(self):
        """Сброс данных однофазного расчета"""
        self.power_single.delete(0, tk.END)
        self.voltage_single.delete(0, tk.END)
        self.voltage_single.insert(0, "220")
        self.cos_phi_single.delete(0, tk.END)
        self.cos_phi_single.insert(0, "0.8")
        self.result_single.config(text="Результат: ")

    def reset_three_phase(self):
        """Сброс данных трехфазного расчета"""
        self.power_three.delete(0, tk.END)
        self.voltage_three.delete(0, tk.END)
        self.voltage_three.insert(0, "380")
        self.cos_phi_three.delete(0, tk.END)
        self.cos_phi_three.insert(0, "0.8")
        self.result_three.config(text="Результат: ")

    def reset_cosinus(self):
        """Сброс данных расчета общего косинуса"""
        for entry in self.power_entries + self.cos_entries:
            entry.delete(0, tk.END)
            entry.insert(0, "0")

        self.result_cos.config(text="Результат: ")

    def reset_ppg(self):
        """Сброс данных расчета нагрузок квартир"""
        self.pgaz.delete(0, tk.END)
        self.result_ppg.config(text="Результат: ")

    def reset_ppe(self):
        """Сброс данных расчета нагрузок квартир"""
        self.pel.delete(0, tk.END)
        self.result_ppe.config(text="Результат: ")

    def reset_ppp(self):
        """Сброс данных расчета нагрузок квартир ПК"""
        self.pu.delete(0, tk.END)
        self.pn.delete(0, tk.END)
        self.result_ppp.config(text="Результат: ")



def main():
    root = tk.Tk()
    app = CurrentCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()