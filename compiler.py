import sys as sys
import os as os

if "--no-logo" not in sys.argv or "--show-logo" in sys.argv:
    print("###############################################")
    print("#                                             #")
    print("#                                             #")
    print("#                                             #") 
    print("# No doing with copyright. Use at free will.  #")
    print("#                                             #")
    print("#                                             #")
    print("#                                             #")
    print("###############################################")

def compile(file_path):
    code = open(file_path, "r")
    tmp = open(os.path.dirname(file_path)+"bin/"+os.path.splitext(file_path)[0]+".bin", "w")
    for line in code.read():
        string = line
        if "\n{" in line:
            string = string.replace("\n{",":")
        elif "}" in line:
            string = string.replace("}","")
        elif "{" in line:
            string = string.replace("{",  ":")
        elif ";" in line:
            string = string.replace(";", "")
        elif ">>" in line:
            string = string.replace(">>", ".")
        tmp.write(string)
    tmp.flush()
    tmp.close()

def compile_all(filepath):
    println("Compiling all sources")
    for dirname, dirnames, filenames in os.walk('.'):
        # print path to all subdirectories first.

        # print path to all filenames.
        for filename in filenames:
            if ".coo" in filename:
                compile(filename)

def println(line):
    #Check if the user is asking for no output
    if "--no-noise" not in sys.argv:
        print(line)

def error(line):
    println("Coo ERR: "+line)

#Compile the source code into .bin file
def compile_src(file_path):
    if not os.path.isdir(os.path.dirname(file_path)):
        os.system("mkdir bin")
    
    compile(file_path)

    os.system("python "+os.path.dirname(file_path)+"bin/"+os.path.splitext(file_path)[0]+".bin")
    compile_all(os.path.dirname(file_path))
    if "--delete-bin" in sys.argv:
        os.system("rm "+os.path.dirname(file_path)+"bin/"+os.path.splitext(file_path)[0]+".bin")


def get_proj(ring):
    try:
        compile_src(ring)
    except Exception as e:
        print("IO"+str(e))

if(sys.argv[1] == "--delete-bin"):
    try:
        get_proj(sys.argv[2])
    except Exception as e:
        print("IO"+str(e))
elif(sys.argv[1] == "--help"):
    println("python compiler.py [OPTION] file.coo")
elif(sys.argv[1] == "--no-noise"):
    get_proj(sys.argv[1])
else:
    get_proj(sys.argv[1])

