---
layout: default
title: The Minary Primitive of Computational Autopoiesis
---

# The Minary Primitive of Computational Autopoiesis
**arXiv**：[2601.04501v1](https://arxiv.org/abs/2601.04501) · [PDF](https://arxiv.org/pdf/2601.04501.pdf)  
**作者**：Daniel Connor, Colin Defant  

**一句话要点**：提出Minary计算框架作为首个可形式化证明的自创生原语，用于构建自维持分布式系统。

**关键词**：自创生计算, 概率事件建模, 线性叠加, 随机过程收敛, 分布式系统, 主观身份

## 3 点简述
- 核心问题：定义可形式化证明的自创生计算原语，以支持主观身份概念的系统构建。
- 方法要点：使用多维向量表示概率事件，通过线性叠加在[-1,1]范围内实现干扰，基于能力矩阵驱动随机过程。
- 实验或效果：证明系统收敛于唯一平稳分布，推导出共识的均值和方差公式，展示能力结构对共识的影响。

## 摘要（原文）

> We introduce Minary, a computational framework designed as a candidate for the first formally provable autopoietic primitive. Minary represents interacting probabilistic events as multi-dimensional vectors and combines them via linear superposition rather than multiplicative scalar operations, thereby preserving uncertainty and enabling constructive and destructive interference in the range $[-1,1]$. A fixed set of ``perspectives'' evaluates ``semantic dimensions'' according to hidden competencies, and their interactions drive two discrete-time stochastic processes. We model this system as an iterated random affine map and use the theory of iterated random functions to prove that it converges in distribution to a unique stationary law; we moreover obtain an explicit closed form for the limiting expectation in terms of row, column, and global averages of the competency matrix. We then derive exact formulas for the mean and variance of the normalized consensus conditioned on the activation of a given semantic dimension, revealing how consensus depends on competency structure rather than raw input signals. Finally, we argue that Minary is organizationally closed yet operationally open in the sense of Maturana and Varela, and we discuss implications for building self-maintaining, distributed, and parallelizable computational systems that house a uniquely subjective notion of identity.

