import bpy
import os


for i in range(1, 4):

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False, confirm=False)

    print( 'blender script' + os.getcwd())
    bpy.ops.import_scene.obj(filepath='..\\static\\SHObj\\shoe' + str(i) + '\\shoe.obj')
    bpy.ops.import_scene.gltf(filepath='..\\static\\SHObj\\human6\\inish_model2.glb')
    bpy.ops.export_scene.gltf(filepath='..\\static\\productmodels\\untitled' +str(i) +'.gltf')


for i in range(4, 6):
    
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False, confirm=False)

    print( 'blender script' + os.getcwd())
    bpy.ops.import_scene.obj(filepath='..\\static\\SHObj\\shoe' + str(i) + '\\shoe.obj')
    bpy.ops.import_scene.gltf(filepath='..\\static\\SHObj\\human6\\inish_model.glb')
    bpy.ops.export_scene.gltf(filepath='..\\static\\productmodels\\untitled' +str(i) +'.gltf')





