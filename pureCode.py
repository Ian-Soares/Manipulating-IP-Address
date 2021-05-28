def mainFunction():

    while True:
        try:
            input_ip =input('- Insert here the IP Address: ')
            octet_in_list = input_ip.split('.')
            int_octet_in_list = [int(i)for i in octet_in_list]
            if (len(int_octet_in_list)==4) and \
                (256>int_octet_in_list[0]>=0) and \
                (256>int_octet_in_list[1]>=0) and \
                (256>int_octet_in_list[2]>=0) and \
                (256>int_octet_in_list[3]>=0):
                break
            elif len(int_octet_in_list) != 4:
                print('The IP Address needs to have 4 octets, just like this: 172.16.25.1')
            else:
                print('You must enter a IP in this format, for example: 192.168.25.12')
        except: 
            print('Try again, something went wrong! (Example of IP Address input: 192.168.0.12)')

    while True:
        try:
            input_mask = input('- Insert here the Subnet Mask: /').replace(' ','').replace('/','')
            if int(input_mask)>=0 and int(input_mask)<= 32:
                break
            elif int(input_mask) > 32:
                print('The subnet mask value cannot be greater than 32.')
            elif int(input_mask) < 0:
                print('The subnet mask value cannot be negative.')
        except:
            print('Something went wrong, try again. (Example of a subnet mask: /24)')

    binary_mask = str(int(input_mask)*'1')+'0'*(32-int(input_mask))
    mask_octets = int(binary_mask[:8],2),int(binary_mask[8:16],2),int(binary_mask[16:24],2),int(binary_mask[24:32],2)

    ip_in_binary = []
    ip_binary_oct = [bin(i).split('b')[1]for i in int_octet_in_list]

    for i in range(0,len(ip_binary_oct)):
        if len(ip_binary_oct[i]) < 8:
            formatted_binary = ip_binary_oct[i].zfill(8)
            ip_in_binary.append(formatted_binary)
        else:
            ip_in_binary.append(ip_binary_oct[i])
     
    ip_bin = f'{ip_in_binary[0]}.{ip_in_binary[1]}.{ip_in_binary[2]}.{ip_in_binary[3]}'
    subnet_mask = f'{binary_mask[:8]}.{binary_mask[8:16]}.{binary_mask[16:24]}.{binary_mask[24:]}'

    decimal_mask = f'{int(binary_mask[:8],2)}.{int(binary_mask[8:16],2)}.{int(binary_mask[16:24],2)}.{int(binary_mask[24:],2)}'

    zeros_in_mask = binary_mask.count('0')
    ones_in_mask = 32 - zeros_in_mask
    num_of_hosts = (2**zeros_in_mask)-2

    wildcard_mask = []
    for i in mask_octets:
        wildcard_bit = 255 - i
        wildcard_mask.append(wildcard_bit)
    wildcard_value = '.'.join([str(i) for i in wildcard_mask])
    ip_binary_mask = ''.join(ip_in_binary)

    network_in_binary = ip_binary_mask[:ones_in_mask] + "0" * zeros_in_mask
    broadcast_in_binary = ip_binary_mask[:ones_in_mask] + "1" * zeros_in_mask
    
    network_oct_bin = []
    broadcast_oct_bin = []

    [network_oct_bin.append(i) for i in [network_in_binary[n:n+8]
    for n in range(0,len(network_in_binary),8)]]
    [broadcast_oct_bin.append(i)for i in [broadcast_in_binary[n:n+8]
    for n in range(0,len(broadcast_in_binary),8)]]
    network_id = '.'.join([str(int(i,2)) for i in network_oct_bin])
    broadcast_id = '.'.join([str(int(i,2)) for i in broadcast_oct_bin])

    first_host_ip = network_oct_bin[0:3] + [(bin(int(network_oct_bin[3],2)+1).split("b")[1].zfill(8))]
    first_ip = '.'.join([str(int(i,2)) for i in first_host_ip])

    last_host_ip = broadcast_oct_bin[0:3] + [bin(int(broadcast_oct_bin[3],2) - 1).split("b")[1].zfill(8)]
    last_ip = '.'.join([str(int(i,2)) for i in last_host_ip])

    input_ip = input_ip.split('.')
    if int(input_ip[0]) > 0 and int(input_ip[0]) < 128:
        ip_class = 'A'
    elif int(input_ip[0]) > 127 and int(input_ip[0]) < 192:
        ip_class = 'B'
    elif int(input_ip[0]) > 191 and int(input_ip[0]) < 224:
        ip_class = 'C'
    elif int(input_ip[0]) > 223 and int(input_ip[0]) < 240:
        ip_class = 'D'
    elif int(input_ip[0]) > 239:
        ip_class = 'E'

    print(f' > Your Network ID is: {network_id}')
    print(f' > Binary form of the IP address: {ip_bin}')
    print(f' > Decimal form of the subnet mask: {decimal_mask}')
    print(f' > The subnet mask: {subnet_mask}')
    print(f' > The range of the network: {first_ip} - {last_ip}')
    print(f' > The number of hosts available: {num_of_hosts} ({num_of_hosts+2} IP\'s in total)')
    print(f' > Your IP is a class: {ip_class}')
    print(f' > The wildcard mask is: {wildcard_value}')
    print(f' > Your broadcast address is: {broadcast_id}')

follow = 'y'
while follow[0] == 'y':
    mainFunction()
    follow = input('Do you want to continue calculating?[y/n]: ')
    if follow[0].lower() == 'y':
        continue
    elif follow[0].lower() == 'n':
        break
    else:
        print('Something went wrong, the project will be closed.')
        break

print('* Thank you for testing our program *')
