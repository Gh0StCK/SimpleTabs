import bpy


def startup_timer():
    """Таймер, который просто вызывает обновление вкладок SimpleTabs."""
    bpy.ops.simpletabs.update()
    # Возвращаем None, чтобы таймер сработал один раз
    return None
