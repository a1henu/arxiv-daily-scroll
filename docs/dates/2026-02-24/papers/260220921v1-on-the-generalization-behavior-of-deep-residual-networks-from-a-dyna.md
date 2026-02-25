---
layout: default
title: On the Generalization Behavior of Deep Residual Networks From a Dynamical System Perspective
---

# On the Generalization Behavior of Deep Residual Networks From a Dynamical System Perspective
**arXiv**：[2602.20921v1](https://arxiv.org/abs/2602.20921) · [PDF](https://arxiv.org/pdf/2602.20921.pdf)  
**作者**：Jinshu Huang, Mingfei Sun, Chunlin Wu  

**一句话要点**：结合动力系统视角，为离散和连续时间残差网络建立深度均匀的泛化误差界

**关键词**：残差网络, 泛化误差界, 动力系统建模, Rademacher复杂度, 深度极限

## 3 点简述
- 研究深度残差网络在离散和连续时间设置下的泛化行为，统一理解其样本复杂度
- 利用Rademacher复杂度、动力系统流映射和深度极限收敛性，推导出O(1/√S)阶的泛化误差界
- 误差界包含结构依赖负项，在较温和假设下提供深度均匀和渐近泛化保证

## 摘要（原文）

> Deep neural networks (DNNs) have significantly advanced machine learning, with model depth playing a central role in their successes. The dynamical system modeling approach has recently emerged as a powerful framework, offering new mathematical insights into the structure and learning behavior of DNNs. In this work, we establish generalization error bounds for both discrete- and continuous-time residual networks (ResNets) by combining Rademacher complexity, flow maps of dynamical systems, and the convergence behavior of ResNets in the deep-layer limit. The resulting bounds are of order $O(1/\sqrt{S})$ with respect to the number of training samples $S$, and include a structure-dependent negative term, yielding depth-uniform and asymptotic generalization bounds under milder assumptions. These findings provide a unified understanding of generalization across both discrete- and continuous-time ResNets, helping to close the gap in both the order of sample complexity and assumptions between the discrete- and continuous-time settings.

