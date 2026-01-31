---
layout: default
title: Dynamical Adapter Fusion: Constructing A Global Adapter for Pre-Trained Model-based Class-Incremental Learning
---

# Dynamical Adapter Fusion: Constructing A Global Adapter for Pre-Trained Model-based Class-Incremental Learning
**arXiv**：[2601.21341v1](https://arxiv.org/abs/2601.21341) · [PDF](https://arxiv.org/pdf/2601.21341.pdf)  
**作者**：Ruiqi Liu, Boyu Diao, Zijia An, Zhulin An, Fei Wang, Yongjun Xu  

**一句话要点**：提出动态适配器融合以构建全局适配器，解决类增量学习中的遗忘与干扰问题。

**关键词**：类增量学习, 适配器融合, PAC-Bayes定理, 稳定性与可塑性平衡, 预训练模型, 灾难性遗忘

## 3 点简述
- 核心问题：类增量学习中，冻结预训练模型并训练任务特定适配器导致知识迁移受限和检索成本高，参数融合易引发破坏性干扰和灾难性遗忘。
- 方法要点：基于PAC-Bayes定理，融合任务特定适配器参数、先前全局适配器参数和初始化参数，利用损失函数泰勒展开动态优化融合系数，平衡稳定性与可塑性。
- 实验或效果：在多个类增量学习基准测试中实现最先进性能，验证了方法的有效性。

## 摘要（原文）

> Class-Incremental Learning (CIL) requires models to continuously acquire new classes without forgetting previously learned ones. A dominant paradigm involves freezing a pre-trained model and training lightweight, task-specific adapters. However, maintaining task-specific parameters hinders knowledge transfer and incurs high retrieval costs, while naive parameter fusion often leads to destructive interference and catastrophic forgetting. To address these challenges, we propose Dynamical Adapter Fusion (DAF) to construct a single robust global adapter. Grounded in the PAC-Bayes theorem, we derive a fusion mechanism that explicitly integrates three components: the optimized task-specific adapter parameters, the previous global adapter parameters, and the initialization parameters. We utilize the Taylor expansion of the loss function to derive the optimal fusion coefficients, dynamically achieving the best balance between stability and plasticity. Furthermore, we propose a Robust Initialization strategy to effectively capture global knowledge patterns. Experiments on multiple CIL benchmarks demonstrate that DAF achieves state-of-the-art (SOTA) performance.

