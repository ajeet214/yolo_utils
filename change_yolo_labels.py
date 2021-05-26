import os


def label_changer(source_path=None, dest_path=None, old_label=None, new_label=None):

    #get the list of all label files's name
    train = os.listdir(source_path)
    # print(train)

    lst = list()

    for i in train:

        with open(f'{source_path}\\{i}', 'r') as file:
            """store the content of each file as item in list lst, each item is itself a list 
            consisting of all the lines in the file"""
            lst.append(file.readlines())

    # print(lst)

    l2 = list()

    for i in lst:
        """here i is the content of each file"""
        in_lst = list()

        """iterate over each line in the file i"""
        for j in i:
            """here we are checking if the line starts with class label 10"""
            if j.startswith(f'{old_label} '):
                """replacing the class label 10 with new class(here 5)
                3rd argument(here 1) in replace funtion means we wanna replace only the first occurance because we only 
                interested in chnaging the class not the boxes"""
                in_lst.append(j.replace(f'{old_label} ', f'{new_label} ', 1))
            else:
                in_lst.append(j)
        l2.append(in_lst)

    # print(l2)
    """new_l is the list of tuple, where each tuple has 2 item. the first item is the 
    original file name and second item is the content itself after changing the class label"""
    new_l = list(zip(train, l2))
    # print(new_l)

    """we iterate over all the files and write them down in specified path"""
    for name, data in new_l:
        # print(name, data)

        with open(f"{dest_path}\\{name}", "w") as file:
            for i in data:
                file.write(i)


if __name__ == "__main__":

    """"for example: here we  are changing the box class label from 10 to 5 for all the files in 
    source path and saving at des_path with same files name"""
    label_changer(source_path="C:\\Users\\vermaak\\Desktop\\test_old",
                  dest_path="C:\\Users\\vermaak\\Desktop\\test_new",
                  old_label='10',
                  new_label='5')
