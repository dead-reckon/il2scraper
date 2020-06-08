import csv
import re
import os
import shutil

def file_to_array():
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
    for line in plane_texts:
        path_to_file = info_path + "/" + line
        # print("Reading File: " + path_to_file)
        raw = open(path_to_file, "r", encoding="utf8")
        data = raw.read().split("\n")
        raw.close()

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

        circus_bool = False
        circus = ""

        for row in data:
            if "&name" in row:
                plane_id = re.sub(r'\.txt', '', line)
                final = re.sub(r'^.*&name=', '', row)
                p_id_circus = plane_id
                p_name_circus = final
                f_info.write("- id: " + plane_id + "\n")
                f_info.write("  name: " + final + "\n")
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
                    eng_mode.append(row) 
            if "Takeoff speed:" in row:
                spd_mode_bool = True
                spd_mode.append(row)
            elif spd_mode_bool:
                if re.match(r'^$', row) is not None:
                    spd_mode_bool = False
                else:
                    spd_mode.append(row)
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
                temp_mode.append(row)
            elif temp_mode_bool:
                if re.match(r'^$', row) is not None:
                    temp_mode_bool = False
                else:
                    temp_mode.append(row)
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
            if "Combat debut" in row:
                result = re.sub(":", ":</strong>", row)
                debut_mode = "  debut: <strong>" + result.strip() + "<br>\n"
                winfo = row.split(":")
                d_mode = "  " + re.sub(r'^.*\ ','',winfo[0].strip()) + ": " + re.sub(r'\D+','',winfo[1].strip()) + "\n"
            if "Dive speed limit" in row:
                result = re.sub(":", ":</strong>", row)
                dive_mode = "  dive: <strong>" + result.strip() + "<br>\n"

        if circus:
            f_info.write(circus)
            short = re.sub(r'\ .*$','', p_name_circus)
            l_circus.append(short.lower())
        else:
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
            s_info.write("- name: "+ p_name_circus +"\n")
            for line in weight_mode:
                if re.match(r'^\(', line):
                    pass
                else:
                    result = re.sub(":", ":</strong>", line)
                    f_info.write("    <strong>" + result.strip() + "<br>\n")
                    winfo = line.split(":")
                    if "Fuel load" in winfo[0]:
                        splitit = winfo[1].split("/")
                        # print(winfo)
                        print(splitit)
                        clean = re.sub(r'l.*$','',splitit[1])
                        s_info.write("  " + re.sub(r'\ .*$','',winfo[0].strip()) + ": " + clean.strip() + "\n")
                    else:
                        clean = re.sub(r'm.*$','',winfo[1])
                        clean2 = re.sub(r'kg.*$','',clean)
                        s_info.write("  " + re.sub(r'\ .*$','',winfo[0].strip()) + ": " + clean2.strip() + "\n")
            f_info.write("  temp: |\n")
            for line in temp_mode:
                if re.match(r'^\(', line):
                    pass
                else:
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
            f_info.write(debut_mode)
            s_info.write(d_mode)
            f_info.write(dive_mode)
            
    s_info.close()
    f_info.close()

    with open("circus.csv", "w", encoding="utf8") as circus:
        for line in l_circus:
            circus.write('"' + line + '"' + ",\n")
        # circus.write(line[0] + "," + line[1] +  "," + line[2] + "\n")

    # print(plane_texts) Empty weight:


# Extract Data from unzipped swf GTP file
# extract_data()
master_yml()

# Old Code
list_meta = [ "Takeoff speed", 
            "Glideslope speed", 
            "Landing speed" , 
            "Service ceiling", 
            "Dive speed limit",
            "Climb rate at sea level",
            "Climb rate at 3000 m",
            "Climb rate at 6000 m",
            "Flight endurance at 3000 m",
            "Fuel load",
            "Supercharger",
            "Indicated stall speed",
            "Maximum performance turn"]

list_engine = [ "Nominal",
                "Combat power",
                "Emergency power",
                "Boosted power",
                "Take-off power",
                "Max Cruising power",
                "International power",
                "Emergency Max All",
                "Climb power",
                "Model"]

list_speed = [ "Nominal",
                "Combat power",
                "Emergency power",
                "Boosted power",
                "Take-off power",
                "Max Cruising power",
                "International power",
                "Emergency Max All",
                "Climb power",
                "Model"]

def engine_settings(info, search_list):
    file = open("engine.md", "w")

    plane_name = ""

    for line in info:
        if re.search("## ",line):
            file.write(line)
        for row in search_list:
            if re.match(row, line):
                file.write("\n" + line)
    file.close()

def op_features(info):
    file = open("op.md", "w")

    plane_name = ""

    for line in info:
        if re.search("## ",line):
            file.write("\n" + line)
        if re.match('-', line):
            file.write("\n" + line)
    file.close()

def airspeed(info):
    file = open("airspeed.md", "w")

    plane_name = ""

    for line in info:
        if re.search("## ",line):
            file.write("\n" + line)
        if re.match('Maximum true air speed', line):
            file.write("\n" + line)
    file.close()

def oil_water_temp(info):
    file = open("oil_water.md", "w")

    plane_name = ""

    for line in info:
        if re.search("## ",line):
            file.write("\n" + line)
        elif re.match('Oil cap', line):
            pass
        elif re.match('Oil', line) or re.match('Water', line):
            file.write("\n" + line)
    file.close()

def plane_meta(info,search_list):
    # Contains; takeoff/glideslope/landing speeds, dive speed limit, service ceiling, climb rate sea/3k/6k
    file = open("meta.md", "w")

    plane_name = ""

    for line in info:
        if re.search("## ",line):
            file.write(line)
        for row in search_list:
            if re.match(row, line):
                file.write("\n" + line)
    file.close()

# Generate Log of Plane list on exectuion
# generate_log(forum_scrape(html))

#plane_meta(forum_scrape(html),list_meta)
#op_features(forum_scrape(html))
#oil_water_temp(forum_scrape(html))
#engine_settings(forum_scrape(html),list_engine)
#airspeed(forum_scrape(html))