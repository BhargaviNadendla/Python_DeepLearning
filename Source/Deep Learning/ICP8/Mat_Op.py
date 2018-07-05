import tensorflow as tf

a = list(map(int, input("Enter the shape of a,b").split()))  #taking the console input for the shape of a,b in a list of integers
                                                             #the shape of a,b should be same as they have to be added

c=list(map(int,input("Enter shape of c").split())) #taking the console input for c as the above
                                                   #the shape of c can be differet bi=ut the order should be compatible to multiply

sm, la = map(int, input("please enter the range of numbers").split()) #asking for the range for the random numbers
ip1 = tf.random_uniform(a, sm, la, dtype=tf.int32, seed=27)   #generating random matrix of ip1
ip2 = tf.random_uniform(a, sm, la, dtype=tf.int32, seed=9)    #generating random matrix of ip2
ip3 = tf.random_uniform(c, sm, la, dtype=tf.int32, seed=18)   #generating random matrix of ip3
#taking matrices into a,b,c for convineance
a = tf.Variable(ip1)
b = tf.Variable(ip2)
c = tf.Variable(ip3)

# (a^2 + b)*c

power = tf.pow(a, 2) #calculating power of 2 for (a^2)
sum1 = tf.add(power, b) #adding with b (a^2+b)
mul = tf.matmul(sum1, c) #multiplying with c ((a^2+b)*c)

init = tf.global_variables_initializer() #initializing the global variables

with tf.Session() as sess: #creating a session
    sess.run(init) #initializing the session

    print("The matrix a is: ", sess.run(a)) #getting a by running the session variable
    print("The matrix b is: ", sess.run(b)) #getting b
    print("The matrix c is: ", sess.run(c)) #getting c
    print("The power a^2 is: ", sess.run(power)) #getting a^2
    print("The sum a^2 + b is: ", sess.run(sum1))#getting sum
    print("The resultant a^2 +b is: ", sess.run(mul))#getting multiplication