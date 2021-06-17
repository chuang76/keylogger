# Collect email address
# Target: NCKU CSIE student who enrolled in 2020 

f = open("email_list.txt", "w")
for bit_6 in range(9):
    for bit_7 in range(9):
        for bit_8 in range(9):
            for bit_9 in range(9):
                email = "F7409" + str(bit_6) + str(bit_7) + str(bit_8) + str(bit_9) + "@gs.ncku.edu.tw\n"
                f.write(email)
