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

def alt_parse(planes):
    result = []
    # print(planes)

    with open("ct.yml", "w", encoding="utf8") as ct:
        # ct.write("- id: {0} \n".format(planes['id']))
        # ct.write("  name: {0} \n".format(planes['name']))
        for line in planes:
            # for row in line:
            #     print(row)
            # print(line)
            if "xx" in line[0]:
                ct.write("- id: {0} \n".format(line[1]))
                ct.write("  name: {0} \n".format(line[2]))
            # print(data[0])
            # if re.match(r'^0$',plane):
            #     return val
            # elif re.match(r'^1000$',plane):
            #     return val
            # elif re.match(r'^2000$',plane):
            #     return val 
            # elif re.match(r'^3000$',plane):
            #     return val 
            # elif re.match(r'^4000$',plane):
            #     return val 
            # elif re.match(r'^5000$',plane):
            #     return val
            # elif re.match(r'^6000$',plane):
            #     return val
            # elif re.match(r'^7000$',plane):
            #     return val 
            # else:
            #     return Null
            pass


def parse_ai():
    path = os.getcwd()
    ai_path = path + "/Ai"
    ai_dir = os.listdir(ai_path)

    list_plane = []

    lst_ai = []
    
    list_speed = []
    
    list_ct = []
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
                        lst_climb_time.append([d_set[0].strip(),d_set[1].strip()])
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

        alt_parse(list_climb_time)
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


# extract_src()
parse_ai()
