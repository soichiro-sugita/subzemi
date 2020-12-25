import numpy as np
#from  folder1.dict_module import *
import folder1 as fl


def f( x ):
    return x**2


x_plot = np.arange(-10, 10 ,0.1)
y_plot = f(x=x_plot)
l_obj = fl.lineplot(xlim= (-10 , 10) ,ylim= (-1, 100) , filename='imgs/lineplot.png')
s_obj = fl.scatter(xlim= (-10 , 10) ,ylim= (-1, 100) , filename='imgs/scatter.png')

l_obj.plot(x_plot , y_plot)
s_obj.plot(x_plot , y_plot)

#exec_dict =　{
  #  "lineplot_0":{"xilim":}
#}
###gitを使う

###conflictを起こしてみる

###