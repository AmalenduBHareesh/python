data={
    'u1':{'un':'abc','age':20,'city':'bangalore'},
    'u2':{'un':'xyz','age':21,'city':'hyderabad'},
    'u3':{'un':'wyu','age':22,'city':'bangalore'},
    'u4':{'un':'acb','age':23,'city':'goa'},
}

for i in data:
        if data[i]['city']=='bangalore':
            print(data[i]['un'])
