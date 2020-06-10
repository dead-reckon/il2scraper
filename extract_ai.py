import csv
import re
import os
import shutil
import codecs


def extract_src():
    path = os.getcwd()
    src_ai = path + "/(null)/luascripts/ai"
    src_dir = os.listdir(src_ai)
    # print(src_dir)

    ai_path = path + "/Ai"
    if os.path.isdir(ai_path):
        shutil.rmtree(ai_path)
    else:
        os.mkdir(ai_path)

    for line in src_dir:
        if "caeroplane.txt" in line or "cplaneai.txt" in line:
            pass
        else:
            src_name = src_ai + "/" + line
            final_name = re.sub(r'caeroplane_','', line)
            tgt_name = ai_path + "/" + final_name

            shutil.copy2(src_name,tgt_name)




def parse_ai():
    path = os.getcwd()
    ai_path = path + "/Ai"
    ai_dir = os.listdir(ai_path)

    list_plane = []

    lst_ai = []
    
    list_speed = []
    
    list_max_alt = []
    list_turn = []
    list_turn_optimal = []

    plane_type = [
                    ['Fighter','1'],
                    ['Heavy Fighter','2'],
                    ['Light Bomber','3'],
                    ['Bomber','4'],
                    ['Light Recon','5'],
                    ['Recon','6'],
                    ['Shturmovik','7'],
                    ['Cargo','8']
                ]
    for line in ai_dir:
        filename = ai_path + "/" + line
        plid = re.sub(r'\.txt.*$','',line)
        with open(filename, "r",encoding="ascii", errors="backslashreplace") as lst:
            data = lst.read().split("\n")
            plane_name = data[2]

            dict_ai = []

            lst_climb_time = []
            lst_max_alt = []
            lst_turn = []
            lst_turn_optimal = []
            list_climb_time = []

            list_ctn_var1 = []
            list_ctn_var2 =[]

            if 'xf3-2' in plane_name:
                dict_ai = {'name': 'PO 2 VS'}
                # list_climb_time = {'id' : plid}
                # list_climb_time['name'] = dict_ai['name']
                # lst_climb_time.append("xx"+plid+","+dict_ai['name'])
                lst_climb_time.append(["xx",plid,dict_ai['name']])
            else:
                dict_ai = {'name': re.sub(r'^.*//\ ','',plane_name).strip()}
                # list_climb_time = {'id' : plid}
                # list_climb_time['name'] = dict_ai['name']
                # lst_climb_time.append("xx,"+plid+","+dict_ai['name'])
                lst_climb_time.append(["xx",plid,dict_ai['name']])

            for row in data:

                if "//" not in row:
                    if "ClimbTime" in row:
                        clean = re.sub(r'^.*=\ ','', row)
                        d_set = clean.split(",")
                        list_ctn_var1.append(d_set[0].strip())
                        list_ctn_var2.append(d_set[1].strip())
                        # lst_climb_time.append([d_set[0].strip(),d_set[1].strip()])
                        # lst_climb_time.append([d_set[0].strip() +","+d_set[1].strip()])
                    elif "MaxAltTAS" in row:
                        clean = re.sub(r'^.*=\ ','', row)
                        d_set = clean.split(",")
                        lst_max_alt.append([dict_ai['name'],d_set[0].strip(),d_set[1].strip()])
                    elif "TurnTimeAlt" in row:
                        clean = re.sub(r'^.*=\ ','', row)
                        d_set = clean.split(",")
                        lst_turn.append([dict_ai['name'],d_set[0].strip(),d_set[1].strip()])
                    elif "TurnOptimal_CAS_Alt" in row:
                        clean = re.sub(r'^.*=\ ','', row)
                        d_set = clean.split(",")
                        lst_turn_optimal.append([dict_ai['name'],d_set[0].strip(),d_set[1].strip()])

                if "MaxSpeed" in row:
                    clean1 = row.strip()
                    final = re.sub(r'\\.*$','',re.sub(r'//.*$','',re.sub(r'^.*=\ ','', row)))
                    dict_ai['MaxSpeed'] = final # 
                elif "MaxClimbRate" in row:
                    clean1 = row.strip()
                    final = re.sub(r'\\.*$','',re.sub(r'//.*$','',re.sub(r'^.*=\ ','', row)))
                    dict_ai['MaxClimbRate'] = final
                elif "ServiceCeiling" in row:
                    clean1 = row.strip()
                    final = re.sub(r'\\.*$','',re.sub(r'//.*$','',re.sub(r'^.*=\ ','', row)))
                    dict_ai['ServiceCeiling'] = final
                elif "TurnRate" in row:
                    clean1 = row.strip()
                    final = re.sub(r'\\.*$','',re.sub(r'//.*$','',re.sub(r'^.*=\ ','', row)))
                    dict_ai['TurnRate'] = final
                elif "MaxClimbCAS" in row:
                    clean1 = row.strip()
                    final = re.sub(r'\\.*$','',re.sub(r'//.*$','',re.sub(r'^.*=\ ','', row)))
                    dict_ai['MaxClimbCAS'] = final
                elif "DiveCAS" in row:
                    clean1 = row.strip()
                    final = re.sub(r'\\.*$','',re.sub(r'//.*$','',re.sub(r'^.*=\ ','', row)))
                    dict_ai['DiveCAS'] = final
                elif "CruiseCAS" in row:
                    clean1 = row.strip()
                    final = re.sub(r'\\.*$','',re.sub(r'//.*$','',re.sub(r'^.*=\ ','', row)))
                    dict_ai['CruiseCAS'] = final
                elif "ClimbCAS" in row:
                    clean1 = row.strip()
                    final = re.sub(r'\\.*$','',re.sub(r'//.*$','',re.sub(r'^.*=\ ','', row)))
                    dict_ai['ClimbCAS'] = final
                elif "PriorityType" in row:
                    clean1 = row.strip()
                    final = re.sub(r'\\.*$','',re.sub(r'//.*$','',re.sub(r'^.*=\ ','', row)))
                    result = ""
                    for pln in plane_type:
                        if pln[1] in final:
                            result = pln[0]
                    dict_ai['PriorityType'] = result
                else:
                    pass

            # list_climb_time['data'] = lst_climb_time
            list_climb_time.append(lst_climb_time)

            lst_ai.append(dict_ai)

        # alt_parse(list_climb_time)
        # print(lst_climb_time)

    datafile = path + "/ai.yml"
    dfile = open(datafile, "w", encoding="utf8")
    for line in lst_ai:
        dfile.write("- name: " + line['name'] + "\n")
        dfile.write("  MaxSpeed: " + line['MaxSpeed'] + "\n")
        dfile.write("  MaxClimbRate: " + line['MaxClimbRate'] + "\n")
        dfile.write("  ServiceCeiling: " + line['ServiceCeiling'] + "\n")
        dfile.write("  TurnRate: " + line['TurnRate'] + "\n")
        dfile.write("  MaxClimbCAS: " + line['MaxClimbCAS'] + "\n")
        dfile.write("  DiveCAS: " + line['DiveCAS'] + "\n")
        dfile.write("  CruiseCAS: " + line['CruiseCAS'] + "\n")
        dfile.write("  ClimbCAS: " + line['ClimbCAS'] + "\n")
        dfile.write("  PriorityType: " + line['PriorityType'] + "\n")
    dfile.close()

    # for line in lst_ai:
    #     print("{:<30}{:<30}".format(line['name'],line['PriorityType']))
    # print (lst_ai[0])


