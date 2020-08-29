import sys
#
all_ball = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
#
print("现有13个小球，已知其中12个是质量相同的正品，还有1个是质量有差异的次品")
print("要求称重3次找到次品")
print("小球编号如下： ", all_ball)
print("下面进入分组称重查找次品环节")
print("#")
print("------------我是分割线------------")
#
List_A = []
print("请输入第一组4个小球的编号且以逗号分隔，按回车确认：")
input_char = input()
#
if (len(input_char) == 7):
    for i in range(4):
        if input_char[i*2] in all_ball:
            List_A.append(input_char[i*2])
            all_ball.remove(input_char[i*2])
        else:
            print("输入第一组小球编号错误，过程终止")
            sys.exit()
else:
  print("输入第一组小球编号位数错误，过程终止")
  sys.exit()
#
List_B = []
print("请输入第二组4个小球的编号且以逗号分隔，按回车确认：")
input_char = input()
#
if (len(input_char) == 7):
    for i in range(4):
        if input_char[i*2] in all_ball:
            List_B.append(input_char[i*2])
            all_ball.remove(input_char[i*2])
        else:
            print("输入第二组小球编号错误，过程终止")
            sys.exit()
else:
  print("输入二组小球编号位数错误，过程终止")
  sys.exit()
#
print("第一组小球编号=",List_A)
print("第二组小球编号=",List_B)
print("第三组小球编号=",all_ball)
print("#")
print("------------我是分割线------------")
print("接下来进入第一阶段对比称重环节：第一组小球 VS 第二组小球")
print("第一组小球重则输入1，反之则输入2，等重请输入0")
print("请输入比较结果：1，2，0")
#
input_result = input()
if (input_result == '0'):
    print("次品小球在第三组",all_ball)
    print("请从第三组中选择3个球，编为第四组")
    List_C = []
    print("请输入3个小球的编号且以逗号分隔，按回车确认：")
    input_char = input()
    #
    if (len(input_char) == 5):
        for i in range(3):
            if input_char[i*2] in all_ball:
                List_C.append(input_char[i*2])
                all_ball.remove(input_char[i*2])
            else:
                print("第四组小球过程中输入编号错误，过程终止")
                sys.exit()
    else:
        print("第四组小球过程中输入编号错误，过程终止")
        sys.exit()
    #
    print("第四组小球编号=",List_C)
    print("剩下第五组未选择小球编号=",all_ball)
    print("#")
    print("------------我是分割线------------")
    print("接下来进入第二阶段对比称重环节：第四组小球 VS 正品小球")
    print("第四组小球重则输入1，反之则输入2，等重请输入0")
    print("请输入比较结果：1，2，0")
    input_result_2 = input()
    if (input_result_2 == '0'):
        print("次品小球在第五组",all_ball)
        print("第三次称重时，随机抽取第五组小球与正品比较")
        print("不一致则说明抽到的球是次品，且知道次品是轻或重")
        print("一致则说明第五组未抽到的球是次品，但不知是轻是重")
    elif (input_result_2 == '1'):
        print("次品小球在第四组，它比正品重",List_C)
        print("第三次称重时，随机从第四组中抽取两个小球相比")
        print("不一致则说明重球是次品")
        print("一致则说明第四组未抽到的球是次品")
    elif (input_result_2 == '2'):
        print("次品小球在第四组，它比正品轻",List_C)
        print("第三次称重时，随机从第四组中抽取两个小球相比")
        print("不一致则说明轻球是次品")
        print("一致则说明第四组未抽到的球是次品")
    else:
        print("第二次称重结果输入错误，程序终止")
        sys.exit()
    #
