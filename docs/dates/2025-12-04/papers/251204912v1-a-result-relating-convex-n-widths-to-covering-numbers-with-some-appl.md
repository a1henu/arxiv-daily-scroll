---
layout: default
title: A result relating convex n-widths to covering numbers with some applications to neural networks
---

# A result relating convex n-widths to covering numbers with some applications to neural networks
**arXiv**：[2512.04912v1](https://arxiv.org/abs/2512.04912) · [PDF](https://arxiv.org/pdf/2512.04912.pdf)  
**作者**：Jonathan Baxter, Peter Bartlett  

**一句话要点**：提出凸核覆盖数与函数类逼近误差的关系，应用于神经网络逼近率上界分析。

**关键词**：凸核覆盖数, 函数逼近, 神经网络逼近, 高维输入, 特征组合

## 3 点简述
- 核心问题：高维函数类逼近困难，但某些问题如人脸识别可用小特征集线性组合解决。
- 方法要点：建立函数类逼近误差与其凸核覆盖数的一般关系，推导神经网络逼近上界。
- 实验或效果：未知，论文基于理论分析，未提及具体实验或效果验证。

## 摘要（原文）

> In general, approximating classes of functions defined over high-dimensional input spaces by linear combinations of a fixed set of basis functions or ``features'' is known to be hard. Typically, the worst-case error of the best basis set decays only as fast as $Θ\(n^{-1/d}\)$, where $n$ is the number of basis functions and $d$ is the input dimension. However, there are many examples of high-dimensional pattern recognition problems (such as face recognition) where linear combinations of small sets of features do solve the problem well. Hence these function classes do not suffer from the ``curse of dimensionality'' associated with more general classes. It is natural then, to look for characterizations of high-dimensional function classes that nevertheless are approximated well by linear combinations of small sets of features. In this paper we give a general result relating the error of approximation of a function class to the covering number of its ``convex core''. For one-hidden-layer neural networks, covering numbers of the class of functions computed by a single hidden node upper bound the covering numbers of the convex core. Hence, using standard results we obtain upper bounds on the approximation rate of neural network classes.

