for /r %%i in (*) do blender -b "%%i" -P list_materials.py
pause