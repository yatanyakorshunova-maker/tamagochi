[app]

# Название приложения
title = Tamagotchi

# Уникальный идентификатор
package.name = tamagotchi
package.domain = org.yourcompany

# Версия
version = 1.0.0

# Требования (ВАЖНО: без указания версии Python)
requirements = python3,kivy==2.3.0,kivymd==1.1.1

# Иконка
app.icon = assets/icon.png

# Ориентация
orientation = portrait

# Разрешения
android.permissions = INTERNET

# Настройки Android (проверенные значения)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.enable_androidx = True
android.gradle_dependencies = 'androidx.appcompat:appcompat:1.6.1'

# Игнорируемые файлы
source.include_exts = py,png,jpg,kv,atlas
source.exclude_exts = spec,md,gitignore,pyc
source.exclude_dirs = tests, bin, docs, venv, .git, .github

# Логгирование
log_level = 2

[buildozer]

# Папки для копирования
source.dir = .
log_level = 2

# Настройки Gradle
android.accept_sdk_license = True
android.archs = armeabi-v7a, arm64-v8a
android.bootstrap = sdl2
android.gradle_build_tools_version = 33.0.0
android.gradle_plugin_version = 7.4.2
android.ndk_version = 25b
