import os

def find_all_files(root, files):
	try:
		for lists in os.listdir(root):
			name = lists
			path = os.path.join(root, lists)
			if os.path.isfile(path):
				files.append((name, path))
			if os.path.isdir(path):
				find_all_files(path, files)
	except OSError:
		files = []

# search file
def search_file(language, templates):
	language = language.lower() + ".gitignore"
	for template in templates:
		if language == template[0].lower():
			return template[1]
	return ""

def read_all_from_file(filepath):
	content = ""
	try:
		file_to_read = open(filepath, 'r')
		content = file_to_read.read()
	except:
		content = ""
	finally:
		file_to_read.close()
		return content