---
layout: default
title: DPL: Spatial-Conditioned Diffusion Prototype Enhancement for One-Shot Medical Segmentation
---

# DPL: Spatial-Conditioned Diffusion Prototype Enhancement for One-Shot Medical Segmentation
**arXiv**：[2510.12159v1](https://arxiv.org/abs/2510.12159) · [PDF](https://arxiv.org/pdf/2510.12159.pdf)  
**作者**：Ziyuan Gao, Philippe Morel  

**一句话要点**：提出DPL框架以解决少样本医学图像分割中的原型表示脆弱性问题

**关键词**：少样本医学分割, 扩散模型, 原型学习, 空间条件机制, 保守融合策略

## 3 点简述
- 核心问题：少样本医学分割中，传统原型方法因数据有限和患者解剖变异导致表示脆弱。
- 方法要点：使用扩散模型将原型建模为概率分布，生成多样且语义一致的变体。
- 实验或效果：在腹部MRI和CT数据集上实现SOTA性能，显著提升分割精度。

## 摘要（原文）

> One-shot medical image segmentation faces fundamental challenges in prototype
> representation due to limited annotated data and significant anatomical
> variability across patients. Traditional prototype-based methods rely on
> deterministic averaging of support features, creating brittle representations
> that fail to capture intra-class diversity essential for robust generalization.
> This work introduces Diffusion Prototype Learning (DPL), a novel framework that
> reformulates prototype construction through diffusion-based feature space
> exploration. DPL models one-shot prototypes as learnable probability
> distributions, enabling controlled generation of diverse yet semantically
> coherent prototype variants from minimal labeled data. The framework operates
> through three core innovations: (1) a diffusion-based prototype enhancement
> module that transforms single support prototypes into diverse variant sets via
> forward-reverse diffusion processes, (2) a spatial-aware conditioning mechanism
> that leverages geometric properties derived from prototype feature statistics,
> and (3) a conservative fusion strategy that preserves prototype fidelity while
> maximizing representational diversity. DPL ensures training-inference
> consistency by using the same diffusion enhancement and fusion pipeline in both
> phases. This process generates enhanced prototypes that serve as the final
> representations for similarity calculations, while the diffusion process itself
> acts as a regularizer. Extensive experiments on abdominal MRI and CT datasets
> demonstrate significant improvements respectively, establishing new
> state-of-the-art performance in one-shot medical image segmentation.

