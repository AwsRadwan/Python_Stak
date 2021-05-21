#  1
# list_big=[1,2,3,-5,-7,6]
# def big(list_big):
#     x=int(len(list_big))
#     for i in range(0,x):
#         if list_big[i]>=0:
#             list_big[i]="Big"
#     return list_big
# print(big(list_big))

# 2
# def pos(x):
#     count=0
#     for s in range(0,len(x)):
#         if x[s]>0:
#             count+=1
#     x.pop()
#     x.append(count)
#     return x
# x=[1,5,2,4,-8,-5,1,4]
# r=pos(x)
# print(r)
#  3
# def sum_all(x):
#     sum=0
#     for i in range(0,len(x)):
#         sum+=x[i]
#     return sum
# x=[1,2,3,5,3,5]
# print(sum_all(x))
#  4
# def avg(x):
#     sum=0
#     for i in range(0,len(x)):
#         sum+=x[i]
#     avg=sum/len(x)
#     return avg
# x=[1,2,3,5,3,4]
# print(avg(x))
# 5
# def length(x):
#     return len(x)
# x=[1,2,3,5,3,4]
# print(length(x))
#  6
# def minimum(x):
#     mini=x[0]
#     for i in range(0,len(x)):
#         if x[i]<mini:
#             mini=x[i]
#     if len(x)=0:
#         return False
#     return mini
# x=[1,5,7,6,-1,6,3,-3]
# print(minimum(x))
#  7
# def maximum(x):
#     maxi=x[0]
#     for i in range(0,len(x)):
#         if x[i]>maxi:
#             maxi=x[i]
#     if len(x)==0:
#         return False
#     return maxi
# x=[1,5,7,6,-1,6,3,-3]
# print(maximum(x))
# 8
# def dic(x):
#     sum=0
#     mini=x[0]
#     maxi=x[0]
#     l=len(x)
#     for i in range(0,len(x)):
#         sum+=x[i]
#         if x[i]<mini:
#             mini=x[i]
#         if x[i]>maxi:
#             maxi=x[i]
#     avg=sum/len(x)
#     dictionary={
#         'sumTotal': sum,
#         'average': avg,
#         'minimum': mini,
#         'maximum': maxi,
#         'length of the list': l
#     }
#     return dictionary
# x=[5,1,2,4,8,-5,-9,6,7]
# print(dic(x))
# 9 
# def reverse(x):
#     l=int(len(x)/2)
#     for i in range(0,l,1):
#         temp=x[i]
#         x[i]=x[len(x)-1-i]
#         x[len(x)-1-i]=temp
#     return x
# x=[5,1,2,4,8,-5,6]
# print(reverse(x))





