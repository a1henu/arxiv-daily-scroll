---
layout: default
title: DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep Operator Networks
---

# DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep Operator Networks
**arXiv**：[2512.07162v1](https://arxiv.org/abs/2512.07162) · [PDF](https://arxiv.org/pdf/2512.07162.pdf)  
**作者**：Kieran A. Malandain, Selim Kalici, Hakob Chakhoyan  

**一句话要点**：提出DeepSVM以解决随机波动率模型实时校准中的计算瓶颈

**关键词**：随机波动率模型, 物理信息深度学习, 深度算子网络, 期权定价, 自适应训练, 计算金融

## 3 点简述
- 核心问题：随机波动率模型校准需重复求解耦合偏微分方程，计算成本高。
- 方法要点：使用物理信息深度算子网络，无需标注数据，通过硬约束和自适应细化稳定训练。
- 实验或效果：训练损失达10^{-5}，期权定价准确，但ATM区域导数存在噪声。

## 摘要（原文）

> Real-time calibration of stochastic volatility models (SVMs) is computationally bottlenecked by the need to repeatedly solve coupled partial differential equations (PDEs). In this work, we propose DeepSVM, a physics-informed Deep Operator Network (PI-DeepONet) designed to learn the solution operator of the Heston model across its entire parameter space. Unlike standard data-driven deep learning (DL) approaches, DeepSVM requires no labelled training data. Rather, we employ a hard-constrained ansatz that enforces terminal payoffs and static no-arbitrage conditions by design. Furthermore, we use Residual-based Adaptive Refinement (RAR) to stabilize training in difficult regions subject to high gradients. Overall, DeepSVM achieves a final training loss of $10^{-5}$ and predicts highly accurate option prices across a range of typical market dynamics. While pricing accuracy is high, we find that the model's derivatives (Greeks) exhibit noise in the at-the-money (ATM) regime, highlighting the specific need for higher-order regularization in physics-informed operator learning.

