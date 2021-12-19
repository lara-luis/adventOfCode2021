import sys 

my_file = open("input", "r")
content = my_file.readlines()

decoder = {
"0":"0000",
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

def decode_package(decoded, operation_result):
    if decoded == "":
        return ""

    packet_version = int(decoded[0:3],2)
    packet_type_id = int(decoded[3:6],2)

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
        operation_result[0] = decimal_rep
        return remaining_string
    elif packet_type_id == 0:
        i = decoded[6:7]
        if i == "0":
            # 15 bits
            l = decoded[7:(7+15)]
            length_of_subpackets = int(l,2)
            op_result = 0
            if length_of_subpackets > 0:
                initial_index = (7+15)
                remaining_string = decoded[initial_index:]
                remaining_bits = len(remaining_string)
                consumed_bits = 0
                packet_value = [0]
                while remaining_bits > 0 and consumed_bits < length_of_subpackets:
                    subpackets = remaining_string[0:]
                    initial_index = initial_index+length_of_subpackets
                    remaining_string =  decode_package(subpackets, packet_value)
                    op_result += packet_value[0]
                    consumed_bits += remaining_bits - len(remaining_string)
                    remaining_bits = len(remaining_string)

            operation_result[0] = op_result
            return remaining_string
        else:
            # 11 bits
            l = decoded[7:(7+11)]
            length_of_subpackets = int(l,2)
            initial_index = 7+11
            subpackets = list()
            op_result = 0

            if length_of_subpackets > 0:
                remaining_string = decoded[initial_index:]
                remaining_bits = len(remaining_string)
                consumed_packets = 0
                packet_value = [0]
                while remaining_bits > 0 and consumed_packets < length_of_subpackets:
                    subpackets = remaining_string[0:]
                    remaining_string =  decode_package(subpackets, packet_value)
                    op_result += packet_value[0]
                    consumed_packets += 1
                    remaining_bits = len(remaining_string)
                    initial_index = initial_index + remaining_bits
            operation_result[0] = op_result
            return remaining_string
    elif packet_type_id == 1:
        i = decoded[6:7]
        if i == "0":
            # 15 bits
            l = decoded[7:(7+15)]
            length_of_subpackets = int(l,2)
            op_result = 1
            if length_of_subpackets > 0:
                initial_index = (7+15)
                remaining_string = decoded[initial_index:]
                remaining_bits = len(remaining_string)
                consumed_bits = 0
                packet_value = [0]
                operation_result[0] = 1 # avoid to multiply by 0
                while remaining_bits > 0 and consumed_bits < length_of_subpackets:
                    subpackets = remaining_string[0:]
                    initial_index = initial_index+length_of_subpackets
                    remaining_string =  decode_package(subpackets, packet_value)
                    op_result *= packet_value[0]
                    consumed_bits += remaining_bits - len(remaining_string)
                    remaining_bits = len(remaining_string)
            operation_result[0] = op_result
            return remaining_string
        else:
            # 11 bits
            l = decoded[7:(7+11)]
            length_of_subpackets = int(l,2)
            initial_index = 7+11
            subpackets = list()
            op_result = 1

            if length_of_subpackets > 0:
                remaining_string = decoded[initial_index:]
                remaining_bits = len(remaining_string)
                consumed_packets = 0
                packet_value = [0]
                operation_result[0] = 1
                while remaining_bits > 0 and consumed_packets < length_of_subpackets:
                    subpackets = remaining_string[0:]
                    remaining_string =  decode_package(subpackets, packet_value)
                    op_result *= packet_value[0]
                    consumed_packets += 1
                    remaining_bits = len(remaining_string)
                    initial_index = initial_index + remaining_bits
            operation_result[0] = op_result     
            return remaining_string
    elif packet_type_id == 2:
        i = decoded[6:7]
        if i == "0":
            # 15 bits
            l = decoded[7:(7+15)]
            length_of_subpackets = int(l,2)
            op_result = sys.maxsize
            if length_of_subpackets > 0:
                initial_index = (7+15)
                remaining_string = decoded[initial_index:]
                remaining_bits = len(remaining_string)
                consumed_bits = 0
                packet_value = [0]
                operation_result[0] = sys.maxsize
                while remaining_bits > 0 and consumed_bits < length_of_subpackets:
                    subpackets = remaining_string[0:]
                    initial_index = initial_index+length_of_subpackets
                    remaining_string =  decode_package(subpackets, packet_value)
                    op_result = min(op_result, packet_value[0])
                    consumed_bits += remaining_bits - len(remaining_string)
                    remaining_bits = len(remaining_string)
            operation_result[0] = op_result
            return remaining_string
        else:
            # 11 bits
            l = decoded[7:(7+11)]
            length_of_subpackets = int(l,2)
            initial_index = 7+11
            subpackets = list()
            op_result = sys.maxsize

            if length_of_subpackets > 0:
                remaining_string = decoded[initial_index:]
                remaining_bits = len(remaining_string)
                consumed_packets = 0
                packet_value = [0]
                operation_result[0] = sys.maxsize
                while remaining_bits > 0 and consumed_packets < length_of_subpackets:
                    subpackets = remaining_string[0:]
                    remaining_string =  decode_package(subpackets, packet_value)
                    op_result = min(op_result, packet_value[0])
                    consumed_packets += 1
                    remaining_bits = len(remaining_string)
                    initial_index = initial_index + remaining_bits

            operation_result[0] = op_result
            return remaining_string
    elif packet_type_id == 3:
        i = decoded[6:7]
        if i == "0":
            # 15 bits
            l = decoded[7:(7+15)]
            length_of_subpackets = int(l,2)
            op_result = -sys.maxsize-1
            if length_of_subpackets > 0:
                initial_index = (7+15)
                remaining_string = decoded[initial_index:]
                remaining_bits = len(remaining_string)
                consumed_bits = 0
                packet_value = [0]
                operation_result[0] = -sys.maxsize-1 
                while remaining_bits > 0 and consumed_bits < length_of_subpackets:
                    subpackets = remaining_string[0:]
                    initial_index = initial_index+length_of_subpackets
                    remaining_string =  decode_package(subpackets, packet_value)
                    op_result = max(op_result, packet_value[0])
                    consumed_bits += remaining_bits - len(remaining_string)
                    remaining_bits = len(remaining_string)
            operation_result[0] = op_result
            return remaining_string
        else:
            # 11 bits
            l = decoded[7:(7+11)]
            length_of_subpackets = int(l,2)
            initial_index = 7+11
            subpackets = list()
            op_result = -sys.maxsize-1

            if length_of_subpackets > 0:
                remaining_string = decoded[initial_index:]
                remaining_bits = len(remaining_string)
                consumed_packets = 0
                packet_value = [0]
                operation_result[0] = -sys.maxsize-1
                while remaining_bits > 0 and consumed_packets < length_of_subpackets:
                    subpackets = remaining_string[0:]
                    remaining_string =  decode_package(subpackets, packet_value)
                    op_result = max(op_result, packet_value[0])
                    consumed_packets += 1
                    remaining_bits = len(remaining_string)
                    initial_index = initial_index + remaining_bits
      
            operation_result[0] = op_result
            return remaining_string
    elif packet_type_id == 5:
        i = decoded[6:7]
        if i == "0":
            # 15 bits
            l = decoded[7:(7+15)]
            length_of_subpackets = int(l,2)
            op_result = -sys.maxsize-1

            if length_of_subpackets > 0:
                initial_index = (7+15)
                remaining_string = decoded[initial_index:]
                remaining_bits = len(remaining_string)
                consumed_bits = 0
                packet_value = [0]
                first_packet = -sys.maxsize-1
                while remaining_bits > 0 and consumed_bits < length_of_subpackets:
                    subpackets = remaining_string[0:]
                    initial_index = initial_index+length_of_subpackets
                    remaining_string = decode_package(subpackets, packet_value)

                    if first_packet == -sys.maxsize-1:
                        first_packet = packet_value[0]
                    else: 
                        if first_packet > packet_value[0]:
                            op_result = 1
                        else:
                            op_result = 0
                    consumed_bits += remaining_bits - len(remaining_string)
                    remaining_bits = len(remaining_string)
            operation_result[0] = op_result
            return remaining_string
        else:
            # 11 bits
            l = decoded[7:(7+11)]
            length_of_subpackets = int(l,2)
            initial_index = 7+11
            subpackets = list()
            op_result = -sys.maxsize-1

            if length_of_subpackets > 0:
                remaining_string = decoded[initial_index:]
                remaining_bits = len(remaining_string)
                consumed_packets = 0
                packet_value = [0]
                first_packet = -sys.maxsize-1
                while remaining_bits > 0 and consumed_packets < length_of_subpackets:
                    subpackets = remaining_string[0:]
                    remaining_string =  decode_package(subpackets, packet_value)

                    if first_packet == -sys.maxsize-1:
                        first_packet = packet_value[0]
                    else: 
                        if first_packet > packet_value[0]:
                            op_result = 1
                        else:
                            op_result = 0
                    consumed_packets += 1
                    remaining_bits = len(remaining_string)
                    initial_index = initial_index + remaining_bits
            operation_result[0] = op_result
            return remaining_string
    elif packet_type_id == 6:
        i = decoded[6:7]
        if i == "0":
            # 15 bits
            l = decoded[7:(7+15)]
            length_of_subpackets = int(l,2)
            op_result = sys.maxsize
            if length_of_subpackets > 0:
                initial_index = (7+15)
                remaining_string = decoded[initial_index:]
                remaining_bits = len(remaining_string)
                consumed_bits = 0
                packet_value = [0]
                first_packet = sys.maxsize
                while remaining_bits > 0 and consumed_bits < length_of_subpackets:
                    subpackets = remaining_string[0:]
                    initial_index = initial_index+length_of_subpackets
                    remaining_string =  decode_package(subpackets, packet_value)
                    
                    if first_packet == sys.maxsize:
                        first_packet = packet_value[0]
                    else: 
                        if first_packet < packet_value[0]:
                            op_result = 1
                        else:
                            op_result = 0
                    consumed_bits += remaining_bits - len(remaining_string)
                    remaining_bits = len(remaining_string)
            operation_result[0] = op_result
            return remaining_string
        else:
            # 11 bits
            l = decoded[7:(7+11)]
            length_of_subpackets = int(l,2)
            initial_index = 7+11
            subpackets = list()
            op_result = sys.maxsize

            if length_of_subpackets > 0:
                remaining_string = decoded[initial_index:]
                remaining_bits = len(remaining_string)
                consumed_packets = 0
                packet_value = [0]
                first_packet = sys.maxsize
                while remaining_bits > 0 and consumed_packets < length_of_subpackets:
                    subpackets = remaining_string[0:]
                    remaining_string =  decode_package(subpackets, packet_value)

                    if first_packet == sys.maxsize:
                        first_packet = packet_value[0]
                    else: 
                        if first_packet < packet_value[0]:
                            op_result = 1
                        else:
                            op_result = 0
                    consumed_packets += 1
                    remaining_bits = len(remaining_string)
                    initial_index = initial_index + remaining_bits
            operation_result[0] = op_result
            return remaining_string
    elif packet_type_id == 7:
        i = decoded[6:7]
        if i == "0":
            # 15 bits
            l = decoded[7:(7+15)]
            length_of_subpackets = int(l,2)
            op_result = -sys.maxsize-1
            if length_of_subpackets > 0:
                initial_index = (7+15)
                remaining_string = decoded[initial_index:]
                remaining_bits = len(remaining_string)
                consumed_bits = 0
                packet_value = [0]
                first_packet = -sys.maxsize-1
                while remaining_bits > 0 and consumed_bits < length_of_subpackets:
                    subpackets = remaining_string[0:]
                    initial_index = initial_index+length_of_subpackets
                    remaining_string =  decode_package(subpackets, packet_value)

                    if first_packet == -sys.maxsize-1:
                        first_packet = packet_value[0]
                    else: 
                        if first_packet == packet_value[0]:
                            op_result = 1
                        else:
                            op_result = 0
                    consumed_bits += remaining_bits - len(remaining_string)
                    remaining_bits = len(remaining_string)
            operation_result[0] = op_result
            return remaining_string
        else:
            # 11 bits
            l = decoded[7:(7+11)]
            length_of_subpackets = int(l,2)
            initial_index = 7+11
            subpackets = list()
            op_result = -sys.maxsize-1

            if length_of_subpackets > 0:
                remaining_string = decoded[initial_index:]
                remaining_bits = len(remaining_string)
                consumed_packets = 0
                packet_value = [0]
                first_packet = -sys.maxsize-1
                while remaining_bits > 0 and consumed_packets < length_of_subpackets:
                    subpackets = remaining_string[0:]
                    remaining_string =  decode_package(subpackets, packet_value)

                    if first_packet == -sys.maxsize-1:
                        first_packet = packet_value[0]
                    else: 
                        if first_packet == packet_value[0]:
                            op_result = 1
                        else:
                            op_result = 0
                    consumed_packets += 1
                    remaining_bits = len(remaining_string)
                    initial_index = initial_index + remaining_bits
            operation_result[0] = op_result
            return remaining_string

to_decode = content[0]
decoded = ""
for x in to_decode:
    decoded += decoder[x]

operation_sum = 0
wrapper_sum = [operation_sum]
result = decode_package(decoded, wrapper_sum)
print(wrapper_sum[0])