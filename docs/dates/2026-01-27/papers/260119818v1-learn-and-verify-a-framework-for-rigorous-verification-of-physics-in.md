---
layout: default
title: Learn and Verify: A Framework for Rigorous Verification of Physics-Informed Neural Networks
---

# Learn and Verify: A Framework for Rigorous Verification of Physics-Informed Neural Networks
**arXiv**：[2601.19818v1](https://arxiv.org/abs/2601.19818) · [PDF](https://arxiv.org/pdf/2601.19818.pdf)  
**作者**：Kazuaki Tanaka, Kohei Yatabe  

**一句话要点**：提出Learn and Verify框架，为物理信息神经网络提供可计算的严格误差界

**关键词**：物理信息神经网络, 误差界验证, 区间算术, 科学机器学习, 微分方程求解

## 3 点简述
- 核心问题：PINNs缺乏经典数值方法的收敛保证和严格误差界，优化过程非确定性难以数学认证精度
- 方法要点：结合新颖的Doubly Smoothed Maximum损失训练和区间算术验证，计算后验误差界作为机器可验证证明
- 实验或效果：在非线性ODE（含时变系数和有限时间爆炸问题）上成功构建真实解的严格包围，奠定可信科学机器学习基础

## 摘要（原文）

> The numerical solution of differential equations using neural networks has become a central topic in scientific computing, with Physics-Informed Neural Networks (PINNs) emerging as a powerful paradigm for both forward and inverse problems. However, unlike classical numerical methods that offer established convergence guarantees, neural network-based approximations typically lack rigorous error bounds. Furthermore, the non-deterministic nature of their optimization makes it difficult to mathematically certify their accuracy. To address these challenges, we propose a "Learn and Verify" framework that provides computable, mathematically rigorous error bounds for the solutions of differential equations. By combining a novel Doubly Smoothed Maximum (DSM) loss for training with interval arithmetic for verification, we compute rigorous a posteriori error bounds as machine-verifiable proofs. Numerical experiments on nonlinear Ordinary Differential Equations (ODEs), including problems with time-varying coefficients and finite-time blow-up, demonstrate that the proposed framework successfully constructs rigorous enclosures of the true solutions, establishing a foundation for trustworthy scientific machine learning.

