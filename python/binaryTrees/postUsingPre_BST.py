#! /usr/bin/python3


def postUsingPre(pre):
    if len(pre)!=0:
        if len(pre)==1:
            print(pre[0])
        else:
            root = pre[0]
            for i in range(1,len(pre)):
                if pre[i]>root:
                    break
            postUsingPre(pre[1:i])
            postUsingPre(pre[i:len(pre)])
            print(root)

inOrder = [40 ,30 ,32, 35, 80, 90 ,100 ,120]
postUsingPre(inOrder)

print("*******")

inOrder = [40 ,30, 35, 80, 100]
postUsingPre(inOrder)