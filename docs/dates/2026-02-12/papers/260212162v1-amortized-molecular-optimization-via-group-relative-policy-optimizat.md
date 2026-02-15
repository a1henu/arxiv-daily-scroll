---
layout: default
title: Amortized Molecular Optimization via Group Relative Policy Optimization
---

# Amortized Molecular Optimization via Group Relative Policy Optimization
**arXiv**：[2602.12162v1](https://arxiv.org/abs/2602.12162) · [PDF](https://arxiv.org/pdf/2602.12162.pdf)  
**作者**：Muhammad bin Javaid, Hasham Hussain, Ashima Khanna, Berke Kisin, Jonathan Pirnay, Alexander Mitsos, Dominik G. Grimm, Martin Grohe  

**一句话要点**：提出GRXForm方法，通过组相对策略优化解决分子结构优化中的高方差问题。

**关键词**：分子优化, 图Transformer, 策略优化, 泛化学习, 多目标优化

## 3 点简述
- 核心问题：现有方法在分子结构优化中因起始结构异质性导致高方差，难以泛化。
- 方法要点：基于预训练图Transformer，采用组相对策略优化进行目标导向微调，归一化奖励以降低方差。
- 实验或效果：在分布外分子支架上实现泛化，多目标优化得分与领先实例优化器竞争，无需推理时调用外部模型或精炼。

## 摘要（原文）

> Molecular design encompasses tasks ranging from de-novo design to structural alteration of given molecules or fragments. For the latter, state-of-the-art methods predominantly function as "Instance Optimizers'', expending significant compute restarting the search for every input structure. While model-based approaches theoretically offer amortized efficiency by learning a policy transferable to unseen structures, existing methods struggle to generalize. We identify a key failure mode: the high variance arising from the heterogeneous difficulty of distinct starting structures. To address this, we introduce GRXForm, adapting a pre-trained Graph Transformer model that optimizes molecules via sequential atom-and-bond additions. We employ Group Relative Policy Optimization (GRPO) for goal-directed fine-tuning to mitigate variance by normalizing rewards relative to the starting structure. Empirically, GRXForm generalizes to out-of-distribution molecular scaffolds without inference-time oracle calls or refinement, achieving scores in multi-objective optimization competitive with leading instance optimizers.

