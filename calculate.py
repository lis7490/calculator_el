import tkinter as tk
from tkinter import ttk, messagebox
import math

class CurrentCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор тока")
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

        
        self.tab_control.pack(expand=1, fill='both')
        
        self.setup_main_tab()
        self.setup_single_phase_tab()
        self.setup_three_phase_tab()
        self.setup_cosinus_tab()
    
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
        btn_three = tk.Button(self.tab_main, text="Расчет общего косинуса",
                             command=self.show_cosinus,
                             font=("Arial", 12), width=20, height=2)
        btn_three.pack(pady=10)
        
       
        # Информация о программе
        info_label = tk.Label(self.tab_main, 
                             text="Помощь проектировщику электрику.\n"
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
        self.voltage_single.insert(0, "220")  # Значение по умолчанию
        self.voltage_single.grid(row=1, column=1, pady=5, padx=10)
        tk.Label(input_frame, text="В").grid(row=1, column=2, sticky="w", pady=5)
        
        # Косинус фи
        tk.Label(input_frame, text="cos(φ):", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
        self.cos_phi_single = tk.Entry(input_frame, font=("Arial", 10), width=15)
        self.cos_phi_single.insert(0, "0.8")  # Значение по умолчанию
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
        self.voltage_three.insert(0, "380")  # Значение по умолчанию
        self.voltage_three.grid(row=1, column=1, pady=5, padx=10)
        tk.Label(input_frame, text="В").grid(row=1, column=2, sticky="w", pady=5)
        
        # Косинус фи
        tk.Label(input_frame, text="cos(φ):", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
        self.cos_phi_three = tk.Entry(input_frame, font=("Arial", 10), width=15)
        self.cos_phi_three.insert(0, "0.8")  # Значение по умолчанию
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
        
              
        # Поля ввода
        input_frame = tk.Frame(self.tab_cosinus)
        input_frame.pack(pady=20)
        
        # Мощность 1 ЭП
        tk.Label(input_frame, text="Мощность 1 электроприемника, P(кВт):", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
        self.power_three1 = tk.Entry(input_frame, font=("Arial", 10), width=10)
        self.power_three1.insert(0, '0')   # Значение по умолчанию
        self.power_three1.grid(row=0, column=1, pady=5, padx=10)
        tk.Label(input_frame, text="кВт").grid(row=0, column=2, sticky="w", pady=5, padx=(0, 50))
        
                
        # Косинус фи
        tk.Label(input_frame, text="cos(φ):", font=("Arial", 10)).grid(row=0, column=5, sticky="w", pady=5)
        self.cos_phi_three1 = tk.Entry(input_frame, font=("Arial", 10), width=10)
        self.cos_phi_three1.insert(0, "0")  # Значение по умолчанию
        self.cos_phi_three1.grid(row=0, column=6, pady=5, padx=10)

        # Мощность 2 ЭП
        tk.Label(input_frame, text="Мощность 2 электроприемника, P(кВт):", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
        self.power_three2 = tk.Entry(input_frame, font=("Arial", 10), width=10)
        self.power_three2.insert(0, '0')   # Значение по умолчанию
        self.power_three2.grid(row=1, column=1, pady=5, padx=10)
        tk.Label(input_frame, text="кВт").grid(row=1, column=2, sticky="w", pady=5)

        # Косинус фи
        tk.Label(input_frame, text="cos(φ):", font=("Arial", 10)).grid(row=1, column=5, sticky="w", pady=5)
        self.cos_phi_three2 = tk.Entry(input_frame, font=("Arial", 10), width=10)
        self.cos_phi_three2.insert(0, "0")  # Значение по умолчанию
        self.cos_phi_three2.grid(row=1, column=6, pady=5, padx=10)

        # Мощность 3 ЭП
        tk.Label(input_frame, text="Мощность 3 электроприемника, P(кВт):", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
        self.power_three3 = tk.Entry(input_frame, font=("Arial", 10), width=10)
        self.power_three3.insert(0, '0')   # Значение по умолчанию
        self.power_three3.grid(row=2, column=1, pady=5, padx=10)
        tk.Label(input_frame, text="кВт").grid(row=2, column=2, sticky="w", pady=5)

        # Косинус фи
        tk.Label(input_frame, text="cos(φ):", font=("Arial", 10)).grid(row=2, column=5, sticky="w", pady=5)
        self.cos_phi_three3 = tk.Entry(input_frame, font=("Arial", 10), width=10)
        self.cos_phi_three3.insert(0, "0")  # Значение по умолчанию
        self.cos_phi_three3.grid(row=2, column=6, pady=5, padx=10)

        # Мощность 4 ЭП
        tk.Label(input_frame, text="Мощность 4 электроприемника, P(кВт):", font=("Arial", 10)).grid(row=3, column=0, sticky="w", pady=5)
        self.power_three4 = tk.Entry(input_frame, font=("Arial", 10), width=10)
        self.power_three4.insert(0, '0')   # Значение по умолчанию
        self.power_three4.grid(row=3, column=1, pady=5, padx=10)
        tk.Label(input_frame, text="кВт").grid(row=3, column=2, sticky="w", pady=5)

        # Косинус фи
        tk.Label(input_frame, text="cos(φ):", font=("Arial", 10)).grid(row=3, column=5, sticky="w", pady=5)
        self.cos_phi_three4 = tk.Entry(input_frame, font=("Arial", 10), width=10)
        self.cos_phi_three4.insert(0, "0")  # Значение по умолчанию
        self.cos_phi_three4.grid(row=3, column=6, pady=5, padx=10)

        # Мощность 5 ЭП
        tk.Label(input_frame, text="Мощность 5 электроприемника, P(кВт):", font=("Arial", 10)).grid(row=4, column=0, sticky="w", pady=5)
        self.power_three5 = tk.Entry(input_frame, font=("Arial", 10), width=10)
        self.power_three5.insert(0, '0')   # Значение по умолчанию
        self.power_three5.grid(row=4, column=1, pady=5, padx=10)
        tk.Label(input_frame, text="кВт").grid(row=4, column=2, sticky="w", pady=5)

        # Косинус фи
        tk.Label(input_frame, text="cos(φ):", font=("Arial", 10)).grid(row=4, column=5, sticky="w", pady=5)
        self.cos_phi_three5 = tk.Entry(input_frame, font=("Arial", 10), width=10)
        self.cos_phi_three5.insert(0, "0")  # Значение по умолчанию
        self.cos_phi_three5.grid(row=4, column=6, pady=5, padx=10)

        # Мощность 6 ЭП
        tk.Label(input_frame, text="Мощность 6 электроприемника, P(кВт):", font=("Arial", 10)).grid(row=5, column=0, sticky="w", pady=5)
        self.power_three6 = tk.Entry(input_frame, font=("Arial", 10), width=10)
        self.power_three6.insert(0, '0')   # Значение по умолчанию
        self.power_three6.grid(row=5, column=1, pady=5, padx=10)
        tk.Label(input_frame, text="кВт").grid(row=5, column=2, sticky="w", pady=5)

        # Косинус фи
        tk.Label(input_frame, text="cos(φ):", font=("Arial", 10)).grid(row=5, column=5, sticky="w", pady=5)
        self.cos_phi_three6 = tk.Entry(input_frame, font=("Arial", 10), width=10)
        self.cos_phi_three6.insert(0, "0")  # Значение по умолчанию
        self.cos_phi_three6.grid(row=5, column=6, pady=5, padx=10)

        # Мощность 7 ЭП
        tk.Label(input_frame, text="Мощность 7 электроприемника, P(кВт):", font=("Arial", 10)).grid(row=6, column=0, sticky="w", pady=5)
        self.power_three7 = tk.Entry(input_frame, font=("Arial", 10), width=10)
        self.power_three7.insert(0, '0')   # Значение по умолчанию
        self.power_three7.grid(row=6, column=1, pady=5, padx=10)
        tk.Label(input_frame, text="кВт").grid(row=6, column=2, sticky="w", pady=5)

        # Косинус фи
        tk.Label(input_frame, text="cos(φ):", font=("Arial", 10)).grid(row=6, column=5, sticky="w", pady=5)
        self.cos_phi_three7 = tk.Entry(input_frame, font=("Arial", 10), width=10)
        self.cos_phi_three7.insert(0, "0")  # Значение по умолчанию
        self.cos_phi_three7.grid(row=6, column=6, pady=5, padx=10)

        # Мощность 8 ЭП
        tk.Label(input_frame, text="Мощность 8 электроприемника, P(кВт):", font=("Arial", 10)).grid(row=7, column=0, sticky="w", pady=5)
        self.power_three8 = tk.Entry(input_frame, font=("Arial", 10), width=10)
        self.power_three8.insert(0, '0')   # Значение по умолчанию
        self.power_three8.grid(row=7, column=1, pady=5, padx=10)
        tk.Label(input_frame, text="кВт").grid(row=7, column=2, sticky="w", pady=5)

        # Косинус фи
        tk.Label(input_frame, text="cos(φ):", font=("Arial", 10)).grid(row=7, column=5, sticky="w", pady=5)
        self.cos_phi_three8 = tk.Entry(input_frame, font=("Arial", 10), width=10)
        self.cos_phi_three8.insert(0, "0")  # Значение по умолчанию
        self.cos_phi_three8.grid(row=7, column=6, pady=5, padx=10)

        # Фрейм для кнопок
        button_frame = tk.Frame(self.tab_cosinus)
        button_frame.pack(pady=10)
              
        # Кнопка расчета
        calc_btn = tk.Button(button_frame, text="Общий косинус",
                           command=self.calculate_cosinus,
                           font=("Arial", 12), bg="lightgreen", width=20)
        calc_btn.grid(row=0, column=0, padx=10)
        
        # Кнопка сброса
        reset_btn = tk.Button(button_frame, text="Сброс",
                            command=self.reset_cosinus,
                            font=("Arial", 12), bg="lightcoral", width=20)
        reset_btn.grid(row=0, column=1, padx=10)
        
        # Поле результата
        self.result_cos = tk.Label(self.tab_cosinus, text="Результат: ",
                                    font=("Arial", 12, "bold"), fg="green")
        self.result_cos.pack(pady=10)
        
        # Кнопка возврата
        back_btn = tk.Button(self.tab_cosinus, text="Назад в меню",
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
        """Расчет косинуа"""
        try:
            p1 = float(self.power_three1.get())
            cos1 = float(self.cos_phi_three1.get())
            
            if cos1 < 0 or cos1 > 1:
                raise ValueError("Ошибка: вводите данные через точку")
            
            acos1 = math.acos(cos1)
            tg1 = math.tan(acos1)
            Q1 = p1*tg1

            p2 = float(self.power_three2.get())
            cos2 = float(self.cos_phi_three2.get())
            
            if cos2 < 0 or cos2 > 1:
                raise ValueError("Ошибка: вводите данные через точку")
            
            acos2 = math.acos(cos2)
            tg2 = math.tan(acos2)
            Q2 = p2*tg2
            p3 = float(self.power_three3.get())
            cos3 = float(self.cos_phi_three3.get())
            
            if cos3 < 0 or cos3 > 1:
                raise ValueError("Ошибка: вводите данные через точку")
            
            acos3 = math.acos(cos3)
            tg3 = math.tan(acos3)
            Q3 = p3*tg3

            p4 = float(self.power_three4.get())
            cos4 = float(self.cos_phi_three4.get())
            
            if cos4 < 0 or cos4 > 1:
                raise ValueError("Ошибка: вводите данные через точку")
            
            acos4 = math.acos(cos4)
            tg4 = math.tan(acos4)
            Q4 = p4*tg4

            p5 = float(self.power_three5.get())
            cos5 = float(self.cos_phi_three5.get())
            
            if cos5 < 0 or cos5 > 1:
                raise ValueError("Ошибка: вводите данные через точку")
            
            acos5 = math.acos(cos5)
            tg5 = math.tan(acos5)
            Q5 = p5*tg5

            p6 = float(self.power_three6.get())
            cos6 = float(self.cos_phi_three6.get())
            
            if cos6 < 0 or cos6 > 1:
                raise ValueError("Ошибка: вводите данные через точку")
            
            acos6 = math.acos(cos6)
            tg6 = math.tan(acos6)
            Q6 = p6*tg6

            p7 = float(self.power_three7.get())
            cos7 = float(self.cos_phi_three7.get())
            
            if cos7 < 0 or cos7 > 1:
                raise ValueError("Ошибка: вводите данные через точку")
            
            acos7 = math.acos(cos7)
            tg7 = math.tan(acos7)
            Q7 = p7*tg7


            p8 = float(self.power_three8.get())
            cos8 = float(self.cos_phi_three8.get())
            
            if cos8 < 0 or cos8 > 1:
                raise ValueError("Ошибка: вводите данные через точку")
            
            acos8 = math.acos(cos8)
            tg8 = math.tan(acos8)
            Q8 = p8*tg8

            Pp = p1+p2+p3+p4+p5+p6+p7+p8
            Qp = Q1+Q2+Q3+Q4+Q5+Q6+Q7+Q8
            tan = Qp/Pp
            f = math.atan(tan)
            cos = math.cos(f)

            self.result_cos.config(text=f"Результат: cos(φ) = {cos :.2f}")
            
        except ValueError as e:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректный косинус")

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
        entries = [
            self.power_three1, self.cos_phi_three1,
            self.power_three2, self.cos_phi_three2,
            self.power_three3, self.cos_phi_three3,
            self.power_three4, self.cos_phi_three4,
            self.power_three5, self.cos_phi_three5,
            self.power_three6, self.cos_phi_three6,
            self.power_three7, self.cos_phi_three7,
            self.power_three8, self.cos_phi_three8
        ]
        
        for entry in entries:
            entry.delete(0, tk.END)
            if "power" in str(entry):
                entry.insert(0, "0")
            else:
                entry.insert(0, "0")
        
        self.result_cos.config(text="Результат: ")
        

    
def main():
    root = tk.Tk()
    app = CurrentCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()