v1 = c(3,6,7,3,1)
v1
v2 = c(6,3,0,6,1)
v2
this = v1+v2
this #normal
this = v1*v2
this #normal
this = v1-v2
this #normal
this = v1/v2
this #dividing by zero causes an Infinity result (the limit) instead of crashing the system

this = v1^v2
this #normal
this = sqrt(v2)
this #normal
this = log10(v2)
this #log of 0 goes to -infinity instead of crashing the system
