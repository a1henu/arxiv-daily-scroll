---
layout: default
title: HeadLighter: Disentangling Illumination in Generative 3D Gaussian Heads via Lightstage Captures
---

# HeadLighter: Disentangling Illumination in Generative 3D Gaussian Heads via Lightstage Captures
**arXiv**：[2601.02103v1](https://arxiv.org/abs/2601.02103) · [PDF](https://arxiv.org/pdf/2601.02103.pdf)  
**作者**：Yating Wang, Yuan Sun, Xuan Wang, Ran Yi, Boyao Zhou, Yipengjing Sun, Hongyu Liu, Yinuo Wang, Lizhuang Ma  

**一句话要点**：提出HeadLighter框架，通过光舞台数据监督解耦生成式3D高斯人头中的光照与外观

**关键词**：3D高斯人头生成, 光照解耦, 光舞台数据, 渐进解耦训练, 实时渲染, 可控重光照

## 3 点简述
- 核心问题：现有3D高斯人头生成模型光照与外观深度纠缠，难以可控重光照
- 方法要点：采用双分支架构和渐进解耦训练，基于光舞台多视图图像监督学习物理可分解的渲染
- 实验或效果：保持高质量实时渲染，支持显式光照和视角编辑，并公开代码与数据集

## 摘要（原文）

> Recent 3D-aware head generative models based on 3D Gaussian Splatting achieve real-time, photorealistic and view-consistent head synthesis. However, a fundamental limitation persists: the deep entanglement of illumination and intrinsic appearance prevents controllable relighting. Existing disentanglement methods rely on strong assumptions to enable weakly supervised learning, which restricts their capacity for complex illumination. To address this challenge, we introduce HeadLighter, a novel supervised framework that learns a physically plausible decomposition of appearance and illumination in head generative models. Specifically, we design a dual-branch architecture that separately models lighting-invariant head attributes and physically grounded rendering components. A progressive disentanglement training is employed to gradually inject head appearance priors into the generative architecture, supervised by multi-view images captured under controlled light conditions with a light stage setup. We further introduce a distillation strategy to generate high-quality normals for realistic rendering. Experiments demonstrate that our method preserves high-quality generation and real-time rendering, while simultaneously supporting explicit lighting and viewpoint editing. We will publicly release our code and dataset.

