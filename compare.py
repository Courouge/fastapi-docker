import subprocess
import os

current_dir = os.getcwd()
tags_dir = [dI for dI in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, dI))]

for tag in tags_dir:
    go_to_current_dir = current_dir
    #subprocess.run(cd)
    tmp_cmd = "docker build -t " + tag + " --file \"" + tag + "/Dockerfile\"" + " -q ./" + tag + "/"
    print(tmp_cmd)
    print(os.getcwd())
    cmd1 = "cd " + os.getcwd()
    cmd2 = tmp_cmd
    cmd_lol = cmd1 + " && " + cmd2
    list_dir = subprocess.Popen([cmd2])
    list_dir.wait()
    #subprocess.exec([cmd_lol])

#docker build -t "$tag1" --file "${tag1}/Dockerfile" -q "./${tag1}/"  && docker image ls |grep "$tag1" && docker run -p 8000:8000 -it "$tag1"

