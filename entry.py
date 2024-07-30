from stockApp import app, db, Product, Entry
import datetime 

app.app_context().push()
db.create_all()

entry_1 = Entry(entrydate=datetime.datetime(2024,5,1),
                productid=1,
                quantity=100,
                mov_type='in')
entry_2 = Entry(entrydate=datetime.datetime(2024,5,1),
                productid=2,
                quantity=100,
                mov_type='in')
entry_3 = Entry(entrydate=datetime.datetime(2024,5,1),
                productid=3,
                quantity=100,
                mov_type='in')
entry_4 = Entry(entrydate=datetime.datetime(2024,5,1),
                productid=4,
                quantity=100,
                mov_type='in')
entry_5 = Entry(entrydate=datetime.datetime(2024,5,1),
                productid=5,
                quantity=100,
                mov_type='in')
entry_6 = Entry(entrydate=datetime.datetime(2024,5,1),
                productid=6,
                quantity=100,
                mov_type='in')

entry_7 = Entry(entrydate=datetime.datetime(2024,5,1),
                productid=1,
                quantity=1,
                mov_type='out')
entry_8 = Entry(entrydate=datetime.datetime(2024,5,1),
                productid=1,
                quantity=2,
                mov_type='out')
entry_9 = Entry(entrydate=datetime.datetime(2024,5,1),
                productid=1,
                quantity=11,
                mov_type='out')
entry_10 = Entry(entrydate=datetime.datetime(2024,5,1),
                 productid=4,
                 quantity=4,
                 mov_type='out')
entry_11 = Entry(entrydate=datetime.datetime(2024,5,1),
                 productid=4,
                 quantity=2,
                 mov_type='in')
entry_12 = Entry(entrydate=datetime.datetime(2024,5,1),
                 productid=4,
                 quantity=15,
                 mov_type='out')

db.session.add(entry_1)
db.session.add(entry_2)
db.session.add(entry_3)
db.session.add(entry_4)
db.session.add(entry_5)
db.session.add(entry_6)
db.session.add(entry_7)
db.session.add(entry_8)
db.session.add(entry_9)
db.session.add(entry_10)
db.session.add(entry_11)
db.session.add(entry_12)

db.session.commit()
