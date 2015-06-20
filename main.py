
import commands

def find_copies(file_list):
    for n in range(0, len(file_list) - 1):
        for k in range(n + 1, len(file_list)):
            output_string = commands.getoutput("diff %s %s" % (file_list[n], file_list[k]))
            if output_string == '':
                print("files %s and %s are identical" % (file_list[n], file_list[k]))
            else:
                print("files %s and %s are different" % (file_list[n], file_list[k]))

def find_later_versions(item_list):

    for ls_line in item_list[1:len(item_list)]:
        ls_items = ls_line.split(" ")
        current_date = [ls_items[len(ls_items) - 4],
                    ls_items[len(ls_items) - 3],
                    ls_items[len(ls_items) - 2],
                    ls_items[len(ls_items) - 1]]
        print(current_date)


if __name__ == '__main__':
    output_string = commands.getoutput("ls")
    print(output_string)
    file_list = output_string.splitlines()
    find_copies(file_list)

    output_string = commands.getoutput("ls -l")
    print(output_string)
    item_list = output_string.splitlines()
    find_later_versions(item_list)

