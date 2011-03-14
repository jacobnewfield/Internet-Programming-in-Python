import pymongo, sqlite3

sqlite_conn = sqlite3.connect('sqlite3.db')
c = sqlite_conn.cursor()
x = sqlite_conn.cursor()
y = sqlite_conn.cursor()

mongo_conn = pymongo.Connection("localhost", 27017)
family_db = mongo_conn.family

c.execute('SELECT * FROM "family_family" ORDER BY "family_family"."id"')
for family in c:
	family_db.families.save({'_id': family[0], 'name': family[1], 
		'pub_date': family[2]}) 
	#print '%s, %s, %s' % (family[0], family[1], family[2])

c.execute('SELECT * FROM "contacts_contact"')
for contact in c:
	c_id = (contact[0],)
	x.execute('SELECT * FROM "contacts_info" WHERE "contacts_info"."contact_id" = ?', c_id)
	info = x.fetchall()[0]
	birthdate = info[2]
	phone = info[3]
	cell = info[4]
	email = info[5]
	address = info[6]
	family_db.contacts.save({'_id': contact[0], 'name': contact[1], 'phone': phone, 'cell': cell, 'email': email, 'address': address, 'pub_date': contact[2]})

c.execute('SELECT * FROM "family_member"')
for member in c:
	m_id = (member[0],)
	f_id = (member[1],)
	c_id = (member[2],)
	
	x.execute('SELECT "family_family"."family" FROM "family_family" WHERE "family_family"."id" = ?', f_id)
	family = x.fetchone()[0]

	y.execute('SELECT "contacts_contact"."contact" FROM "contacts_contact" WHERE "contacts_contact"."id" = ?', c_id)
	name = y.fetchone()[0]
	
	family_db.members.save({"_id": member[0], "name": name, "family": family, "relation": member[3]})

sqlite_conn.close()
