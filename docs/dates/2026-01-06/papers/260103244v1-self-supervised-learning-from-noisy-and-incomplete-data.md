---
layout: default
title: Self-Supervised Learning from Noisy and Incomplete Data
---

# Self-Supervised Learning from Noisy and Incomplete Data
**arXiv**：[2601.03244v1](https://arxiv.org/abs/2601.03244) · [PDF](https://arxiv.org/pdf/2601.03244.pdf)  
**作者**：Julián Tachella, Mike Davies  

**一句话要点**：总结自监督学习方法以解决无真值参考的逆问题

**关键词**：自监督学习, 逆问题, 噪声数据, 不完整观测, 成像应用

## 3 点简述
- 核心问题：从噪声或不完整观测中推断信号，缺乏真值参考训练数据。
- 方法要点：综述自监督学习方法，强调理论基础，应用于成像逆问题。
- 实验或效果：未知具体实验，但提供实际应用示例。

## 摘要（原文）

> Many important problems in science and engineering involve inferring a signal from noisy and/or incomplete observations, where the observation process is known. Historically, this problem has been tackled using hand-crafted regularization (e.g., sparsity, total-variation) to obtain meaningful estimates. Recent data-driven methods often offer better solutions by directly learning a solver from examples of ground-truth signals and associated observations. However, in many real-world applications, obtaining ground-truth references for training is expensive or impossible. Self-supervised learning methods offer a promising alternative by learning a solver from measurement data alone, bypassing the need for ground-truth references. This manuscript provides a comprehensive summary of different self-supervised methods for inverse problems, with a special emphasis on their theoretical underpinnings, and presents practical applications in imaging inverse problems.

