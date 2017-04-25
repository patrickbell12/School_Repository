v1 = c(3,6,7,3,1) 
v2 = c(6,3,0,6,1)
#the dot multiplication of vecors results in a single number
m = v1 %*% v2
m
m = v2 %*% v1
m #we got a single number

M = matrix(
  c(3,6,7,1),
  nrow=2,
  ncol=2
)
M
v = c(3,1)
v
a = M%*%v #we should get 2 numbers
a
a = v%*%M #we should get 2 different numbers
a