elif (input_result == '1'):
    print("次品小球在第一组和第二组中，第一组比较重")
    #
    print("第一组小球编号=",List_A)
    print("第二组小球编号=",List_B)
    print("需要从第一组挑选3个小球，从第二组挑选2个小球，组成第四组")
    print("第一组第二组剩下的3个小球，组成第五组")
    List_C = []
    List_D = []
    print("请输入第一组3个小球的编号且以逗号分隔，按回车确认：")
    input_char = input()
    #
    if (len(input_char) == 5):
        for i in range(3):
            if input_char[i*2] in List_A:
                List_C.append(input_char[i*2])
                List_A.remove(input_char[i*2])
            else:
                print("第四组小球过程中输入编号错误，过程终止")
                sys.exit()
    else:
        print("第四组小球过程中输入编号错误，过程终止")
        sys.exit()
    #
    print("请输入第二组2个小球的编号且以逗号分隔，按回车确认：")
    input_char = input()
    #
    if (len(input_char) == 3):
        for i in range(2):
            if input_char[i*2] in List_B:
                List_D.append(input_char[i*2])
                List_B.remove(input_char[i*2])
            else:
                print("第四组小球过程中输入编号错误，过程终止")
                sys.exit()
    else:
        print("第四组小球过程中输入编号错误，过程终止")
        sys.exit()
    #
    print("第四组小球编号=",List_C + List_D)
    print("第五组小球编号=",List_A + List_B)
    print("接下来进入第二阶段对比称重环节：第四组小球 VS 正品小球")
    print("第四组小球重则输入1，反之则输入2，等重请输入0")
    print("请输入比较结果：1，2，0")
    input_result_2 = input()
    #
    if (input_result_2 == '0'):
        print("次品小球在第五组",List_A + List_B)
        print("并且在第一次称重时，属于重的一方有",List_A)
        print("属于轻的一方有",List_B)
        print("#")
        print("------------我是分割线------------")
        print("接下来进入第三阶段对比称重环节：抽取两个轻球相互比较")
        print("如果两球等重，则次品为未抽到的重球")
        print("如果两球不等，则次品为其中的轻球")
    elif (input_result_2 == '1'):
        print("次品较重，在第一组选中到第四组的3个小球内",List_C)
        print("#")
        print("------------我是分割线------------")
        print("接下来进入第三阶段对比称重环节：三个小球随机抽两个相互比较")
        print("如果两球等重，则次品为未抽到的重球")
        print("如果两球不等，则次品为其中的重球")
    elif (input_result_2 == '2'):
        print("次品较轻，在第二组选中到第四组的2个小球内",List_D)
        print("#")
        print("------------我是分割线------------")
        print("接下来进入第三阶段对比称重环节：从2个小球随机抽1个与正品比较")
        print("如果两球等重，则次品为未抽到的轻球")
        print("如果两球不等，则次品为其中的轻球")
    else:
        print("第二次称重结果输入错误，程序终止")
        sys.exit()
    #
elif (input_result == '2'):
    print("次品小球在第一组和第二组中，第二组比较重")
    #
    print("第一组小球编号=",List_A)
    print("第二组小球编号=",List_B)
    print("需要从第一组挑选3个小球，从第二组挑选2个小球，组成第四组")
    print("第一组第二组剩下的3个小球，组成第五组")
    List_C = []
    List_D = []
    print("请输入第一组3个小球的编号且以逗号分隔，按回车确认：")
    input_char = input()
    #
    if (len(input_char) == 5):
        for i in range(3):
            if input_char[i*2] in List_A:
                List_C.append(input_char[i*2])
                List_A.remove(input_char[i*2])
            else:
                print("第四组小球过程中输入编号错误，过程终止")
                sys.exit()
    else:
        print("第四组小球过程中输入编号错误，过程终止")
        sys.exit()
    #
    print("请输入第二组2个小球的编号且以逗号分隔，按回车确认：")
    input_char = input()
    #
    if (len(input_char) == 3):
        for i in range(2):
            if input_char[i*2] in List_B:
                List_D.append(input_char[i*2])
                List_B.remove(input_char[i*2])
            else:
                print("第四组小球过程中输入编号错误，过程终止")
                sys.exit()
    else:
        print("第四组小球过程中输入编号错误，过程终止")
        sys.exit()
    #
    print("第四组小球编号=",List_C + List_D)
    print("第五组小球编号=",List_A + List_B)
    print("接下来进入第二阶段对比称重环节：第四组小球 VS 正品小球")
    print("第四组小球重则输入1，反之则输入2，等重请输入0")
    print("请输入比较结果：1，2，0")
    input_result_2 = input()
    #
    if (input_result_2 == '0'):
        print("次品小球在第五组",List_A + List_B)
        print("并且在第一次称重时，属于轻的一方有",List_A)
        print("属于重的一方有",List_B)
        print("#")
        print("------------我是分割线------------")
        print("接下来进入第三阶段对比称重环节：抽取两个重球相互比较")
        print("如果两球等重，则次品为未抽到的轻球")
        print("如果两球不等，则次品为其中的重球")
    elif (input_result_2 == '1'):
        print("次品较重，在第二组选中到第四组的2个小球内",List_D)
        print("#")
        print("------------我是分割线------------")
        print("接下来进入第三阶段对比称重环节：从2个小球随机抽1个与正品比较")
        print("如果两球等重，则次品为未抽到的重球")
        print("如果两球不等，则次品为其中的重球")
    elif (input_result_2 == '2'):
        print("次品较轻，在第一组选中到第四组的3个小球内",List_C)
        print("#")
        print("------------我是分割线------------")
        print("接下来进入第三阶段对比称重环节：三个小球随机抽两个相互比较")
        print("如果两球等重，则次品为未抽到的轻球")
        print("如果两球不等，则次品为其中的轻球")
    else:
        print("第二次称重结果输入错误，程序终止")
        sys.exit()
    #
else:
    print("第一次称重结果输入错误，程序终止")
    sys.exit()
    

