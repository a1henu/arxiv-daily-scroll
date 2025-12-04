---
layout: default
title: Motion4D: Learning 3D-Consistent Motion and Semantics for 4D Scene Understanding
---

# Motion4D: Learning 3D-Consistent Motion and Semantics for 4D Scene Understanding
**arXiv**：[2512.03601v1](https://arxiv.org/abs/2512.03601) · [PDF](https://arxiv.org/pdf/2512.03601.pdf)  
**作者**：Haoran Zhou, Gim Hee Lee  

**一句话要点**：提出Motion4D框架，通过4D高斯溅射整合2D先验，解决动态场景理解中的3D不一致问题。

**关键词**：4D场景理解, 高斯溅射, 运动估计, 语义分割, 单目视频分析, 迭代优化

## 3 点简述
- 核心问题：2D基础模型在单目视频分析中缺乏3D一致性，导致空间错位和时间闪烁。
- 方法要点：采用两阶段迭代优化，结合3D置信度图和自适应重采样，提升运动和语义一致性。
- 实验或效果：在点跟踪、视频对象分割和新视图合成等任务中优于现有方法。

## 摘要（原文）

> Recent advancements in foundation models for 2D vision have substantially improved the analysis of dynamic scenes from monocular videos. However, despite their strong generalization capabilities, these models often lack 3D consistency, a fundamental requirement for understanding scene geometry and motion, thereby causing severe spatial misalignment and temporal flickering in complex 3D environments. In this paper, we present Motion4D, a novel framework that addresses these challenges by integrating 2D priors from foundation models into a unified 4D Gaussian Splatting representation. Our method features a two-part iterative optimization framework: 1) Sequential optimization, which updates motion and semantic fields in consecutive stages to maintain local consistency, and 2) Global optimization, which jointly refines all attributes for long-term coherence. To enhance motion accuracy, we introduce a 3D confidence map that dynamically adjusts the motion priors, and an adaptive resampling process that inserts new Gaussians into under-represented regions based on per-pixel RGB and semantic errors. Furthermore, we enhance semantic coherence through an iterative refinement process that resolves semantic inconsistencies by alternately optimizing the semantic fields and updating prompts of SAM2. Extensive evaluations demonstrate that our Motion4D significantly outperforms both 2D foundation models and existing 3D-based approaches across diverse scene understanding tasks, including point-based tracking, video object segmentation, and novel view synthesis. Our code is available at https://hrzhou2.github.io/motion4d-web/.

