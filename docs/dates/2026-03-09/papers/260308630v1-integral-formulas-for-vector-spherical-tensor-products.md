---
layout: default
title: Integral Formulas for Vector Spherical Tensor Products
---

# Integral Formulas for Vector Spherical Tensor Products
**arXiv**：[2603.08630v1](https://arxiv.org/abs/2603.08630) · [PDF](https://arxiv.org/pdf/2603.08630.pdf)  
**作者**：Valentin Heyraud, Zachary Weller-Davies, Jules Tilly  

**一句话要点**：提出向量球面张量积的积分公式，以简化SO(3)-等变神经网络中的张量计算

**关键词**：向量球面张量积, SO(3)-等变神经网络, 积分公式, Gaunt系数, 张量积简化, 计算效率优化

## 3 点简述
- 核心问题：向量球面张量积计算复杂，需简化以提升效率
- 方法要点：推导积分公式，获得反对称Gaunt系数的闭式表达式
- 实验或效果：实现9倍计算量减少，支持等变神经网络应用

## 摘要（原文）

> We derive integral formulas that simplify the Vector Spherical Tensor Product recently introduced by Xie et al., which generalizes the Gaunt tensor product to antisymmetric couplings. In particular, we obtain explicit closed-form expressions for the antisymmetric analogues of the Gaunt coefficients. This enables us to simulate the Clebsch-Gordan tensor product using a single Vector Spherical Tensor Product, yielding a $9\times$ reduction in the required tensor product evaluations. Our results enable efficient and practical implementations of the Vector Spherical Tensor Product, paving the way for applications of this generalization of Gaunt tensor products in $\mathrm{SO}(3)$-equivariant neural networks. Moreover, we discuss how the Gaunt and the Vector Spherical Tensor Products allow to control the expressivity-runtime tradeoff associated with the usual Clebsch-Gordan Tensor Products. Finally, we investigate low rank decompositions of the normalizations of the considered tensor products in view of their use in equivariant neural networks.

