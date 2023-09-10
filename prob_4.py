def sorter(word_list):
    temp = ''
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if (word_list[i] > word_list[j]):
                temp = word_list[i]
                word_list[i] = word_list[j]
                word_list[j] = temp
    return word_list

def main():
    input_file_path = input('give path to input file')
    output_file_path = input('give path to output file')

    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        input_file_string = input_file.read()
        sorted_output = sorter(input_file_string.split('\n'))
        output_file.write('\n'.join(sorted_output))


main()