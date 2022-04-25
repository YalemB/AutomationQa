from Base.SQL.pointer import  DB


class Qaury:
    x = DB("Arsenal_squd")
    # s1 = x.ser("select*from players_squ WHERE Full_name like 'A%' ")
    # print("full names".title())
    # for i in s1:
    #     print(i[0])
    # s2 = x.ser("select * from players_squ WHERE Age > 26")
    # for i in s2:
    #     print("Player name:", i[0])
    #     print("Pos:", i[1])
    #     print("Age:", i[2])
    # s3 = x.ser("select Full_name,Positions,Age,max(Rating) from players_squ")
    # print("Top rated player:", s3[0])
    # s4 = x.ser("select count(*) from players_squ group by Positions = 'Centre Back' ")
    # print("count of CB:", s4[1][0])
    # s5 = x.ser("select distinct  Positions from players_squ")
    # for i in s5:
    #     print(i[0])
    #
    # y = DB("myflixdb")
    # j1 = y.ser("""select  b.category_id , b.title , a.category_name , a.remarks
    #               from categories as a inner join movies as b
    #               on a.category_id = b.category_id""")
    # for i in j1:
    #     print(i)

    # y = DB("sakila")
    # j2 = y.ser("""select  a.actor_id,concat(a.first_name,' ',a.last_name) as full_name ,c.title
    #               from actor as a
    #               inner join film_actor as b
    #               on a.actor_id = b.actor_id
    #               inner join film as c
    #               on b.film_id = c.film_id""")
    # for i in j2:
    #     print(i)


