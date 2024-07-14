#2. Write Program for simple interest. Simple Interest = (P x T x R)/100
def simple_intreset (p,t,r):
    print('The pricipal is:',p)
    print('The time is:',t)
    print('The rate is:',r)
    
    si=(p * t * r)/100
    print('The simple intreset is',si)
    

p= int(input('the pricipal amount:'))
t= int(input('the time amount:'))
r= int(input('the rate amount:'))
simple_intreset(p,t,r)