import subprocess


# subprocess.run(["ls", "-l"])
# compelted = subprocess.run(["ls", "-l"])
# print(type(compelted))
# print("args", compelted.args)
# print("returncode", compelted.returncode)
# print("stderr", compelted.stderr)
# print("stdout", compelted.stdout)


# compelted = subprocess.run(["ls", "-l"],
#                            capture_output=1,
#                            text=True)
# print("args", compelted.args)
# print("returncode", compelted.returncode)
# print("stderr", compelted.stderr)
# print("stdout", compelted.stdout)


# compelted = subprocess.run(["python3.8", "other.py"],
#                            capture_output=1,
#                            text=True)
# print("args", compelted.args)
# print("returncode", compelted.returncode)
# print("stderr", compelted.stderr)
# print("stdout", compelted.stdout)


try:
    compelted = subprocess.run(["false"],
                               capture_output=1,
                               text=True,
                               check=True)
    print("args", compelted.args)
    print("returncode", compelted.returncode)
    print("stderr", compelted.stderr)
    print("stdout", compelted.stdout)
    # if compelted.returncode != 0:
    #     print(compelted.stderr)
except subprocess.CalledProcessError as ex:
    print(ex)
