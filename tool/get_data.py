def data():
    with open('./data/login.txt','r',encoding='utf-8')as f:
       return f.readlines()

if __name__ == '__main__':

    mylist=[]
    for i in data():
        mylist.append(tuple(i.strip().split(',')))
    print(mylist[1:])