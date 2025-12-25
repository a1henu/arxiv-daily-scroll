---
layout: default
title: A Mechanistic Analysis of Transformers for Dynamical Systems
---

# A Mechanistic Analysis of Transformers for Dynamical Systems
**arXiv**：[2512.21113v1](https://arxiv.org/abs/2512.21113) · [PDF](https://arxiv.org/pdf/2512.21113.pdf)  
**作者**：Gregory Duthé, Nikolaos Evangelou, Wei Liu, Ioannis G. Kevrekidis, Eleni Chatzi  

**一句话要点**：分析单层Transformer在动力学系统中的表示能力与限制，揭示其作为动力学模型的成功与失败条件。

**关键词**：Transformer机制分析, 动力学系统建模, 自注意力限制, 时间序列预测, 状态重构

## 3 点简述
- 核心问题：Transformer作为黑盒模型在动力学系统建模中的内部机制不明确，缺乏理论理解。
- 方法要点：从动力学系统视角将因果自注意力解释为线性历史依赖递归，分析其处理时间信息的方式。
- 实验或效果：通过线性和非线性案例研究，识别不同操作机制，如线性系统中的凸性限制和非线性系统中的自适应延迟嵌入。

## 摘要（原文）

> Transformers are increasingly adopted for modeling and forecasting time-series, yet their internal mechanisms remain poorly understood from a dynamical systems perspective. In contrast to classical autoregressive and state-space models, which benefit from well-established theoretical foundations, Transformer architectures are typically treated as black boxes. This gap becomes particularly relevant as attention-based models are considered for general-purpose or zero-shot forecasting across diverse dynamical regimes. In this work, we do not propose a new forecasting model, but instead investigate the representational capabilities and limitations of single-layer Transformers when applied to dynamical data. Building on a dynamical systems perspective we interpret causal self-attention as a linear, history-dependent recurrence and analyze how it processes temporal information. Through a series of linear and nonlinear case studies, we identify distinct operational regimes. For linear systems, we show that the convexity constraint imposed by softmax attention fundamentally restricts the class of dynamics that can be represented, leading to oversmoothing in oscillatory settings. For nonlinear systems under partial observability, attention instead acts as an adaptive delay-embedding mechanism, enabling effective state reconstruction when sufficient temporal context and latent dimensionality are available. These results help bridge empirical observations with classical dynamical systems theory, providing insight into when and why Transformers succeed or fail as models of dynamical systems.

