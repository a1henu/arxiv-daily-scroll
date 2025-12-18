---
layout: default
title: How Many Heads Make an SSM? A Unified Framework for Attention and State Space Models
---

# How Many Heads Make an SSM? A Unified Framework for Attention and State Space Models
**arXiv**：[2512.15115v1](https://arxiv.org/abs/2512.15115) · [PDF](https://arxiv.org/pdf/2512.15115.pdf)  
**作者**：Ali Ghodsi  

**一句话要点**：提出统一框架以分析注意力与状态空间模型的表达性与梯度传播权衡

**关键词**：序列建模, 注意力机制, 状态空间模型, 表达性分析, 梯度传播, 理论框架

## 3 点简述
- 核心问题：序列建模架构多样，但表达性与可训练性权衡缺乏统一理论理解
- 方法要点：引入基于输入依赖交互算子的框架，区分显式因子化与隐式结构化动态模式
- 实验或效果：证明交互秩间隙、头数等价定理和梯度高速公路结果，形式化表达性与梯度传播的权衡

## 摘要（原文）

> Sequence modeling has produced diverse architectures -- from classical recurrent neural networks to modern Transformers and state space models (SSMs) -- yet a unified theoretical understanding of expressivity and trainability trade-offs remains limited. We introduce a unified framework that represents a broad class of sequence maps via an input-dependent effective interaction operator $W_{ij}(X)$, making explicit two recurring construction patterns: (i) the Unified Factorized Framework (Explicit) (attention-style mixing), in which $W_{ij}(X)$ varies through scalar coefficients applied to shared value maps, and (ii) Structured Dynamics (Implicit) (state-space recurrences), in which $W_{ij}$ is induced by a latent dynamical system. Using this framework, we derive three theoretical results. First, we establish the Interaction Rank Gap: models in the Unified Factorized Framework, such as single-head attention, are constrained to a low-dimensional operator span and cannot represent certain structured dynamical maps. Second, we prove an Equivalence (Head-Count) Theorem showing that, within our multi-head factorized class, representing a linear SSM whose lag operators span a $k$-dimensional subspace on length-$n$ sequences requires and is achievable with $H=k$ heads. Third, we prove a Gradient Highway Result, showing that attention layers admit inputs with distance-independent gradient paths, whereas stable linear dynamics exhibit distance-dependent gradient attenuation. Together, these results formalize a fundamental trade-off between algebraic expressivity (interaction/operator span) and long-range gradient propagation, providing theoretical grounding for modern sequence architecture design.

