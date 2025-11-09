import tkinter as tk
from tkinter import ttk, messagebox
import math


class CurrentCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор инженера проектировщика")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c3e50')

        # Устанавливаем иконку приложения (замените на путь к вашей иконке)
        try:
            self.root.iconbitmap("calculator_icon.ico")
        except:
            pass

        self.setup_custom_style()

        # Создание вкладок
        self.tab_control = ttk.Notebook(root, style="Modern.TNotebook")

        # Создаем вкладки с tk.Frame вместо ttk.Frame
        tabs = [
            ('Главное меню', self.setup_main_tab),
            ('Однофазный ток', self.setup_single_phase_tab),
            ('Трехфазный ток', self.setup_three_phase_tab),
            ('Общий косинус', self.setup_cosinus_tab),
            ('Нагрузка квартир (ГАЗ)', self.setup_ppg_tab),
            ('Нагрузка квартир (ЭЛ)', self.setup_ppe_tab)
        ]

        self.tabs = {}
        for text, setup_method in tabs:
            tab = tk.Frame(self.tab_control, bg='#2c3e50')  # Используем tk.Frame
            self.tab_control.add(tab, text=text)
            self.tabs[text] = tab
            setup_method()

        self.tab_control.pack(expand=1, fill='both', padx=10, pady=10)

    def setup_custom_style(self):
        """Настройка современного стиля"""
        style = ttk.Style()

        # Современная тема
        style.theme_use('clam')

        # Стиль для Notebook
        style.configure("Modern.TNotebook",
                        background='#34495e',
                        borderwidth=0,
                        tabmargins=[0, 0, 0, 0])

        style.configure("Modern.TNotebook.Tab",
                        background='#34495e',
                        foreground='#ecf0f1',
                        padding=[20, 10],
                        font=('Arial', 10, 'bold'),
                        borderwidth=0,
                        focuscolor='none')

        style.map("Modern.TNotebook.Tab",
                  background=[('selected', '#e74c3c'),
                              ('active', '#c0392b')],
                  foreground=[('selected', 'white'),
                              ('active', 'white')])

        # Стиль для кнопок
        style.configure("Modern.TButton",
                        background='#3498db',
                        foreground='white',
                        font=('Arial', 10, 'bold'),
                        padding=[15, 10],
                        borderwidth=0,
                        focuscolor='none')

        style.map("Modern.TButton",
                  background=[('active', '#2980b9'),
                              ('pressed', '#21618c')])

    def create_modern_button(self, parent, text, command, **kwargs):
        """Создание современной кнопки"""
        bg = kwargs.get('bg', '#3498db')
        fg = kwargs.get('fg', 'white')
        width = kwargs.get('width', 20)
        height = kwargs.get('height', 2)
        font = kwargs.get('font', ('Arial', 11, 'bold'))

        btn = tk.Button(parent, text=text, command=command,
                        bg=bg, fg=fg, font=font,
                        width=width, height=height,
                        relief='flat', bd=0,
                        cursor='hand2')
        return btn

    def create_section_title(self, parent, text):
        """Создание заголовка раздела"""
        label = tk.Label(parent, text=text,
                         font=('Arial', 16, 'bold'),
                         bg='#2c3e50', fg='#ecf0f1',
                         pady=10)
        return label

    def create_formula_label(self, parent, text):
        """Создание метки с формулой"""
        label = tk.Label(parent, text=text,
                         font=('Arial', 12, 'italic'),
                         bg='#2c3e50', fg='#3498db',
                         pady=5)
        return label

    def setup_main_tab(self):
        """Настройка главной вкладки с кнопками"""
        tab = self.tabs['Главное меню']

        # Заголовок
        title = self.create_section_title(tab, "Калькулятор инженера-проектировщика")
        title.pack(pady=20)

        subtitle = tk.Label(tab, text="Выберите тип расчета:",
                            font=('Arial', 14),
                            bg='#2c3e50', fg='#bdc3c7')
        subtitle.pack(pady=10)

        # Фрейм для кнопок
        button_frame = tk.Frame(tab, bg='#2c3e50')
        button_frame.pack(pady=20)

        # Кнопки расчетов
        buttons = [
            ("⚡ Расчет однофазного тока", self.show_single_phase, '#e74c3c'),
            ("⚡ Расчет трехфазного тока", self.show_three_phase, '#e67e22'),
            ("📊 Расчет общего косинуса", self.show_cosinus, '#f39c12'),
            ("🏠 Расчет нагрузки квартир (ГАЗ)", self.show_ppg, '#27ae60'),
            ("🏠 Расчет нагрузки квартир (ЭЛ)", self.show_ppe, '#2980b9')
        ]

        for text, command, color in buttons:
            btn = self.create_modern_button(button_frame, text, command, bg=color, width=30)
            btn.pack(pady=8)

        # Информация о программе
        info_frame = tk.Frame(tab, bg='#2c3e50')
        info_frame.pack(side=tk.BOTTOM, pady=20)

        info_label = tk.Label(info_frame,
                              text="Помощь проектировщику электрику\n"
                                   "Ступников Дмитрий",
                              font=('Arial', 10),
                              bg='#2c3e50', fg='#7f8c8d')
        info_label.pack()

    def setup_single_phase_tab(self):
        """Настройка вкладки для однофазного тока"""
        tab = self.tabs['Однофазный ток']

        # Заголовок
        title = self.create_section_title(tab, "Расчет однофазного тока")
        title.pack(pady=10)

        # Формула
        formula = self.create_formula_label(tab, "Формула: I = P / (U × cos(φ))")
        formula.pack()

        # Основной контейнер
        main_frame = tk.Frame(tab, bg='#34495e', relief='ridge', bd=2)
        main_frame.pack(pady=20, padx=30, fill='both', expand=True)

        # Поля ввода
        input_frame = tk.Frame(main_frame, bg='#34495e')
        input_frame.pack(pady=30)

        self.setup_input_field(input_frame, "Мощность P (Вт):", "power_single", 0)
        self.setup_input_field(input_frame, "Напряжение U (В):", "voltage_single", 1, "220")
        self.setup_input_field(input_frame, "cos(φ):", "cos_phi_single", 2, "0.8")

        # Фрейм для кнопок
        button_frame = tk.Frame(main_frame, bg='#34495e')
        button_frame.pack(pady=20)

        # Кнопка расчета
        calc_btn = self.create_modern_button(button_frame, "🧮 Рассчитать ток",
                                             self.calculate_single_phase, bg='#27ae60')
        calc_btn.grid(row=0, column=0, padx=10)

        # Кнопка сброса
        reset_btn = self.create_modern_button(button_frame, "🔄 Сброс",
                                              self.reset_single_phase, bg='#e74c3c')
        reset_btn.grid(row=0, column=1, padx=10)

        # Поле результата
        self.result_single = tk.Label(main_frame, text="Результат: ",
                                      font=('Arial', 12, 'bold'),
                                      bg='#34495e', fg='#2ecc71')
        self.result_single.pack(pady=20)

        # Кнопка возврата
        back_btn = self.create_modern_button(tab, "← Назад в меню",
                                             self.show_main, bg='#7f8c8d', width=15)
        back_btn.pack(side=tk.BOTTOM, pady=10)

    def setup_input_field(self, parent, label_text, attr_name, row, default=""):
        """Создание поля ввода с меткой"""
        tk.Label(parent, text=label_text, font=('Arial', 10),
                 bg='#34495e', fg='#ecf0f1').grid(row=row, column=0, sticky="w", pady=8, padx=10)

        entry = tk.Entry(parent, font=('Arial', 10), width=15,
                         bg='#ecf0f1', fg='#2c3e50', relief='flat',
                         insertbackground='#3498db')
        if default:
            entry.insert(0, default)
        entry.grid(row=row, column=1, pady=8, padx=10)
        setattr(self, attr_name, entry)

        return entry

    def setup_three_phase_tab(self):
        """Настройка вкладки для трехфазного тока"""
        tab = self.tabs['Трехфазный ток']

        # Заголовок
        title = self.create_section_title(tab, "Расчет трехфазного тока")
        title.pack(pady=10)

        # Формула
        formula = self.create_formula_label(tab, "Формула: I = P / (√3 × U × cos(φ))")
        formula.pack()

        # Основной контейнер
        main_frame = tk.Frame(tab, bg='#34495e', relief='ridge', bd=2)
        main_frame.pack(pady=20, padx=30, fill='both', expand=True)

        # Поля ввода
        input_frame = tk.Frame(main_frame, bg='#34495e')
        input_frame.pack(pady=30)

        self.setup_input_field(input_frame, "Мощность P (Вт):", "power_three", 0)
        self.setup_input_field(input_frame, "Напряжение U (В):", "voltage_three", 1, "380")
        self.setup_input_field(input_frame, "cos(φ):", "cos_phi_three", 2, "0.8")

        # Фрейм для кнопок
        button_frame = tk.Frame(main_frame, bg='#34495e')
        button_frame.pack(pady=20)

        # Кнопка расчета
        calc_btn = self.create_modern_button(button_frame, "🧮 Рассчитать ток",
                                             self.calculate_three_phase, bg='#27ae60')
        calc_btn.grid(row=0, column=0, padx=10)

        # Кнопка сброса
        reset_btn = self.create_modern_button(button_frame, "🔄 Сброс",
                                              self.reset_three_phase, bg='#e74c3c')
        reset_btn.grid(row=0, column=1, padx=10)

        # Поле результата
        self.result_three = tk.Label(main_frame, text="Результат: ",
                                     font=('Arial', 12, 'bold'),
                                     bg='#34495e', fg='#2ecc71')
        self.result_three.pack(pady=20)

        # Кнопка возврата
        back_btn = self.create_modern_button(tab, "← Назад в меню",
                                             self.show_main, bg='#7f8c8d', width=15)
        back_btn.pack(side=tk.BOTTOM, pady=10)

    def setup_cosinus_tab(self):
        """Настройка вкладки для расчета общего косинуса"""
        tab = self.tabs['Общий косинус']

        # Заголовок
        title = self.create_section_title(tab, "Расчет общего косинуса")
        title.pack(pady=10)

        # Формула
        formula = self.create_formula_label(tab, "Формула: cos(φ)общ = P∑ / √(P∑² + Q∑²)")
        formula.pack()

        # Основной контейнер
        main_frame = tk.Frame(tab, bg='#34495e', relief='ridge', bd=2)
        main_frame.pack(pady=20, padx=30, fill='both', expand=True)

        # Поля ввода
        input_frame = tk.Frame(main_frame, bg='#34495e')
        input_frame.pack(pady=20)

        # Создаем 8 пар полей ввода
        self.power_entries = []
        self.cos_entries = []

        for i in range(8):
            row_frame = tk.Frame(input_frame, bg='#34495e')
            row_frame.pack(pady=2)

            # Мощность
            tk.Label(row_frame, text=f"ЭП {i + 1} P(кВт):", font=('Arial', 9),
                     bg='#34495e', fg='#ecf0f1').pack(side=tk.LEFT, padx=5)

            power_entry = tk.Entry(row_frame, font=('Arial', 9), width=8,
                                   bg='#ecf0f1', fg='#2c3e50', relief='flat')
            power_entry.insert(0, '0')
            power_entry.pack(side=tk.LEFT, padx=5)
            self.power_entries.append(power_entry)

            # Косинус фи
            tk.Label(row_frame, text="cos(φ):", font=('Arial', 9),
                     bg='#34495e', fg='#ecf0f1').pack(side=tk.LEFT, padx=5)

            cos_entry = tk.Entry(row_frame, font=('Arial', 9), width=8,
                                 bg='#ecf0f1', fg='#2c3e50', relief='flat')
            cos_entry.insert(0, "0")
            cos_entry.pack(side=tk.LEFT, padx=5)
            self.cos_entries.append(cos_entry)

        # Фрейм для кнопок
        button_frame = tk.Frame(main_frame, bg='#34495e')
        button_frame.pack(pady=20)

        # Кнопка расчета
        calc_btn = self.create_modern_button(button_frame, "🧮 Рассчитать",
                                             self.calculate_cosinus, bg='#27ae60')
        calc_btn.grid(row=0, column=0, padx=10)

        # Кнопка сброса
        reset_btn = self.create_modern_button(button_frame, "🔄 Сброс",
                                              self.reset_cosinus, bg='#e74c3c')
        reset_btn.grid(row=0, column=1, padx=10)

        # Поле результата
        self.result_cos = tk.Label(main_frame, text="Результат: ",
                                   font=('Arial', 12, 'bold'),
                                   bg='#34495e', fg='#2ecc71')
        self.result_cos.pack(pady=20)

        # Кнопка возврата
        back_btn = self.create_modern_button(tab, "← Назад в меню",
                                             self.show_main, bg='#7f8c8d', width=15)
        back_btn.pack(side=tk.BOTTOM, pady=10)

    def setup_ppg_tab(self):
        """Настройка вкладки для расчета нагрузки квартир на ГАЗЕ"""
        tab = self.tabs['Нагрузка квартир (ГАЗ)']

        # Заголовок
        title = self.create_section_title(tab, "Расчет нагрузки квартир с плитами на ГАЗЕ")
        title.pack(pady=10)

        # Ссылка на СП
        sp_label = tk.Label(tab, text="СП 256.1325800.2016, таблица 7.1",
                            font=('Arial', 11), fg='#27ae60', bg='#2c3e50')
        sp_label.pack(pady=5)

        # Формула
        formula = self.create_formula_label(tab, "Формула: Pкв = Pкв.уд × n")
        formula.pack()

        # Основной контейнер
        main_frame = tk.Frame(tab, bg='#34495e', relief='ridge', bd=2)
        main_frame.pack(pady=20, padx=50, fill='both', expand=True)

        # Поля ввода
        input_frame = tk.Frame(main_frame, bg='#34495e')
        input_frame.pack(pady=30)

        tk.Label(input_frame, text="Количество квартир с плитами на природном газе, шт.",
                 font=('Arial', 10), wraplength=200,
                 bg='#34495e', fg='#ecf0f1').pack(pady=10)

        self.pgaz = tk.Entry(input_frame, font=('Arial', 12), width=15,
                             bg='#ecf0f1', fg='#2c3e50', relief='flat',
                             justify='center')
        self.pgaz.insert(0, "0")
        self.pgaz.pack(pady=10)

        # Фрейм для кнопок
        button_frame = tk.Frame(main_frame, bg='#34495e')
        button_frame.pack(pady=20)

        # Кнопка расчета
        calc_btn = self.create_modern_button(button_frame, "🧮 Рассчитать мощность",
                                             self.calculate_ppg, bg='#27ae60', width=25)
        calc_btn.pack(pady=10)

        # Кнопка сброса
        reset_btn = self.create_modern_button(button_frame, "🔄 Сброс",
                                              self.reset_ppg, bg='#e74c3c')
        reset_btn.pack(pady=5)

        # Поле результата
        self.result_ppg = tk.Label(main_frame, text="Результат на газе: ",
                                   font=('Arial', 12, 'bold'),
                                   bg='#34495e', fg='#2ecc71')
        self.result_ppg.pack(pady=20)

        # Кнопка возврата
        back_btn = self.create_modern_button(tab, "← Назад в меню",
                                             self.show_main, bg='#7f8c8d', width=15)
        back_btn.pack(side=tk.BOTTOM, pady=10)

    def setup_ppe_tab(self):
        """Настройка вкладки для расчета нагрузки квартир на Электричестве"""
        tab = self.tabs['Нагрузка квартир (ЭЛ)']

        # Заголовок
        title = self.create_section_title(tab, "Расчет нагрузки квартир с плитами на ЭЛЕКТРИЧЕСТВЕ")
        title.pack(pady=10)

        # Ссылка на СП
        sp_label = tk.Label(tab, text="СП 256.1325800.2016, таблица 7.1",
                            font=('Arial', 11), fg='#27ae60', bg='#2c3e50')
        sp_label.pack(pady=5)

        # Формула
        formula = self.create_formula_label(tab, "Формула: Pкв = Pкв.уд × n")
        formula.pack()

        # Основной контейнер
        main_frame = tk.Frame(tab, bg='#34495e', relief='ridge', bd=2)
        main_frame.pack(pady=20, padx=50, fill='both', expand=True)

        # Поля ввода
        input_frame = tk.Frame(main_frame, bg='#34495e')
        input_frame.pack(pady=30)

        tk.Label(input_frame, text="Количество квартир с электрическими плитами, шт.",
                 font=('Arial', 10), wraplength=200,
                 bg='#34495e', fg='#ecf0f1').pack(pady=10)

        self.pel = tk.Entry(input_frame, font=('Arial', 12), width=15,
                            bg='#ecf0f1', fg='#2c3e50', relief='flat',
                            justify='center')
        self.pel.insert(0, "0")
        self.pel.pack(pady=10)

        # Фрейм для кнопок
        button_frame = tk.Frame(main_frame, bg='#34495e')
        button_frame.pack(pady=20)

        # Кнопка расчета
        calc_btn = self.create_modern_button(button_frame, "🧮 Рассчитать мощность",
                                             self.calculate_ppe, bg='#27ae60', width=25)
        calc_btn.pack(pady=10)

        # Кнопка сброса
        reset_btn = self.create_modern_button(button_frame, "🔄 Сброс",
                                              self.reset_ppe, bg='#e74c3c')
        reset_btn.pack(pady=5)

        # Поле результата
        self.result_ppe = tk.Label(main_frame, text="Результат на электричестве: ",
                                   font=('Arial', 12, 'bold'),
                                   bg='#34495e', fg='#2ecc71')
        self.result_ppe.pack(pady=20)

        # Кнопка возврата
        back_btn = self.create_modern_button(tab, "← Назад в меню",
                                             self.show_main, bg='#7f8c8d', width=15)
        back_btn.pack(side=tk.BOTTOM, pady=10)

    # Методы для переключения вкладок
    def show_main(self):
        self.tab_control.select(0)

    def show_single_phase(self):
        self.tab_control.select(1)

    def show_three_phase(self):
        self.tab_control.select(2)

    def show_cosinus(self):
        self.tab_control.select(3)

    def show_ppg(self):
        self.tab_control.select(4)

    def show_ppe(self):
        self.tab_control.select(5)

    # Вставьте сюда все методы calculate_* и reset_* из вашего предыдущего кода
    # Они остаются без изменений...
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
        one_five = 10
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

            if 1 <= ng <= 5:
                Ppg = one_five * ng
            elif ng == 6:
                Ppg = six * ng
            elif 6 < ng < 9:
                Ppg = ((nine - six) / (9 - 6) * (ng - 6) + six) * ng
            elif ng == 9:
                Ppg = nine * ng
            elif 9 < ng < 12:
                Ppg = ((twelw - nine) / (12 - 9) * (ng - 9) + nine) * ng
            elif ng == 12:
                Ppg = twelw * ng
            elif 12 < ng < 15:
                Ppg = ((fifteen - twelw) / (15 - 12) * (ng - 12) + twelw) * ng
            elif ng == 15:
                Ppg = fifteen * ng
            elif 15 < ng < 18:
                Ppg = ((eighteen - fifteen) / (18 - 15) * (ng - 15) + fifteen) * ng
            elif ng == 18:
                Ppg = eighteen * ng
            elif 18 < ng < 24:
                Ppg = ((twentyfour - eighteen) / (24 - 18) * (ng - 18) + eighteen) * ng
            elif ng == 24:
                Ppg = twentyfour * ng
            elif 24 < ng < 40:
                Ppg = ((forty - twentyfour) / (40 - 24) * (ng - 24) + twentyfour) * ng
            elif ng == 40:
                Ppg = forty * ng
            elif 40 < ng < 60:
                Ppg = ((sixty - forty) / (60 - 40) * (ng - 40) + forty) * ng
            elif ng == 60:
                Ppg = sixty * ng
            elif 60 < ng < 100:
                Ppg = ((onehundred - sixty) / (100 - 60) * (ng - 60) + sixty) * ng
            elif ng == 100:
                Ppg = onehundred * ng
            elif 100 < ng < 200:
                Ppg = ((twohundred - onehundred) / (200 - 100) * (ng - 100) + onehundred) * ng
            elif ng == 200:
                Ppg = twohundred * ng
            elif 200 < ng < 400:
                Ppg = ((fourhundred - twohundred) / (400 - 200) * (ng - 200) + twohundred) * ng
            elif ng == 400:
                Ppg = fourhundred * ng
            elif 400 < ng < 600:
                Ppg = ((sixhundred - fourhundred) / (600 - 400) * (ng - 400) + fourhundred) * ng
            elif ng == 600:
                Ppg = sixhundred * ng
            elif 600 < ng < 1000:
                Ppg = ((onethousand - sixhundred) / (1000 - 600) * (ng - 600) + sixhundred) * ng
            elif ng == 1000:
                Ppg = onethousand * ng

            self.result_ppg.config(text=f"Результат:\n\nPкв.уд = {Ppg / ng:.3f} кВт/кв.\n\nPкв = {Ppg:.2f} кВт")

        except ValueError as e:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения")

    def calculate_ppe(self):
        """Расчет нагрузок квартир на ЭЛЕКТРИЧЕСТВЕ"""
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

            if 1 <= ne <= 5:
                Ppe = one_five * ne
            elif ne == 6:
                Ppe = sixe * ne
            elif 6 < ne < 9:
                Ppe = ((ninee - sixe) / (9 - 6) * (ne - 6) + sixe) * ne
            elif ne == 9:
                Ppe = ninee * ne
            elif 9 < ne < 12:
                Ppe = ((twelwe - ninee) / (12 - 9) * (ne - 9) + ninee) * ne
            elif ne == 12:
                Ppe = twelwe * ne
            elif 12 < ne < 15:
                Ppe = ((fifteene - twelwe) / (15 - 12) * (ne - 12) + twelwe) * ne
            elif ne == 15:
                Ppe = fifteene * ne
            elif 15 < ne < 18:
                Ppe = ((eighteene - fifteene) / (18 - 15) * (ne - 15) + fifteene) * ne
            elif ne == 18:
                Ppe = eighteene * ne
            elif 18 < ne < 24:
                Ppe = ((twentyfoure - eighteene) / (24 - 18) * (ne - 18) + eighteene) * ne
            elif ne == 24:
                Ppe = twentyfoure * ne
            elif 24 < ne < 40:
                Ppe = ((fortye - twentyfoure) / (40 - 24) * (ne - 24) + twentyfoure) * ne
            elif ne == 40:
                Ppe = fortye * ne
            elif 40 < ne < 60:
                Ppe = ((sixtye - fortye) / (60 - 40) * (ne - 40) + fortye) * ne
            elif ne == 60:
                Ppe = sixtye * ne
            elif 60 < ne < 100:
                Ppe = ((onehundrede - sixtye) / (100 - 60) * (ne - 60) + sixtye) * ne
            elif ne == 100:
                Ppe = onehundrede * ne
            elif 100 < ne < 200:
                Ppe = ((twohundrede - onehundrede) / (200 - 100) * (ne - 100) + onehundrede) * ne
            elif ne == 200:
                Ppe = twohundrede * ne
            elif 200 < ne < 400:
                Ppe = ((fourhundrede - twohundrede) / (400 - 200) * (ne - 200) + twohundrede) * ne
            elif ne == 400:
                Ppe = fourhundrede * ne
            elif 400 < ne < 600:
                Ppe = ((sixhundrede - fourhundrede) / (600 - 400) * (ne - 400) + fourhundrede) * ne
            elif ne == 600:
                Ppe = sixhundrede * ne
            elif 600 < ne < 1000:
                Ppe = ((onethousande - sixhundrede) / (1000 - 600) * (ne - 600) + sixhundrede) * ne
            elif ne == 1000:
                Ppe = onethousande * ne

            self.result_ppe.config(text=f"Результат:\n\nPкв.уд = {Ppe / ne:.3f} кВт/кв.\n\nPкв = {Ppe:.2f} кВт")

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
        self.pgaz.insert(0, "0")
        self.result_ppg.config(text="Результат на газе: ")

    def reset_ppe(self):
        """Сброс данных расчета нагрузок квартир"""
        self.pel.delete(0, tk.END)
        self.pel.insert(0, "0")
        self.result_ppe.config(text="Результат на электричестве: ")


def main():
    root = tk.Tk()
    app = CurrentCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()