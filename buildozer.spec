[app]

# Название приложения
title = Мой цифровой питомец

# Уникальный идентификатор
package.name = digitalpet
package.domain = org.yourcompany

# Версия
version = 1.0.0

# Требования (важно: правильные версии!)
requirements = python3,kivy==2.2.0

# Иконка
app.icon = icon.png

# Ориентация
orientation = portrait

# Разрешения
android.permissions = INTERNET

# Настройки Android
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

# Указываем корневую папку проекта
source.dir = .

# Настройки сборки
android.accept_sdk_license = True
android.archs = armeabi-v7a, arm64-v8a
android.bootstrap = sdl2
android.gradle_build_tools_version = 33.0.2
android.gradle_plugin_version = 7.4.2
android.ndk_version = 25b
