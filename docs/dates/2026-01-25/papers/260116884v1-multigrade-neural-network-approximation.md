---
layout: default
title: Multigrade Neural Network Approximation
---

# Multigrade Neural Network Approximation
**arXiv**：[2601.16884v1](https://arxiv.org/abs/2601.16884) · [PDF](https://arxiv.org/pdf/2601.16884.pdf)  
**作者**：Shijun Zhang, Zuowei Shen, Yuesheng Xu  

**一句话要点**：提出多级神经网络逼近框架，通过逐级训练解决深度网络优化难题，实现可解释的误差细化。

**关键词**：多级深度学习, 神经网络逼近, 残差训练, 优化稳定性, 理论保证, ReLU网络

## 3 点简述
- 核心问题：深度神经网络训练因高度非凸和病态优化而困难，浅层网络如单隐层ReLU模型可凸化训练。
- 方法要点：MGDL逐级训练深度网络，冻结已学级，新残差块仅减少剩余误差，提供稳定层次细化过程。
- 实验或效果：理论证明存在固定宽度多级ReLU方案，残差严格递减并一致收敛到零，数值实验验证结果。

## 摘要（原文）

> We study multigrade deep learning (MGDL) as a principled framework for structured error refinement in deep neural networks. While the approximation power of neural networks is now relatively well understood, training very deep architectures remains challenging due to highly non-convex and often ill-conditioned optimization landscapes. In contrast, for relatively shallow networks, most notably one-hidden-layer $\texttt{ReLU}$ models, training admits convex reformulations with global guarantees, motivating learning paradigms that improve stability while scaling to depth. MGDL builds upon this insight by training deep networks grade by grade: previously learned grades are frozen, and each new residual block is trained solely to reduce the remaining approximation error, yielding an interpretable and stable hierarchical refinement process. We develop an operator-theoretic foundation for MGDL and prove that, for any continuous target function, there exists a fixed-width multigrade $\texttt{ReLU}$ scheme whose residuals decrease strictly across grades and converge uniformly to zero. To the best of our knowledge, this work provides the first rigorous theoretical guarantee that grade-wise training yields provable vanishing approximation error in deep networks. Numerical experiments further illustrate the theoretical results.

