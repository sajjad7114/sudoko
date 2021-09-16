ss = []
#########خواندن فایل و ریختن آن در لیست##########
with open('input.txt','r') as f :
    l = f.read()
    g = l.split('\n')
    for a in range(9) :
        ss[a : a] = [g[a].split()]
f.close()


asli = []
############ایجاد لیست داوطلبان هر خانه###########
for i in range(9) :
    for j in range(9) :
        asli2 = [int(ss[i][j])]
        k = 1
        while k < 10 :
            asli2[k : k] = [k]
            k = k + 1
        asli[9 * i + j : 9 * i + j] = [asli2]



########تابع حذف کننده داوطلبان اضافی############
def mokhatab() :
    #####ستون####
    for i in range(9) :
        for j in range(9) :
            if asli[9 * i + j][0] == 0 :
                for k in range(9) :
                    if asli[9 * i + k][0] > 0 :
                        del asli[9 * i + j][asli[9 * i + k][0]]
                        asli[9 * i + j][asli[9 * i + k][0] : asli[9 * i + k][0]] = [0]
    ####سطر######
    for i in range(9) :
        for j in range(9) :
            if asli[9 * i + j][0] == 0 :
                for k in range(9) :
                    if asli[9 * k + j][0] > 0 :
                        del asli[9 * i + j][asli[9 * k + j][0]]
                        asli[9 * i + j][asli[9 * k + j][0] : asli[9 * k + j][0]] = [0]
    #####مربع#####
    for i in range(9) :
        for j in range(9) :
            if asli[9 * i + j][0] == 0 :
                for k in range(3) :
                    for d in range(3) :
                        a = int(i / 3)
                        b = int(j / 3)
                        if asli[9 * (3 * a + k) + (3 * b + d)][0] > 0 :
                            del asli[9 * i + j][asli[9 * (3 * a + k) + (3 * b + d)][0]]
                            asli[9 * i + j][asli[9 * (3 * a + k) + (3 * b + d)][0] : asli[9 * (3 * a + k) + (3 * b + d)][0]] = [0]
    #####نربع آبی#####
    for i in range(8) :
        if i == 4 or i == 0 :
            i = i + 1
        for j in range(8) :
            if j == 4 or j == 0 :
                j = j + 1
            if asli[9 * i + j][0] == 0 :
                for k in range(3) :
                    for d in range(3):
                        m = 5
                        if i < 4 :
                            m = 1
                        n = 5
                        if j < 4 :
                            n = 1
                        if asli[9 * (m + k) + (n + d)][0] > 0 :
                            del asli[9 * i + j][asli[9 * (m + k) + (n + d)][0]]
                            asli[9 * i + j][asli[9 * (m + k) + (n + d)][0] : asli[9 * (m + k) + (n + d)][0]] = [0]




######تابع پیدا کننده عدد######
def haltak() :
    ######داوطلب تنها#######
    for i in range(9) :
        for j in range(9) :
            if asli[9 * i + j][0] == 0 :
                tedad = 0
                k = 1
                while k < 10 :
                    if asli[9 * i + j][k] == k :
                        tedad = tedad + 1
                        w = k
                    k = k + 1
                if tedad == 1 :
                        del asli[9 * i + j][0]
                        asli[9 * i + j][0 : 0] = [w]
                        return 1
    return 0

def halsoton() :
    #####ستون######
    for i in range(9) :
        k = 1
        while k < 10 :
            tedad = 0
            for j in range(9) :
                if asli[9 * i + j][0] == 0 :
                    if asli[9 * i + j][k] == k :
                        j2 = j
                        tedad = tedad + 1
            if tedad == 1 :
                del asli[9 * i + j2][0]
                asli[9 * i + j2][0 : 0] = [k]
                return 1
            k = k + 1
    return 0

def halsatr() :
    ####سطر######
    for j in range(9) :
        k = 1
        while k < 10:
            tedad = 0
            for i in range(9) :
                if asli[9 * i + j][0] == 0 :
                    if asli[9 * i + j][k] == k :
                        i2 = i
                        tedad = tedad + 1
            if tedad == 1 :
                del asli[9 * i2 + j][0]
                asli[9 * i2 + j][0 : 0] = [k]
                return 1
            k = k + 1
    return 0

def halmorabaa() :
#####مربع#####
    for a in range(3) :
        for b in range(3) :
            k = 1
            while k < 10 :
                tedad = 0
                for c in range(3) :
                    for d in range(3) :
                        i = 3 * a + c
                        j = 3 * b + d
                        if asli[9 * i + j][0] == 0 :
                            if asli[9 * i + j][k] == k :
                                i2 = i
                                j2 = j
                                tedad = tedad + 1
                if tedad == 1 :
                    del asli[9 * i2 + j2][0]
                    asli[9 * i2 + j2][0 : 0] = [k]
                    return 1
                k = k + 1
    return 0

def halbluemorabaa() :
#####نربع آبی#####
    a = 1
    while a < 8 :
        b = 1
        while b < 8 :
            k = 1
            while k < 10 :
                tedad = 0
                for c in range(3) :
                    for d in range(3) :
                        i = a + c
                        j = b + d
                        if asli[9 * i + j][0] == 0 :
                            if asli[9 * i + j][k] == k :
                                i2 = i
                                j2 = j
                                tedad = tedad + 1
                if tedad == 1 :
                    del asli[9 * i2 + j2][0]
                    asli[9 * i2 + j2][0 : 0] = [k]
                    return 1
                k = k + 1
            b = b + 4
        a = a + 4
    return 0



######استفاده از توابع حل کننده تا زمانی که سودوکو کامل حل شود#####
t = 1
while t == 1 :
    mokhatab()
    a = haltak()
    if a == 0 :
        b = halsoton()
        if b == 0 :
            c = halsatr()
            if c == 0 :
                d = halmorabaa()
                if d == 0 :
                    t = halbluemorabaa()


########نوشتن سودوکو حل شده در فایل خروجی########
with open('output.txt','w') as f :
    for i in range(9) :
        for j in range(9) :
            f.write(str(asli[9 * i + j][0]))
            f.write(' ')
        f.write('\n')
f.close()
