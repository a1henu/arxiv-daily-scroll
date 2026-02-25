---
layout: default
title: VINA: Variational Invertible Neural Architectures
---

# VINA: Variational Invertible Neural Architectures
**arXiv**：[2602.20480v1](https://arxiv.org/abs/2602.20480) · [PDF](https://arxiv.org/pdf/2602.20480.pdf)  
**作者**：Shubhanshu Shekhar, Mohammad Javad Khojasteh, Ananya Acharya, Tony Tohme, Kamal Youcef-Toumi  

**一句话要点**：提出VINA框架，基于变分无监督损失统一INNs和NFs，提供理论保证并应用于海洋声学反演问题。

**关键词**：可逆神经网络, 归一化流, 变分推断, 生成建模, 反问题求解, 理论保证

## 3 点简述
- 核心问题：INNs和NFs在现实假设下缺乏近似质量的理论保证。
- 方法要点：引入变分无监督损失框架，推导后验和分布准确性的理论性能保证。
- 实验或效果：通过案例研究提炼设计原则，并在海洋声学反演中验证有效性。

## 摘要（原文）

> The distinctive architectural features of normalizing flows (NFs), notably bijectivity and tractable Jacobians, make them well-suited for generative modeling. Invertible neural networks (INNs) build on these principles to address supervised inverse problems, enabling direct modeling of both forward and inverse mappings. In this paper, we revisit these architectures from both theoretical and practical perspectives and address a key gap in the literature: the lack of theoretical guarantees on approximation quality under realistic assumptions, whether for posterior inference in INNs or for generative modeling with NFs.
>   We introduce a unified framework for INNs and NFs based on variational unsupervised loss functions, inspired by analogous formulations in related areas such as generative adversarial networks (GANs) and the Precision-Recall divergence for training normalizing flows. Within this framework, we derive theoretical performance guarantees, quantifying posterior accuracy for INNs and distributional accuracy for NFs, under assumptions that are weaker and more practically realistic than those used in prior work.
>   Building on these theoretical results, we conduct extensive case studies to distill general design principles and practical guidelines. We conclude by demonstrating the effectiveness of our approach on a realistic ocean-acoustic inversion problem.

