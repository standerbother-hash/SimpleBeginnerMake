import os
import subprocess


c_files = [f for f in os.listdir(".") if f.endswith(".c")]

so_libs = [f[3:-3] for f in os.listdir(".") if f.startswith("lib") and f.endswith(".so")]

for c_file in c_files:
    exec_name = os.path.splitext(c_file)[0]
    
    
    cmd = ["gcc", "-I.", c_file, "-L.", "-Wl,-rpath=.", "-o", exec_name]
    

    for lib in so_libs:
        cmd.append(f"-l{lib}")
    

    print(f"[*] programing: {c_file} -> {exec_name}")
    subprocess.run(cmd)
