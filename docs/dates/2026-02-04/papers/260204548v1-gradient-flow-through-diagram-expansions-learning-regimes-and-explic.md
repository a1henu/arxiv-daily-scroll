---
layout: default
title: Gradient Flow Through Diagram Expansions: Learning Regimes and Explicit Solutions
---

# Gradient Flow Through Diagram Expansions: Learning Regimes and Explicit Solutions
**arXiv**：[2602.04548v1](https://arxiv.org/abs/2602.04548) · [PDF](https://arxiv.org/pdf/2602.04548.pdf)  
**作者**：Dmitry Yarotsky, Eugene Golikov, Yaroslav Gusev  

**一句话要点**：提出基于图展开的梯度流分析框架，用于学习张量分解的标度机制与显式解。

**关键词**：梯度流分析, 图展开方法, 张量分解, 学习机制, 显式解, 标度理论

## 3 点简述
- 核心问题：分析大规模学习问题中梯度流的标度机制与非线性动态。
- 方法要点：利用类似费曼图的图展开形式幂级数，推导损失演化的大尺寸极限。
- 实验或效果：理论预测与实验高度一致，揭示张量分解的多种学习相。

## 摘要（原文）

> We develop a general mathematical framework to analyze scaling regimes and derive explicit analytic solutions for gradient flow (GF) in large learning problems. Our key innovation is a formal power series expansion of the loss evolution, with coefficients encoded by diagrams akin to Feynman diagrams. We show that this expansion has a well-defined large-size limit that can be used to reveal different learning phases and, in some cases, to obtain explicit solutions of the nonlinear GF. We focus on learning Canonical Polyadic (CP) decompositions of high-order tensors, and show that this model has several distinct extreme lazy and rich GF regimes such as free evolution, NTK and under- and over-parameterized mean-field. We show that these regimes depend on the parameter scaling, tensor order, and symmetry of the model in a specific and subtle way. Moreover, we propose a general approach to summing the formal loss expansion by reducing it to a PDE; in a wide range of scenarios, it turns out to be 1st order and solvable by the method of characteristics. We observe a very good agreement of our theoretical predictions with experiment.

