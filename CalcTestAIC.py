#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import AIC

# テストデータで検証
x = np.arange(0,1+0.1,0.1)
x = list(x)
y = [0.012,0.121,-0.0194,-0.0183,-0.032,-0.037,0.196,0.077,0.343,0.448,0.434]
a = 0.138573

# 最大対数尤度は3.23417
l = AIC.l_MAX(a,x,y)
print(l,AIC.AIC(l,1))

a = [-0.0852364,0.447618]
# 最大対数尤度は8.50008
l = AIC.l_MAX(a,x,y)
print(l,AIC.AIC(l,2))

a = [0.0602566,-0.522335,0.969953]
# 最大対数尤度は13.37498
l = AIC.l_MAX(a,x,y)
print(l,AIC.AIC(l,3))

a = [0.078849,-0.817746,1.74463,-0.516453]
# 最大対数尤度は13.53748
l = AIC.l_MAX(a,x,y)
print(l,AIC.AIC(l,4))
