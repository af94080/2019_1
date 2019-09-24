lines = []

lines_out = []

with open('5rows.txt') as fh:
	lines = fh.readlines()



for line in lines:
	line = line.replace("[", "\"logdate\": \"")
	line = line.replace("] ", "\", ")
	line = line.replace(", ", ", \"")
	line = line.replace("=", "\"=" )
	line = line.replace("=\""," : \"").replace("=<"," : \"").replace(">","\"")
	# print(line)
	lines_out.append(line)

# write to json

with open('5rows.json', "w") as fw:
	for line in lines_out:
		fw.write("{" + line + "}, \n")

