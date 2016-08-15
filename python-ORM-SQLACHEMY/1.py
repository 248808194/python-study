from sqlalchemy import  create_engine

engine = create_engine("mysql+pymysql://root:newbie@127.0.0.1:3306/world",max_overflow=5)
engine.execute(
    "INSERT INTO city (name,CountryCode,District,Population) VALUES ('zhoutao','ZT','zhoutao2',123456)"
)


result = engine.execute('select * from city')

a=result.fetchall()
for i in a:
    print(i)