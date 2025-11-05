---
layout: default
title: OmniField: Conditioned Neural Fields for Robust Multimodal Spatiotemporal Learning
---

# OmniField: Conditioned Neural Fields for Robust Multimodal Spatiotemporal Learning
**arXiv**：[2511.02205v1](https://arxiv.org/abs/2511.02205) · [PDF](https://arxiv.org/pdf/2511.02205.pdf)  
**作者**：Kevin Valencia, Thilina Balasooriya, Xihaier Luo, Shinjae Yoo, David Keetae Park  

**一句话要点**：提出OmniField以解决多模态时空数据稀疏、噪声和模态缺失问题

**关键词**：神经场, 多模态学习, 时空建模, 跨模态融合, 鲁棒性学习

## 3 点简述
- 核心问题：多模态时空数据稀疏、不规则、噪声大，且模态在时空上变化
- 方法要点：使用条件神经场和跨模态融合块，实现连续学习与对齐
- 实验或效果：在噪声下性能稳定，优于多个基线模型

## 摘要（原文）

> Multimodal spatiotemporal learning on real-world experimental data is
> constrained by two challenges: within-modality measurements are sparse,
> irregular, and noisy (QA/QC artifacts) but cross-modally correlated; the set of
> available modalities varies across space and time, shrinking the usable record
> unless models can adapt to arbitrary subsets at train and test time. We propose
> OmniField, a continuity-aware framework that learns a continuous neural field
> conditioned on available modalities and iteratively fuses cross-modal context.
> A multimodal crosstalk block architecture paired with iterative cross-modal
> refinement aligns signals prior to the decoder, enabling unified
> reconstruction, interpolation, forecasting, and cross-modal prediction without
> gridding or surrogate preprocessing. Extensive evaluations show that OmniField
> consistently outperforms eight strong multimodal spatiotemporal baselines.
> Under heavy simulated sensor noise, performance remains close to clean-input
> levels, highlighting robustness to corrupted measurements.

