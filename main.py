"""
Тамагочи - виртуальный питомец на KivyMD
GitHub: https://github.com/ТВОЙ_НИК/tamagotchi-kivy
"""

from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty

class TamagotchiApp(MDApp):
    """
    Основной класс приложения-тамагочи
    Управляет состоянием питомца и действиями
    """
    
    # Свойства питомца (будут автоматически обновлять интерфейс)
    name = "Питомец"
    hunger = NumericProperty(50)      # 0-100, 0 - сытый
    happiness = NumericProperty(50)    # 0-100, 0 - грустный
    energy = NumericProperty(50)       # 0-100, 0 - уставший
    mood_icon = StringProperty("😊")   # Иконка настроения
    is_alive = True                    # Жив ли питомец

    def build(self):
        """Инициализация приложения"""
        # Запускаем таймер обновления каждую секунду
        Clock.schedule_interval(self.update_pet, 1)
        return

    def update_pet(self, dt):
        """
        Обновляет состояние питомца каждую секунду
        Вызывается автоматически таймером
        """
        if not self.is_alive:
            return

        # Изменение параметров со временем
        self.hunger = min(100, self.hunger + 0.5)
        self.happiness = max(0, self.happiness - 0.3)
        self.energy = max(0, self.energy - 0.2)

        # Обновление иконки в зависимости от настроения
        if self.happiness > 70:
            self.mood_icon = "😊"
        elif self.happiness > 30:
            self.mood_icon = "😐"
        else:
            self.mood_icon = "😢"

        # Проверка на смерть
        if self.hunger >= 100 or self.happiness <= 0 or self.energy <= 0:
            self.mood_icon = "💀"
            self.is_alive = False
            Clock.unschedule(self.update_pet)

    def feed(self):
        """Покормить питомца"""
        if not self.is_alive:
            return
        self.hunger = max(0, self.hunger - 20)
        self.happiness = min(100, self.happiness + 5)

    def play(self):
        """Поиграть с питомцем"""
        if not self.is_alive:
            return
        self.happiness = min(100, self.happiness + 20)
        self.energy = max(0, self.energy - 10)
        self.hunger = min(100, self.hunger + 10)

    def sleep(self):
        """Уложить питомца спать"""
        if not self.is_alive:
            return
        self.energy = min(100, self.energy + 30)
        self.hunger = min(100, self.hunger + 5)

    def reset(self):
        """Сбросить состояние питомца (перезапуск)"""
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.mood_icon = "😊"
        self.is_alive = True
        Clock.schedule_interval(self.update_pet, 1)

if __name__ == "__main__":
    TamagotchiApp().run()
