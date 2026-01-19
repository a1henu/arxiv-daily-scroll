---
layout: default
title: Operator learning on domain boundary through combining fundamental solution-based artificial data and boundary integral techniques
---

# Operator learning on domain boundary through combining fundamental solution-based artificial data and boundary integral techniques
**arXiv**：[2601.11222v1](https://arxiv.org/abs/2601.11222) · [PDF](https://arxiv.org/pdf/2601.11222.pdf)  
**作者**：Haochen Wu, Heng Wu, Benzhuo Lu  

**一句话要点**：提出MAD-BNO框架，通过边界数据和基本解学习线性偏微分方程的算子映射。

**关键词**：算子学习, 边界积分方法, 数学人工数据, 偏微分方程求解, 数据驱动建模

## 3 点简述
- 针对已知基本解的线性偏微分方程，仅使用边界数据学习算子，避免全域采样。
- 结合数学人工数据方法生成训练数据，实现物理一致性和数据驱动，无需外部模拟。
- 在二维拉普拉斯、泊松和亥姆霍兹方程上验证，精度高且训练时间显著减少。

## 摘要（原文）

> For linear partial differential equations with known fundamental solutions, this work introduces a novel operator learning framework that relies exclusively on domain boundary data, including solution values and normal derivatives, rather than full-domain sampling. By integrating the previously developed Mathematical Artificial Data (MAD) method, which enforces physical consistency, all training data are synthesized directly from the fundamental solutions of the target problems, resulting in a fully data-driven pipeline without the need for external measurements or numerical simulations. We refer to this approach as the Mathematical Artificial Data Boundary Neural Operator (MAD-BNO), which learns boundary-to-boundary mappings using MAD-generated Dirichlet-Neumann data pairs. Once trained, the interior solution at arbitrary locations can be efficiently recovered through boundary integral formulations, supporting Dirichlet, Neumann, and mixed boundary conditions as well as general source terms. The proposed method is validated on benchmark operator learning tasks for two-dimensional Laplace, Poisson, and Helmholtz equations, where it achieves accuracy comparable to or better than existing neural operator approaches while significantly reducing training time. The framework is naturally extensible to three-dimensional problems and complex geometries.

