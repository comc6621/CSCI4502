#Conors imports
import sys
import arff
import os
import csv

path = sys.argv[1]
file_ = '''
%
@RELATION weather

@ATTRIBUTE id NUMERIC
@ATTRIBUTE Subject NUMERIC
@ATTRIBUTE Relation STRING
@ATTRIBUTE Object NUMERIC


@DATA
%
%
% '''
def getDescription():
    description = input('Enter a description for the arff file:')
    return description

def get_Attribute_Info():
    attributeTuple = [
    ('subject_time_stamp','STRING'),
    ('subject_name','STRING'),
    ('subject_description','STRING'),
    ('subject_url','STRING'),
    ('subject_lastmod','STRING'),
    ('subject_gid','STRING'),
    ('subject_owner_id','STRING'),
    ('subject_image','STRING'),
    ('subject_lat','STRING'),
    ('subject_longitude','STRING'),
    ('subject_cTmp','STRING'),
    ('subject_roleName','STRING'),
    ('subject_tagName','STRING'),
    ('obj_time_stamp','STRING'),
    ('obj_name','STRING'),
    ('obj_description','STRING'),
    ('obj_url','STRING'),
    ('obj_lastmod','STRING'),
    ('obj_gid','STRING'),
    ('obj_owner_id','STRING'),
    ('obj_image','STRING'),
    ('obj_lat','STRING'),
    ('obj_longitude','STRING'),
    ('obj_cTmp','STRING'),
    ('obj_roleName','STRING'),
    ('obj_tagName','STRING'),
    ('relationTableID','STRING'),
    ('obj_id','STRING'),
    ('relationship_id','STRING'),
    ('subject_id','STRING'),
    ('tmp','STRING'),
    ('relationship_name','STRING'),
    ('relationship_description','STRING'),
    ('relationship_type','STRING'),
    ('relationship_inverse','STRING'),
    ('relationship_inverse_id','STRING'),
    ('subject_group_number','STRING'),
    ('subject_owner_role','STRING'),
    ('subject_owner_user_id','STRING') 
    ]
    return attributeTuple
def dump_arff(dictionary, sheetName):
    arffdump = arff.dumps(dictionary)
    #Create arff file with name of sheet as name
    file = open(sheetName+'.arff','w+')
    #write data into arff file
    file.write(arffdump)
    #close file
    file.close()


############################
dataArffDictionary=arff.loads(file_)

#get description for data arff file
arffDescription = getDescription()
dataArffDictionary['description'] = arffDescription
print ("Program Completed!")

#Get attributes
attribute=get_Attribute_Info()
#add attribute info to arff dictionary
dataArffDictionary['attributes'] = attribute

#OPEN
rowList=[]
with open(path,"r") as ifile:
    reader = csv.reader(ifile)
    rowNumber = 0
    for row in reader:
        if rowNumber == 0:
            print ("row1")
            rowNumber+=1
        else:
            rowNumber+=1
            for value in row:
                if "," in value:
                    value = value.replace(",", ";")
            rowList.append(row)

dataArffDictionary['data']= rowList
dump_arff(dataArffDictionary, "DataV2")
 #Close
ifile.close()