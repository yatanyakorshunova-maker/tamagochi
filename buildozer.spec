[app]

# Название приложения
title = Tamagotchi

# Пакет (уникальный идентификатор)
package.name = tamagotchi
package.domain = org.yourcompany

# Версия
version = 1.0.0
version.regex = __version__ = ['"](.*)['"]
# В разделе [app]
requirements = python3==3.11,kivy==2.3.0,kivymd==1.1.1
android.api = 33
android.minapi = 21
android.ndk = 23c
android.sdk = 33
android.gradle_dependencies = 'androidx.appcompat:appcompat:1.6.1'
android.enable_androidx = True
# Требования для Android
requirements = python3==3.11,kivy==2.3.0,kivymd==1.1.1

# Иконка
app.icon = assets/icon.png

# Ориентация экрана
orientation = portrait

# Разрешения
android.permissions = INTERNET

# Минимальная версия Android
android.minapi = 21
android.api = 33
android.ndk = 23c
android.sdk = 33

# Режим отладки
android.gradle_dependencies = 'androidx.appcompat:appcompat:1.6.1'
android.enable_androidx = True

[buildozer]

# Логгирование
log_level = 2

# Папки для копирования в APK
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Игнорируемые папки и файлы
source.exclude_exts = spec,md,gitignore
source.exclude_dirs = tests, bin, docs, venv

