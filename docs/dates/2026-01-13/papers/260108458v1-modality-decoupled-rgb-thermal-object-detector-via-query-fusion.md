---
layout: default
title: Modality-Decoupled RGB-Thermal Object Detector via Query Fusion
---

# Modality-Decoupled RGB-Thermal Object Detector via Query Fusion
**arXiv**：[2601.08458v1](https://arxiv.org/abs/2601.08458) · [PDF](https://arxiv.org/pdf/2601.08458.pdf)  
**作者**：Chao Tian, Zikun Zhou, Chao Yang, Guoqing Zhu, Fu'an Zhong, Zhenyu He  

**一句话要点**：提出模态解耦RGB-热红外检测框架MDQF，通过查询融合平衡模态互补与分离，提升极端条件下的检测鲁棒性。

**关键词**：RGB-热红外检测, 模态解耦, 查询融合, DETR检测器, 非配对数据训练, 极端条件鲁棒性

## 3 点简述
- 核心问题：RGB-热红外检测在极端条件下，单一模态质量差会干扰检测，需平衡模态互补与分离。
- 方法要点：采用DETR-like检测器作为独立分支，通过查询选择与适应实现跨分支查询融合，排除退化模态影响。
- 实验或效果：在RGB-T检测任务中优于现有方法，支持非配对数据训练，增强模态独立性。

## 摘要（原文）

> The advantage of RGB-Thermal (RGB-T) detection lies in its ability to perform modality fusion and integrate cross-modality complementary information, enabling robust detection under diverse illumination and weather conditions. However, under extreme conditions where one modality exhibits poor quality and disturbs detection, modality separation is necessary to mitigate the impact of noise. To address this problem, we propose a Modality-Decoupled RGB-T detection framework with Query Fusion (MDQF) to balance modality complementation and separation. In this framework, DETR-like detectors are employed as separate branches for the RGB and TIR images, with query fusion interspersed between the two branches in each refinement stage. Herein, query fusion is performed by feeding the high-quality queries from one branch to the other one after query selection and adaptation. This design effectively excludes the degraded modality and corrects the predictions using high-quality queries. Moreover, the decoupled framework allows us to optimize each individual branch with unpaired RGB or TIR images, eliminating the need for paired RGB-T data. Extensive experiments demonstrate that our approach delivers superior performance to existing RGB-T detectors and achieves better modality independence.

