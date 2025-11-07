import tkinter as tk
from tkinter import ttk, messagebox
import math


class CurrentCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор инженера проектировщика")
        self.root.geometry("600x500")

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

        # Удельная расчетная электрическая нагрузка электроприемников квартир жилых зданий, кВт/квартиру
        self.tab_pp = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_pp, text='Нагрузка квартир')

        self.tab_control.pack(expand=1, fill='both')

        self.setup_main_tab()
        self.setup_single_phase_tab()
        self.setup_three_phase_tab()
        self.setup_cosinus_tab()
        self.setup_pp_tab()

    def setup_main_tab(self):
        """Настройка главной вкладки с кнопками"""
        label = tk.Label(self.tab_main, text="Выберите тип расчета:",
                         font=("Arial", 14))
        label.pack(pady=20)

        # Кнопка для однофазного тока
        btn_single = tk.Button(self.tab_main, text="Расчет однофазного тока",
                               command=self.show_single_phase,
                               font=("Arial", 12), width=20, height=2)
        btn_single.pack(pady=10)

        # Кнопка для трехфазного тока
        btn_three = tk.Button(self.tab_main, text="Расчет трехфазного тока",
                              command=self.show_three_phase,
                              font=("Arial", 12), width=20, height=2)
        btn_three.pack(pady=10)

        # Кнопка для косинуса
        btn_cos = tk.Button(self.tab_main, text="Расчет общего косинуса",
                            command=self.show_cosinus,
                            font=("Arial", 12), width=20, height=2)
        btn_cos.pack(pady=10)

         # Кнопка для косинуса
        btn_pp = tk.Button(self.tab_main, text="Расчет нагрузки квартир",
                            command=self.show_pp,
                            font=("Arial", 12), width=20, height=2)
        btn_pp.pack(pady=10)

        # Кнопка сброса всех данных
        reset_btn = tk.Button(self.tab_main, text="Сброс всех данных",
                              command=self.reset_all_data,
                              font=("Arial", 10), bg="lightcoral")
        reset_btn.pack(pady=20)

        # Информация о программе
        info_label = tk.Label(self.tab_main,
                              text="Помощь проектировщику электрику\n"
                                   "Ступников Дмитрий",
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

    def setup_pp_tab(self):
        """Настройка вкладки для расчета нагрузки квартир"""
        # Заголовок
        title_label = tk.Label(self.tab_pp,
                               text="Расчет нагрузки картир",
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Ссылка на СП
        sp_label = tk.Label(self.tab_pp,
                               text="СП 256.1325800.2016, таблица 7.1",
                               font=("Arial", 12), fg="green")
        sp_label.pack(pady=5)

        # Формула
        formula_label = tk.Label(self.tab_pp,
                                 text="Формула: Pкв = Pкв.уд × n",
                                 font=("Arial", 12), fg="blue")
        formula_label.pack(pady=5)

        # Поля ввода
        input_frame = tk.Frame(self.tab_pp)
        input_frame.pack(pady=20)

        # Количество квартир с плитами на газе
        tk.Label(input_frame, text="Количество квартир с плитами на природном газе, шт.", wraplength=150, font=("Arial", 10)).grid(row=0, column=0, pady=5, padx=20)
        self.pgaz = tk.Entry(input_frame, font=("Arial", 10), width=15)
        self.pgaz.insert(0, "0")
        self.pgaz.grid(row=1, column=0, pady=5, padx=10)
        

        # Количество квартир с электрическими плитами
        tk.Label(input_frame, text="Количество квартир с электрическими плитами, шт", wraplength=150, font=("Arial", 10)).grid(row=0, column=1, pady=5, padx=20)
        self.pel = tk.Entry(input_frame, font=("Arial", 10), width=15)
        self.pel.insert(0, "0")
        self.pel.grid(row=1, column=1, pady=5, padx=10)
        

       
        # Фрейм для кнопок
        button_frame = tk.Frame(self.tab_pp)
        button_frame.pack(pady=10)

        # Кнопка расчета
        calc_btn = tk.Button(button_frame, text="Рассчитать мощность",
                             command=self.calculate_pp,
                             font=("Arial", 12), bg="lightgreen", width=25)
        calc_btn.grid(row=0, column=0, pady=20)

        # Кнопка сброса
        reset_btn = tk.Button(button_frame, text="Сброс",
                              command=self.reset_pp,
                              font=("Arial", 12), bg="lightcoral", width=15)
        reset_btn.grid(row=1, column=0)

        # Поле результата
        self.result_ppg = tk.Label(self.tab_pp, text="Результат на газе: ",
                                     font=("Arial", 12, "bold"), fg="green")
        self.result_ppg.pack(pady=10)

        self.result_ppe = tk.Label(self.tab_pp, text="Результат на электричестве: ",
                                     font=("Arial", 12, "bold"), fg="green")
        self.result_ppe.pack(pady=10)

        # Кнопка возврата
        back_btn = tk.Button(self.tab_pp, text="Назад в меню",
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
    
    def show_pp(self):
        """Показать вкладку расчета нагрузки квартир"""
        self.tab_control.select(4)

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

    def calculate_pp(self):
        """Расчет нагрузок квартир"""
       
        one_five = 10
        six = 2.8
        sixe = 5.1
        nine = 2.3
        ninee = 3.8
        twelw = 2
        twelwe = 3.2
        fifteen = 1.8
        fifteene = 2.8
        eighteen = 1.65
        eighteene = 2.6
        twentyfour = 1.4
        twentyfoure = 2.2
        forty = 1.2
        fortye = 1.95
        sixty = 1.05
        sixtye = 1.7
        onehundred = 0.85
        onehundrede = 1.5
        twohundred = 0.77
        twohundrede = 1.36
        fourhundred = 0.71
        fourhundrede = 1.27
        sixhundred = 0.69
        sixhundrede = 1.23
        onethousand = 0.67
        onethousande = 1.19
        try:
            Ppg = 0
            Ppe = 0
            Pkvg = 0
            ng = float(self.pgaz.get())
            ne = float(self.pel.get())
            
            if ng < 0 or ng > 1000 or ne < 0 or ne > 1000:
                raise ValueError("Некорректные значения")
            if ng in range(1, 6) or ne in range(1, 6):
                Ppg = one_five*ng
                Ppe = one_five*ne
            elif ng == 6 or ne == 6:
                Ppg = six*ng
                Ppe = sixe*ne
            elif ng > 6 and ng < 9 or ne > 6 and ne < 9:
                Ppg = ((nine-six)/(9-6)*(ng-6)+six)*ng
                Ppe = ((ninee-sixe)/(9-6)*(ne-6)+sixe)*ne
            elif ng == 9 or ne == 9:
                Ppg = nine*ng
                Ppe = ninee*ne
            elif ng > 9 and ng < 12 or ne > 9 and ne < 12:
                Ppg = ((twelw-nine)/(12-9)*(ng-9)+nine)*ng
                Ppe = ((twelwe-ninee)/(12-9)*(ne-9)+ninee)*ne
            elif ng == 12 or ne == 12:
                Ppg = twelw*ng
                Ppe = twelwe*ne
            elif ng > 12 and ng < 15 or ne > 12 and ne < 15:
                Ppg = ((fifteen-twelw)/(15-12)*(ng-12)+twelw)*ng
                Ppe = ((fifteene-twelwe)/(15-12)*(ne-12)+twelwe)*ne
            elif ng == 15 or ne == 15:
                Ppg = fifteen*ng
                Ppe = fifteene*ne
            elif ng > 15 and ng < 18 or ne > 15 and ne < 18:
                Ppg = ((eighteen-fifteen)/(18-15)*(ng-15)+fifteen)*ng
                Ppe = ((eighteene-fifteene)/(18-15)*(ne-15)+fifteene)*ne
            elif ng == 18 or ne == 18:
                Ppg = eighteen*ng
                Ppe = eighteene*ne
            elif ng > 18 and ng < 24 or ne > 18 and ne < 24:
                Ppg = ((twentyfour-eighteen)/(24-18)*(ng-18)+eighteen)*ng
                Ppe = ((twentyfoure-eighteene)/(24-18)*(ne-18)+eighteene)*ne
               

            
            
            

            self.result_ppg.config(text=f"Результат на газе: Pкв.уд = {Ppg/ng:.3f} кВт/кв., Pкв = {Ppg:.3f} кВт")
            self.result_ppe.config(text=f"Результат на электричестве: Pкв.уд = {Ppe/ne:.3f} кВт/кв., Pкв = {Ppe:.3f} кВт")
            

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

    def reset_pp(self):
        """Сброс данных расчета нагрузок квартир"""
        self.pgaz.delete(0, tk.END)
        self.pgaz.insert(0, "0")
        self.pel.delete(0, tk.END)
        self.pel.insert(0, "0")
        self.result_ppg.config(text="Результат на газе: ")
        self.result_ppe.config(text="Результат на электричестве: ")
        

    def reset_all_data(self):
        """Сброс всех данных во всех вкладках"""
        self.reset_single_phase()
        self.reset_three_phase()
        self.reset_cosinus()
        messagebox.showinfo("Сброс", "Все данные во всех вкладках сброшены")


def main():
    root = tk.Tk()
    app = CurrentCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()