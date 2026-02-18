---
layout: default
title: A Scalable Curiosity-Driven Game-Theoretic Framework for Long-Tail Multi-Label Learning in Data Mining
---

# A Scalable Curiosity-Driven Game-Theoretic Framework for Long-Tail Multi-Label Learning in Data Mining
**arXiv**：[2602.15330v1](https://arxiv.org/abs/2602.15330) · [PDF](https://arxiv.org/pdf/2602.15330.pdf)  
**作者**：Jing Yang, Keze Wang  

**一句话要点**：提出好奇心驱动博弈论框架以解决长尾多标签分类中的标签不平衡问题

**关键词**：长尾多标签分类, 博弈论学习, 好奇心驱动, 标签不平衡, 数据挖掘, 自适应优化

## 3 点简述
- 核心问题：长尾分布导致少数头部标签主导，尾部标签学习困难，现有方法易破坏标签间依赖或需繁琐调参。
- 方法要点：将多标签分类建模为多玩家博弈，子预测器基于尾部标签稀有性和玩家间分歧获得好奇心奖励，自适应增强尾部学习。
- 实验或效果：在7个基准数据集上验证，包括超3万标签的极端多标签分类，CD-GTMLL在稀有标签性能上超越现有方法，提升达+1.6% P@3。

## 摘要（原文）

> The long-tail distribution, where a few head labels dominate while rare tail labels abound, poses a persistent challenge for large-scale Multi-Label Classification (MLC) in real-world data mining applications. Existing resampling and reweighting strategies often disrupt inter-label dependencies or require brittle hyperparameter tuning, especially as the label space expands to tens of thousands of labels. To address this issue, we propose Curiosity-Driven Game-Theoretic Multi-Label Learning (CD-GTMLL), a scalable cooperative framework that recasts long-tail MLC as a multi-player game - each sub-predictor ("player") specializes in a partition of the label space, collaborating to maximize global accuracy while pursuing intrinsic curiosity rewards based on tail label rarity and inter-player disagreement. This mechanism adaptively injects learning signals into under-represented tail labels without manual balancing or tuning. We further provide a theoretical analysis showing that our CD-GTMLL converges to a tail-aware equilibrium and formally links the optimization dynamics to improvements in the Rare-F1 metric. Extensive experiments across 7 benchmarks, including extreme multi-label classification datasets with 30,000+ labels, demonstrate that CD-GTMLL consistently surpasses state-of-the-art methods, with gains up to +1.6% P@3 on Wiki10-31K. Ablation studies further confirm the contributions of both game-theoretic cooperation and curiosity-driven exploration to robust tail performance. By integrating game theory with curiosity mechanisms, CD-GTMLL not only enhances model efficiency in resource-constrained environments but also paves the way for more adaptive learning in imbalanced data scenarios across industries like e-commerce and healthcare.

