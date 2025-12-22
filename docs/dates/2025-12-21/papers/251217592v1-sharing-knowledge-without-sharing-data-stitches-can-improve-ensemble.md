---
layout: default
title: Sharing Knowledge without Sharing Data: Stitches can improve ensembles of disjointly trained models
---

# Sharing Knowledge without Sharing Data: Stitches can improve ensembles of disjointly trained models
**arXiv**：[2512.17592v1](https://arxiv.org/abs/2512.17592) · [PDF](https://arxiv.org/pdf/2512.17592.pdf)  
**作者**：Arthur Guijt, Dirk Thierens, Ellen Kerkhof, Jan Wiersma, Tanja Alderliesten, Peter A. N. Bosman  

**一句话要点**：提出缝合层方法以在数据不共享场景下异步集成独立训练模型

**关键词**：异步协作, 模型集成, 缝合层, 数据隐私, 多目标优化, 深度学习

## 3 点简述
- 核心问题：数据分散且无法共享时，异步协作模型性能受限，传统联邦学习需同步训练
- 方法要点：通过缝合层组合独立训练模型的中间表示，提升泛化能力并保持各方数据性能
- 实验或效果：缝合方法在各方数据集上恢复竞争性能，同时改善泛化，优于简单集成

## 摘要（原文）

> Deep learning has been shown to be very capable at performing many real-world tasks. However, this performance is often dependent on the presence of large and varied datasets. In some settings, like in the medical domain, data is often fragmented across parties, and cannot be readily shared. While federated learning addresses this situation, it is a solution that requires synchronicity of parties training a single model together, exchanging information about model weights. We investigate how asynchronous collaboration, where only already trained models are shared (e.g. as part of a publication), affects performance, and propose to use stitching as a method for combining models.
>   Through taking a multi-objective perspective, where performance on each parties' data is viewed independently, we find that training solely on a single parties' data results in similar performance when merging with another parties' data, when considering performance on that single parties' data, while performance on other parties' data is notably worse. Moreover, while an ensemble of such individually trained networks generalizes better, performance on each parties' own dataset suffers. We find that combining intermediate representations in individually trained models with a well placed pair of stitching layers allows this performance to recover to a competitive degree while maintaining improved generalization, showing that asynchronous collaboration can yield competitive results.

