---
layout: default
title: Smoothness Adaptivity in Constant-Depth Neural Networks: Optimal Rates via Smooth Activations
---

# Smoothness Adaptivity in Constant-Depth Neural Networks: Optimal Rates via Smooth Activations
**arXiv**：[2602.19691v1](https://arxiv.org/abs/2602.19691) · [PDF](https://arxiv.org/pdf/2602.19691.pdf)  
**作者**：Yuhao Liu, Zilin Wang, Lei Wu, Shaobo Zhang  

**一句话要点**：证明平滑激活函数在常数深度网络中实现最优逼近与估计误差率

**关键词**：平滑激活函数, 常数深度神经网络, Sobolev空间逼近, 统计最优性, 构造性近似, 经验风险最小化

## 3 点简述
- 研究平滑激活函数在Sobolev空间中的逼近与统计性质
- 通过构造性框架控制参数范数和模型大小，确保统计可学习性
- 对比非平滑激活函数，平滑激活能自动利用高阶平滑性，无需深度增长

## 摘要（原文）

> Smooth activation functions are ubiquitous in modern deep learning, yet their theoretical advantages over non-smooth counterparts remain poorly understood. In this work, we characterize both approximation and statistical properties of neural networks with smooth activations over the Sobolev space $W^{s,\infty}([0,1]^d)$ for arbitrary smoothness $s>0$. We prove that constant-depth networks equipped with smooth activations automatically exploit arbitrarily high orders of target function smoothness, achieving the minimax-optimal approximation and estimation error rates (up to logarithmic factors). In sharp contrast, networks with non-smooth activations, such as ReLU, lack this adaptivity: their attainable approximation order is strictly limited by depth, and capturing higher-order smoothness requires proportional depth growth. These results identify activation smoothness as a fundamental mechanism, alternative to depth, for attaining statistical optimality. Technically, our results are established via a constructive approximation framework that produces explicit neural network approximators with carefully controlled parameter norms and model size. This complexity control ensures statistical learnability under empirical risk minimization (ERM) and removes the impractical sparsity constraints commonly required in prior analyses.

