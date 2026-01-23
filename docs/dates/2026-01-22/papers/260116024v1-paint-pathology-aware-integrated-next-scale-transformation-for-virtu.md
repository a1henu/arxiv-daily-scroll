---
layout: default
title: PAINT: Pathology-Aware Integrated Next-Scale Transformation for Virtual Immunohistochemistry
---

# PAINT: Pathology-Aware Integrated Next-Scale Transformation for Virtual Immunohistochemistry
**arXiv**：[2601.16024v1](https://arxiv.org/abs/2601.16024) · [PDF](https://arxiv.org/pdf/2601.16024.pdf)  
**作者**：Rongze Ma, Mengkang Lu, Zhenyu Xiang, Yongsheng Pan, Yicheng Wu, Qingjie Zeng, Yong Xia  

**一句话要点**：提出PAINT框架，通过结构优先的自回归生成解决虚拟免疫组化中的语义不一致问题。

**关键词**：虚拟免疫组化, 自回归生成, 结构先验, 医学图像合成, 条件生成

## 3 点简述
- 核心问题：H&E图像到IHC的合成因形态模糊和结构相似性导致语义不一致。
- 方法要点：引入3S-Map作为结构先验，以自回归方式条件生成分子细节。
- 实验或效果：在IHC4BC和MIST数据集上，PAINT在结构保真度和临床任务中优于现有方法。

## 摘要（原文）

> Virtual immunohistochemistry (IHC) aims to computationally synthesize molecular staining patterns from routine Hematoxylin and Eosin (H\&E) images, offering a cost-effective and tissue-efficient alternative to traditional physical staining. However, this task is particularly challenging: H\&E morphology provides ambiguous cues about protein expression, and similar tissue structures may correspond to distinct molecular states. Most existing methods focus on direct appearance synthesis to implicitly achieve cross-modal generation, often resulting in semantic inconsistencies due to insufficient structural priors. In this paper, we propose Pathology-Aware Integrated Next-Scale Transformation (PAINT), a visual autoregressive framework that reformulates the synthesis process as a structure-first conditional generation task. Unlike direct image translation, PAINT enforces a causal order by resolving molecular details conditioned on a global structural layout. Central to this approach is the introduction of a Spatial Structural Start Map (3S-Map), which grounds the autoregressive initialization in observed morphology, ensuring deterministic, spatially aligned synthesis. Experiments on the IHC4BC and MIST datasets demonstrate that PAINT outperforms state-of-the-art methods in structural fidelity and clinical downstream tasks, validating the potential of structure-guided autoregressive modeling.

