[app]

# Nama aplikasi
title = UniversalPOS

# Package Android harus unik
package.name = universalpos
package.domain = org.universalpos

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt,svg,ttf
source.exclude_dirs = .git,.github,.buildozer,bin,__pycache__,venv,.venv

version = 1.0.0

requirements = python3,kivy,pillow,pyjnius

orientation = portrait
fullscreen = 0

# Ikon aplikasi
icon.filename = %(source.dir)s/assets/icon.png

# Android permissions
android.permissions = BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_SCAN,BLUETOOTH_CONNECT,READ_MEDIA_IMAGES,READ_EXTERNAL_STORAGE

# Target modern Android
android.api = 35
android.minapi = 23
android.ndk = 27c
android.accept_sdk_license = True

# Untuk beberapa printer Bluetooth Classic
android.add_src = android_src

# Android 12+ menggunakan permission runtime untuk Bluetooth.
# Aplikasi juga melakukan request permission saat startup bila tersedia.

# Build optimization
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = True

[buildozer]

log_level = 2
warn_on_root = 1
