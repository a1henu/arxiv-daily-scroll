---
layout: default
title: Perfect reconstruction of sparse signals using nonconvexity control and one-step RSB message passing
---

# Perfect reconstruction of sparse signals using nonconvexity control and one-step RSB message passing
**arXiv**：[2512.17426v1](https://arxiv.org/abs/2512.17426) · [PDF](https://arxiv.org/pdf/2512.17426.pdf)  
**作者**：Xiaosi Gu, Ayaka Sakata, Tomoyuki Obuchi  

**一句话要点**：提出基于非凸性控制和一步复本对称破缺消息传递的稀疏信号完美重建方法

**关键词**：稀疏信号重建, 非凸优化, 消息传递算法, 复本对称破缺, 状态演化, 算法极限

## 3 点简述
- 研究稀疏信号重建问题，采用平滑截断绝对偏差惩罚最小化方法
- 开发一步复本对称破缺近似消息传递算法及其状态演化方程，改进算法极限
- 通过数值实验验证性能提升，但增益有限且略低于贝叶斯最优阈值

## 摘要（原文）

> We consider sparse signal reconstruction via minimization of the smoothly clipped absolute deviation (SCAD) penalty, and develop one-step replica-symmetry-breaking (1RSB) extensions of approximate message passing (AMP), termed 1RSB-AMP. Starting from the 1RSB formulation of belief propagation, we derive explicit update rules of 1RSB-AMP together with the corresponding state evolution (1RSB-SE) equations. A detailed comparison shows that 1RSB-AMP and 1RSB-SE agree remarkably well at the macroscopic level, even in parameter regions where replica-symmetric (RS) AMP, termed RS-AMP, diverges and where the 1RSB description itself is not expected to be thermodynamically exact. Fixed-point analysis of 1RSB-SE reveals a phase diagram consisting of success, failure, and diverging phases, as in the RS case. However, the diverging-region boundary now depends on the Parisi parameter due to the 1RSB ansatz, and we propose a new criterion -- minimizing the size of the diverging region -- rather than the conventional zero-complexity condition, to determine its value. Combining this criterion with the nonconvexity-control (NCC) protocol proposed in a previous RS study improves the algorithmic limit of perfect reconstruction compared with RS-AMP. Numerical solutions of 1RSB-SE and experiments with 1RSB-AMP confirm that this improved limit is achieved in practice, though the gain is modest and remains slightly inferior to the Bayes-optimal threshold. We also report the behavior of thermodynamic quantities -- overlaps, free entropy, complexity, and the non-self-averaging susceptibility -- that characterize the 1RSB phase in this problem.

