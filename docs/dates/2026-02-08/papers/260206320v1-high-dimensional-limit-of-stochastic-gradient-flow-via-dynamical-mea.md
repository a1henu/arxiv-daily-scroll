---
layout: default
title: High-Dimensional Limit of Stochastic Gradient Flow via Dynamical Mean-Field Theory
---

# High-Dimensional Limit of Stochastic Gradient Flow via Dynamical Mean-Field Theory
**arXiv**：[2602.06320v1](https://arxiv.org/abs/2602.06320) · [PDF](https://arxiv.org/pdf/2602.06320.pdf)  
**作者**：Sota Nishiyama, Masaaki Imaizumi  

**一句话要点**：提出基于动态平均场理论的随机梯度流高维极限分析，统一多轮小批量SGD动力学描述。

**关键词**：随机梯度下降, 高维极限, 动态平均场理论, 非线性模型, 随机微分方程, 机器学习动力学

## 3 点简述
- 核心问题：缺乏非线性模型多轮小批量SGD高维渐进行为的分析框架。
- 方法要点：利用动态平均场理论推导随机梯度流的低维连续时间方程，证明其刻画参数渐近分布。
- 实验或效果：理论适用于广义线性模型和两层神经网络，并统一了现有SGD高维描述。

## 摘要（原文）

> Modern machine learning models are typically trained via multi-pass stochastic gradient descent (SGD) with small batch sizes, and understanding their dynamics in high dimensions is of great interest. However, an analytical framework for describing the high-dimensional asymptotic behavior of multi-pass SGD with small batch sizes for nonlinear models is currently missing. In this study, we address this gap by analyzing the high-dimensional dynamics of a stochastic differential equation called a \emph{stochastic gradient flow} (SGF), which approximates multi-pass SGD in this regime. In the limit where the number of data samples $n$ and the dimension $d$ grow proportionally, we derive a closed system of low-dimensional and continuous-time equations and prove that it characterizes the asymptotic distribution of the SGF parameters. Our theory is based on the dynamical mean-field theory (DMFT) and is applicable to a wide range of models encompassing generalized linear models and two-layer neural networks. We further show that the resulting DMFT equations recover several existing high-dimensional descriptions of SGD dynamics as special cases, thereby providing a unifying perspective on prior frameworks such as online SGD and high-dimensional linear regression. Our proof builds on the existing DMFT technique for gradient flow and extends it to handle the stochasticity in SGF using tools from stochastic calculus.

