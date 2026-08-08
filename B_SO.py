import os
import subprocess


c_files = [f for f in os.listdir(".") if f.endswith(".c")]

for c_file in c_files:

    lib_name = f"{os.path.splitext(c_file)[0]}.so"
    

    cmd = ["gcc", "-shared", "-fPIC", "-I.", c_file, "-o", lib_name]
    

    subprocess.run(cmd)
    print(f"[*] so: {c_file} -> {lib_name}")
