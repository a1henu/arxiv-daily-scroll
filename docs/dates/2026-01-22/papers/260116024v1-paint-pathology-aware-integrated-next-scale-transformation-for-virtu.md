---
layout: default
title: PAINT: Pathology-Aware Integrated Next-Scale Transformation for Virtual Immunohistochemistry
---

# PAINT: Pathology-Aware Integrated Next-Scale Transformation for Virtual Immunohistochemistry
**arXiv**：[2601.16024v1](https://arxiv.org/abs/2601.16024) · [PDF](https://arxiv.org/pdf/2601.16024.pdf)  
**作者**：Rongze Ma, Mengkang Lu, Zhenyu Xiang, Yongsheng Pan, Yicheng Wu, Qingjie Zeng, Yong Xia  

**一句话要点**：提出PAINT框架，通过结构优先的自回归生成解决虚拟免疫组化中的语义不一致问题。

**关键词**：虚拟免疫组化, 自回归生成, 结构引导合成, 病理图像分析, 跨模态生成

## 3 点简述
- 核心问题：H&E图像形态提供模糊线索，现有方法因结构先验不足导致语义不一致。
- 方法要点：引入空间结构起始图，以全局结构布局为条件自回归生成分子细节。
- 实验或效果：在IHC4BC和MIST数据集上优于现有方法，验证结构引导自回归建模的潜力。

## 摘要（原文）

> Virtual immunohistochemistry (IHC) aims to computationally synthesize molecular staining patterns from routine Hematoxylin and Eosin (H\&E) images, offering a cost-effective and tissue-efficient alternative to traditional physical staining. However, this task is particularly challenging: H\&E morphology provides ambiguous cues about protein expression, and similar tissue structures may correspond to distinct molecular states. Most existing methods focus on direct appearance synthesis to implicitly achieve cross-modal generation, often resulting in semantic inconsistencies due to insufficient structural priors. In this paper, we propose Pathology-Aware Integrated Next-Scale Transformation (PAINT), a visual autoregressive framework that reformulates the synthesis process as a structure-first conditional generation task. Unlike direct image translation, PAINT enforces a causal order by resolving molecular details conditioned on a global structural layout. Central to this approach is the introduction of a Spatial Structural Start Map (3S-Map), which grounds the autoregressive initialization in observed morphology, ensuring deterministic, spatially aligned synthesis. Experiments on the IHC4BC and MIST datasets demonstrate that PAINT outperforms state-of-the-art methods in structural fidelity and clinical downstream tasks, validating the potential of structure-guided autoregressive modeling.

