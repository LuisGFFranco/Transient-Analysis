from CoolProp.CoolProp import PropsSI
from matplotlib import pyplot 
Ccond=1000
UAcond=10
Tamb=32+273
Tcond0=Tamb
delta_t=1
ETA_v=0.7
ETA_g=0.6
ROT=60
VOL=10E-06
T1=35.7+273
Tevap=-17.6+273
Tsub=3
UAcomp=2
Pcond=PropsSI("P","T", Tcond0,"Q",1,"isobutane")
Pevap=PropsSI("P","T", Tevap,"Q",1,"isobutane")
v1=1/PropsSI("D","P",Pevap,"T",T1,"isobutane")
mdot=(ROT*VOL*ETA_v)/v1
h1=PropsSI("H","P",Pevap,"T",T1,"isobutane")
s1=PropsSI("S","P",Pevap,"T",T1,"isobutane")
h2s=PropsSI("H","T",Tcond0,"S",s1,"isobutane")
POT=mdot*(h2s-h1)/ETA_g
h2a=h1+POT/mdot
T2a=PropsSI("T","P",Pcond,"H",h2a,"isobutane")
Qcomp=UAcomp*(T2a-Tamb)
h2=h1+(POT-Qcomp)/mdot
T3=Tcond0-Tsub
h3=PropsSI("H","T",T3 ,"P",Pcond,"isobutane")
T20=PropsSI("T","P",Pcond,"H",h2,"isobutane")
Tcond=[]
T2=[]
for i in range(0,1000):
    value = delta_t*(mdot*(h2-h3)-UAcond*(Tcond0-Tamb))/Ccond + Tcond0
    Tcond.append(value)
    Tcond0=Tcond[i]
    value2=delta_t*(mdot*(h2-h1)-UAcomp*(T20-Tamb))/Ccond+T20
    T2.append(value2)
    T20=T2[i]
    print("T20=",T20)
    print("Tcond0=", Tcond0)
    h2s=PropsSI("H","T",Tcond0,"S",s1,"isobutane")
    Pcond=PropsSI("P","T", Tcond0,"Q",1,"isobutane")
    POT=mdot*(h2s-h1)/ETA_g
    h2a=h1+POT/mdot
    T2a=PropsSI("T","P",Pcond,"H",h2a,"isobutane")
    Qcomp=UAcomp*(T2a-Tamb)
    h2=h1+(POT-Qcomp)/mdot
    T3=Tcond0-Tsub
    h3=PropsSI("H","T",T3 ,"P",Pcond,"isobutane")
t=[]
for i in range(0,1000):
    value = i
    t.append(value)
pyplot.plot(t, Tcond, "-b", label="Tcond")
pyplot.plot(t, T2, "-r", label="T2")
pyplot.legend(loc="upper left")
pyplot.xlabel("tempo")
pyplot.ylabel("Temperatura")
pyplot.show()

