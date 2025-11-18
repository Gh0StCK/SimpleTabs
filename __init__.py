import bpy
from . import tab
from . import prefs
from . import addon


classes = (
    tab.TabProps,
    prefs.AddonPrefs,
    addon.AddonProps,
)


def register():
    # Register property classes safely for Blender 5.0+
    for cls in classes:
        try:
            bpy.utils.register_class(cls)
        except RuntimeError:
            # Class might already be registered (e.g. on reload)
            pass

    # Attach main PointerProperty on WindowManager if not present
    if not hasattr(bpy.types.WindowManager, "simpletabs"):
        bpy.types.WindowManager.simpletabs = bpy.props.PointerProperty(
            type=addon.AddonProps
        )


def unregister():
    # Remove WindowManager property first
    if hasattr(bpy.types.WindowManager, "simpletabs"):
        del bpy.types.WindowManager.simpletabs

    # Unregister classes in reverse order
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            # Class might not be registered, skip
            pass
