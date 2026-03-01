---
layout: default
title: Latent Matters: Learning Deep State-Space Models
---

# Latent Matters: Learning Deep State-Space Models
**arXiv**：[2602.23050v1](https://arxiv.org/abs/2602.23050) · [PDF](https://arxiv.org/pdf/2602.23050.pdf)  
**作者**：Alexej Klushyn, Richard Kurle, Maximilian Soelch, Botond Cseke, Patrick van der Smagt  

**一句话要点**：提出约束优化框架和EKVAE以提升深度状态空间模型的动态学习能力

**关键词**：深度状态空间模型, 约束优化, 变分推断, 贝叶斯滤波, 系统识别, 序列预测

## 3 点简述
- 核心问题：传统训练方法可能无法确保模型学习到序列数据的真实动态
- 方法要点：引入约束优化框架，结合EKVAE融合变分推断与贝叶斯滤波/平滑
- 实验或效果：在系统识别和预测精度上显著改进，EKVAE优于先前模型

## 摘要（原文）

> Deep state-space models (DSSMs) enable temporal predictions by learning the underlying dynamics of observed sequence data. They are often trained by maximising the evidence lower bound. However, as we show, this does not ensure the model actually learns the underlying dynamics. We therefore propose a constrained optimisation framework as a general approach for training DSSMs. Building upon this, we introduce the extended Kalman VAE (EKVAE), which combines amortised variational inference with classic Bayesian filtering/smoothing to model dynamics more accurately than RNN-based DSSMs. Our results show that the constrained optimisation framework significantly improves system identification and prediction accuracy on the example of established state-of-the-art DSSMs. The EKVAE outperforms previous models w.r.t. prediction accuracy, achieves remarkable results in identifying dynamical systems, and can furthermore successfully learn state-space representations where static and dynamic features are disentangled.

