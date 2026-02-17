---
layout: default
title: DeepMTL2R: A Library for Deep Multi-task Learning to Rank
---

# DeepMTL2R: A Library for Deep Multi-task Learning to Rank
**arXiv**：[2602.14519v1](https://arxiv.org/abs/2602.14519) · [PDF](https://arxiv.org/pdf/2602.14519.pdf)  
**作者**：Chaosheng Dong, Peiyao Xiao, Yijia Wang, Kaiyi Ji  

**一句话要点**：提出DeepMTL2R开源框架，用于多任务学习排序以优化多个相关性标准。

**关键词**：多任务学习排序, Transformer自注意力, 多目标优化, 开源框架, 帕累托最优

## 3 点简述
- 核心问题：多任务学习排序中需同时优化多个相关性标准，处理异构信号和潜在冲突目标。
- 方法要点：基于Transformer自注意力机制，集成21种先进算法，支持多目标优化以识别帕累托最优模型。
- 实验或效果：在公开数据集上验证有效性，报告竞争性性能，可视化目标间权衡，促进MTL策略比较。

## 摘要（原文）

> This paper presents DeepMTL2R, an open-source deep learning framework for Multi-task Learning to Rank (MTL2R), where multiple relevance criteria must be optimized simultaneously. DeepMTL2R integrates heterogeneous relevance signals into a unified, context-aware model by leveraging the self-attention mechanism of transformer architectures, enabling effective learning across diverse and potentially conflicting objectives. The framework includes 21 state-of-the-art multi-task learning algorithms and supports multi-objective optimization to identify Pareto-optimal ranking models. By capturing complex dependencies and long-range interactions among items and labels, DeepMTL2R provides a scalable and expressive solution for modern ranking systems and facilitates controlled comparisons across MTL strategies. We demonstrate its effectiveness on a publicly available dataset, report competitive performance, and visualize the resulting trade-offs among objectives. DeepMTL2R is available at \href{https://github.com/amazon-science/DeepMTL2R}{https://github.com/amazon-science/DeepMTL2R}.

