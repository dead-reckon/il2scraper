import csv
import re
import os
import shutil
import json
from pprint import pprint

def clean_eng(eng):
    pass

def extract_data():
    path = os.getcwd()
    planes_path = path + "/(null)/swf/il2/worldobjects/planes"
    plane_data = os.listdir(planes_path)
    plane_path = path + "/Planes"
    info_path = path + "/Info"

    info_img = info_path + "/img"


    if os.path.isdir(plane_path):
        shutil.rmtree(plane_path)
    if os.path.isdir(info_path):
        shutil.rmtree(info_path)

    os.mkdir(plane_path)
    os.mkdir(info_path)
    os.mkdir(info_img)
    os.mkdir(info_path + "/Text")

    plane_list = []
    for line in plane_data:
        if "random" not in line:
            plane_list.append(line)

    for line in plane_list:
        tgt_dir = plane_path + "/" + line
        tgt_info = tgt_dir + "/" + line + ".txt"
        tgt_info_all = info_path + "/Text/" + line + ".txt"
        # tgt_info_img = info_img + "/" + line + ".txt"
        tgt_preview2 = info_img + "/l_" + line + ".png"
        tgt_preview = info_img + "/s_" + line + ".png"

        src_info = planes_path + "/" + line + "/info.locale=eng.txt"
        src_mod = planes_path + "/" + line + "/modifications"

        src_preview = planes_path + "/" + line + "/preview.png"
        src_preview2 = planes_path + "/" + line + "/preview2.png"

        os.mkdir(tgt_dir)
        
        shutil.copy2(src_info, tgt_info)
        shutil.copy2(src_info, tgt_info_all)
        # shutil.copy2(src_info, tgt_info_small)
        # shutil.copy2(src_info, tgt_info_large)

        shutil.copy2(src_preview, tgt_dir)
        shutil.copy2(src_preview2, tgt_dir)

        shutil.copy2(src_preview2, tgt_preview2)
        shutil.copy2(src_preview, tgt_preview)

        # if os.path.isdir(src_mod):
        #     shutil.copytree(src_mod, tgt_dir + "/mod")
    # Test
    # [print(line) for line in plane_list]

