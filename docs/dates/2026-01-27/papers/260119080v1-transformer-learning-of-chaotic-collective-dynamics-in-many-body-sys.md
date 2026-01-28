---
layout: default
title: Transformer Learning of Chaotic Collective Dynamics in Many-Body Systems
---

# Transformer Learning of Chaotic Collective Dynamics in Many-Body Systems
**arXiv**：[2601.19080v1](https://arxiv.org/abs/2601.19080) · [PDF](https://arxiv.org/pdf/2601.19080.pdf)  
**作者**：Ho Jang, Gia-Wei Chern  

**一句话要点**：提出基于自注意力Transformer框架以学习混沌多体系统的集体动力学

**关键词**：混沌动力学, 多体系统, Transformer, 自注意力, 降维描述, 时间序列分析

## 3 点简述
- 核心问题：混沌多体动力学中集体可观测量具有强记忆性和指数敏感性，难以降维描述。
- 方法要点：利用自注意力机制选择性重加权长程时间相关性，学习非马尔可夫降维描述。
- 实验或效果：在一维半经典Holstein模型中，Transformer能准确复现混沌的统计特性，如时间相关性和衰减尺度。

## 摘要（原文）

> Learning reduced descriptions of chaotic many-body dynamics is fundamentally challenging: although microscopic equations are Markovian, collective observables exhibit strong memory and exponential sensitivity to initial conditions and prediction errors. We show that a self-attention-based transformer framework provides an effective approach for modeling such chaotic collective dynamics directly from time-series data. By selectively reweighting long-range temporal correlations, the transformer learns a non-Markovian reduced description that overcomes intrinsic limitations of conventional recurrent architectures. As a concrete demonstration, we study the one-dimensional semiclassical Holstein model, where interaction quenches induce strongly nonlinear and chaotic dynamics of the charge-density-wave order parameter. While pointwise predictions inevitably diverge at long times, the transformer faithfully reproduces the statistical "climate" of the chaos, including temporal correlations and characteristic decay scales. Our results establish self-attention as a powerful mechanism for learning effective reduced dynamics in chaotic many-body systems.

