---
layout: default
title: FluoCLIP: Stain-Aware Focus Quality Assessment in Fluorescence Microscopy
---

# FluoCLIP: Stain-Aware Focus Quality Assessment in Fluorescence Microscopy
**arXiv**：[2602.23791v1](https://arxiv.org/abs/2602.23791) · [PDF](https://arxiv.org/pdf/2602.23791.pdf)  
**作者**：Hyejin Park, Jiwon Yoon, Sumin Park, Suree Kim, Sinae Jang, Eunsoo Lee, Dongmin Kang, Dongbo Min  

**一句话要点**：提出FluoCLIP框架以解决荧光显微镜中染色感知的聚焦质量评估问题

**关键词**：荧光显微镜, 聚焦质量评估, 染色感知建模, 视觉语言框架, 数据集构建, 泛化性能

## 3 点简述
- 核心问题：荧光染料的光学特性导致聚焦质量随染色变化，现有方法忽略此变异性。
- 方法要点：提出两阶段视觉语言框架FluoCLIP，利用CLIP对齐能力学习染色表示并优化染色特定排序提示。
- 实验或效果：构建FluoMix数据集，FluoCLIP在多样化荧光显微镜条件下实现强泛化性能。

## 摘要（原文）

> Accurate focus quality assessment (FQA) in fluorescence microscopy remains challenging, as the stain-dependent optical properties of fluorescent dyes cause abrupt and heterogeneous focus shifts. However, existing datasets and models overlook this variability, treating focus quality as a stain-agnostic problem. In this work, we formulate the task of stain-aware FQA, emphasizing that focus behavior in fluorescence microscopy must be modeled as a function of staining characteristics. Through quantitative analysis of existing datasets (FocusPath, BBBC006) and our newly curated FluoMix, we demonstrate that focus-rank relationships vary substantially across stains, underscoring the need for stain-aware modeling in fluorescence microscopy. To support this new formulation, we propose FluoMix, the first dataset for stain-aware FQA that encompasses multiple tissues, fluorescent stains, and focus variations. Building on this dataset, we propose FluoCLIP, a two-stage vision-language framework that leverages CLIP's alignment capability to interpret focus quality in the context of biological staining. In the stain-grounding phase, FluoCLIP learns general stain representations by aligning textual stain tokens with visual features, while in the stain-guided ranking phase, it optimizes stain-specific rank prompts for ordinal focus prediction. Together, our formulation, dataset, and framework establish the first foundation for stain-aware FQA, and FluoCLIP achieves strong generalization across diverse fluorescence microscopy conditions.

