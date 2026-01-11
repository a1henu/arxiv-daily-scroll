---
layout: default
title: How to Set the Learning Rate for Large-Scale Pre-training?
---

# How to Set the Learning Rate for Large-Scale Pre-training?
**arXiv**：[2601.05049v1](https://arxiv.org/abs/2601.05049) · [PDF](https://arxiv.org/pdf/2601.05049.pdf)  
**作者**：Yunhua Zhou, Shuhao Xing, Junhao Huang, Xipeng Qiu, Qipeng Guo  

**一句话要点**：提出学习率缩放定律与扩展μTransfer至MoE架构，以优化大规模预训练中的学习率配置。

**关键词**：大规模预训练, 学习率优化, 缩放定律, μTransfer, 混合专家模型, 超参数调优

## 3 点简述
- 核心问题：大规模预训练中学习率配置成本高，需从低成本实验外推最优值。
- 方法要点：引入搜索因子缩放定律降低复杂度，扩展μTransfer至MoE架构以覆盖更多超参数。
- 实验或效果：比较拟合与迁移范式，挑战μTransfer在大规模场景的可扩展性，分析模块级调参不足原因。

## 摘要（原文）

> Optimal configuration of the learning rate (LR) is a fundamental yet formidable challenge in large-scale pre-training. Given the stringent trade-off between training costs and model performance, the pivotal question is whether the optimal LR can be accurately extrapolated from low-cost experiments. In this paper, we formalize this investigation into two distinct research paradigms: Fitting and Transfer. Within the Fitting Paradigm, we innovatively introduce a Scaling Law for search factor, effectively reducing the search complexity from O(n^3) to O(n*C_D*C_η) via predictive modeling. Within the Transfer Paradigm, we extend the principles of $μ$Transfer to the Mixture of Experts (MoE) architecture, broadening its applicability to encompass model depth, weight decay, and token horizons. By pushing the boundaries of existing hyperparameter research in terms of scale, we conduct a comprehensive comparison between these two paradigms. Our empirical results challenge the scalability of the widely adopted $μ$ Transfer in large-scale pre-training scenarios. Furthermore, we provide a rigorous analysis through the dual lenses of training stability and feature learning to elucidate the underlying reasons why module-wise parameter tuning underperforms in large-scale settings. This work offers systematic practical guidelines and a fresh theoretical perspective for optimizing industrial-level pre-training.

