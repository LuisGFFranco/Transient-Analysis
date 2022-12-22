from CoolProp.CoolProp import PropsSI
from matplotlib import pyplot 
Cevap=1000
delta_t=1
Rot=60
Vdot=10E-06
ETA_v=0.7
ETA_g=0.6
e=0.8
UAcond=10
UAcomp=2
UAevap=10
Tsup=3
TRFR=5+273
Tamb = 32+273
Tcond = 50.77+273
Tevap0=Tamb
T5=Tevap0+Tsup
T3=Tcond-Tsup
T1=T5+e*(T3-T5)
Pevap=PropsSI("P","T", Tevap0,"Q",1,"isobutane")
Pcond=PropsSI("P","T", Tcond,"Q",1,"isobutane")
v1=1/PropsSI("D","P",Pevap,"T",T1,"isobutane")
mdot=(Rot*Vdot*ETA_v)/v1
h1=PropsSI("H","P",Pevap,"T",T1,"isobutane")
h3=PropsSI("H","T",T3,"P",Pcond,"isobutane")
Tevap=[]
for i in range(0,1000):
    value = delta_t*(UAevap*(TRFR-Tevap0)-mdot*(h1-h3))/Cevap+Tevap0
    Tevap.append(value)
    Tevap0=Tevap[i]
    print("Tevap0=", Tevap0)
    T5=Tevap0+Tsup
    T3=Tcond-Tsup
    T1=T5+e*(T3-T5)
    Pevap=PropsSI("P","T", Tevap0,"Q",1,"isobutane")
    Pcond=PropsSI("P","T", Tcond,"Q",1,"isobutane")
    v1=1/PropsSI("D","P",Pevap,"T",T1,"isobutane")
    mdot=(Rot*Vdot*ETA_v)/v1
    h1=PropsSI("H","P",Pevap,"T",T1,"isobutane")
    h3=PropsSI("H","T",T3,"P",Pcond,"isobutane")
    Qevap=UAevap*(TRFR-Tevap0)
t=[]
for i in range(0,1000):
    value = i
    t.append(value)
pyplot.plot(t, Tevap)
pyplot.xlabel("tempo")
pyplot.ylabel("Temperatura")
pyplot.show()