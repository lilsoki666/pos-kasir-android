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

requirements = python3,kivy,pyjnius

orientation = portrait
fullscreen = 0

# Ikon aplikasi
icon.filename = %(source.dir)s/assets/icon.png

# Android permissions
android.permissions = BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_SCAN,BLUETOOTH_CONNECT,READ_MEDIA_IMAGES,READ_EXTERNAL_STORAGE

# Add this line to specify pip version compatibility
p4a.pip_install_options = --no-build-isolation

# Or alternatively, ensure requirements are properly pinned
requirements = python3,kivy,pyjnius

# Add this to clear the build cache and force a fresh environment
android.ndk_version = 27c
android.api = 35
android.minapi = 24
android.gradle_version = 8.1.1

# Untuk beberapa printer Bluetooth Classic
android.add_src = android_src

# Android 12+ menggunakan permission runtime untuk Bluetooth.
# Aplikasi juga melakukan request permission saat startup bila tersedia.

# Build optimization
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = True

[buildozer]
# ... existing config ...

# Ensure compatible Python version
python_version = 3.11

log_level = 2
warn_on_root = 1
