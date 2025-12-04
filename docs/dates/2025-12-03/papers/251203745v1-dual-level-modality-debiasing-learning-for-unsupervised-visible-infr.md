---
layout: default
title: Dual-level Modality Debiasing Learning for Unsupervised Visible-Infrared Person Re-Identification
---

# Dual-level Modality Debiasing Learning for Unsupervised Visible-Infrared Person Re-Identification
**arXiv**：[2512.03745v1](https://arxiv.org/abs/2512.03745) · [PDF](https://arxiv.org/pdf/2512.03745.pdf)  
**作者**：Jiaze Li, Yan Lu, Bin Liu, Guojun Yin, Mang Ye  

**一句话要点**：提出双层级模态去偏学习框架以解决无监督可见光-红外行人重识别中的模态偏差问题

**关键词**：无监督学习, 可见光-红外行人重识别, 模态去偏, 因果建模, 特征对齐

## 3 点简述
- 核心问题：两阶段学习流程在无监督可见光-红外行人重识别中引入模态偏差，损害身份判别和泛化能力。
- 方法要点：在模型层级使用因果调整干预模块，在优化层级采用协作无偏训练策略，实现双层级去偏。
- 实验或效果：在基准数据集上验证了框架能实现模态不变特征学习和更泛化的模型。

## 摘要（原文）

> Two-stage learning pipeline has achieved promising results in unsupervised visible-infrared person re-identification (USL-VI-ReID). It first performs single-modality learning and then operates cross-modality learning to tackle the modality discrepancy. Although promising, this pipeline inevitably introduces modality bias: modality-specific cues learned in the single-modality training naturally propagate into the following cross-modality learning, impairing identity discrimination and generalization. To address this issue, we propose a Dual-level Modality Debiasing Learning (DMDL) framework that implements debiasing at both the model and optimization levels. At the model level, we propose a Causality-inspired Adjustment Intervention (CAI) module that replaces likelihood-based modeling with causal modeling, preventing modality-induced spurious patterns from being introduced, leading to a low-biased model. At the optimization level, a Collaborative Bias-free Training (CBT) strategy is introduced to interrupt the propagation of modality bias across data, labels, and features by integrating modality-specific augmentation, label refinement, and feature alignment. Extensive experiments on benchmark datasets demonstrate that DMDL could enable modality-invariant feature learning and a more generalized model.

