class Temp_Celsius:
    def __init__(self, t):
        if t > -273.15:
            self.__t = float(t)
        else:
            self.__t = -273.15

    def __str__(self):
        return f'Температура {self.__t} градусов Цельсия'

    @property
    def t(self):
        return self.__t

    @t.setter
    def t(self, new_t):
        if new_t > -273.15:
            self.__t = float(new_t)
        else:
            self.__t = -273.15

    def __add__(self, other):
        t = self.__t + float(other)
        return Temp_Celsius(t)

    def __sub__(self, other):
        t = self.__t - float(other)
        return Temp_Celsius(t)

    def __float__(self):
        return float(self.__t)

    def __eq__(self, other):
        return self.__t == float(other)

    def __gt__(self, other):
        return self.__t > float(other)

    def convectr(self, kelvin=False, fahrenheit=False):
        if kelvin:
            t_k = self.__t + 273.15
            return Temp_Kelvin(t_k)
        if fahrenheit:
            t_f = (self.__t * 9 / 5) + 32.0
            return Temp_Fahrenheit(round(t_f, 2))


class Temp_Fahrenheit(Temp_Celsius):
    def __init__(self, t):
        super().__init__(t)
        if t > -459.67:
            self.__t = float(t)
        else:
            self.__t = -459.67

    def __str__(self):
        return f'Температура {self.__t} градусов Фаренгейта'

    @property
    def t(self):
        return self.__t

    @t.setter
    def t(self, new_t):
        if new_t > -459.67:
            self.__t = float(new_t)
        else:
            self.__t = -459.67

    def __add__(self, other):
        t = self.__t + float(other)
        return Temp_Fahrenheit(t)

    def __sub__(self, other):
        t = self.__t - float(other)
        return Temp_Fahrenheit(t)
    #
    # def __float__(self):
    #     return float(self.__t)
    #
    # def __eq__(self, other):
    #     return self.__t == float(other)
    #
    # def __gt__(self, other):
    #     return self.__t > float(other)

    def convectr(self, celsius=False, kelvin=False):
        if celsius:
            t_c = (self.__t - 32.0) * 5 / 9
            return Temp_Celsius(round(t_c, 2))
        if kelvin:
            t_k = (self.__t - 32.0) * 5 / 9 + 273.15
            return Temp_Kelvin(round(t_k, 2))


class Temp_Kelvin(Temp_Celsius):
    def __init__(self, t):
        super().__init__(t)
        if t > 0.0:
            self.__t = float(t)
        else:
            self.__t = 0.0

    def __str__(self):
        return f'Температура {self.__t} градусов Кельвину'

    @property
    def t(self):
        return self.__t

    @t.setter
    def t(self, new_t):
        if new_t >= 0.0:
            self.__t = float(new_t)
        else:
            self.__t = 0.0

    def __add__(self, other):
        t = self.__t + float(other)
        return Temp_Kelvin(t)

    def __sub__(self, other):
        t = self.__t - float(other)
        return Temp_Kelvin(t)
    #
    # def __float__(self):
    #     return float(self.__t)
    #
    # def __eq__(self, other):
    #     return self.__t == float(other)
    #
    # def __gt__(self, other):
    #     return self.__t > float(other)

    def convectr(self, celsius=False, fahrenheit=False):
        if celsius:
            t_c = self.__t - 273.15
            return Temp_Celsius(round(t_c, 2))
        if fahrenheit:
            t_f = (self.__t - 273.15) * 9 / 5 + 32.0
            return Temp_Fahrenheit(round(t_f, 2))


t = Temp_Fahrenheit(100)
print(t)
print(t.convectr(celsius=True))
print(t.convectr(kelvin=True))
