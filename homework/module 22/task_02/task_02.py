def reverse_txt(txt_input):
    text_file = open(txt_input, 'r')
    imported_text = text_file.read().split("\n")
    text_file.close()

    for line in imported_text[::-1]:
        print(line)


source = "zen.txt"
reverse_txt(source)
