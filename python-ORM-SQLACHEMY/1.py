
from sqlalchemy import  create_engine



engine = create_engine("mysql+pymysql://zhoutao:123@192.168.77.129/S13",max_overflow = 5)


engine.execute("insert into T10(name,price,type_id) VALUES ('zt',111,1)")



result = engine.execute("select * from T10")

a=result.fetchall()
print(a)