import ast
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('--importModule', dest='importModule', type=str)
parser.add_argument('--functions', dest='functions', type=str)
args = parser.parse_args()

importModuleInput = [item for item in args.importModule.split(',')]
functionsInput = [item for item in args.functions.split(',')]

with open(sys.argv[1], 'r') as file:
    code = file.read()

tree = ast.parse(code)

importModule = []
functions = []

for i in ast.walk(tree):
    if isinstance(i, ast.Import) or isinstance(i, ast.ImportFrom):
        for j in i.names:
            importModule.append(j.name)

    if isinstance(i, ast.Call) and isinstance(i.func, ast.Attribute):
        # print(i.func.attr, len(i.args), [ast.unparse(j) for j in i.args])
        functions.append(i.func.attr)

if all(item in importModule for item in importModuleInput) and all(item in functions for item in functionsInput):
    print("Ok")
    exit(0)
else:
    print("Wrong")
    exit(2)
