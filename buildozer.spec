[app]

# ============================================================
# INFORMASI APLIKASI
# ============================================================

title = UniversalPOS

package.name = universalpos

package.domain = org.universalpos

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,json,txt,db,atlas

version = 1.0.0

# ============================================================
# REQUIREMENTS
# ============================================================

requirements = python3.11,kivy,pyjnius


# ============================================================
# ORIENTASI
# ============================================================

orientation = portrait

fullscreen = 0


# ============================================================
# ANDROID
# ============================================================

android.api = 35
android.minapi = 24
android.ndk_version = 27c
android.archs = arm64-v8a

# ============================================================
# ANDROID APP SETTINGS
# ============================================================

android.accept_sdk_license = True

android.enable_androidx = True

android.enable_jetifier = True


# ============================================================
# PERMISSION
# ============================================================

android.permissions = \
    INTERNET, \
    BLUETOOTH, \
    BLUETOOTH_ADMIN, \
    BLUETOOTH_CONNECT, \
    BLUETOOTH_SCAN, \
    READ_EXTERNAL_STORAGE, \
    WRITE_EXTERNAL_STORAGE


# ============================================================
# ICON
# ============================================================

icon.filename = %(source.dir)s/assets/icon.png


# ============================================================
# PRESPLASH
# ============================================================

presplash.filename = %(source.dir)s/assets/presplash.png


# ============================================================
# SCREEN
# ============================================================

# Tidak menggunakan fullscreen
# fullscreen = 0


# ============================================================
# ANDROID BACKUP
# ============================================================

android.allow_backup = True


# ============================================================
# ANDROID PRIVATE STORAGE
# ============================================================

android.private_storage = True


# ============================================================
# LOGCAT
# ============================================================

log_level = 2


# ============================================================
# KIVY
# ============================================================

# Uncomment jika menggunakan file .kv
# source.include_exts = py,kv,png,jpg,jpeg,atlas,json,txt


# ============================================================
# BUILD OPTIONS
# ============================================================

warn_on_root = 1

# Jangan menggunakan SDK internal Buildozer secara paksa.
# SDK akan disiapkan oleh GitHub Actions.


# ============================================================
# BLACKLIST
# ============================================================

# Jangan memasukkan file development yang tidak diperlukan.
source.exclude_dirs = \
    .git, \
    .github, \
    .buildozer, \
    bin, \
    __pycache__, \
    tests


# ============================================================
# DEPENDENCIES
# ============================================================

# Jangan masukkan Pillow dulu.
# Pillow dapat ditambahkan setelah APK dasar berhasil dibuat.


[buildozer]

# ============================================================
# BUILDOZER GLOBAL
# ============================================================

log_level = 2

warn_on_root = 1
