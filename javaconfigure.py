import subprocess, sys

bins = ["java", "javac", "jar", "jshell"]

for bin in bins:
    command = f"sudo update-alternatives --install /usr/bin/{bin} {bin} /usr/lib/jvm/{sys.argv[1]}/bin/{bin} 1"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
