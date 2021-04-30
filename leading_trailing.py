# @ represents null
# Reading grammar from grammar.txt file

term_n=int(input("Enter the number of terminals: "))
print("Enter the terminals: ")
term_set=[]
for i in range(term_n):
    term_set.append(input())

def lead(nonterm,gra,arr=[],leadset={}):
    lead_=set()
    for left_v in gra:
        if left_v==nonterm:
            for prod in gra[left_v]:
                if len(prod)==1:
                    if prod in term_set:
                        lead_=lead_|{prod}
                    else:
                        if prod!=nonterm and prod not in arr:
                            arr.append(prod)
                            lead_=lead_ | lead(prod,gra,arr,leadset)
                        elif prod!=nonterm and prod in leadset:
                            lead_=lead_ | leadset[prod]
                else:
                    for i in prod:
                        if i in term_set:
                            lead_=lead_|{i}
                            if prod.index(i)!=0:
                                if prod[0]!=nonterm and prod[0] not in arr:
                                    arr.append(prod[0])
                                    lead_=lead_|lead(prod[0],gra,arr,leadset)
                                    
                                elif prod[0]!=nonterm and prod[0] in leadset:
                                    lead_=lead_ | leadset[prod[0]]
                            break
    leadset[nonterm]=lead_
    return lead_

def trail(nonterm,gra,arr=[],trailset={}):
    trail_=set()
    for left_v in gra:
        if left_v==nonterm:
            for prod in gra[left_v]:
                if len(prod)==1:
                    if prod in term_set:
                        trail_=trail_|{prod}
                    else:
                        if (prod!=nonterm) and (prod not in arr):
                            arr.append(prod)
                            trail_=trail_ | trail(prod,gra,arr,trailset)
                        elif prod!=nonterm and prod in trailset:
                            trail_=trail_ | trailset[prod]
                else:
                    for i in prod[::-1]:
                        if i in term_set:
                            trail_=trail_|{i}
                            if prod.index(i)!=len(prod)-1:
                                if (prod[len(prod)-1]!=nonterm) and (prod[len(prod)-1] not in arr):
                                    arr.append(prod[len(prod)-1])
                                    trail_=trail_|trail(prod[len(prod)-1],gra,arr,trailset)
                                elif prod[len(prod)-1]!=nonterm and prod[len(prod)-1] in trailset:
                                    trail_=trail_ | trailset[prod[len(prod)-1]]
                            break
    trailset[nonterm]=trail_
    return trail_

def read_gra(fname):
    f=open(fname,"r")
    raw_gra=f.read()
    lines=raw_gra.split('\n')
    gra=dict({})
    for i in lines:
        words=i.split('->')
        for i in range(len(words)):
            words[i]=words[i].strip()
        prod=words[1].split('/')
        gra[words[0]]=prod
    return gra

def checkgrammar(gra):
    isoperatorgra=True
    for left_v in gra:
        for prod in gra[left_v]:
            j=1
            if len(prod)>1:
                for i in range(len(prod)-1):
                    if (prod[i] not in term_set) and (prod[j] not in term_set):
                        isoperatorgra=False
                        break
                    j+=1   

            elif prod=='@':
                isoperatorgra=False

            if isoperatorgra==False:
                break
        if isoperatorgra==False:
            break
    return isoperatorgra

def printLead(gra):
    for i in gra:
        print("Leading of ",i,":",lead(i,gra))
    
def printTrail(gra):
    for i in gra:
        print("Trailing of ",i,":",trail(i,gra))

gra=read_gra('grammar.txt')
print("Grammar: ",gra)
print("Terminals: ",term_set)
if(checkgrammar(gra)):
    print("Grammar is operator grammar")
    printLead(gra)
    printTrail(gra)
else:
    print("Grammar is not a operator grammar")

