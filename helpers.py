def open_file(input):
    f = open(input, "r")
    return f.read()

def txt_to_D_list(input):
    with open(input) as f:
      D_List = f.readlines()

    return  [x.replace('\n','') for x in D_List]

def txt_to_2D_list(input, separator):
    D_List = txt_to_D_list(input)
    List_2D = []
    for item in D_List:
       new_item = item.split(separator)
       List_2D.append(new_item)
    return List_2D