from parametric_simulation import run_one_simulation_helper
from parametric_simulation import run_one_parameter_parametric

eplus_run_path = '../eplus_test/energyplus9.5/energyplus'
idf_path = '../eplus_test/1ZoneUncontrolled_win_1.idf'
parameter_key = ['WindowMaterial:SimpleGlazingSystem', 'SimpleWindow:DOUBLE PANE WINDOW', 'solar_heat_gain_coefficient']
parameter_vals = [0.25, 0.27, 0.29, 0.31, 0.33, 0.35, 0.37, 0.39, 0.41, 0.43, 0.45, 0.47, 0.49, 0.51, 0.53, 0.55, 0.57, 0.59, 0.61, 0.63, 0.65, 0.67, 0.69, 0.71, 0.73]
output_dir = '../eplus_test/param_exp_1'
run_one_parameter_parametric(eplus_run_path, idf_path, output_dir, parameter_key, parameter_vals)