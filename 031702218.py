import re
import json
import jieba
shi=["北京市","天津市","上海市","重庆市"]
luming=["街","路","道","巷","弄","里","胡同"]
q=re.compile(r'1\d{10}')
#q.findall(strr1)                                                                                               
def transfer(strr):
    if strr[-1]==".":
        strr=strr.strip(".")
    mo=strr.split("!")
    mode=mo[0]
    strr=mo[1]
    mo2=strr.split(",")
    name=mo2[0]
    strr=mo2[1]
    phone=q.findall(strr)[0]
    mo3=strr.split(phone)
    strr=mo3[0]+mo3[1]
    addr1=["","","","",""]
    addr2=["","",""]
    res=jieba.lcut(strr)
    k=0
    for sh in shi:
        if res[0]==sh:
            k=1
            addr1[1]=sh
            addr1[0]=sh[:-1]
            res.insert(0,"")
            break
    if k==0:
        addr1[0]=res[0]
        addr1[1]=res[1]
    if res[2][-1]=="县" or res[2][-1]=="区" or res[2][-1]=="市":
        addr1[2]=res[2]
    del res[0]
    del res[0]
    del res[0]
    res.insert(0,"   ")
    #strr=''.join(strr)
    te=0
    n=len(res)
    for i in range(n):
        if res[i][-2:]=="街道" or res[i][-1]=="镇" or res[i][-1]=="乡":
            addr1[3]=''.join(res[1:i+1])
            te=1
            break
    if te==1:
        for j in range(i+1):
            del res[0]
    addr1[4]=''.join(res)
    detail=addr1[4]
    temp=0
    if mode=="1":
        temp=1
    elif mode=="2":
        m=-1
        for ro in range(7):
            if detail.find(luming[ro])!=-1:
                m=detail.find(luming[ro])
                if ro==6:
                    m=m+1
                addr2[0]=detail[:m+1]
                ml=detail.find("号")
                if ml!=-1:
                    addr2[1]=detail[m+1:ml+1]
                    addr2[2]=detail[ml+1:]
                else:
                    addr2[2]=detail[m+1:]
                break;
        if m==-1:
            addr2[2]=detail
        addr1.pop()
        addr1.extend(addr2)
    else:
        del addr1
    final={
    "姓名": name,
    "手机": phone,
    "地址": addr1
    }
    result = json.dumps(final,ensure_ascii=False)
    print(result)
    
def main():
    while (1):
        strr=input()
        if strr=="END":
            break
        else:
            transfer(strr)

main()
