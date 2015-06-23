
import commands

month_dict = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5,
                "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9,
                "Oct": 10, "Nov": 11, "Dec": 12}

def find_copies(file_list):
    for n in range(0, len(file_list) - 1):
        for k in range(n + 1, len(file_list)):
            output_string = commands.getoutput("diff %s %s" % (file_list[n], file_list[k]))
            if output_string == '':
                print("files %s and %s are identical" % (file_list[n], file_list[k]))
            else:
                print("files %s and %s are different" % (file_list[n], file_list[k]))

def format_time_list(item_list):
    current_date_list = []
    for ls_line in item_list[1:len(item_list)]:
        ls_items = ls_line.split(" ")
        current_date = [ls_items[len(ls_items) - 4],
                    ls_items[len(ls_items) - 3],
                    ls_items[len(ls_items) - 2],
                    ls_items[len(ls_items) - 1]]
        temp = current_date[2]
        new_temp = temp.replace(":", "")
        current_date[2] = new_temp
        current_date_list.append(current_date)
    return current_date_list

def compare_time(time_table, input_time):
    for date in time_table:
        if month_dict[date[0]] > month_dict[input_time[0]]:
            print("%s was modified later than specified time" % (date[3]))
        elif (month_dict[date[0]] == month_dict[input_time[0]]) & \
                (int(date[1]) > int(input_time[1])):
            print("%s was modified later than specified time" % (date[3]))
        elif (month_dict[date[0]] == month_dict[input_time[0]]) & \
                (int(date[1]) == int(input_time[1])) & \
                (int(date[2]) > int(input_time[2])):
            print("%s was modified later than specified time" % (date[3]))
        else:
            print("%s was not modified later than specified time" % (date[3]))


if __name__ == '__main__':
    print("please enter the comparison time in format \n"
          "(month abbrev.) (day) (time) *not built for files built in different years*\n"
          "for example 'Jun 3 20:43'")
    comparison_time = raw_input("enter time here:")
    comparison_time = comparison_time.split(" ")
    temp = comparison_time[2]
    new_temp = temp.replace(":", "")
    comparison_time[2] = new_temp

    output_string = commands.getoutput("ls")
    #print(output_string)
    file_list = output_string.splitlines()
    find_copies(file_list)

    output_string = commands.getoutput("ls -l")
    #print(output_string)
    item_list = output_string.splitlines()
    time_table = format_time_list(item_list)
    compare_time(time_table, comparison_time)


