# Date of the first creation: 2022-10-18
# This file is for EnergyPlus parametric simulation
import json
import copy
from StaticEplusEngine import run_eplus_model, convert_json_idf


def run_one_simulation_helper(eplus_run_path, idf_path, output_dir, 
	                            parameter_key, parameter_val):


    #This is a helper function to run one simulation with the change value of the parameter_key

    ######### step 1: convert an IDF file into JSON file ########
    convert_json_idf(eplus_run_path, idf_path)
    epjson_path = idf_path.split('.idf')[0] + '.epJSON'

    ######### step 2: load the JSON file into a JSON dict ########
    with open(epjson_path) as epJSON:
        epjson_dict = json.load(epJSON)
    
    ######### step 3: change the JSON dict value ########
    
    inner_dict = epjson_dict
    for i in range(len(parameter_key)):
        if i < len(parameter_key) - 1:
            inner_dict = inner_dict[parameter_key[i]]
    inner_dict[parameter_key[-1]] = parameter_val 
    

    ######### step 4: dump the JSON dict to JSON file ########  
    with open(epjson_path, 'w') as epjson:
        json.dump(epjson_dict, epjson)  


    ######### step 5: convert JSON file to IDF file ######## 
    convert_json_idf(eplus_run_path, epjson_path) 

    ######### step 6: run simulation ########  
    run_eplus_model(eplus_run_path, idf_path, output_dir)        
    
    	

    #run_eplus_model(eplus_run_path, idf_path, output_dir)

def run_one_parameter_parametric(eplus_run_path, idf_path, output_dir, 
	                            parameter_key, parameter_vals):
    
    


    import os.path
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    # import file operation module, if there is no catalogue named output_dir, then create a new catalogue named output_dir.
    
    dicta_result = {}
    # create a new dictionary named dicta_result to collect the results.
    
    for i in range(len(parameter_vals)):
    # parameter_vals is the list with 25 different values. 
    # create an index i for looping the fuction 25 times. Each i corresponding to one parameter_val.

        parameter_val = parameter_vals[i]
        this_output_dir = output_dir + '/run_' + str(i + 1)
    # every time completing the loop, string i has to add 1 for next loop. The result of each loop is output to this_output_dir.  
        
        
        this_res_path = this_output_dir + '/eplusout.csv'  
    # export the result as csv file as the new path named this_res_path.      
        

        this_res_path = run_one_simulation_helper(eplus_run_path, idf_path,
                                this_output_dir, parameter_key, parameter_val)

    # run the simulation as this_res_path.    

        dicta_result[parameter_val] = this_res_path

    # import the results into dictionary, one key corresponding to one result.    

    return dicta_result  






    return None # TO-DO!	                              