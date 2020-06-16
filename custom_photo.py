import os
from shutil import copyfile, move

src_dir = "X:/SteamLibrary/steamapps/common/IL-2 Sturmovik Battle of Stalingrad/data/graphics/Planes"


def custom_photo():
    path = os.getcwd()
    tgt_photo = path + "/custom_photo.dds"
    lst_plane_dirs = os.listdir(src_dir)

    for line in lst_plane_dirs:
        plane_path = src_dir + "/" + line + "/Textures/"
        src_photo = plane_path + "custom_photo.dds"
        src_backup = plane_path + "custom_photo_backup.dds"

        # print(src_photo)
        if os.path.exists(src_photo):
            if os.path.exists(src_backup):
                print("There is already a backup file, make sure you want to overwrite these.")
                exit()
            else:
                move(src_photo, src_backup)
            
        copyfile(tgt_photo, src_photo)

custom_photo()