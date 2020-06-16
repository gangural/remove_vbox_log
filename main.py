from os import path, remove
from glob import glob

to_del = glob(path.join(path.expanduser('~'), '**/VBox.log*'), recursive=True)

if to_del:
	for f in to_del:
		remove(f)
		print(f'Removed {f}')
else:
	print("Nothing to remove!")
