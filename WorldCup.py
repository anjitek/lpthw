# first two round points statistics

rlt = [1, -1, 0]
all_rlt = []
allchances = []
a_pts = []
b_pts = []
c_pts = []
d_pts = []

def rtp(a):
    if a == 1:
        return 3
    elif a == 0:
        return 1
    else:
        return 0

for a_rlt in rlt:
    #print(f"a_rlt is {a_rlt}")
    for b_rlt in rlt:
        #print(f"b_rlt is {b_rlt}")
        for c_rlt in rlt:
            #print(f"c_rlt is {c_rlt}")
            for d_rlt in rlt:
                #print(f"d_rlt is {d_rlt}")
                if (a_rlt + b_rlt + c_rlt + d_rlt) == 0:
                    all_rlt = [a_rlt, b_rlt, c_rlt, d_rlt]
                    allchances.append(all_rlt)
                    a_pts.append(rtp(a_rlt))
                    b_pts.append(rtp(b_rlt))
                    c_pts.append(rtp(c_rlt))
                    d_pts.append(rtp(d_rlt))

                    #print(f"this is a valid result:------> {all_rlt}")
                #else:
                    #print("invalid results")
for showall in allchances:
    print(showall)

for aall in a_pts:
    print(aall)
