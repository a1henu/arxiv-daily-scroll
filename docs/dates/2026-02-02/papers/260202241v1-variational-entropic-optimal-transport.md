---
layout: default
title: Variational Entropic Optimal Transport
---

# Variational Entropic Optimal Transport
**arXiv**：[2602.02241v1](https://arxiv.org/abs/2602.02241) · [PDF](https://arxiv.org/pdf/2602.02241.pdf)  
**作者**：Roman Dyachenko, Nikita Gushchin, Kirill Sokolov, Petr Mokrov, Evgeny Burnaev, Alexander Korotin  

**一句话要点**：提出变分熵最优传输以解决连续空间中弱对偶熵最优传输目标计算效率低的问题。

**关键词**：熵最优传输, 变分方法, 弱对偶目标, 图像翻译, 计算效率, 泛化保证

## 3 点简述
- 核心问题：弱对偶熵最优传输目标中的对数配分项计算困难，导致训练效率低下。
- 方法要点：通过变分重构将对数配分项转化为可处理的辅助正归一化器最小化问题，避免模拟训练。
- 实验或效果：在合成数据和未配对图像翻译实验中展示竞争性或改进的翻译质量，验证优化原理优势。

## 摘要（原文）

> Entropic optimal transport (EOT) in continuous spaces with quadratic cost is a classical tool for solving the domain translation problem. In practice, recent approaches optimize a weak dual EOT objective depending on a single potential, but doing so is computationally not efficient due to the intractable log-partition term. Existing methods typically resolve this obstacle in one of two ways: by significantly restricting the transport family to obtain closed-form normalization (via Gaussian-mixture parameterizations), or by using general neural parameterizations that require simulation-based training procedures. We propose Variational Entropic Optimal Transport (VarEOT), based on an exact variational reformulation of the log-partition $\log \mathbb{E}[\exp(\cdot)]$ as a tractable minimization over an auxiliary positive normalizer. This yields a differentiable learning objective optimized with stochastic gradients and avoids the necessity of MCMC simulations during the training. We provide theoretical guarantees, including finite-sample generalization bounds and approximation results under universal function approximation. Experiments on synthetic data and unpaired image-to-image translation demonstrate competitive or improved translation quality, while comparisons within the solvers that use the same weak dual EOT objective support the benefit of the proposed optimization principle.

