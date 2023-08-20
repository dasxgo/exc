from .module1 import city
from .module2 import is_positive

# Call module => from <name file> import <funtion> 
# Run the package => python3 -m <folder> || python3 <name file>

print('='*64)

def add_list(a,b):
    return a+b

output = list(map(add_list,[2,6,3],[3,4,5]))
print(output)
print('='*64)