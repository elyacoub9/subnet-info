
from sys import exit,argv

def to_binary(decnum):

    q=decnum//2
    r=decnum%2
    lbin=[r]
    while q!=0:
        r=q%2
        lbin.insert(0,r)
        q=q//2
    while len(lbin)<8:
        lbin.insert(0,0)
    return (lbin) #=[1, 0, 1, 0]



def to_decimal(nbin):

    nbin=str(nbin)
    nbin=nbin[-1::-1]
    ndec=0
    for i in range(len(nbin)):
        ndec=ndec+(2**i)*int(nbin[i])
    return (ndec) #=10


def cidr_to_binary(cidr):
    binlist=[]

    for i in range(32):
        if int(len(binlist))<cidr:
            binlist.append((1))
        else:
            binlist.append((0))
    return binlist #=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]


def cidr_to_decimal(cidr):
    binlist=[]
    binlist1=cidr_to_binary(cidr)
    [binlist.append(str(i)) for i in binlist1 ]

    for i in range(len(binlist)):
        if i==8 or i==17 or i==26 :
            binlist.insert(i,",")
    binlist="".join(binlist)
    binlist=binlist.split(",")

    declist=[]
    for i  in binlist:
        declist.append(to_decimal(i))

    return declist # =print(cidr_to_decimal(24))



def bin_add_to_deci(binadd1):
    binadd=[]
    [binadd.append(str(i)) for i in binadd1 ]
    for i in range(len(binadd)):
        if i==8 or i==17 or i==26 :
            binadd.insert(i,",")
    binadd="".join(binadd)
    binadd=binadd.split(",")

    realbinadd=[]
    for i  in binadd:
        realbinadd.append(to_decimal(i))
    return realbinadd


def listtostring(mylist):
    mylist2=mylist
    mylist=[]
    for i in mylist2:
        mylist.append(str(i))
    mylist=".".join(mylist)
    return mylist



add=str(argv[1])
cidr=(argv[2])
cidr=int(cidr)

add1=add.split(".")
add_bin=[]
[add_bin.append(to_binary(int(i))) for i in add1]

addcheck=add.split(".")


_3ayro="This's an invalid address U IDIOT, \nA valid address its octets must be belong to the range [1:255]"

if int(addcheck[0])==0:
    print(_3ayro)
    exit()
elif int(addcheck[0] )>255 or int(addcheck[1] )>255 or int(addcheck[2] )>255 or int(addcheck[3] )>255:
    print(_3ayro)
    exit()

else:
#get the class  from a giving net id and if it's prv/pub
    add_class =""
    PrivatOrPublic=""

    if 0<=int(add1[0])<=127:
        add_class="class A"
        if int(add1[0])==127:
            PrivatOrPublic=("loopback address")
        elif int(add1[0])==10:
            PrivatOrPublic="privat"
        else:
            PrivatOrPublic="public"

    elif 128<=int(add1[0])<=191:
        add_class="class B"
        if int(add1[0])==172 and 16<=int(add1[1])<=31:
            PrivatOrPublic="privat"
        else:
            PrivatOrPublic="public"


    elif 192<=int(add1[0])<=223:
        add_class="class C "
        if int(add1[0])==192 and int(add1[1])==168:
            PrivatOrPublic="privat"
        else:
            PrivatOrPublic="public"


    elif 224<=int(add1[0])<=239:
        add_class="class D "
    elif 240<=int(add1[0])<=255:
        add_class="class E "


    real_cidr=cidr_to_binary(cidr)

#the network id
    netadd1=[]
    for i in range(len(add_bin)):
        for j in range(len(add_bin[i])):
            netadd1.append(add_bin[i][j])


    for i in range(len(real_cidr)):
        if real_cidr[i]==0 :
            netadd1[i]=0
    netadd=(bin_add_to_deci(netadd1))
    netadd=listtostring(netadd)

#the broadcast id
    bdcadd1=[]
    for i in range(len(add_bin)):
        for j in range(len(add_bin[i])):
            bdcadd1.append(add_bin[i][j])

    for i in range(len(real_cidr)):
        if real_cidr[i]==0 :
            bdcadd1[i]=1
    bdcadd=bin_add_to_deci(bdcadd1)
    bdcadd=listtostring(bdcadd)

#the 1st add
    firsadd1=netadd1
    firsadd1[-1]=1
    firsadd=bin_add_to_deci(firsadd1)
    firsadd=listtostring(firsadd)

#the last add
    lastadd1=bdcadd1
    lastadd1[-1]=0
    lastadd=bin_add_to_deci(lastadd1)
    lastadd=listtostring(lastadd)

##
    adds=2**(32-cidr)-2

    submask=cidr_to_decimal(cidr)
    submask=listtostring(submask)
    add1=listtostring(add1)

    content={
    "class":add_class,
    "type":PrivatOrPublic,
    "subnet mask":submask,
    "network ID":netadd,
    "broadcast ID":bdcadd,
    "first address":firsadd,
    "last address":lastadd,
    "nb of addresses":adds,
    }
    def result(mycontent):
        print("-"*60)
        print(f" {add1}/{cidr} ".center(60))
        print("-"*60)
        for i,j in mycontent.items():
            print(f" {str(i)} ".capitalize().ljust(30)+"|"+f" {str(j).center(30)}")

result(content)






