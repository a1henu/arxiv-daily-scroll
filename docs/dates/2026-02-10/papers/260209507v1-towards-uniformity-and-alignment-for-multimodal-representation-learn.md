---
layout: default
title: Towards Uniformity and Alignment for Multimodal Representation Learning
---

# Towards Uniformity and Alignment for Multimodal Representation Learning
**arXiv**：[2602.09507v1](https://arxiv.org/abs/2602.09507) · [PDF](https://arxiv.org/pdf/2602.09507.pdf)  
**作者**：Wenzhe Yin, Pan Zhou, Zehao Xiao, Jie Liu, Shujian Yu, Jan-Jakob Sonke, Efstratios Gavves  

**一句话要点**：提出解耦对齐与均匀性的方法以解决多模态表示学习中的分布冲突问题

**关键词**：多模态表示学习, 对齐-均匀性冲突, 分布差距, 检索任务, 生成任务, Hölder散度

## 3 点简述
- 核心问题：基于InfoNCE的目标在多模态学习中引发对齐-均匀性冲突和内部对齐冲突，导致模态间分布差距
- 方法要点：通过解耦对齐和均匀性，提供无冲突的多模态学习方案，支持判别和生成任务，无需任务特定模块
- 实验或效果：在检索和UnCLIP风格生成任务上实验显示一致性能提升，理论保证减少模态间分布差距

## 摘要（原文）

> Multimodal representation learning aims to construct a shared embedding space in which heterogeneous modalities are semantically aligned. Despite strong empirical results, InfoNCE-based objectives introduce inherent conflicts that yield distribution gaps across modalities. In this work, we identify two conflicts in the multimodal regime, both exacerbated as the number of modalities increases: (i) an alignment-uniformity conflict, whereby the repulsion of uniformity undermines pairwise alignment, and (ii) an intra-alignment conflict, where aligning multiple modalities induces competing alignment directions. To address these issues, we propose a principled decoupling of alignment and uniformity for multimodal representations, providing a conflict-free recipe for multimodal learning that simultaneously supports discriminative and generative use cases without task-specific modules. We then provide a theoretical guarantee that our method acts as an efficient proxy for a global Hölder divergence over multiple modality distributions, and thus reduces the distribution gap among modalities. Extensive experiments on retrieval and UnCLIP-style generation demonstrate consistent gains.

