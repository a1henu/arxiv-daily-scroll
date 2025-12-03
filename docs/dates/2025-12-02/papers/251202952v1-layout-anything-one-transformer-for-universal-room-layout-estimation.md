---
layout: default
title: Layout Anything: One Transformer for Universal Room Layout Estimation
---

# Layout Anything: One Transformer for Universal Room Layout Estimation
**arXiv**：[2512.02952v1](https://arxiv.org/abs/2512.02952) · [PDF](https://arxiv.org/pdf/2512.02952.pdf)  
**作者**：Md Sohag Mia, Muhammad Abdullah Adnan  

**一句话要点**：提出Layout Anything框架，基于OneFormer架构实现室内布局估计，结合几何约束与高效推理

**关键词**：室内布局估计, Transformer架构, 几何约束学习, 高效推理, 增强现实应用

## 3 点简述
- 核心问题：室内布局估计需处理几何结构预测，传统方法依赖复杂后处理，影响效率与精度。
- 方法要点：采用OneFormer的通用分割架构，集成任务条件查询、对比学习、布局退化策略和可微几何损失。
- 实验或效果：在LSUN、Hedau和Matterport3D-Layout数据集上达到先进性能，推理速度114ms，适用于增强现实和大规模3D重建。

## 摘要（原文）

> We present Layout Anything, a transformer-based framework for indoor layout estimation that adapts the OneFormer's universal segmentation architecture to geometric structure prediction. Our approach integrates OneFormer's task-conditioned queries and contrastive learning with two key modules: (1) a layout degeneration strategy that augments training data while preserving Manhattan-world constraints through topology-aware transformations, and (2) differentiable geometric losses that directly enforce planar consistency and sharp boundary predictions during training. By unifying these components in an end-to-end framework, the model eliminates complex post-processing pipelines while achieving high-speed inference at 114ms. Extensive experiments demonstrate state-of-the-art performance across standard benchmarks, with pixel error (PE) of 5.43% and corner error (CE) of 4.02% on the LSUN, PE of 7.04% (CE 5.17%) on the Hedau and PE of 4.03% (CE 3.15%) on the Matterport3D-Layout datasets. The framework's combination of geometric awareness and computational efficiency makes it particularly suitable for augmented reality applications and large-scale 3D scene reconstruction tasks.

