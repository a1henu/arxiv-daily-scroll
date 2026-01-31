---
layout: default
title: Why Adam Works Better with $β_1 = β_2$: The Missing Gradient Scale Invariance Principle
---

# Why Adam Works Better with $β_1 = β_2$: The Missing Gradient Scale Invariance Principle
**arXiv**：[2601.21739v1](https://arxiv.org/abs/2601.21739) · [PDF](https://arxiv.org/pdf/2601.21739.pdf)  
**作者**：Alberto Fernández-Hernández, Cristian Pérez-Corral, Jose I. Mestre, Manuel F. Dolz, Enrique S. Quintana-Ortí  

**一句话要点**：揭示Adam优化器在β₁=β₂时因梯度尺度不变性而表现更优的原理

**关键词**：Adam优化器, 梯度尺度不变性, 深度学习优化, 动量参数, 训练稳定性

## 3 点简述
- 核心问题：Adam优化器中β₁=β₂为何能提升训练效果，缺乏理论解释
- 方法要点：提出梯度尺度不变性概念，证明Adam一阶梯度尺度不变当且仅当β₁=β₂
- 实验或效果：在视觉和语言任务中验证梯度缩放对更新平滑性的影响

## 摘要（原文）

> Adam has been at the core of large-scale training for almost a decade, yet a simple empirical fact remains unaccounted for: both validation scores and the qualitative behaviour of the training runs improve when the momentum parameters satisfy $β_{1}=β_{2}$. Some recent studies have reported this pattern, but there is still no explanation for why this choice helps. We show that this choice is closely tied to a structural property that we refer to as \textit{gradient scale invariance}. We formalize this notion and prove that Adam becomes gradient scale invariant of first order if and only if $β_{1}=β_{2}$. This perspective places the balanced regime of Adam in direct alignment with the design principles underlying several recent optimizers that explicitly enforce scale-robust updates. The theory is supported by experiments across vision and language tasks, and across different architectural families, in which rescaling the gradient has a markedly smoother effect on the update when $β_{1}=β_{2}$. Overall, our results offer a coherent explanation for an open question in the behavior of Adam and provide a simple principle that helps guide the design of future optimizers.

