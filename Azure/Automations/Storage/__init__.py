import sys
import os


___directory_depth = 2
___relative_path = "TamnoonPlaybooks/Azure/"

___splits = sys.path[0].split("/")
___import_path = os.path.join(
    "/".join(___splits[0 : ___splits.__len__() - ___directory_depth]), ___relative_path
)
sys.path.append(___import_path)
