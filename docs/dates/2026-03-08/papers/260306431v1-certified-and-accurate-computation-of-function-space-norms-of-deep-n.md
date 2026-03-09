---
layout: default
title: Certified and accurate computation of function space norms of deep neural networks
---

# Certified and accurate computation of function space norms of deep neural networks
**arXiv**：[2603.06431v1](https://arxiv.org/abs/2603.06431) · [PDF](https://arxiv.org/pdf/2603.06431.pdf)  
**作者**：Johannes Gründler, Moritz Maibaum, Philipp Petersen  

**一句话要点**：提出基于区间算术和自适应积分的框架，以认证计算神经网络在函数空间中的范数。

**关键词**：神经网络认证计算, 函数空间范数, 区间算术, 自适应积分, PDE求解, 误差控制

## 3 点简述
- 核心问题：神经网络在PDE求解中缺乏函数空间范数的可靠误差控制，点值评估不足以提供确定性保证。
- 方法要点：利用神经网络结构，结合区间算术包围和自适应标记/细化，计算积分量的认证上下界。
- 实验或效果：数值实验验证了方法在L^p、W^{1,p}和W^{2,p}范数计算中的准确性和实用性。

## 摘要（原文）

> Neural network methods for PDEs require reliable error control in function space norms. However, trained neural networks can typically only be probed at a finite number of point values. Without strong assumptions, point evaluations alone do not provide enough information to derive tight deterministic and guaranteed bounds on function space norms. In this work, we move beyond a purely black-box setting and exploit the neural network structure directly. We present a framework for the certified and accurate computation of integral quantities of neural networks, including Lebesgue and Sobolev norms, by combining interval arithmetic enclosures on axis-aligned boxes with adaptive marking/refinement and quadrature-based aggregation. On each box, we compute guaranteed lower and upper bounds for function values and derivatives, and propagate these local certificates to global lower and upper bounds for the target integrals. Our analysis provides a general convergence theorem for such certified adaptive quadrature procedures and instantiates it for function values, Jacobians, and Hessians, yielding certified computation of $L^p$, $W^{1,p}$, and $W^{2,p}$ norms. We further show how these ingredients lead to practical certified bounds for PINN interior residuals. Numerical experiments illustrate the accuracy and practical behavior of the proposed methods.

