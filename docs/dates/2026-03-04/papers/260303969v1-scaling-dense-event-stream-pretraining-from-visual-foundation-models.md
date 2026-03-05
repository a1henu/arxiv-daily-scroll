---
layout: default
title: Scaling Dense Event-Stream Pretraining from Visual Foundation Models
---

# Scaling Dense Event-Stream Pretraining from Visual Foundation Models
**arXiv**：[2603.03969v1](https://arxiv.org/abs/2603.03969) · [PDF](https://arxiv.org/pdf/2603.03969.pdf)  
**作者**：Zhiwen Chen, Junhui Hou, Zhiyu Zhu, Jinjian Wu, Guangming Shi  

**一句话要点**：提出基于视觉基础模型的结构感知蒸馏方法，以解决事件流表示学习中的语义崩溃问题。

**关键词**：事件流表示学习, 视觉基础模型, 结构感知蒸馏, 自监督预训练, 跨模态对齐, 密集事件表示

## 3 点简述
- 核心问题：事件流表示学习受限于标注成本，且图像与事件域在稀疏性和粒度上不匹配，导致语义崩溃。
- 方法要点：利用大规模同步图像-事件数据集，通过结构感知蒸馏损失，对齐视觉基础模型提供的语义结构，优化密集事件表示。
- 实验或效果：在多个下游基准测试中显著超越传统方法和现有预训练技术，提升泛化性、数据效率和可迁移性。

## 摘要（原文）

> Learning versatile, fine-grained representations from irregular event streams is pivotal yet nontrivial, primarily due to the heavy annotation that hinders scalability in dataset size, semantic richness, and application scope. To mitigate this dilemma, we launch a novel self-supervised pretraining method that distills visual foundation models (VFMs) to push the boundaries of event representation at scale. Specifically, we curate an extensive synchronized image-event collection to amplify cross-modal alignment. Nevertheless, due to inherent mismatches in sparsity and granularity between image-event domains, existing distillation paradigms are prone to semantic collapse in event representations, particularly at high resolutions. To bridge this gap, we propose to extend the alignment objective to semantic structures provided off-the-shelf by VFMs, indicating a broader receptive field and stronger supervision. The key ingredient of our method is a structure-aware distillation loss that grounds higher-quality image-event correspondences for alignment, optimizing dense event representations. Extensive experiments demonstrate that our approach takes a great leap in downstream benchmarks, significantly surpassing traditional methods and existing pretraining techniques. This breakthrough manifests in enhanced generalization, superior data efficiency and elevated transferability.

