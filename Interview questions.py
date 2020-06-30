str1 = 'abc'
str2 ='def'
str3 = 'dabecf'  # valid or invalid


def IsShuffle(str1,str2,str3):
    
    if len(str1) + len(str2) != len(str3):
        return False
    
    first_position = str3.find(str1[0])
    second_position = str3.find(str1[1])
    third_position = str3.find(str1[2])
    
    first_position2 = str3.find(str2[0])
    second_position2 = str3.find(str2[1])
    third_position2 = str3.find(str2[2])

    if (first_position < second_position < third_position) and (first_position2 < second_position2 < third_position2):
        return True
    else:
        return False

IsShuffle('abc','def','abdcef')
IsShuffle('abe','adf','abadfe')


