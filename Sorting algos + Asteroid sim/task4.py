import sys
size_array = 10


class Node(object):
    def __init__(self, KeyData, ValueData):
        self.data_main = KeyData
        self.data_side = ValueData
        self.next_pos = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        cur_node = self.head
        while cur_node:
            print("this is the key " + str(cur_node.data_main) + ", this is the data " + str(cur_node.data_side))
            cur_node = cur_node.next_pos

    def append_end(self, Keydata, Valuedata):
        new_node = Node(Keydata, Valuedata)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next_pos:
            last_node = last_node.next_pos
        last_node.next_pos = new_node

    def delete_specific(self, index):
        place1 = 0
        place2 = 0

        if index == 0:
            cur_node = self.head
            self.head = cur_node.next_pos

        else:
            last_node = self.head
            unwanted = self.head
            while place1 != index - 1:
                last_node = last_node.next_pos
                place1 += 1

            while place2 != index:
                unwanted = unwanted.next_pos
                place2 += 1

            last_node.next_pos = unwanted.next_pos
            unwanted.next_pos = None

    def find_value(self, Data):
        cur_node = self.head
        index = 0

        while cur_node:

            if cur_node.data_main == Data:
                return True, index, cur_node.data_side
            index += 1
            cur_node = cur_node.next_pos

        return False



def hash_function(key, data, action_type):
    index = 0

    if isinstance(key, int):
        index = key % size_array
        if action_type == 1:
            add_data_function(index, data, key, 1)

        elif action_type == 2:
            if arr_int[index].find_value(key):
                print("this key is present and its data is: " + arr_int[index].find_value(key)[2])
            else:
                print("this key is not present")
        elif action_type == 3:
            if arr_int[index].find_value(key):
                print("this key is present and has been deleted")
                arr_int[index].delete_specific((arr_int[index].find_value(key)[1]))
            else:
                print("this key is not present")

    elif isinstance(key, str):
        for x in key:
            index += ord(x)

        index = index % size_array
        if action_type == 1:
            add_data_function(index, data, key, 2)

        elif action_type == 2:
            if arr_str[index].find_value(key):
                print("this key is present and its data is: " + arr_str[index].find_value(key)[2])
            else:
                print("this key is not present")

        elif action_type == 3:
            if arr_str[index].find_value(key):
                print("this key is present and has been deleted")
                arr_str[index].delete_specific((arr_str[index].find_value(key)[1]))
            else:
                print("this key is not present")

    elif isinstance(key, float):
        index = key % size_array

        index = round(index)
        if action_type == 1:
            add_data_function(index, data, key, 3)

        elif action_type == 2:
            if arr_float[index].find_value(key):
                print("this key is present and its data is: " + arr_float[index].find_value(key)[2])
            else:
                print("this key is not present")

        elif action_type == 3:
            if arr_float[index].find_value(key):
                print("this key is present and has been deleted")
                arr_float[index].delete_specific((arr_float[index].find_value(key)[1]))
            else:
                print("this key is not present")


def add_data_function(index, data, key, arr_type):
    if arr_type == 1:
        arr_int[index].append_end(key, data)

    if arr_type == 2:
        arr_str[index].append_end(key, data)

    if arr_type == 3:
        arr_float[index].append_end(key, data)


if __name__ == '__main__':

    arr_int = [None] * size_array
    arr_str = [None] * size_array
    arr_float = [None] * size_array

    for i in range(size_array):
        arr_int[i] = LinkedList()
        arr_str[i] = LinkedList()
        arr_float[i] = LinkedList()

    hash_function(1, "this is an int  with key 1", 1)
    hash_function(4, "this is an int  with key 4", 1)
    hash_function(43, "this is an int  with key 43", 1)
    hash_function(42, "this is an int  with key 42", 1)
    hash_function(52, "this is an int  with key 52", 1)
    hash_function(62, "this is an int  with key 62", 1)
    hash_function(34, "this is an int  with key 34", 1)

    while True:

        user_input = input("\nWhat would you like to do? Add something (1), check if something exists (2), delete something(3) or exit (4) ")

        if user_input == "1":  # adding something
            print("What would you like to add? ")
            user_input = input("Key: ")
            key_main_menu = user_input

            user_input = input("what type of value will this be? int(1), float(2) or str(enter) ")

            if user_input == "1":
                key_main_menu = int(key_main_menu)
            elif user_input == "2":
                key_main_menu = float(key_main_menu)
            else:
                pass

            user_input = input("Data: ")
            data_main_menu = user_input
            hash_function(key_main_menu, data_main_menu, 1)

        elif user_input == "2":
            print("What would you like to look for?")
            user_input = input("Key: ")
            key_main_menu = user_input

            user_input = input("what type of value will this be? int(1), float(2) or str(enter) ")

            if user_input == "1":
                key_main_menu = int(key_main_menu)
            elif user_input == "2":
                key_main_menu = float(key_main_menu)
            else:
                pass

            hash_function(key_main_menu, data_main_menu, 2)

        elif user_input == "3":
            print("What would you like to delete?")
            user_input = input("Key: ")
            key_main_menu = user_input

            user_input = input("what type of value will this be? int(1), float(2) or str(enter) ")

            if user_input == "1":
                key_main_menu = int(key_main_menu)
            elif user_input == "2":
                key_main_menu = float(key_main_menu)
            else:
                pass
            hash_function(key_main_menu, data_main_menu, 3)

        elif user_input == "4":
            break

    sys.exit(0)
