import  executor


file="test_script"
data_file="output"

#here function arguments are the input file name and output file name  without the extensions
executor.python_execute(file, data_file)

executor.c_compile(file,data_file)

executor.c_plus_compile(file,data_file)