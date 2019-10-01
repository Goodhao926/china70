import turtle



def star(long,x,y,angle):
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(angle)
    turtle.pendown()
    turtle.color('yellow')
    turtle.begin_fill()
    turtle.forward(long)
    turtle.left(72)

    turtle.forward(long)
    turtle.right(144)


    turtle.forward(long)
    turtle.left(72)


    turtle.forward(long)
    turtle.right(144)

    turtle.forward(long)
    turtle.left(72)

    turtle.forward(long)
    turtle.right(144)

    turtle.forward(long)
    turtle.left(72)

    turtle.forward(long)
    turtle.right(144)

    turtle.forward(long)
    turtle.left(72)

    turtle.forward(long)
    turtle.end_fill()
def DrawRece(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color('red')
    turtle.begin_fill()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(200)
    turtle.end_fill()
   # turtle.setup(width=0.5, height=0.75, startx=None, starty=None)，参数：width, height: 输入宽和高为整数时, 表示像素;
   # 为小数时, 表示占据电脑屏幕的比例，(startx, starty): 这一坐标表示矩形窗口左上角顶点的位置, 如果为空, 则窗口位于屏幕中心。
turtle.setup(width=800,height=500)
turtle.title('Goodhao')
DrawRece(-150,100)#300,200
x=-150
y=100
star(30,x+25,y-50,0)
star(7,x+120,y-25,60)
star(7,x+135,y-50,30)
star(7,x+135,y-75,0)
star(7,x+120,y-109,60)
turtle.penup()
turtle.goto(x,-120)
turtle.pendown()
turtle.setheading(0)
turtle.color('black')
#turtle.write("Done", font=('Arial', 40, 'normal'))
turtle.write('热烈祝贺中华人民共和国成立70周年   BY:GoodHao',font=('微软雅黑',10))
turtle.done()