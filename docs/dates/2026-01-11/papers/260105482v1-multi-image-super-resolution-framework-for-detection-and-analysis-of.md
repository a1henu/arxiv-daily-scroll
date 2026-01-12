---
layout: default
title: Multi-Image Super Resolution Framework for Detection and Analysis of Plant Roots
---

# Multi-Image Super Resolution Framework for Detection and Analysis of Plant Roots
**arXiv**：[2601.05482v1](https://arxiv.org/abs/2601.05482) · [PDF](https://arxiv.org/pdf/2601.05482.pdf)  
**作者**：Shubham Agarwal, Ofek Nourian, Michael Sidorov, Sharon Chemweno, Ofer Hadar, Naftali Lazarovitch, Jhonathan E. Ephrath  

**一句话要点**：提出多图像超分辨率框架以增强地下植物根系检测与分析

**关键词**：植物根系成像, 多图像超分辨率, 地下视觉, 深度学习, 合成数据集, 表型分析

## 3 点简述
- 核心问题：地下植物根系成像受遮挡、低对比度等环境因素影响，传统视觉方法效果有限。
- 方法要点：开发基于深度学习的多图像超分辨率框架，利用多视图空间冗余重建高分辨率图像。
- 实验或效果：在合成数据集上评估，优于现有超分辨率基线，提升图像质量，支持根系表型分析。

## 摘要（原文）

> Understanding plant root systems is critical for advancing research in soil-plant interactions, nutrient uptake, and overall plant health. However, accurate imaging of roots in subterranean environments remains a persistent challenge due to adverse conditions such as occlusion, varying soil moisture, and inherently low contrast, which limit the effectiveness of conventional vision-based approaches. In this work, we propose a novel underground imaging system that captures multiple overlapping views of plant roots and integrates a deep learning-based Multi-Image Super Resolution (MISR) framework designed to enhance root visibility and detail. To train and evaluate our approach, we construct a synthetic dataset that simulates realistic underground imaging scenarios, incorporating key environmental factors that affect image quality. Our proposed MISR algorithm leverages spatial redundancy across views to reconstruct high-resolution images with improved structural fidelity and visual clarity. Quantitative evaluations show that our approach outperforms state-of-the-art super resolution baselines, achieving a 2.3 percent reduction in BRISQUE, indicating improved image quality with the same CLIP-IQA score, thereby enabling enhanced phenotypic analysis of root systems. This, in turn, facilitates accurate estimation of critical root traits, including root hair count and root hair density. The proposed framework presents a promising direction for robust automatic underground plant root imaging and trait quantification for agricultural and ecological research.

