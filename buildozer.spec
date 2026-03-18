[app]
title = WanaboyAI
package.name = wanaboyai
package.domain = org.wanaboy
version = 1.0

source.dir = .
source.include_exts = py,kv

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

# FIX BUILD
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

android.skip_update = True
android.accept_sdk_license = True
android.build_tools = 31.0.0

log_level = 2
