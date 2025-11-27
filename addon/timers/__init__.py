import bpy
from bpy.app.handlers import persistent

from . import startup
from .. import utils


@persistent
def simpletabs_load_post(dummy):
    """Запускает SimpleTabs после загрузки .blend-файла."""
    # Берём настройки аддона
    prefs = utils.addon.prefs()

    # Задержка, как в prefs (если там None или 0 — будет 0.0)
    delay = getattr(prefs, "startup_delay", 0.0) or 0.0

    # Если таймер ещё не зарегистрирован — регистрируем
    if not bpy.app.timers.is_registered(startup.startup_timer):
        bpy.app.timers.register(startup.startup_timer, first_interval=delay)


def register():
    """Регистрация таймера при запуске Blender и хендлера загрузки .blend."""
    prefs = utils.addon.prefs()

    # Таймер при старте Blender (как было)
    if not bpy.app.timers.is_registered(startup.startup_timer):
        bpy.app.timers.register(startup.startup_timer, first_interval=prefs.startup_delay)

    # Хендлер при загрузке .blend
    if simpletabs_load_post not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(simpletabs_load_post)


def unregister():
    """Отмена таймера и хендлера при отключении аддона."""
    # Снимаем таймер
    if bpy.app.timers.is_registered(startup.startup_timer):
        bpy.app.timers.unregister(startup.startup_timer)

    # Убираем обработчик load_post
    if simpletabs_load_post in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(simpletabs_load_post)