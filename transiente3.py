from CoolProp.CoolProp import PropsSI
import  matplotlib.pyplot  as plt

"""
Evaporador e Gabinete

"""
Cevap=1000
Cgab=1000
delta_t=1
Rot=60
Vdot=10E-06
ETA_v=0.7
ETA_g=0.6
e=0.8
UAcond=10
UAcomp=2
UAevap=10
UAgab=5
Tsup=3
Tsub=3
TRFR=5+273
Tamb = 32+273
Tgab0=Tamb
Tcond = Tamb
Tevap0=Tamb
T5=Tevap0+Tsup
T3=Tcond-Tsub
T1=T5+e*(T3-T5)
Pevap=PropsSI("P","T", Tevap0,"Q",1,"isobutane")
Pcond=PropsSI("P","T", Tcond,"Q",1,"isobutane")
v1=1/PropsSI("D","P",Pevap,"T",T1,"isobutane")
mdot=(Rot*Vdot*ETA_v)/v1
h1=PropsSI("H","P",Pevap,"T",T1,"isobutane")
h3=PropsSI("H","T",T3,"P",Pcond,"isobutane")

"""
Temperatura desejada para o Gabinete

"""


Tdesejada=20+273


#while Tgab0>
Tgab=[]
Tevap=[]

for i in range(0,1000):
    value2=delta_t*(UAgab*(Tamb-Tgab0)-UAevap*(TRFR-Tevap0))/Cgab+Tgab0
    Tgab.append(value2)
    Tgab0=Tgab[i]
    value = delta_t*(UAevap*(TRFR-Tevap0)-mdot*(h1-h3))/Cevap+Tevap0
    Tevap.append(value)
    Tevap0=Tevap[i]
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
plt.plot(t, Tevap)
plt.xlabel("tempo")
plt.ylabel("Temperatura Tevap")
plt.show()
plt.plot(t, Tgab)
plt.xlabel("tempo")
plt.ylabel("Temperatura Gabinete")
plt.show()
T1final=Tevap0
Tgabfinal=Tgab0-273
print("Tgabfinal=", Tgabfinal)
"""
Compressor

"""

ROT=60
VOL=10E-06
Ccomp=100
T20=Tamb

v1=1/PropsSI("D","P",Pevap,"T",T1,"isobutane")
mdot=(Rot*Vdot*ETA_v)/v1
h1=PropsSI("H","P",Pevap,"T",T1final+Tsup,"isobutane")
s1=PropsSI("S","P",Pevap,"T",T1,"isobutane")
h2s=PropsSI("H","T",Tcond,"S",s1,"isobutane")
POT=mdot*(h2s-h1)/ETA_g
h2a=h1+POT/mdot
T2a=PropsSI("T","P",Pcond,"H",h2a,"isobutane")
Qcomp=UAcomp*(T2a-Tamb)
h2=h1+(POT-Qcomp)/mdot
T2=[]
for i in range(0,1000):
    value = delta_t*(mdot*(h2-h1)-UAcomp*(T20-Tamb)+POT)/Cevap+T20
    T2.append(value)
    T20=T2[i]
    h2s=PropsSI("H","T",Tcond,"S",s1,"isobutane")
    POT=mdot*(h2s-h1)/ETA_g
    h2a=h1+POT/mdot
    T2a=PropsSI("T","P",Pcond,"H",h2a,"isobutane")
    Qcomp=UAcomp*(T2a-Tamb)
    h2=h1+(POT-Qcomp)/mdot
t=[]
for i in range(0,1000):
    value = i
    t.append(value)
plt.plot(t, T2)
plt.xlabel("tempo")
plt.ylabel("Temperatura T2")
plt.show()
T2final=T20

"""
Condensador

"""

Ccond=1000
Tcond = Tamb
T3=Tcond-Tsub
Pcond=PropsSI("P","T", Tcond,"Q",1,"isobutane")
h3=PropsSI("H","T",T3 ,"P",Pcond,"isobutane")
h2=PropsSI("H","T",T2final ,"P",Pcond,"isobutane")

Tcond2=[]
for i in range(0,1000):
    value = delta_t*(mdot*(h2-h3)-UAcond*(Tcond-Tamb))/Ccond + Tcond
    Tcond2.append(value)
    Tcond=Tcond2[i]
    h2=PropsSI("H","T",T2final ,"P",Pcond,"isobutane")
    T3=Tcond-Tsub
    h3=PropsSI("H","T",T3 ,"P",Pcond,"isobutane")
t=[]
for i in range(0,1000):
    value = i
    t.append(value)
plt.plot(t, Tcond2)
plt.xlabel("tempo")
plt.ylabel("Temperatura Tcond")
plt.show()