def listToString(s):  
    str1 = ", " 
    return (str1.join(s))


def get_colors(n):  
    color_pairs = [
                    ["CadetBlue","BurlyWood"],
                    ["Chartreuse","CadetBlue"],
                    ["Chocolate","Chartreuse"],
                    ["Coral","Chocolate"],
                    ["CornflowerBlue","Coral"],
                    ["Crimson","CornflowerBlue"],
                    ["Cyan","Crimson"],
                    ["DarkBlue","Cyan"],
                    ["DarkCyan","DarkBlue"],
                    ["DarkGoldenRod","DarkCyan"],
                    ["DarkGray","DarkGoldenRod"],
                    ["DarkGreen","DarkGray"],
                    ["DarkKhaki","DarkGreen"],
                    ["DarkMagenta","DarkKhaki"],
                    ["DarkOliveGreen","DarkMagenta"],
                    ["DarkOrange","DarkOliveGreen"],
                    ["DarkOrchid","DarkOrange"],
                    ["DarkRed","DarkOrchid"],
                    ["DarkSalmon","DarkRed"],
                    ["DarkSeaGreen","DarkSalmon"],
                    ["DarkSlateBlue","DarkSeaGreen"],
                    ["DarkSlateGrey","DarkSlateBlue"],
                    ["DarkTurquoise","DarkSlateGrey"],
                    ["DarkViolet","DarkTurquoise"],
                    ["DeepPink","DarkViolet"],
                    ["DeepSkyBlue","DeepPink"],
                    ["DimGray","DeepSkyBlue"],
                    ["DodgerBlue","DimGray"],
                    ["FireBrick","DodgerBlue"],
                    ["ForestGreen","FireBrick"],
                    ["Fuchsia","ForestGreen"],
                    ["Gainsboro","Fuchsia"],
                    ["Gold","Gainsboro"],
                    ["GoldenRod","Gold"],
                    ["Gray","GoldenRod"],
                    ["Green","Gray"],
                    ["GreenYellow","Green"],
                    ["HotPink","GreenYellow"],
                    ["Brown","BlueViolet"],
                    ["BurlyWood","Brown"],
                    ["CadetBlue","BurlyWood"],
                    ["Chartreuse","CadetBlue"],
                    ["Chocolate","Chartreuse"],
                    ["Coral","Chocolate"],
                    ["CornflowerBlue","Coral"],
                    ["Crimson","CornflowerBlue"],
                    ["Cyan","Crimson"],
                    ["DarkBlue","Cyan"],
                    ["DarkCyan","DarkBlue"],
                    ["DarkGoldenRod","DarkCyan"],
                    ["DarkGray","DarkGoldenRod"],
                    ["DarkGreen","DarkGray"],
                    ["DarkKhaki","DarkGreen"],
                    ["DarkMagenta","DarkKhaki"],
                    ["DarkOliveGreen","DarkMagenta"],
                    ["DarkOrange","DarkOliveGreen"],
                    ["DarkOrchid","DarkOrange"],
                    ["DarkRed","DarkOrchid"],
                    ["DarkSalmon","DarkRed"],
                    ["DarkSeaGreen","DarkSalmon"],
                    ["DarkSlateBlue","DarkSeaGreen"],
                    ["DarkSlateGrey","DarkSlateBlue"],
                    ["DarkTurquoise","DarkSlateGrey"],
                    ["DarkViolet","DarkTurquoise"],
                    ["DeepPink","DarkViolet"],
                    ["DeepSkyBlue","DeepPink"],
                    ["DimGray","DeepSkyBlue"],
                    ["DodgerBlue","DimGray"],
                    ["FireBrick","DodgerBlue"],
                    ["ForestGreen","FireBrick"],
                    ["Fuchsia","ForestGreen"],
                    ["Gainsboro","Fuchsia"],
                    ["Gold","Gainsboro"],
                    ["GoldenRod","Gold"],
                    ["Gray","GoldenRod"],
                    ["Green","Gray"],
                    ["Blue","Black"],
                    ["BlueViolet","Blue"],
                    ["Brown","BlueViolet"],
                    ["BurlyWood","Brown"],
                    ["CadetBlue","BurlyWood"],
                    ["Chartreuse","CadetBlue"],
                    ["Chocolate","Chartreuse"],
                    ["Coral","Chocolate"],
                    ["CornflowerBlue","Coral"],
                    ["Crimson","CornflowerBlue"],
                    ["Cyan","Crimson"],
                    ["DarkBlue","Cyan"],
                    ["DarkCyan","DarkBlue"],
                    ["DarkGoldenRod","DarkCyan"],
                    ["DarkGray","DarkGoldenRod"],
                    ["DarkGreen","DarkGray"],
                    ["DarkKhaki","DarkGreen"],
                    ["DarkMagenta","DarkKhaki"],
                    ["DarkOliveGreen","DarkMagenta"],
                    ["DarkOrange","DarkOliveGreen"],
                    ["DarkOrchid","DarkOrange"],
                    ["DarkRed","DarkOrchid"],
                    ["DarkSalmon","DarkRed"],
                    ["DarkSeaGreen","DarkSalmon"],
                    ["DarkSlateBlue","DarkSeaGreen"],
                    ["DarkSlateGrey","DarkSlateBlue"],
                    ["DarkTurquoise","DarkSlateGrey"],
                    ["DarkViolet","DarkTurquoise"],
                    ["DeepPink","DarkViolet"],
                    ["DeepSkyBlue","DeepPink"],
                    ["DimGray","DeepSkyBlue"],
                    ["DodgerBlue","DimGray"],
                    ["FireBrick","DodgerBlue"],
                    ["ForestGreen","FireBrick"],
                    ["Fuchsia","ForestGreen"]
                ]

    return color_pairs[n]

