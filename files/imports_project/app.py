from imports_project.utils.common.file_operations import save_to_file, read_file
from imports_project.utils.find import find_in

save_to_file('Rolf', 'data.txt')
print(read_file('data.txt'))

print(__name__)