---
layout: default
title: Finite-Time Analysis of Gradient Descent for Shallow Transformers
---

# Finite-Time Analysis of Gradient Descent for Shallow Transformers
**arXiv**：[2601.16514v1](https://arxiv.org/abs/2601.16514) · [PDF](https://arxiv.org/pdf/2601.16514.pdf)  
**作者**：Enes Arda, Semih Cayci, Atilla Eryilmaz  

**一句话要点**：分析浅层Transformer梯度下降的有限时间收敛性，揭示宽度对数缩放与序列长度无关的优化误差。

**关键词**：Transformer优化, 梯度下降分析, 核机制, 非凸优化, 序列长度无关性

## 3 点简述
- 核心问题：Transformer非凸优化难以理解，需分析其收敛性。
- 方法要点：在核机制下，用投影梯度下降训练浅层Transformer，推导非渐近保证。
- 实验或效果：数值验证理论，确认宽度对数缩放和优化误差与序列长度无关。

## 摘要（原文）

> Understanding why Transformers perform so well remains challenging due to their non-convex optimization landscape. In this work, we analyze a shallow Transformer with $m$ independent heads trained by projected gradient descent in the kernel regime. Our analysis reveals two main findings: (i) the width required for nonasymptotic guarantees scales only logarithmically with the sample size $n$, and (ii) the optimization error is independent of the sequence length $T$. This contrasts sharply with recurrent architectures, where the optimization error can grow exponentially with $T$. The trade-off is memory: to keep the full context, the Transformer's memory requirement grows with the sequence length. We validate our theoretical results numerically in a teacher-student setting and confirm the predicted scaling laws for Transformers.

