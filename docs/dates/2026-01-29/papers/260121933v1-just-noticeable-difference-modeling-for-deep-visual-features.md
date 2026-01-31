---
layout: default
title: Just Noticeable Difference Modeling for Deep Visual Features
---

# Just Noticeable Difference Modeling for Deep Visual Features
**arXiv**：[2601.21933v1](https://arxiv.org/abs/2601.21933) · [PDF](https://arxiv.org/pdf/2601.21933.pdf)  
**作者**：Rui Zhao, Wenrui Li, Lin Zhu, Yajing Zheng, Weisi Lin  

**一句话要点**：提出FeatJND模型以预测深度视觉特征的最大可容忍扰动，保持下游任务性能。

**关键词**：深度视觉特征, 可察觉差异建模, 特征质量控制, 任务对齐扰动, 动态量化

## 3 点简述
- 核心问题：深度视觉特征在机器感知中缺乏任务对齐的质量控制方法。
- 方法要点：扩展JND到特征空间，预测每个特征的最大可容忍扰动图。
- 实验或效果：在分类、检测和分割任务中验证，FeatJND扰动比高斯扰动更优，并应用于动态量化。

## 摘要（原文）

> Deep visual features are increasingly used as the interface in vision systems, motivating the need to describe feature characteristics and control feature quality for machine perception. Just noticeable difference (JND) characterizes the maximum imperceptible distortion for images under human or machine vision. Extending it to deep visual features naturally meets the above demand by providing a task-aligned tolerance boundary in feature space, offering a practical reference for controlling feature quality under constrained resources. We propose FeatJND, a task-aligned JND formulation that predicts the maximum tolerable per-feature perturbation map while preserving downstream task performance. We propose a FeatJND estimator at standardized split points and validate it across image classification, detection, and instance segmentation. Under matched distortion strength, FeatJND-based distortions consistently preserve higher task performance than unstructured Gaussian perturbations, and attribution visualizations suggest FeatJND can suppress non-critical feature regions. As an application, we further apply FeatJND to token-wise dynamic quantization and show that FeatJND-guided step-size allocation yields clear gains over random step-size permutation and global uniform step size under the same noise budget. Our code will be released after publication.

