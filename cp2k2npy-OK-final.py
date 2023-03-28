import numpy as np
import matplotlib.pyplot as plt


#################################

################################################
project_name=input("Please input CP2K  project name:")
coord_name = project_name + "-pos-1.xyz"
force_name = project_name + "-frc-1.xyz"
energy_name = project_name + "-1.ener"
box_name = project_name + "-1.cell" 

energy_npy ="./" + project_name + "/set.000/energy.npy"
force_npy ="./" + project_name + "/set.000/force.npy"
coord_npy ="./" + project_name + "/set.000/coord.npy"
box_npy = "./" + project_name + "/set.000/box.npy"
type_raw ="./" + project_name + "/type.raw"
type_map_raw ="./" + project_name + "/type_map.raw"
#####################################

#
#####################################
temp_file = open(energy_name,"r")
lines = temp_file.readlines()
print(lines)
fram_num = len(lines) - 1
print("fram_num",fram_num)
energy_array = np.zeros(fram_num)
for i in range(fram_num):
	energy_array[i] = float(lines[i+1].split()[4])
print(energy_array)
np.save(energy_npy,energy_array)


temp_file.close()
######################################
"""
tmp_data=np.genfromtxt(path+eng_name, names=True)
for name in tmp_data.dtype.names[1:-1]:
    plt.plot(tmp_data['StepNr'],tmp_data[name], label=name)
frames=len(tmp_data['StepNr'])

print(frames)
#print(tmp_data['Pot'])
ss=tmp_data['Pot']
eng_array=np.array(tmp_data['Pot'])
#print(eng_array)
np.save('./data/set.000/energy',eng_array)
#print(tmp_data['Pot.[a.u.]'])

##################################
#
# type.raw,type_map.raw
#
##################################
"""
coord_f=open(coord_name,'r')
atoms_line = coord_f.readline()
print(atoms_line)
atoms=int(atoms_line)
print(atoms)
type_r=open(type_raw,'w',encoding='utf-8')
type_map=open(type_map_raw,'w',encoding='utf-8')
temp_c=''
atoms_line = coord_f.readline()
symbol_c = -1
temp_str=""
for i in range(atoms):
    tmp_line = coord_f.readline()
    type_str=str.split(tmp_line)
    #type_r.write(type_str[0]+'\n')
    
    if temp_c != type_str[0]:
        temp_c = type_str[0] 
        type_map.write(type_str[0]+'\n') 
        symbol_c = symbol_c + 1
    #print(symbol_c)
    temp_str += str(symbol_c)+"\n"

type_r.writelines(temp_str)
print(temp_str)
type_r.close()
type_map.close()
coord_f.close()


########################################
#
# read ans write coord
#
#######################################
coord_array=np.zeros((fram_num,3*atoms))
coord_line=np.zeros((1,3*atoms))
coord_f=open(coord_name,'r')
for i in range(fram_num):
    tmp_line = coord_f.readline()
    tmp_line = coord_f.readline()
    for j in range(atoms):
        tmp_line = coord_f.readline()
        xyz_str=str.split(tmp_line)
        coord_line[0,3*j]=float(xyz_str[1])
        coord_line[0,3*j+1]=float(xyz_str[2])
        coord_line[0,3*j+2]=float(xyz_str[3])
        #print(xyz_str)
        #print(coord_line)
    coord_array[i]=coord_line
#print(coord_array[1])
np.save(coord_npy,coord_array)
coord_f.close()
################################
#
#read and write force
#
################################

force_array=np.zeros((fram_num,3*atoms))
force_line=np.zeros((1,3*atoms))
force_f=open(force_name,'r')
for i in range(fram_num):
    tmp_line = force_f.readline()
    tmp_line = force_f.readline()
    for j in range(atoms):
        tmp_line = force_f.readline()
        xyz_str=str.split(tmp_line)
        force_line[0,3*j]=float(xyz_str[1])
        force_line[0,3*j+1]=float(xyz_str[2])
        force_line[0,3*j+2]=float(xyz_str[3])
        #print(xyz_str)
        #print(coord_line)
    force_array[i]=force_line
#print(force_array[1])
np.save(force_npy,force_array)
force_f.close()

################################
#
#read and write CELL
#
################################
box_array=np.zeros((fram_num,3*3))
box_f=open(box_name,'r')
tmp_line = box_f.readline()
for i in range(fram_num):
#    tmp_line = force_f.readline()
    tmp_line = box_f.readline()
    xyz_str=str.split(tmp_line)
    #print(xyz_str)
    box_array[i,0]=float(xyz_str[2])
    box_array[i,1]=float(xyz_str[3])
    box_array[i,2]=float(xyz_str[4])
    box_array[i,3]=float(xyz_str[5])
    box_array[i,4]=float(xyz_str[6])
    box_array[i,5]=float(xyz_str[7])
    box_array[i,6]=float(xyz_str[8])
    box_array[i,7]=float(xyz_str[9])
    box_array[i,8]=float(xyz_str[10])

np.save(box_npy,box_array)
box_f.close()

