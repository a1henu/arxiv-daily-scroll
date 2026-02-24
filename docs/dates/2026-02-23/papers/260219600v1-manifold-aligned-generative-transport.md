---
layout: default
title: Manifold-Aligned Generative Transport
---

# Manifold-Aligned Generative Transport
**arXiv**：[2602.19600v1](https://arxiv.org/abs/2602.19600) · [PDF](https://arxiv.org/pdf/2602.19600.pdf)  
**作者**：Xinyu Tian, Xiaotong Shen  

**一句话要点**：提出MAGT以解决高维生成建模中支持保真度与采样效率的平衡问题

**关键词**：生成建模, 流形学习, 传输模型, 高斯平滑, 重要性采样, Wasserstein界

## 3 点简述
- 核心问题：高维数据集中于低维流形，需平衡支持保真度与采样效率
- 方法要点：学习单次前向的流形对齐传输，基于固定高斯平滑水平训练
- 实验或效果：在合成和基准数据集上提升保真度和流形集中度，采样快于扩散模型

## 摘要（原文）

> High-dimensional generative modeling is fundamentally a manifold-learning problem: real data concentrate near a low-dimensional structure embedded in the ambient space. Effective generators must therefore balance support fidelity -- placing probability mass near the data manifold -- with sampling efficiency. Diffusion models often capture near-manifold structure but require many iterative denoising steps and can leak off-support; normalizing flows sample in one pass but are limited by invertibility and dimension preservation. We propose MAGT (Manifold-Aligned Generative Transport), a flow-like generator that learns a one-shot, manifold-aligned transport from a low-dimensional base distribution to the data space. Training is performed at a fixed Gaussian smoothing level, where the score is well-defined and numerically stable. We approximate this fixed-level score using a finite set of latent anchor points with self-normalized importance sampling, yielding a tractable objective. MAGT samples in a single forward pass, concentrates probability near the learned support, and induces an intrinsic density with respect to the manifold volume measure, enabling principled likelihood evaluation for generated samples. We establish finite-sample Wasserstein bounds linking smoothing level and score-approximation accuracy to generative fidelity, and empirically improve fidelity and manifold concentration across synthetic and benchmark datasets while sampling substantially faster than diffusion models.

