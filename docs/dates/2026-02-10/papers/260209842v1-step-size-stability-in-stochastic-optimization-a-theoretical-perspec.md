---
layout: default
title: Step-Size Stability in Stochastic Optimization: A Theoretical Perspective
---

# Step-Size Stability in Stochastic Optimization: A Theoretical Perspective
**arXiv**：[2602.09842v1](https://arxiv.org/abs/2602.09842) · [PDF](https://arxiv.org/pdf/2602.09842.pdf)  
**作者**：Fabian Schaipp, Robert M. Gower, Adrien Taylor  

**一句话要点**：提出步长稳定性理论分析，量化自适应方法优于SGD的鲁棒性

**关键词**：随机优化, 步长稳定性, 自适应方法, 理论分析, 鲁棒性

## 3 点简述
- 核心问题：分析随机优化方法对步长的敏感性，量化性能随步长增大的退化程度
- 方法要点：识别关键量，证明其影响凸问题的次优性界，提供自适应方法更鲁棒的理论证据
- 实验或效果：理论界定性地反映实际性能随步长的变化，适用于非凸问题

## 摘要（原文）

> We present a theoretical analysis of stochastic optimization methods in terms of their sensitivity with respect to the step size. We identify a key quantity that, for each method, describes how the performance degrades as the step size becomes too large. For convex problems, we show that this quantity directly impacts the suboptimality bound of the method. Most importantly, our analysis provides direct theoretical evidence that adaptive step-size methods, such as SPS or NGN, are more robust than SGD. This allows us to quantify the advantage of these adaptive methods beyond empirical evaluation. Finally, we show through experiments that our theoretical bound qualitatively mirrors the actual performance as a function of the step size, even for nonconvex problems.

