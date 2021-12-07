import os

blender_code = """
		import bpy
		file = open("materials.txt", "a");
		for mat in bpy.data.materials:
    		file.write(mat.name + "\n")
	"""

files = [f for f in os.listdir('.') if os.path.isfile(f) and os.path.splitext(filename)[1] == ".blend"]
for f in files:
	os.system("blender -b "+f+" --python-text "+blender_code)