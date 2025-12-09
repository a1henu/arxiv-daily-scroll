---
layout: default
title: Modality-Aware Bias Mitigation and Invariance Learning for Unsupervised Visible-Infrared Person Re-Identification
---

# Modality-Aware Bias Mitigation and Invariance Learning for Unsupervised Visible-Infrared Person Re-Identification
**arXiv**：[2512.07760v1](https://arxiv.org/abs/2512.07760) · [PDF](https://arxiv.org/pdf/2512.07760.pdf)  
**作者**：Menglin Wang, Xiaojin Gong, Jiachen Li, Genlin Ji  

**一句话要点**：提出模态感知偏差缓解与不变性学习方法，以解决无监督可见光-红外行人重识别中的跨模态关联挑战。

**关键词**：无监督行人重识别, 跨模态学习, 模态偏差缓解, 不变性表示学习, 全局聚类, 原型对齐

## 3 点简述
- 核心问题：无监督可见光-红外行人重识别中，模态差异导致跨模态关联不可靠，现有方法易传播局部聚类错误并忽略全局实例关系。
- 方法要点：设计模态感知Jaccard距离缓解模态偏差，通过全局聚类估计可靠关联；采用'分割-对比'策略获取模态特定全局原型，在全局关联指导下对齐以实现模态不变表示学习。
- 实验或效果：在基准VI-ReID数据集上取得最先进性能，显著优于现有方法，验证了有效性。

## 摘要（原文）

> Unsupervised visible-infrared person re-identification (USVI-ReID) aims to match individuals across visible and infrared cameras without relying on any annotation. Given the significant gap across visible and infrared modality, estimating reliable cross-modality association becomes a major challenge in USVI-ReID. Existing methods usually adopt optimal transport to associate the intra-modality clusters, which is prone to propagating the local cluster errors, and also overlooks global instance-level relations. By mining and attending to the visible-infrared modality bias, this paper focuses on addressing cross-modality learning from two aspects: bias-mitigated global association and modality-invariant representation learning. Motivated by the camera-aware distance rectification in single-modality re-ID, we propose modality-aware Jaccard distance to mitigate the distance bias caused by modality discrepancy, so that more reliable cross-modality associations can be estimated through global clustering. To further improve cross-modality representation learning, a `split-and-contrast' strategy is designed to obtain modality-specific global prototypes. By explicitly aligning these prototypes under global association guidance, modality-invariant yet ID-discriminative representation learning can be achieved. While conceptually simple, our method obtains state-of-the-art performance on benchmark VI-ReID datasets and outperforms existing methods by a significant margin, validating its effectiveness.

