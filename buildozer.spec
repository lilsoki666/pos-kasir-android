[app]

# ============================================================
# APPLICATION
# ============================================================

title = UniversalPOS

package.name = universalpos

package.domain = org.universalpos

version = 1.0.0


# ============================================================
# SOURCE
# ============================================================

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,json,txt,atlas,db

source.exclude_dirs = .git,.github,.buildozer,bin,__pycache__,tests


# ============================================================
# PYTHON / KIVY
# ============================================================

requirements = python3,kivy,pyjnius


# ============================================================
# SCREEN
# ============================================================

orientation = portrait

fullscreen = 0


# ============================================================
# ICON
# ============================================================

icon.filename = %(source.dir)s/assets/icon.png


# ============================================================
# ANDROID
# ============================================================

android.api = 35

android.minapi = 24

android.ndk_version = 27c

android.archs = arm64-v8a


# ============================================================
# ANDROIDX
# ============================================================

android.enable_androidx = True

android.enable_jetifier = True


# ============================================================
# ANDROID LICENSE
# ============================================================

android.accept_sdk_license = True


# ============================================================
# PERMISSIONS
# ============================================================

android.permissions = INTERNET,BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,BLUETOOTH_SCAN


# ============================================================
# ANDROID BACKUP
# ============================================================

android.allow_backup = True


# ============================================================
# LOG
# ============================================================

log_level = 2


[buildozer]

log_level = 2

warn_on_root = 1
