---
layout: default
title: A Teacher-Student Perspective on the Dynamics of Learning Near the Optimal Point
---

# A Teacher-Student Perspective on the Dynamics of Learning Near the Optimal Point
**arXiv**：[2512.15606v1](https://arxiv.org/abs/2512.15606) · [PDF](https://arxiv.org/pdf/2512.15606.pdf)  
**作者**：Carlos Couto, José Mourão, Mário A. T. Figueiredo, Pedro Ribeiro  

**一句话要点**：分析师生网络在最优学习点附近的Hessian谱，揭示小特征值决定长期性能

**关键词**：师生网络, Hessian谱分析, 梯度下降动力学, 最优学习点, 神经网络理论

## 3 点简述
- 研究神经网络在最优学习点附近梯度下降性能，由损失函数Hessian矩阵主导
- 针对师生网络匹配权重情况，解析线性网络Hessian谱渐近分布，数值分析非线性网络
- 发现多项式网络Hessian秩可视为有效参数数，非线性激活函数网络Hessian通常满秩

## 摘要（原文）

> Near an optimal learning point of a neural network, the learning performance of gradient descent dynamics is dictated by the Hessian matrix of the loss function with respect to the network parameters. We characterize the Hessian eigenspectrum for some classes of teacher-student problems, when the teacher and student networks have matching weights, showing that the smaller eigenvalues of the Hessian determine long-time learning performance. For linear networks, we analytically establish that for large networks the spectrum asymptotically follows a convolution of a scaled chi-square distribution with a scaled Marchenko-Pastur distribution. We numerically analyse the Hessian spectrum for polynomial and other non-linear networks. Furthermore, we show that the rank of the Hessian matrix can be seen as an effective number of parameters for networks using polynomial activation functions. For a generic non-linear activation function, such as the error function, we empirically observe that the Hessian matrix is always full rank.

