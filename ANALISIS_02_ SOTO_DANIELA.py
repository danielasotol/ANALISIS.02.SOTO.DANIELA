# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Import data and generate list

import csv 

with open("synergy_logistics_database.csv","r") as file_csv:
    read = csv.reader(file_csv)
    data = []
    imports=[]
    exports=[]
    for line in read:
        data.append(line)
    data.pop(0)

    # Separate imports and exports
    
    for i in data:
        if i[1] == "Imports":
            imports.append(i)
            
    for i in data:
        if i[1] == "Exports":
            exports.append(i)
            
##### FUNCTIONS ######

# Pairs without rep
    def unique_list(original,place1,place2, final):
        list_aux= []
        
        for i in original:
            if [i[place1],i[place2]] not in list_aux:
                aux =[]
                aux= [i[place1],i[place2]]
                list_aux.append(aux)
                aux2 = []
                aux2 = [i[place1],i[place2],1]
                final.append(aux2)
        
# Counter for the number of reps 
    def counter_list(original,place1,place2, final):
        for i in range(len(final)):
            for j in range(len(original)):
                if final[i][0] == original[j][place1]:
                    if final[i][1] == original[j][place2]:
                        final[i][2] += 1
        
# Sum number from reppeated values
    def sum_list(original,place1,place2, final):
        for i in range(len(final)):
            for j in range(len(original)):
                if final[i][0] == original[j][place1]:
                    aux = 0
                    aux = int(original[j][place2])
                    final[i][1] = final[i][1] + aux
                    
# Create list with sublists and zero. 
 
    def short_list(original,place1, final):
        for i in original:
            aux = []
            aux = [i[place1],0]
            final.append(aux)                      
                        
#### CODE ####
 
# List of movements, imports and exports per route
    
    tot_routes = []
    unique_list(data,2,3,tot_routes)  
    counter_list(data,2,3,tot_routes)  
    
    imp_routes = []    
    unique_list(imports,2,3,imp_routes)  
    counter_list(imports,2,3,imp_routes)  
    
    exp_routes = []    
    unique_list(exports,2,3,exp_routes) 
    counter_list(exports,2,3,exp_routes) 

    
# Top 10 routes (imports and exports )   

    top_tot = []
    tot_routes = sorted(tot_routes, key=lambda x: x[2], reverse=True) 
    for i in range(10):
        top_tot.append(tot_routes[i])
     
    top_imp = []
    imp_routes = sorted(imp_routes, key=lambda x: x[2], reverse=True) 
    for i in range(10):
        top_imp.append(imp_routes[i])

    top_exp = []
    exp_routes = sorted(exp_routes, key=lambda x: x[2], reverse=True) 
    for i in range(10):
        top_exp.append(exp_routes[i])
  
 # Print results
   
    print("Las rutas (imp/exp) más utilizadas son:")
    for i in top_tot:
        print(i[0] + "-" + i[1] + " con " + str(i[2]) + " envíos.")
    print( "Las rutas de importación más utilizadas son:" ) 
    for i in top_imp:
        print(i[0] + "-" + i[1] + " con " + str(i[2]) + " envíos.")
    print("Las rutas de exportación más utilizadas son:" ) 
    for i in top_exp:
        print(i[0] + "-" + i[1] + " con " + str(i[2]) + " envíos.")

# List of transport systems

    transp_aux = []
    unique_list(data,7,7, transp_aux)
    
    transp = []
    short_list(transp_aux,0, transp)

# Top 3 transport systems according to value

    sum_list(data,7,9,transp)       
    
    top_trans=[]
    transp = sorted(transp, key=lambda x: x[1], reverse=True) 
    
    for i in range(3):
        top_trans.append(transp[i])
        
    print("Los medios de transporte más usados son:")
    for i in top_trans:
        print(i[0] + " con ingresos de " + str(i[1]))   
    
# Total sum of imports/exports

    total = 0 
    for i in data:
        aux = int(i[9])
        total = total + aux

# List of countries and import/export values

    countries_aux = []
    unique_list(data,2,2,countries_aux)

    countries = []
    short_list(countries_aux,0,countries)
    
    sum_list(data,2,9,countries)
    countries = sorted(countries, key=lambda x: x[1], reverse=True) 
   
    percent = total*.8

# Countries that give 80% of income

    countr_80 = []
    for i in countries:
        if percent >= 0:
            percent = percent - i[1]
            countr_80.append(i)

    print("Los países que genran el 80% de flujos son:")
    for i in countr_80:
        print(i[0] + " con $" + str(i[1]))

            
            
        