def master_yml():
    path = os.getcwd()
    plane_path = path + "/Planes"
    info_path = path + "/Info/Text"
    plane_texts = os.listdir(info_path)

    f_info = open("info.yml", "w", encoding="utf8")
    s_info = open("stats.yml", "w", encoding="utf8")
    data = []

    p_name_circus = ""
    p_id_circus = ""
    
    l_circus = []
    # l_circus.append(["Name","ID"])

    photo_lst = []
    dds_dict = {}

    for line in plane_texts:
        path_to_file = info_path + "/" + line
        # print("Reading File: " + path_to_file)
        raw = open(path_to_file, "r", encoding="utf8")
        data = raw.read().split("\n")
        raw.close()

        plane_id = re.sub(r'\.txt', '', line)

        photo_dict = {}

        photo_temp = []
        photo_spd = []
        photo_eng = []

        eng_mode_bool = False
        eng_mode = []
        spd_mode_bool = False
        spd_mode = []
        feat_mode_bool = False
        feat_mode = []
        climb_mode_bool = False
        climb_mode = []
        weight_mode_bool = False
        weight_mode = []
        temp_mode_bool = False
        temp_mode = []
        air_mode_bool = False
        air_mode = []
        turn_mode_bool = False
        turn_mode = []
        dim_mode_bool = False
        dim_mode = []
        stall_mode_bool = False
        stall_mode = []
        end_mode = ""
        debut_mode = ""
        d_mode = ""
        dive_mode = ""

        circus_bool = True
        circus = ""

        fuel_hr = ""
        fuel_km = ""
        fuel_cap = ""
        fuel_max_range = ""
        fuel_per_hour = ""

        for row in data:
            if "&name" in row:
                
                final = re.sub(r'^.*&name=', '', row)
                p_id_circus = plane_id
                p_name_circus = final
                f_info.write("- id: " + plane_id + "\n")
                f_info.write("  name: " + final + "\n")
                s_info.write("- id: " + plane_id + "\n")
                s_info.write("  name: " + final + "\n")
                photo_dict['name'] = plane_id

            else:
                final = ""
                if "&description=" in row:
                    final = re.sub(r'^.*&description=\'', '', row)
                    f_info.write("  description: |\n    " + final + "<br>\n")
                else:
                    f_info.write("    " + row + "<br>\n")
            if re.match(r'^References$', row) or re.match(r'^References:$', row):
                circus = "  circus:  1\n"
                # f_info.write("  circus:  1\n")

            if "Engine modes:" in row:
                eng_mode_bool = True
            elif eng_mode_bool:
                if re.match(r'^$', row) is not None:
                    eng_mode_bool = False
                else:
                    if re.match(r'^\(', row):
                        pass
                    else:
                        photo_eng.append(row.split(':'))
                    eng_mode.append(row) 
                    
            if "Takeoff speed:" in row:
                spd_mode_bool = True
                spd_mode.append(row)
                photo_spd.append(row.split(':'))
            elif spd_mode_bool:
                if re.match(r'^$', row) is not None:
                    spd_mode_bool = False
                else:
                    spd_mode.append(row)
                    photo_spd.append(row.split(':'))
            if "Operation features:" in row or "Operational features:" in row:
                feat_mode_bool = True
            elif feat_mode_bool:
                if re.match(r'^$', row) is not None:
                    feat_mode_bool = False
                else:
                    final1 = re.sub(r'^-', "", row)
                    final = re.sub(r'\'$', "", final1)
                    feat_mode.append("<li>" + final + "</li>")
            if "Service ceiling:" in row:
                climb_mode_bool = True
                climb_mode.append(row)
            elif climb_mode_bool:
                if re.match(r'^$', row) is not None:
                    climb_mode_bool = False
                else:
                    climb_mode.append(row)
            if "Empty weight:" in row:
                weight_mode_bool = True
                weight_mode.append(row)
            elif weight_mode_bool:
                if re.match(r'^$', row) is not None:
                    weight_mode_bool = False
                else:
                    weight_mode.append(row)
            if "Maximum true air speed" in row:
                air_mode_bool = True
                air_mode.append(row)
            elif air_mode_bool:
                if re.match(r'^$', row) is not None:
                    air_mode_bool = False
                else:
                    weight_mode.append(row)
            if "Maximum performance turn" in row:
                turn_mode_bool = True
                turn_mode.append(row)
            elif turn_mode_bool:
                if re.match(r'^$', row) is not None:
                    turn_mode_bool = False
                else:
                    weight_mode.append(row)
            if "rated temperature" in row or "maximum temperature" in row:
                temp_mode_bool = True
                clean = re.sub(r'in\ engine\ ','',re.sub(r'temperature','temp',row))
                temp_mode.append(clean)
                photo_temp.append(clean.split(':'))
            elif temp_mode_bool:
                if re.match(r'^$', row) is not None:
                    temp_mode_bool = False
                else:
                    clean = re.sub(r'in\ engine\ ','',re.sub(r'temperature','temp',row))
                    temp_mode.append(clean)
                    photo_temp.append(clean.split(':'))
            if "Length:" in row:
                dim_mode_bool = True
                dim_mode.append(row)
            elif dim_mode_bool:
                if re.match(r'^$', row) is not None:
                    dim_mode_bool = False
                else:
                    dim_mode.append(row)
            if "Indicated stall speed" in row:
                stall_mode.append(row)
            if "Flight endurance at" in row:
                result = re.sub(":", ":</strong>", row)
                end_mode = "  endurance: <strong>" + result.strip() + "<br>\n"
                if "m," in row:
                    fuel_hr = re.sub(r'm,.*$', '', re.sub(r'^.*:','',row)).strip()
                    num = fuel_hr.split("h")
                    num_m = num[1]
                    num_h = num[0]
                    num_f = int(num_h) + (int(num_m)/60)
                    fuel_hr = str(round(num_f, 1))
                else:
                    fuel_hr = re.sub(r'h,.*$', '', re.sub(r'^.*:','',row)).strip()
                fuel_km = re.sub(r'km/h.*$', '', re.sub(r'^.*at\ ','',row)).strip()
                fuel_max_range = int(float(fuel_km)*float(fuel_hr))
                circus_bool = False
            else:
                circus_bool = True
                # print(line)

            if "Combat debut" in row:
                result = re.sub(":", ":</strong>", row)
                debut_mode = "  debut: <strong>" + result.strip() + "<br>\n"
                winfo = row.split(":")
                d_mode = "  " + re.sub(r'^.*\ ','',winfo[0].strip()) + ": " + re.sub(r'\D+','',winfo[1].strip()) + "\n"
            if "Dive speed limit" in row:
                result = re.sub(":", ":</strong>", row)
                dive_mode = "  dive: <strong>" + result.strip() + "<br>\n"

        if fuel_km:
            s_info.write("  circus: 0\n")
            photo_dict['circus'] = False
        else:
            s_info.write("  circus: 1\n")
            photo_dict['circus'] = True

        photo_dict['engine'] = photo_eng
        photo_dict['temp'] = photo_temp
        photo_dict['stall'] = photo_spd
        photo_lst.append(photo_dict)
        dds_dict[plane_id] = photo_dict

        if fuel_km:
            f_info.write("  circus:  0\n")
            f_info.write("  engine: |\n")
            for line in eng_mode:
                if re.match(r'^\(', line):
                    pass
                else:
                    result = re.sub(":", ":</strong><br>", line)
                    f_info.write("    <strong>" + result.strip() + "<br>\n")
            f_info.write("  speeds: |\n")
            for line in spd_mode:
                if re.match(r'^\(', line):
                    pass
                else:
                    result = re.sub(":", ":</strong><br>", line)
                    f_info.write("    <strong>" + result.strip() + "<br>\n")
            f_info.write("  climb: |\n")
            for line in climb_mode:
                if re.match(r'^\(', line):
                    pass
                else:
                    if re.match(r'Climb rate at.*:', line) or re.match(r'Service ceiling:', line):
                        result = re.sub(":", ":</strong>", line)
                        f_info.write("    <strong>" + result.strip() + "<br>\n")
            f_info.write("  weight: |\n")
            for line in weight_mode:
                if re.match(r'^\(', line):
                    pass
                else:
                    result = re.sub(":", ":</strong>", line)
                    f_info.write("    <strong>" + result.strip() + "<br>\n")
                    winfo = line.split(":")
                    if "Fuel load" in winfo[0]:
                        splitit = winfo[1].split("/")
                        # print(winfo))
                        clean = re.sub(r'l.*$','',splitit[1])
                        fuel_cap = clean.strip()
                        s_info.write("  " + re.sub(r'\ .*$','',winfo[0].strip()) + ": " + clean.strip() + "\n")
                        # print(plane_id)
                        fuel_per_hour = int(round(int(fuel_cap)/float(fuel_hr), 1))
                    else:
                        clean = re.sub(r'm.*$','',winfo[1])
                        clean2 = re.sub(r'kg.*$','',clean)
                        s_info.write("  " + re.sub(r'\ .*$','',winfo[0].strip()) + ": " + clean2.strip() + "\n")
            f_info.write("  temp: |\n")
            for line in temp_mode:
                if re.match(r'^\(', line):
                    pass
                else:
                    # if re.match(r'^.*intake.*$',line):
                    #     pass
                    # else:
                    result = re.sub(":", ":</strong><br>", line)
                    f_info.write("    <strong>" + result.strip() + "<br>\n")
            f_info.write("  max_air: |\n")
            for line in air_mode:
                if re.match(r'^\(', line):
                    pass
                else:
                    result = re.sub(":", ":</strong><br>", line)
                    f_info.write("    <strong>" + result.strip() + "<br>\n")
            f_info.write("  turn: |\n")
            for line in turn_mode:
                if re.match(r'^\(', line):
                    pass
                else:
                    result = re.sub(":", ":</strong><br>", line)
                    f_info.write("    <strong>" + result.strip() + "<br>\n")
            f_info.write("  dimensions: |\n")

            for line in dim_mode:
                if re.match(r'^\(', line):
                    pass
                else:
                    result = re.sub(":", ":</strong>", line)
                    f_info.write("    <strong>" + result.strip() + "<br>\n")
                    winfo = line.split(":")
                    # print(winfo)
                    clean = re.sub(r'm.*$','',winfo[1])
                    clean2 = re.sub(r'kg.*$','',clean)
                    s_info.write("  " + re.sub(r'\ .*$','',winfo[0].strip()) + ": " + clean2.strip() + "\n")
            f_info.write("  stall: |\n")
            for line in stall_mode:
                if re.match(r'^\(', line):
                    pass
                else:
                    clean = re.sub("&description='", "", line)
                    result = re.sub(":", ":</strong><br>", clean)
                    f_info.write("    <strong>" + result.strip() + "<br>\n")
            f_info.write("  features: |\n")
            for line in feat_mode:
                f_info.write("    " + line.strip() + "\n")
            f_info.write(end_mode)
            s_info.write("  fuel_lph: " + str(fuel_per_hour).strip() + "\n")
            s_info.write("  fuel_h: " + str(fuel_hr).strip() + "\n")
            s_info.write("  fuel_kmph: " + str(fuel_km).strip() + "\n")
            s_info.write("  fuel_maxrange: " + str(fuel_max_range).strip() + "\n")
            f_info.write("  fuel_lph: " + "<strong>Fuel Consumption per Hour:</strong> <br>" + str(fuel_per_hour).strip() + " L/hr<br>\n")
            f_info.write("  fuel_h: " + "<strong>Flight Time on Full Tank:</strong> <br>" + str(fuel_hr).strip() + " hr<br>\n")
            f_info.write("  fuel_kmph: " + "<strong>Assumed Cruise Speed :</strong> <br>" + str(fuel_km).strip() + " km/hr<br>\n")
            f_info.write("  fuel_maxrange: " + "<strong>Max Range on Full Tank:</strong> <br>" + str(fuel_max_range).strip() + " km<br>\n")
            f_info.write("  fuel_cap: " + "<strong>Max Fuel Capacity:</strong> <br>" + str(fuel_cap).strip() + " L<br>\n")
            f_info.write(debut_mode)
            s_info.write(d_mode)

            f_info.write(dive_mode)
        else:
            f_info.write(circus)
            short = re.sub(r'\ .*$','', p_name_circus)
            l_circus.append(short.lower()) 
    s_info.close()
    f_info.close()
    with open('photo.json', 'w') as f:
        json.dump(photo_lst, f, indent=4, sort_keys=True)

    with open("circus.csv", "w", encoding="utf8") as circus:
        for line in l_circus:
            circus.write('"' + line + '"' + ",\n")
        # circus.write(line[0] + "," + line[1] +  "," + line[2] + "\n")

    # print(plane_texts) Empty weight:


# Extract Data from unzipped swf GTP file
# extract_data()
master_yml()