---
layout: default
title: A Frobenius-Optimal Projection for Enforcing Linear Conservation in Learned Dynamical Models
---

# A Frobenius-Optimal Projection for Enforcing Linear Conservation in Learned Dynamical Models
**arXiv**：[2512.22084v1](https://arxiv.org/abs/2512.22084) · [PDF](https://arxiv.org/pdf/2512.22084.pdf)  
**作者**：John M. Mango, Ronald Katende  

**一句话要点**：提出Frobenius最优投影以在数据驱动线性动力学模型中恢复线性守恒律

**关键词**：线性守恒律, Frobenius范数, 正交投影, 数据驱动模型, 动力学建模, 不变性嵌入

## 3 点简述
- 核心问题：数据驱动线性动力学模型可能违反线性守恒律，需恢复这些不变性
- 方法要点：基于Frobenius范数最小化，推导出正交投影公式，通过低秩修正强制守恒
- 实验或效果：在马尔可夫型示例中验证了精确守恒和最小扰动动态的特性

## 摘要（原文）

> We consider the problem of restoring linear conservation laws in data-driven linear dynamical models. Given a learned operator $\widehat{A}$ and a full-rank constraint matrix $C$ encoding one or more invariants, we show that the matrix closest to $\widehat{A}$ in the Frobenius norm and satisfying $C^\top A = 0$ is the orthogonal projection $A^\star = \widehat{A} - C(C^\top C)^{-1}C^\top \widehat{A}$. This correction is uniquely defined, low rank and fully determined by the violation $C^\top \widehat{A}$. In the single-invariant case it reduces to a rank-one update. We prove that $A^\star$ enforces exact conservation while minimally perturbing the dynamics, and we verify these properties numerically on a Markov-type example. The projection provides an elementary and general mechanism for embedding exact invariants into any learned linear model.

