---
layout: default
title: SAILS: Segment Anything with Incrementally Learned Semantics for Task-Invariant and Training-Free Continual Learning
---

# SAILS: Segment Anything with Incrementally Learned Semantics for Task-Invariant and Training-Free Continual Learning
**arXiv**：[2602.14767v1](https://arxiv.org/abs/2602.14767) · [PDF](https://arxiv.org/pdf/2602.14767.pdf)  
**作者**：Shishir Muralidhara, Didier Stricker, René Schuster  

**一句话要点**：提出SAILS框架，通过无训练方式解决类增量语义分割中的遗忘问题

**关键词**：类增量语义分割, 无训练学习, 原型学习, 持续学习, 语义分割

## 3 点简述
- 核心问题：持续学习面临重复训练、高计算成本和遗忘挑战，限制实际应用
- 方法要点：利用基础模型分两阶段处理，先零样本区域提取，再通过原型进行语义关联
- 实验或效果：在标准数据集上，无训练性能常优于基于训练的方法，完全消除遗忘

## 摘要（原文）

> Continual learning remains constrained by the need for repeated retraining, high computational costs, and the persistent challenge of forgetting. These factors significantly limit the applicability of continuous learning in real-world settings, as iterative model updates require significant computational resources and inherently exacerbate forgetting. We present SAILS -- Segment Anything with Incrementally Learned Semantics, a training-free framework for Class-Incremental Semantic Segmentation (CISS) that sidesteps these challenges entirely. SAILS leverages foundational models to decouple CISS into two stages: Zero-shot region extraction using Segment Anything Model (SAM), followed by semantic association through prototypes in a fixed feature space. SAILS incorporates selective intra-class clustering, resulting in multiple prototypes per class to better model intra-class variability. Our results demonstrate that, despite requiring no incremental training, SAILS typically surpasses the performance of existing training-based approaches on standard CISS datasets, particularly in long and challenging task sequences where forgetting tends to be most severe. By avoiding parameter updates, SAILS completely eliminates forgetting and maintains consistent, task-invariant performance. Furthermore, SAILS exhibits positive backward transfer, where the introduction of new classes can enhance performance on previous classes.

