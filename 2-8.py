while True:
    abc = input('What do you want to convert?')
    if abc =='bye':
             break
    elif abc =='2-8':
        while True:
            a = input('enter any binary number: ')
            if a == 'end':
                break
            else:
                for i in a:
                    if i not in '10':
                        print('Please enter 0 or 1!!!')
                        break
                    if a[0] == '0':
                        print('First number must be 1!!!')
                        break
                else:
                    if len(a)%3 ==0:
                        b,c,d,final_a = [],[],[],[]
                        for i in range(len(a)-1,-1,-3):
                            add1 = int(a[i])*1
                            b.append(add1)

                        for j in range(len(a)-2,-1,-3):
                            add2 = int(a[j])*2
                            c.append(add2)

                        for k in range(len(a)-3,-1,-3):
                            add3 = int(a[k])*4
                            d.append(add3)

                        for x in range(len(b)-1,-1,-1):
                            add_final = b[x]+c[x]+d[x]
                            final_a.append(str(add_final))

                        #
                            
                        final_a1 = ''.join(final_a)
                        print(final_a1)                    
    
                    elif len(a)%3 ==1:
                        b,c,d,final_a = [],[],[],[]
                        for i in range(len(a)-1,-1,-3):
                            add1 = int(a[i])*1
                            b.append(add1)

                        for j in range(len(a)-2,-1,-3):
                            add2 = int(a[j])*2
                            c.append(add2)

                        for k in range(len(a)-3,-1,-3):
                            add3 = int(a[k])*4
                            d.append(add3)

                        for x in range(0,len(d),1):
                            add_final = b[x]+c[x]+d[x]
                            final_a.append(str(add_final))

                        final_a.append(str(b[len(b)-1]))
                        for y in range(len(final_a)-1,-1,-1):
                            final_a.append(final_a[y])

                        for z in range(len(final_a)//2):
                            del final_a[0]

                        #
                                
                        final_a1 = ''.join(final_a)
                        print(final_a1)

                    elif len(a)%3 ==2:
                        b,c,d,final_a = [],[],[],[]
                        for i in range(len(a)-1,-1,-3):
                            add1 = int(a[i])*1
                            b.append(add1)

                        for j in range(len(a)-2,-1,-3):
                            add2 = int(a[j])*2
                            c.append(add2)

                        for k in range(len(a)-3,-1,-3):
                            add3 = int(a[k])*4
                            d.append(add3)
                        for x in range(0,len(d),1):
                            add_final = b[x]+c[x]+d[x]
                            final_a.append(str(add_final))

                        final_a.append(str((b[len(b)-1])+(c[len(c)-1])))
                        for y in range(len(final_a)-1,-1,-1):
                            final_a.append(final_a[y])

                        for z in range(len(final_a)//2):
                            del final_a[0]

                        #
            
                        final_a1 = ''.join(final_a)
                        print(final_a1)
    elif abc =='8-2':
        while True:
            a = input('enter any octal number: ')
            if a == 'end':
                break
            else:
                for i in a:
                    if i not in '01234567':
                        print('Please enter 0~7!!!')
                        break
                    if a[0] == '0':
                        print('First number must within 1~7!!!')
                        break
                else:
                    ans = []
                    for i in range(len(a)-1,-1,-1):
                        if a[i] == '0':
                            ans.append('000')
                        elif a[i] == '1':
                            ans.append('001')
                        elif a[i] == '2':
                            ans.append('010')
                        elif a[i] == '3':
                            ans.append('011')
                        elif a[i] == '4':
                            ans.append('100')
                        elif a[i] == '5':
                            ans.append('101')
                        elif a[i] == '6':
                            ans.append('110')
                        elif a[i] == '7':
                            ans.append('111')
                        
                    if a[0] == '1':
                        del ans[len(ans)-1]
                        ans.append('1')
                    elif a[0] == '2':
                        del ans[len(ans)-1]
                        ans.append('10')
                    elif a[0] == '3':
                        del ans[len(ans)-1]
                        ans.append('11')
                        
                    for j in range(len(ans)-1,-1,-1):
                        ans.append(ans[j])

                    for k in range(len(ans)//2):
                        del ans[0]

                   

                    final_ans = ''.join(ans)
                    print(final_ans)
