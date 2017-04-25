library("data.table")
flights = fread("flights14.csv")
#flights[origin == 'JFK' & month == 6L]
#flights[1:2] #select rows
#flights[order(origin, -dest)] #order rows
#flights[, arr_delay] #select columns, vector notation 
#flights[, .(arr_delay)] #select columns, column notaton (.() == list())
#flights[, .(arr_delay, dep_delay)] #select 2 columns
#flights[, sum((arr_delay + dep_delay)<0)] #j can be computed upon (How many trips have had total delay < 0?)
#flights[origin == "JFK" & month == 6L,.(m_arr = mean(arr_delay), m_dep = mean(dep_delay))]
  #^^^ do both i & j calls (Calculate the average arrival and departure delay for all flights with “JFK” as the origin airport in the month of June.)
#flights[origin == "JFK" & month == 6L, length(dest)]#returns number of entries that are True for i
#flights[origin == "JFK" & month == 6L, .N]# .N == length(some_column)
#flights[, c("arr_delay","dep_delay"),with=FALSE] #presents 2 columns

#using BY

#flights[, .(.N), by = .(origin)] #produces number of flights from each origin
#flights[carrier == "AA", .N, by = origin] #refers specific airline
#flights[carrier == "AA", .N, by = .(origin, dest)] #organized by origin and destination
#flights[carrier == "AA",
 #       .(mean(arr_delay), mean(dep_delay)),
  #      by = .(origin, dest, month)]#organizes by origin, dest, and month, dislaying the av delays for each
#flights[carrier == "AA",
 #       .(mean(arr_delay), mean(dep_delay)),
  #      keyby = .(origin, dest, month)]#same as before, but sorted. original keeps order

#chaining
#ans <- flights[carrier == "AA", .N, by = .(origin, dest)]
#ans <- ans[order(origin, -dest)] #orders based on origin and dest, origin in ascending order and dest in decending order
#ans #using ans as an intermediate is usefull to perform manipulations on a single origin

#ans <- flights[carrier == "AA", .N, by = .(origin, dest)][order(origin, -dest)]#does same as before but in one line
#head(ans, 10)#displays more compactly and specifies how many entries one wants to view

#ans <- flights[, .N, .(dep_delay>0, arr_delay>0)]#by can take expressions, showing combination of arival/departure delays/early arivals
#ans

#using .SD

DT = data.table(ID = c("b","b","b","a","a","c"), a = 1:6, b = 7:12, c = 13:18)
#DT[, print(.SD), by = ID]#.SD represents a subset of data organized by the ID
#DT[, lapply(.SD, mean), by = ID]#lapply applies some functon (mean) to each entry in the subset of data
#flights[carrier == "AA",                       ## Only on trips with carrier "AA"
 #       lapply(.SD, mean),                     ## compute the mean
  #      by = .(origin, dest, month),           ## for every 'origin,dest,month'
   #     .SDcols = c("arr_delay", "dep_delay")] ## for just those specified in .SDcols
#built the table from AA applying the mean to only those specified in .SDcols

#ans <- flights[, head(.SD, 2), by = month]
#ans #gets first 2 lines for each month
DT
DT[, .(val = c(a,b)), by = ID]# concatinates all a and b entries for each ID
DT[, .(val = list(c(a,b))), by = ID] #same thing but a list



