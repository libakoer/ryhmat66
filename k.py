import time
tekst="midagi erilist"
tahetud_aeg=[2021,9,27,10,42]
Filter=0
while Filter!=5:
    a=0
    aeg=time.localtime()
    Filter=0
    for i in tahetud_aeg:
        if aeg[a]==tahetud_aeg[a]:
            a+=1
            Filter+=1
print(tekst)