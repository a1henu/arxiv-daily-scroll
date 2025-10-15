---
layout: default
title: On the Use of Hierarchical Vision Foundation Models for Low-Cost Human Mesh Recovery and Pose Estimation
---

# On the Use of Hierarchical Vision Foundation Models for Low-Cost Human Mesh Recovery and Pose Estimation
**arXiv**：[2510.12660v1](https://arxiv.org/abs/2510.12660) · [PDF](https://arxiv.org/pdf/2510.12660.pdf)  
**作者**：Shuhei Tarashima, Yushan Wang, Norio Tagawa  

**一句话要点**：提出利用分层视觉基础模型早期阶段构建高效人体网格恢复与姿态估计模型

**关键词**：人体网格恢复, 人体姿态估计, 分层视觉基础模型, 轻量化模型, 计算效率优化

## 3 点简述
- 核心问题：现有HMR方法依赖大型非分层视觉变换器，计算成本高，需轻量化方案。
- 方法要点：采用Swin Transformer等分层VFM的前两或三阶段作为编码器，保持特征图高分辨率。
- 实验效果：27个模型评估显示，截断模型在精度与效率间优于现有轻量方法。

## 摘要（原文）

> In this work, we aim to develop simple and efficient models for human mesh
> recovery (HMR) and its predecessor task, human pose estimation (HPE).
> State-of-the-art HMR methods, such as HMR2.0 and its successors, rely on large,
> non-hierarchical vision transformers as encoders, which are inherited from the
> corresponding HPE models like ViTPose. To establish baselines across varying
> computational budgets, we first construct three lightweight HMR2.0 variants by
> adapting the corresponding ViTPose models. In addition, we propose leveraging
> the early stages of hierarchical vision foundation models (VFMs), including
> Swin Transformer, GroupMixFormer, and VMamba, as encoders. This design is
> motivated by the observation that intermediate stages of hierarchical VFMs
> produce feature maps with resolutions comparable to or higher than those of
> non-hierarchical counterparts. We conduct a comprehensive evaluation of 27
> hierarchical-VFM-based HMR and HPE models, demonstrating that using only the
> first two or three stages achieves performance on par with full-stage models.
> Moreover, we show that the resulting truncated models exhibit better trade-offs
> between accuracy and computational efficiency compared to existing lightweight
> alternatives.

