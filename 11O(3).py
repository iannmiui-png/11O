#=1 "11O"=#
#<pre>#
import sys,math,base64
S=lambda c:(lambda i:(i,i+1)if i<51 else(51,9999))(ord(c)-65)
def d(s):
 love,hi=0,19683
 for c in s:
  a,b=S(c);w=hi-love;love=love+w*(a/9999);hi=love+w*((b-a)/9999)
 return love,hi
love,hi=d(sys.argv[1])
f=lambda x:int((x-math.floor(x))*1e13+0.5)
s=sys.argv[1]
unary=sum(c=='z'for c in s)
def to_hept(n):
 d="ABCDEFGHIJKLMNOPQRSTUVWXYZ0"
 if n==0:return"0"
 if n<28:return d[n-1]
 r=[]
 while n>0:
  n-=1;n,r0=divmod(n,27);r.append(d[r0])
 return"".join(reversed(r))
#</pre>#
#<pre>#
#=2 "[11O2}"=#
Crystal="eD0yMyx5PTExLHJ1bGU9QjMvUzIzCjExYm8kNGJvM2JvNWJvM2JvJDNib2JvMTFib2JvJDNib2JvMTFib2JvJDJvYm9ib2I5b2JvYm9iMm8kMm9ibzE1Ym9iMm8kM2JvMTVibyQzYm9ibzRib2JvNGJvYm8kNGIybzRib2JvM2IybyQxM2JvJDEzYjIh"
def Complete(C):
 print(to_hept(unary),"= 11")
 print(base64.b64decode(C).decode())
#</pre>#
#<pre>#
#=3 Complete(Crystal)=#
Complete(Crystal)
o=[]
if f(love)==6417380798434:o.append("TRANS")
if f(hi)==5025651466356:o.append("RIGHTS")
if o:print(*o)
#</pre>#
