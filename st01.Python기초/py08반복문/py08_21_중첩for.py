print("**********")
print("**********")
print("**********")
print("**********")
print("**********")
print("**********")
print("**********")
print("**********")
print("**********")
print("**********")
print("")

i=0
for i in range(0,10,1):
    print("**********")
print("")
    

# 중첩 for문

i=0
ii=0
for i in range(0,10,1):
    for ii in range(0,10,1):
        print("*", end="")
    print()
print()   
    
# 중첩 for문 2

i=0
for i in range(0,10,1):
    i2=i+1
    for ii in range(0,i2,1):
        print("*", end="")
    print(end="\n")
print()
  
# 중첩 for문 3

i=0
i1=0
i2=0
for i in range(0,10,1):
    i1=i
    i2=10-i
    for ii in range(0,i1,1):
        print(" ", end="")
    for iii in range(0,i2,1):
        print("*", end="")
    print()
print()

# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
