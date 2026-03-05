---
layout: default
title: How Predicted Links Influence Network Evolution: Disentangling Choice and Algorithmic Feedback in Dynamic Graphs
---

# How Predicted Links Influence Network Evolution: Disentangling Choice and Algorithmic Feedback in Dynamic Graphs
**arXiv**：[2603.03945v1](https://arxiv.org/abs/2603.03945) · [PDF](https://arxiv.org/pdf/2603.03945.pdf)  
**作者**：Mathilde Perez, Raphaël Romero, Jefrey Lijffijt, Charlotte Laclau  

**一句话要点**：提出基于多元霍克斯过程的时态框架，以分离动态图中同质性的内在倾向与算法反馈效应。

**关键词**：动态图分析, 链接预测, 霍克斯过程, 算法反馈, 同质性分离, 网络演化

## 3 点简述
- 核心问题：链接预测模型在动态网络中的影响常被静态快照评估，混淆了内在交互倾向与算法反馈的放大效应。
- 方法要点：引入基于交互强度的瞬时偏差度量，超越累积指标，捕捉当前强化动态，并提供动态稳定性和收敛的理论分析。
- 实验或效果：实验表明该度量能可靠反映不同链接预测策略下的算法反馈效应。

## 摘要（原文）

> Link prediction models are increasingly used to recommend interactions in evolving networks, yet their impact on network structure is typically assessed from static snapshots. In particular, observed homophily conflates intrinsic interaction tendencies with amplification effects induced by network dynamics and algorithmic feedback. We propose a temporal framework based on multivariate Hawkes processes that disentangles these two sources and introduce an instantaneous bias measure derived from interaction intensities, capturing current reinforcement dynamics beyond cumulative metrics. We provide a theoretical characterization of the stability and convergence of the induced dynamics, and experiments show that the proposed measure reliably reflects algorithmic feedback effects across different link prediction strategies.

