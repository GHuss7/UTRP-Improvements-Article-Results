import argparse

# Arguments from command line
parser = argparse.ArgumentParser()

# Defaults:
find_text = r'y tick label style={/pgf/number format/.cd,fixed,precision=3, zerofill},'
replace_text = r'scaled y ticks={base 10:2}, %y tick label style={/pgf/number format/.cd,fixed,precision=3, zerofill},'
file_name_text = "box_plots.tex"

#-dir DIRECTORY
parser.add_argument("-fn", "--file_name", dest = "file_name", default = file_name_text, help="File name", type=str)
parser.add_argument("-f", "--find", dest = "find", default = find_text, help="To find text", type=str)
parser.add_argument("-r", "--replace", dest = "replace", default = replace_text, help="Replacement text", type=str)

args = parser.parse_args()

arg_find = args.find 
arg_replace = args.replace 
arg_file_name = args.file_name 


#read input file
fin = open(arg_file_name, "rt")
#read file contents to string
data = fin.read()
#replace all occurrences of the required string
data = data.replace(arg_find, arg_replace)
#close the input file
fin.close()
#open the input file in write mode
fin = open(arg_file_name, "wt")
#overrite the input file with the resulting data
fin.write(data)
#close the file
fin.close()

# execute the file
import subprocess
tex_files = [arg_file_name]

for tex_file in tex_files:
    x = subprocess.call(f'pdflatex {tex_file} -interaction nonstopmode -shell-escape') # -interaction nonstopmode -shell-escape
    if x != 0:
        print('Exit-code not 0, check result!')
    else:
        if False:
            os.system('start box_plots.pdf') # opens up the file if successfull