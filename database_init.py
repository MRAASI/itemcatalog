from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///newspapers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete LanguageName if exisitng.
session.query(LanguageName).delete()
# Delete PaperName if exisitng.
session.query(PaperName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(name="Raasi Mathi",
                 email="rasimathi99@gmail.com",
                 picture='http://www.enchanting-costarica.com/wp-content/'
                 'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample Languages 
Lan1 = LanguageName(name="TELUGU",
                     user_id=1)
session.add(Lan1)
session.commit()

Lan2 = LanguageName(name="TAMIL",
                     user_id=1)
session.add(Lan2)
session.commit

Lan3 = LanguageName(name="HINDI",
                     user_id=1)
session.add(Lan3)
session.commit()

Lan4 = LanguageName(name="English",
                     user_id=1)
session.add(Lan4)
session.commit()

Lan5 = LanguageName(name="MALAYALAM",
                     user_id=1)
session.add(Lan5)
session.commit()

Lan6 = LanguageName(name="KANNADA",
                     user_id=1)
session.add(Lan6)
session.commit()

# Populare a Paper with Prices
# Using different users for papers names year also
Paper1 = PaperName(name="sakshi",
                       year="2016",
                       
                       
                       price="4rs",

                        rating="4.2",
                       
                       languagenameid=1,
                       user_id=1)
session.add(Paper1)
session.commit()
Paper1 = PaperName(name="eenadu",
                       year="2016",
                       
                       
                       price="4rs",

                        rating="4.2",
                       
                       languagenameid=1,
                       user_id=2)
session.add(Paper1)
session.commit()


Paper2 = PaperName(name="Dinakaran",
                       year="2019",
                      
                       price="6rs",
                       rating="5",
                       
                       languagenameid=2,
                       user_id=1)
session.add(Paper2)
session.commit()

Paper3 = PaperName(name="AajTak",
                       year="2018",
                       
                       price="4rs",
                       rating="4.0",
                       
                       languagenameid=3,
                       user_id=1)
session.add(Paper3)
session.commit()

Paper4 = PaperName(name="Hindustan Times",
                       year="2017",
                     
                       price="5rs",
                       rating="5",
                     
                       languagenameid=4,
                       user_id=1)
session.add(Paper4)
session.commit()

Paper5 = PaperName(name="Mangalam",
                       year="2014",
                       
                       price="4rs",
                       rating="4.6",
                      
                       languagenameid=5,
                       user_id=1)
session.add(Paper5)
session.commit()

Paper6 = PaperName(name="Prajavani",
                       year="2019",
                      
                       price="4rs",
                       rating="4.5",
                      
                       languagenameid=6,
                       user_id=1)
session.add(Paper6)
session.commit()

print("Your papers database has been inserted!")
