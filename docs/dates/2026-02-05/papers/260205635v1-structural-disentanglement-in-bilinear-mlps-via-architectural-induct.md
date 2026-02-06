---
layout: default
title: Structural Disentanglement in Bilinear MLPs via Architectural Inductive Bias
---

# Structural Disentanglement in Bilinear MLPs via Architectural Inductive Bias
**arXiv**：[2602.05635v1](https://arxiv.org/abs/2602.05635) · [PDF](https://arxiv.org/pdf/2602.05635.pdf)  
**作者**：Ojasva Nema, Kaustubh Sharma, Aditya Chauhan, Parikshit Pareek  

**一句话要点**：提出双线性多层感知机以通过架构归纳偏置实现结构解缠，提升模型编辑性和泛化能力。

**关键词**：结构解缠, 双线性多层感知机, 架构归纳偏置, 选择性遗忘, 长时程外推, 模型编辑性

## 3 点简述
- 核心问题：现代神经网络在选择性遗忘和长时程外推中表现脆弱，源于内部表示结构问题。
- 方法要点：引入显式乘法交互作为架构归纳偏置，分析双线性参数化在梯度流下的非混合性质。
- 实验或效果：在模运算、循环推理、李群动力学和遗忘基准上验证，乘法架构能恢复与代数结构对齐的算子。

## 摘要（原文）

> Selective unlearning and long-horizon extrapolation remain fragile in modern neural networks, even when tasks have underlying algebraic structure. In this work, we argue that these failures arise not solely from optimization or unlearning algorithms, but from how models structure their internal representations during training. We explore if having explicit multiplicative interactions as an architectural inductive bias helps in structural disentanglement, through Bilinear MLPs. We show analytically that bilinear parameterizations possess a `non-mixing' property under gradient flow conditions, where functional components separate into orthogonal subspace representations. This provides a mathematical foundation for surgical model modification. We validate this hypothesis through a series of controlled experiments spanning modular arithmetic, cyclic reasoning, Lie group dynamics, and targeted unlearning benchmarks. Unlike pointwise nonlinear networks, multiplicative architectures are able to recover true operators aligned with the underlying algebraic structure. Our results suggest that model editability and generalization are constrained by representational structure, and that architectural inductive bias plays a central role in enabling reliable unlearning.

