---
layout: default
title: Divine Benevolence is an $x^2$: GLUs scale asymptotically faster than MLPs
---

# Divine Benevolence is an $x^2$: GLUs scale asymptotically faster than MLPs
**arXiv**：[2602.14495v1](https://arxiv.org/abs/2602.14495) · [PDF](https://arxiv.org/pdf/2602.14495.pdf)  
**作者**：Alejandro Francisco Queiruga  

**一句话要点**：提出Gated Quadratic Unit，基于数值分析揭示GLU比MLP具有更快的渐近缩放速度

**关键词**：缩放定律, 数值分析, GLU架构, 函数逼近, 模型架构设计, 渐近分析

## 3 点简述
- 核心问题：GLU架构在大型模型中的成功缺乏理论解释，需从数值分析角度理解其缩放规律
- 方法要点：应用函数逼近理论，证明GLU具有二次逼近阶，导致L(P)∝P^{-3}的缩放斜率优于MLP的P^{-2}
- 实验或效果：在一维函数逼近任务中验证缩放斜率，并设计Gated Quadratic Unit以进一步优化缩放性能

## 摘要（原文）

> Scaling laws can be understood from ground-up numerical analysis, where traditional function approximation theory can explain shifts in model architecture choices. GLU variants now dominate frontier LLMs and similar outer-product architectures are prevalent in ranking models. The success of these architectures has mostly been left as an empirical discovery. In this paper, we apply the tools of numerical analysis to expose a key factor: these models have an $x^2$ which enables \emph{asymptotically} faster scaling than MLPs. GLUs have piecewise quadratic functional forms that are sufficient to exhibit quadratic order of approximation. Our key contribution is to demonstrate that the $L(P)$ scaling slope is $L(P)\propto P^{-3}$ for GLUs but only $L(P)=P^{-2}$ for MLPs on function reconstruction problems. We provide a parameter construction and empirical verification of these slopes for 1D function approximation. From the first principles we discover, we make one stride and propose the ``Gated Quadratic Unit'' which has an even steeper $L(P)$ slope than the GLU and MLP. This opens the possibility of architecture design from first principles numerical theory to unlock superior scaling in large models. Replication code is available at https://github.com/afqueiruga/divine_scaling.

