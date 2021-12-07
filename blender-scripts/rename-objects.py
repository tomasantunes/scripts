import bpy

objects = bpy.context.scene.objects

for i in range(0, len(objects)):
	print(objects[i].name)
	objects[i].name = "object" + str(i)
	objects[i].data.name = "object" + str(i)