---
layout: default
title: Atlas-Assisted Segment Anything Model for Fetal Brain MRI (FeTal-SAM)
---

# Atlas-Assisted Segment Anything Model for Fetal Brain MRI (FeTal-SAM)
**arXiv**：[2601.15759v1](https://arxiv.org/abs/2601.15759) · [PDF](https://arxiv.org/pdf/2601.15759.pdf)  
**作者**：Qi Zeng, Weide Liu, Bo Li, Ryne Didier, P. Ellen Grant, Davood Karimi  

**一句话要点**：提出FeTal-SAM，结合图谱提示与基础模型，实现胎儿脑MRI灵活分割

**关键词**：胎儿脑MRI分割, Segment Anything模型, 图谱提示, 多图谱配准, 灵活分割

## 3 点简述
- 传统方法需大量标注且标签固定，难以适应临床需求变化
- 通过多图谱配准生成密集提示，结合边界框提示，驱动SAM解码器进行逐结构分割
- 在dHCP和内部数据集上评估，对高对比结构性能可比基线，低对比结构精度略低

## 摘要（原文）

> This paper presents FeTal-SAM, a novel adaptation of the Segment Anything Model (SAM) tailored for fetal brain MRI segmentation. Traditional deep learning methods often require large annotated datasets for a fixed set of labels, making them inflexible when clinical or research needs change. By integrating atlas-based prompts and foundation-model principles, FeTal-SAM addresses two key limitations in fetal brain MRI segmentation: (1) the need to retrain models for varying label definitions, and (2) the lack of insight into whether segmentations are driven by genuine image contrast or by learned spatial priors. We leverage multi-atlas registration to generate spatially aligned label templates that serve as dense prompts, alongside a bounding-box prompt, for SAM's segmentation decoder. This strategy enables binary segmentation on a per-structure basis, which is subsequently fused to reconstruct the full 3D segmentation volumes. Evaluations on two datasets, the dHCP dataset and an in-house dataset demonstrate FeTal-SAM's robust performance across gestational ages. Notably, it achieves Dice scores comparable to state-of-the-art baselines which were trained for each dataset and label definition for well-contrasted structures like cortical plate and cerebellum, while maintaining the flexibility to segment any user-specified anatomy. Although slightly lower accuracy is observed for subtle, low-contrast structures (e.g., hippocampus, amygdala), our results highlight FeTal-SAM's potential to serve as a general-purpose segmentation model without exhaustive retraining. This method thus constitutes a promising step toward clinically adaptable fetal brain MRI analysis tools.

