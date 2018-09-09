import os
import subprocess

# running another python script

def python_execute(file_name,output_file):
    with open(output_file+".txt", "w+") as output:
        subprocess.call(["python", "./"+file_name+".py"], stdout=output)


#compiling and running another c file using our term module


def c_plus_compile(file_name,output_file):
    os.system("g++ "+ file_name+".cpp -o "+ file_name)
    with open(output_file+".txt", "w+") as output:
        subprocess.call("./"+file_name, stdout=output)


#compiling a C++ file

def c_compile(file_name,output_file):
    os.system("gcc "+file_name +".c -o"+ file_name)
    # from subprocess import call
    with open(output_file+".txt", "w+") as output:
        subprocess.call("./"+file_name, stdout=output);

