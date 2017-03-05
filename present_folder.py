import os

def get_filetype(dir_, filetype="png"):
    pngs = map(lambda x: os.path.join(dir_,x),
               filter(lambda x: x.endswith("."+filetype), os.listdir(dir_)))
    return list(pngs)

get_filetype("./img")

