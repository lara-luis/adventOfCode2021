my_file = open("input", "r")
content = my_file.readlines()

decoder = {"0":"0000",
"1":"0001",
"2":"0010",
"3":"0011",
"4":"0100",
"5":"0101",
"6":"0110",
"7":"0111",
"8":"1000",
"9":"1001",
"A":"1010",
"B":"1011",
"C":"1100",
"D":"1101",
"E":"1110",
"F":"1111"}

def decode_package(decoded, operation_sum):
    if decoded == "":
        return ""

    packet_version = int(decoded[0:3],2)
    packet_type_id = int(decoded[3:6],2)

    operation_sum[0] += packet_version

    if packet_type_id == 4:
        binary_rep = ""
        remaining_string = ""
        a = decoded[6:11]
        prefix = a[0:1]
        binary_rep += a[1:5]
        remaining_string = decoded[11:]
        current_index = 11

        while prefix != "0":
            b = decoded[current_index:current_index+5]
            prefix = b[0:1]
            binary_rep += b[1:5]
            remaining_string = decoded[current_index+5:]
            current_index = current_index+5
        
        decimal_rep = int(binary_rep,2)
        return remaining_string
    else:
        i = decoded[6:7]
        if i == "0":
            # 15 bits
            l = decoded[7:(7+15)]
            length_of_subpackets = int(l,2)
            if length_of_subpackets > 0:
                initial_index = (7+15)
                remaining_string = decoded[initial_index:]
                remaining_bits = len(remaining_string)
                consumed_bits = 0
                while remaining_bits > 0 and consumed_bits < length_of_subpackets:
                    subpackets = remaining_string[0:]
                    initial_index = initial_index+length_of_subpackets
                    remaining_string =  decode_package(subpackets, operation_sum)
                    consumed_bits += remaining_bits - len(remaining_string)
                    remaining_bits = len(remaining_string)
            return remaining_string
        else:
            # 11 bits
            l = decoded[7:(7+11)]
            length_of_subpackets = int(l,2)
            initial_index = 7+11
            subpackets = list()

            if length_of_subpackets > 0:
                remaining_string = decoded[initial_index:]
                remaining_bits = len(remaining_string)
                consumed_packets = 0
                while remaining_bits > 0 and consumed_packets < length_of_subpackets:
                    subpackets = remaining_string[0:]
                    remaining_string =  decode_package(subpackets, operation_sum)
                    consumed_packets += 1
                    remaining_bits = len(remaining_string)
                    initial_index = initial_index + remaining_bits
            return remaining_string

to_decode = content[0]
decoded = ""
for x in to_decode:
    decoded += decoder[x]

operation_sum = 0
wrapper_sum = [operation_sum]
result = decode_package(decoded, wrapper_sum)
print(wrapper_sum[0])