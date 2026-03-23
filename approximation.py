def approximation_function(value, sf):
    value = str(value)
    valid_nums = ("5", "6", "7", "8", "9")
    for index in range(len(value)):
        if value[index] == ".":
            p = len(value[index : len(value)])
            pw = len(value) - p
            if pw > sf:
                print(pw, sf)
                if value[sf] in valid_nums:
                    integer = value[0:sf]
                    integer = int(integer) + 1
                    power = len(value[sf:pw])
                else:
                    integer = value[0:sf]
                    power = len(value[sf:pw])
                return f" {integer}x10^{power} or {integer}{'0'*power}"
            else:
                return "Error :) please check your values"
        # integer,power= approximation_function(user_input,Significant_figs)


def decimal_function(value, sf):
    value = str(value)
    valid_nums = ("5", "6", "7", "8", "9")
    flag = False
    for index in range(len(value)):
        if value[index] == ".":
            flag = True
            integer = value[0:index]
            decimal = value[index + 1 : len(value)]
            if len(decimal) > sf:
                if decimal[sf] in valid_nums:
                    decimal_cut = int(decimal[0:sf]) + 1
                    Remainder = "0" * len(decimal[sf : len(decimal)])
                    if decimal_cut % 10 == 0:
                        final_value = int(integer) + 1
                    else:
                        final_value = integer + "." + str(decimal_cut) + Remainder
                else:
                    decimal_cut = decimal[0:sf]
                    Remainder = "0" * len(decimal[sf : len(decimal)])
                    final_value = integer + "." + decimal_cut + Remainder
                # return final_value
                break
            else:
                flag = False
                break
        else:
            flag = False
            # return "You did\'nt input a decimal"
    if flag:
        return final_value
    else:
        return "Error :) please check your values"


def sf_function(value, sf):
    flag = False
    value = str(value)
    ff = sf
    if sf > len(value):
        final_value = "Error :) please check your values"
    else:
        for index in range(len(value)):
            if value[index] == ".":
                if index >= sf:
                    flag = True
                    value = int(value[0:index])
                    final_value = approximation_function(float(value), sf)
                    break
                else:
                    flag = False
                    sf = sf - index
                    final_value = decimal_function(float(value), sf)
    if flag:
        if final_value == "Error :) please check your values":
            return final_value
        else:
            return f"{value} in {ff} S.F is {final_value}"
    else:
        if final_value == "Error :) please check your values":
            return final_value
        else:
            return f"{value} in {ff} S.F is {final_value}"


# print(approximation_function(12345.0,2))


Flag = False
user_input = float(input("Input the number you wan to approximate"))
Significant_figs = int(input("How many S.F/D.P do you want to approximate to"))
v1 = decimal_function(user_input, Significant_figs)
v2 = sf_function(user_input, Significant_figs)
if v1 == "Error :) please check your values":
    final = v2
else:
    final = f"{user_input} in decimal is {v1} \n {v2}"
print(final)


# for index in range(len(str(user_input))):
#     value = str(user_input)
#     if value[index] == '.':
#         Flag= True
#         v1= decimal_function(user_input,Significant_figs)
#         v2= sf_function(user_input,Significant_figs)
#         if v1 == "You did'nt input a decimal":
#             final = approximation_function(user_input,Significant_figs)
#         else:
#             final = f'{user_input} in decimal is {v1} {v2}'
#         # final = f'{user_input} in decimal is {v1} {v2}'
#         break
#     else:
#         Flag = False
# if Flag:
#     print(final)
# else:
#     print(final)


# print(decimal_function(user_input,Significant_figs))
