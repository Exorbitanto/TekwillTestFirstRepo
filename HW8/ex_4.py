desired_file_name = input("Introduceti numele fisierului dorit: ")
text = input("Introduceti textul pentru a fi inscris in fisier: ")
file = open(f"{desired_file_name}.txt", 'a+')
file.seek(0)
if len(file.read()) > 0:
    file.write("\n")
file.write(text)
file.close()

file = open(f"{desired_file_name}.txt", 'r')
text = file.read()
file.close()
print(f"Textul inscris in fisier este:\n{text}")