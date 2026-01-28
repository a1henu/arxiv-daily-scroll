---
layout: default
title: QA-ReID: Quality-Aware Query-Adaptive Convolution Leveraging Fused Global and Structural Cues for Clothes-Changing ReID
---

# QA-ReID: Quality-Aware Query-Adaptive Convolution Leveraging Fused Global and Structural Cues for Clothes-Changing ReID
**arXiv**：[2601.19133v1](https://arxiv.org/abs/2601.19133) · [PDF](https://arxiv.org/pdf/2601.19133.pdf)  
**作者**：Yuxiang Wang, Kunming Jiang, Tianxiang Zhang, Ke Tian, Gaozhe Jiang  

**一句话要点**：提出QA-ReID方法，通过质量感知查询自适应卷积融合全局与结构线索，解决换衣场景下的行人重识别问题。

**关键词**：换衣行人重识别, 质量感知匹配, 多模态融合, 查询自适应卷积, 服装不变特征

## 3 点简述
- 核心问题：换衣行人重识别因服装变化导致外观显著差异，传统方法难以应对。
- 方法要点：结合RGB特征与解析表示，通过多模态注意力自适应融合全局外观与服装不变结构线索。
- 实验或效果：在PRCC、LTCC、VC-Clothes等基准上实现最优性能，显著提升跨服装场景的鲁棒性。

## 摘要（原文）

> Unlike conventional person re-identification (ReID), clothes-changing ReID (CC-ReID) presents severe challenges due to substantial appearance variations introduced by clothing changes. In this work, we propose the Quality-Aware Dual-Branch Matching (QA-ReID), which jointly leverages RGB-based features and parsing-based representations to model both global appearance and clothing-invariant structural cues. These heterogeneous features are adaptively fused through a multi-modal attention module. At the matching stage, we further design the Quality-Aware Query Adaptive Convolution (QAConv-QA), which incorporates pixel-level importance weighting and bidirectional consistency constraints to enhance robustness against clothing variations. Extensive experiments demonstrate that QA-ReID achieves state-of-the-art performance on multiple benchmarks, including PRCC, LTCC, and VC-Clothes, and significantly outperforms existing approaches under cross-clothing scenarios.

