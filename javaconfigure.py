import subprocess, sys

version = "javaconfigure 1.0"
author = "Giuseppe Tomarchio aka victi, Victini378"
title = f"{version}, {author}"

if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print(f"""\n{title}
    
        Usage: python3 javaconfigure.py [options] jdk_folder_name
    
        Options:
        --version Show version information
        --help, -h Show this message\n""")
        exit()
elif sys.argv[1] == "--version":
    print (title)
    exit()    

bins = ["java", "javac", "jar", "jshell"]

for bin in bins:
    command = f"sudo update-alternatives --install /usr/bin/{bin} {bin} /usr/lib/jvm/{sys.argv[1]}/bin/{bin} 1"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