def alt_parse():
    path = os.getcwd()
    ai_path = path + "/Ai"
    ai_dir = os.listdir(ai_path)

    lst_ct = []
    lst_cas = []
    lst_tas = []
    lst_tta = []

    for line in ai_dir:
        filename = ai_path + "/" + line
        plid = re.sub(r'\.txt.*$','',line)
        # print(filename)
        with open(filename, "r",encoding="ascii", errors="backslashreplace") as lst:
            data = lst.read().split("\n")
            plane_name = data[2]
            d_plane_ct = {}
            l_stats_ct =[]
            d_plane_cas = {}
            l_stats_cas =[]
            d_plane_tas = {}
            l_stats_tas =[]
            d_plane_tta = {}
            l_stats_tta =[]

            if 'xf3-2' in plane_name:
                d_plane_ct = {'name': 'PO 2 VS'}
                d_plane_cas = {'name': 'PO 2 VS'}
                d_plane_tas = {'name': 'PO 2 VS'}
                d_plane_tta = {'name': 'PO 2 VS'}
                d_plane_ct['id'] = plid
                d_plane_cas['id'] = plid
                d_plane_tas['id'] = plid
                d_plane_tta['id'] = plid
            else:
                d_plane_ct = {'name': re.sub(r'^.*//\ ','',plane_name).strip()}
                d_plane_cas = {'name': re.sub(r'^.*//\ ','',plane_name).strip()}
                d_plane_tas = {'name': re.sub(r'^.*//\ ','',plane_name).strip()}
                d_plane_tta = {'name': re.sub(r'^.*//\ ','',plane_name).strip()}
                d_plane_ct['id'] = plid
                d_plane_cas['id'] = plid
                d_plane_tas['id'] = plid
                d_plane_tta['id'] = plid

            for row in data:

                if "//" not in row:
                    if "ClimbTime" in row:
                        clean = re.sub(r'^.*=\ ','', row)
                        d_set = clean.split(",")
                        l_stats_ct.append(d_set)
                        
                    elif "MaxAltTAS" in row:
                        clean = re.sub(r'^.*=\ ','', row)
                        d_set = clean.split(",")
                        l_stats_cas.append(d_set)
                        
                    elif "TurnTimeAlt" in row:
                        clean = re.sub(r'^.*=\ ','', row)
                        d_set = clean.split(",")
                        l_stats_tas.append(d_set)
                        
                    elif "TurnOptimal_CAS_Alt" in row:
                        clean = re.sub(r'^.*=\ ','', row)
                        d_set = clean.split(",")
                        l_stats_tta.append(d_set)

        d_plane_ct['info'] = l_stats_ct
        lst_ct.append(d_plane_ct)
        d_plane_cas['info'] = l_stats_cas
        lst_cas.append(d_plane_cas)
        d_plane_tas['info'] = l_stats_tas
        lst_tas.append(d_plane_tas)
        d_plane_tta['info'] = l_stats_tta
        lst_tta.append(d_plane_tta)
         
    # print(lst_plane)

    with open("ct.yml", "w", encoding="utf8") as ct:
        num = 0
        for line in lst_ct:
            colors = get_colors(num)
            alt = []
            spd = []
            circus = []
            ct.write("- name: " + line['name'] + "\n")
            ct.write("  id: " + line['id'] + "\n")
            for d in line['info']:
                alt.append(d[0].strip())
                spd.append(d[1].strip())

                if "1500" in str(alt) or "2500" in str(alt):
                    circus = "1"
                else:
                    circus = "0"

            ct.write("  alt: " + listToString(alt) + "\n")
            ct.write("  spd: " + listToString(spd) + "\n")
            ct.write("  bgc: " + colors[0] + "\n")
            ct.write("  bc: " + colors[1] + "\n")
            ct.write("  circus: " + circus + "\n")
            num = num+1

    with open("cas.yml", "w", encoding="utf8") as ct:
        num = 0
        for line in lst_cas:
            colors = get_colors(num)
            alt = []
            spd = []
            circus = []
            ct.write("- name: " + line['name'] + "\n")
            ct.write("  id: " + line['id'] + "\n")
            for d in line['info']:
                alt.append(d[0].strip())
                spd.append(d[1].strip())

                if "1500" in str(alt) or "2500" in str(alt):
                    circus = "1"
                else:
                    circus = "0"

            ct.write("  alt: " + listToString(alt) + "\n")
            ct.write("  spd: " + listToString(spd) + "\n")
            ct.write("  bgc: " + colors[0] + "\n")
            ct.write("  bc: " + colors[1] + "\n")
            ct.write("  circus: " + circus + "\n")
            num = num+1

    with open("tas.yml", "w", encoding="utf8") as ct:
        num = 0
        for line in lst_tas:
            colors = get_colors(num)
            alt = []
            spd = []
            circus = []
            ct.write("- name: " + line['name'] + "\n")
            ct.write("  id: " + line['id'] + "\n")
            for d in line['info']:
                alt.append(d[0].strip())
                spd.append(d[1].strip())

                if "1500" in str(alt) or "2500" in str(alt):
                    circus = "1"
                else:
                    circus = "0"

            ct.write("  alt: " + listToString(alt) + "\n")
            ct.write("  spd: " + listToString(spd) + "\n")
            ct.write("  bgc: " + colors[0] + "\n")
            ct.write("  bc: " + colors[1] + "\n")
            ct.write("  circus: " + circus + "\n")
            num = num+1

    with open("tta.yml", "w", encoding="utf8") as ct:
        num = 0
        for line in lst_tta:
            colors = get_colors(num)
            alt = []
            spd = []
            circus = []
            ct.write("- name: " + line['name'] + "\n")
            ct.write("  id: " + line['id'] + "\n")
            for d in line['info']:
                alt.append(d[0].strip())
                spd.append(d[1].strip())

                if "1500" in str(alt) or "2500" in str(alt):
                    circus = "1"
                else:
                    circus = "0"

            ct.write("  alt: " + listToString(alt) + "\n")
            ct.write("  spd: " + listToString(spd) + "\n")
            ct.write("  bgc: " + colors[0] + "\n")
            ct.write("  bc: " + colors[1] + "\n")
            ct.write("  circus: " + circus + "\n")
            num = num+1


# extract_src()
# parse_ai()
alt_parse()