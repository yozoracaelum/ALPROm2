'''
m =82.0
n =26.0
print("%.f + %.f = %.f"%(m,n,m +n))
print("%.2f -%.2f = %.4f"%(m,n,m -n))
print("%f x %f = %f"%(m,n,m *n))
print("%f / %f = %f"%(m,n,m /n))
print("%f / %f = %f (dibulatkan ke bawah)"%(m,n,m //n))
#floor
print("%f / %f sisa hasil bagi %f" %(m,n,m %n))
#modulo (sisa bagi)
82 : 26 = 3 sisa 4
82 mod 26 = 4
82 % 26 = 4
3 x 26 = 78
82 - 78 = 4
print("(-)%f = %f"%(m,-m))
print("%f^2 = %f"%(m,m**2))
#kuadrat'''
'''
m =5.0
n =7.0
print("m  = n :", (m == n))
#apakah kedua nilai tersebut sama
print("m != n : "+str(m !=n))
#apakah kedua nilai tersebut berbeda
print("m  > n : "+str(m >n))
print("m  < n : "+str(m <n))
print("m >= n : "+str(m >=n))
print("m <= n : "+str(m <=n))'''
#bit = binary digit
#binary = 0 & 1
'''
m = 10
n = 4
#0 = False (F)
#1 = True (T)
#m (biner) = 0000 1010
# 8 + 0 + 2 + 0 = 10
# n (biner) = 0000 0100
# 0 + 4 + 0 + 0 = 4
# 0000 1010
# 0000 0100
# & (AND)
# 0000 0000 = 0
# 0000 1010
# 0000 1100
# | (OR)
# 1 or 1 = 1
# 1 or 0 = 1
# 0 or 1 = 1
# 0 or 0 = 0
# 0000 1110 = 8 + 4 + 2 + 0 = 14
# 0000 1010
# 0000 0100
# ^ (XOR) (exclusive or)
# 1 xor 1 = 0
# 1 xor 0 = 1
# 0 xor 1 = 1
# 0 xor 0 = 0
# 0000 1110 = 8 + 4 + 2 + 0 = 14
# ~ (negasi)
# 0000 0100 = 4
# ~4 = -(0100 + 1)
# ~4 = -(0101) = -(0 + 4 + 0 + 1) = -5
# shifting (<<) (>>)
# 0000 0100
# << 2
# 0001 0000
# 2^4 = 16
# 0000 0100
# >> 1
# 0000 0010
# 2^1 = 2
print ("m AND n = " + str(m & n))
print ("m OR  n = " + str(m | n))
print ("m XOR n = " + str(m ^ n))
print ("    ~n = " + str(~n))
print ("n geser ke kiri 2 bit  = " + str(n << 2))
print ("n geser ke kanan 1 bit = " + str(n >> 1))'''

l =80
m =90
n =0
#yang dibandingkan adalah nilai kebenarannya, baik itu
# False dan juga True
print("    (m >= l) and (m <= n)  : "+str((m >=l)and(m <=n)))
print("    (m >= l) or  (m <= n)  : "+str(not((m >=l)or(m <=n))))
print("not((m >= l) and (m <= n)) : "+str(not((m >=l)and(m <=n))))

# not ( )










