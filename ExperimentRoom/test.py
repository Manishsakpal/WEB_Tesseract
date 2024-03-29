text_SNI="0=@,1=!,2=^,3=*,4=#,5=$,6=(,7=%,8=),9="
print("Value for dictionary is ",text_SNI)




DicNumSym=[Each.split("=") if "=" in Each else (Each+"=").split("=") for Each in str(text_SNI).strip().replace(" ","").split(",")]

print(DicNumSym)
# if all([True if i in DicNumSym.keys() else False for i in "1234567890"]) and all([True if i in DicNumSym.values() else False for i in "!@#$%^&*()"]):
#     for i in "1234567890":
#         if i not in DicNumSym.keys():
#             DicNumSym[i]=""
        
#     for i,v in enumerate("!@#$%^&*()"):
#         if v not in DicNumSym.values():
#             DicNumSym[list(DicNumSym.keys())[i]]=v
            
    
# #print(DicNumSym)
print([v for i,v in enumerate("!@#$%^&*()") if v not in [z[1] if z[1]!="" else "Dum" for z in DicNumSym]])
Dic={}
dum=0
for i,v in enumerate(DicNumSym):
    print("value",v)
    if v[1]=="":
        Dic[[v for i,v in enumerate("!@#$%^&*()") if v not in [z[1] if z[1]!="" else "Dum" for z in DicNumSym]][dum]]=str(v[0])[-1]
        dum+=1
    else:
        Dic[str(v[1])]=str(v[0])[-1]
    # except:
        # Dic[str(i[1])]=
        
        
print("Dic",Dic)
IndexI=0
print([True if i in Dic.keys() else False for i in "!@#$%^&*()"])
if not(all([True if i in Dic.keys() else False for i in "!@#$%^&*()"])):                
    for i,v in enumerate("!@#$%^&*()"):
        if v not in Dic.keys():
            Dic[v]=[i for i,v in enumerate(Dic.keys()) if v not in "!@#$%^&*()"][IndexI]
            IndexI+=1

IndexI=0
print([True if i in Dic.values() else False for i in "1234567890"])
if not(all([True if i in Dic.values() else False for i in "1234567890"])):
    for i in "1234567890":
        if i not in Dic.values():
            Dic[list(Dic.values())[i]]=[i for i,v in enumerate(Dic.values()) if v not in "1234567890"][IndexI]
            IndexI+=1

            

print("No problem 1",len(Dic),"<=Length Value=>",Dic)