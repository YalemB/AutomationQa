from Base.SQL.pointer import  DB


class Update:
    x = DB("myflixdb")
    s1 = x.up("UPDATE members SET full_names = 'yalem bakala' WHERE membership_number = 1")
    s2 = x.up("UPDATE members SET gender = 'Male' WHERE membership_number = 1")
    s3 = x.up("UPDATE members SET date_of_birth = '1994-10-15' WHERE membership_number = 1")
    s4 = x.up("UPDATE members SET physical_address = 'Jerusalem Brazil 100/55' WHERE membership_number = 1")
    s5 = x.up("UPDATE members SET email = 'yalem8@gmail.com' WHERE membership_number = 1")
    show = x.ser("select*from members")
    for i in show:
        print(i)




