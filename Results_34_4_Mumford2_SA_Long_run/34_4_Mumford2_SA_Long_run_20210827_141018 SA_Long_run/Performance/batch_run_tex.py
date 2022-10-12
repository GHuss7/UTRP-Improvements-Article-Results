import subprocess

tex_files = ['attainment_fronts', 'hv_over_time', 'mean_objs_over_time']

for tex_file in tex_files:
    x = subprocess.call(f'pdflatex {tex_file}.tex -interaction nonstopmode -shell-escape') # -interaction nonstopmode -shell-escape
    if x != 0:
        print('Exit-code not 0, check result!')
    else:
        if False:
            os.system('start box_plots.pdf') # opens up the file if successfull