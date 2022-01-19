from re import T

def create_project():
    projData = open('projectInfo.txt','r')
    title = input('Enter title: ')
    totalTarget = int(input('Enter your total target: '))
    details = input('Enter details: ')
    startDate = input('Enter starting date: ')
    endDate = input('Enter end data: ')

    
    r =[]
    n = []
    for i in projData:
        a,b,c,d,e = i.split(',')
        r.append(a)
        n.extend([b,c,d,e])
    mydata = dict(zip(r, n))
    print(mydata)

    pdata = open('projectInfo.txt','a')
    pdata.write(title + ',' + str(totalTarget) + ',' + details + ',' + startDate +',' + endDate + '\n')
    
    print('You just created new project')




def view_project():
    usrData = open('projectInfo.txt','r')
    title = input('Enter the project title: ')


    r =[]
    n = []
    for i in usrData:
        a,b,c,d,e = i.split(',')
        r.append(a)
        n.append([b,c,d,e])
    # print(n)
    # print(r)
    mydata = dict(zip(r, n))

    for key in mydata:
        if key == title:
            print(f'Project data:\nTitle:{title}\nTotal target:{mydata[title][0]}\nDetails:{mydata[title][1]}\nStart date:{mydata[title][2]}\nEnd date:{mydata[title][3]}')

    # if mydata[title] in mydata.keys():
    #     print('kkf')

def viewAll_project():
    usrData = open('projectInfo.txt','r')
    r =[]
    n = []
    for i in usrData:
        a,b,c,d,e = i.split(',')
        r.append(a)
        n.append([b,c,d,e])
    # print(n)
    # print(r)
    mydata = dict(zip(r, n))

    print('Projects list:')
    for key in mydata:
        print(key)


def deleteAll_project():
    usrData = open('projectInfo.txt','r')
    title = input('Enter the project title: ')

    with open("projectInfo.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i != "df":
                f.write(i)
            
        f.truncate()

