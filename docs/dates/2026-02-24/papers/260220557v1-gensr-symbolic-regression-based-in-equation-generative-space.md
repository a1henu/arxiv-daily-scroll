---
layout: default
title: GENSR: Symbolic Regression Based in Equation Generative Space
---

# GENSR: Symbolic Regression Based in Equation Generative Space
**arXiv**：[2602.20557v1](https://arxiv.org/abs/2602.20557) · [PDF](https://arxiv.org/pdf/2602.20557.pdf)  
**作者**：Qian Li, Yuxiao Hu, Juncheng Liu, Yuntian Chen  

**一句话要点**：提出GenSR框架，基于生成潜在空间解决符号回归中离散搜索噪声问题。

**关键词**：符号回归, 生成潜在空间, 条件变分自编码器, CMA-ES优化, 贝叶斯框架, 数值平滑性

## 3 点简述
- 核心问题：离散方程空间的结构修改与数值行为不匹配，导致拟合误差反馈噪声大，难以指导搜索。
- 方法要点：使用双分支条件变分自编码器构建具有符号连续性和局部数值平滑性的生成潜在空间，结合CMA-ES进行精细搜索。
- 实验或效果：实验显示GenSR在预测准确性、表达式简洁性和计算效率方面联合优化，且在噪声下保持鲁棒性。

## 摘要（原文）

> Symbolic Regression (SR) tries to reveal the hidden equations behind observed data. However, most methods search within a discrete equation space, where the structural modifications of equations rarely align with their numerical behavior, leaving fitting error feedback too noisy to guide exploration. To address this challenge, we propose GenSR, a generative latent space-based SR framework following the `map construction -> coarse localization -> fine search'' paradigm. Specifically, GenSR first pretrains a dual-branch Conditional Variational Autoencoder (CVAE) to reparameterize symbolic equations into a generative latent space with symbolic continuity and local numerical smoothness. This space can be regarded as a well-structured `map'' of the equation space, providing directional signals for search. At inference, the CVAE coarsely localizes the input data to promising regions in the latent space. Then, a modified CMA-ES refines the candidate region, leveraging smooth latent gradients. From a Bayesian perspective, GenSR reframes the SR task as maximizing the conditional distribution $p(\mathrm{Equ.} \mid \mathrm{Num.})$, with CVAE training achieving this objective through the Evidence Lower Bound (ELBO). This new perspective provides a theoretical guarantee for the effectiveness of GenSR. Extensive experiments show that GenSR jointly optimizes predictive accuracy, expression simplicity, and computational efficiency, while remaining robust under noise.

