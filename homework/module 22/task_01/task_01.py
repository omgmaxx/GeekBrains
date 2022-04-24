def sum_to(txt_input, txt_output):
    text_file = open(txt_input, 'r')
    imported_text = text_file.read().split()
    text_file.close()

    result = 0
    for index in imported_text:
        result += int(index)

    new_text = open(txt_output, 'w')
    new_text.write(str(result))


source = "numbers.txt"
target = "answer.txt"
sum_to(source, target)
