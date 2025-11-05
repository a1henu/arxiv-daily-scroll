---
layout: default
title: Seeing Across Time and Views: Multi-Temporal Cross-View Learning for Robust Video Person Re-Identification
---

# Seeing Across Time and Views: Multi-Temporal Cross-View Learning for Robust Video Person Re-Identification
**arXiv**：[2511.02564v1](https://arxiv.org/abs/2511.02564) · [PDF](https://arxiv.org/pdf/2511.02564.pdf)  
**作者**：Md Rashidunnabi, Kailash A. Hambarde, Vasco Lopes, Joao C. Neves, Hugo Proenca  

**一句话要点**：提出MTF-CVReID框架以解决跨视角视频行人重识别中的视角偏移和时序不一致问题

**关键词**：视频行人重识别, 跨视角学习, 时序建模, 特征对齐, 参数高效框架, 对比学习

## 3 点简述
- 核心问题：跨视角视频行人重识别存在视角偏移、尺度差异和时序不一致的挑战
- 方法要点：基于ViT-B/16骨干网络，引入七个互补模块增强特征对齐和时序建模
- 实验或效果：在AG-VPReID基准上实现SOTA性能，保持实时效率并具有强泛化能力

## 摘要（原文）

> Video-based person re-identification (ReID) in cross-view domains (for
> example, aerial-ground surveillance) remains an open problem because of extreme
> viewpoint shifts, scale disparities, and temporal inconsistencies. To address
> these challenges, we propose MTF-CVReID, a parameter-efficient framework that
> introduces seven complementary modules over a ViT-B/16 backbone. Specifically,
> we include: (1) Cross-Stream Feature Normalization (CSFN) to correct camera and
> view biases; (2) Multi-Resolution Feature Harmonization (MRFH) for scale
> stabilization across altitudes; (3) Identity-Aware Memory Module (IAMM) to
> reinforce persistent identity traits; (4) Temporal Dynamics Modeling (TDM) for
> motion-aware short-term temporal encoding; (5) Inter-View Feature Alignment
> (IVFA) for perspective-invariant representation alignment; (6) Hierarchical
> Temporal Pattern Learning (HTPL) to capture multi-scale temporal regularities;
> and (7) Multi-View Identity Consistency Learning (MVICL) that enforces
> cross-view identity coherence using a contrastive learning paradigm. Despite
> adding only about 2 million parameters and 0.7 GFLOPs over the baseline,
> MTF-CVReID maintains real-time efficiency (189 FPS) and achieves
> state-of-the-art performance on the AG-VPReID benchmark across all altitude
> levels, with strong cross-dataset generalization to G2A-VReID and MARS
> datasets. These results show that carefully designed adapter-based modules can
> substantially enhance cross-view robustness and temporal consistency without
> compromising computational efficiency. The source code is available at
> https://github.com/MdRashidunnabi/MTF-CVReID

