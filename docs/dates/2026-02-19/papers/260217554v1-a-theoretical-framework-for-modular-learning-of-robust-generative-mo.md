---
layout: default
title: A Theoretical Framework for Modular Learning of Robust Generative Models
---

# A Theoretical Framework for Modular Learning of Robust Generative Models
**arXiv**：[2602.17554v1](https://arxiv.org/abs/2602.17554) · [PDF](https://arxiv.org/pdf/2602.17554.pdf)  
**作者**：Corinna Cortes, Mehryar Mohri, Yutao Zhong  

**一句话要点**：提出模块化生成模型理论框架，通过鲁棒门控机制组合专家模型以匹配整体性能并消除启发式调优。

**关键词**：模块化学习, 生成模型, 鲁棒门控, 极小极大博弈, 泛化理论, 结构蒸馏

## 3 点简述
- 核心问题：大规模生成模型训练资源密集且依赖启发式数据集加权，能否模块化组合专家模型实现鲁棒性能？
- 方法要点：定义归一化门控函数空间，基于极小极大博弈设计鲁棒门控，证明存在性并提供泛化界。
- 实验或效果：在合成和真实数据集上验证模块化架构能缓解梯度冲突，鲁棒超越整体基线模型。

## 摘要（原文）

> Training large-scale generative models is resource-intensive and relies heavily on heuristic dataset weighting. We address two fundamental questions: Can we train Large Language Models (LLMs) modularly-combining small, domain-specific experts to match monolithic performance-and can we do so robustly for any data mixture, eliminating heuristic tuning? We present a theoretical framework for modular generative modeling where a set of pre-trained experts are combined via a gating mechanism. We define the space of normalized gating functions, $G_{1}$, and formulate the problem as a minimax game to find a single robust gate that minimizes divergence to the worst-case data mixture. We prove the existence of such a robust gate using Kakutani's fixed-point theorem and show that modularity acts as a strong regularizer, with generalization bounds scaling with the lightweight gate's complexity. Furthermore, we prove that this modular approach can theoretically outperform models retrained on aggregate data, with the gap characterized by the Jensen-Shannon Divergence. Finally, we introduce a scalable Stochastic Primal-Dual algorithm and a Structural Distillation method for efficient inference. Empirical results on synthetic and real-world datasets confirm that our modular architecture effectively mitigates gradient conflict and can robustly outperform monolithic baselines.

