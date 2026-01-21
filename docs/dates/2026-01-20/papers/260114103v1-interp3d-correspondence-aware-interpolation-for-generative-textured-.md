---
layout: default
title: Interp3D: Correspondence-aware Interpolation for Generative Textured 3D Morphing
---

# Interp3D: Correspondence-aware Interpolation for Generative Textured 3D Morphing
**arXiv**：[2601.14103v1](https://arxiv.org/abs/2601.14103) · [PDF](https://arxiv.org/pdf/2601.14103.pdf)  
**作者**：Xiaolu Liu, Yicong Li, Qiyuan He, Jiayin Zhu, Wei Ji, Angela Yao, Jianke Zhu  

**一句话要点**：提出Interp3D框架以解决纹理3D变形中的几何一致性与纹理对齐问题

**关键词**：纹理3D变形, 生成先验, 渐进对齐, 结构插值, 纹理融合, 无训练框架

## 3 点简述
- 核心问题：现有方法在纹理3D变形中常导致语义模糊、结构错位和纹理模糊
- 方法要点：利用生成先验和渐进对齐原则，通过条件空间插值、SLAT引导结构插值和纹理融合实现
- 实验或效果：构建Interp3DData数据集评估，在保真度、平滑性和合理性上优于先前方法

## 摘要（原文）

> Textured 3D morphing seeks to generate smooth and plausible transitions between two 3D assets, preserving both structural coherence and fine-grained appearance. This ability is crucial not only for advancing 3D generation research but also for practical applications in animation, editing, and digital content creation. Existing approaches either operate directly on geometry, limiting them to shape-only morphing while neglecting textures, or extend 2D interpolation strategies into 3D, which often causes semantic ambiguity, structural misalignment, and texture blurring. These challenges underscore the necessity to jointly preserve geometric consistency, texture alignment, and robustness throughout the transition process. To address this, we propose Interp3D, a novel training-free framework for textured 3D morphing. It harnesses generative priors and adopts a progressive alignment principle to ensure both geometric fidelity and texture coherence. Starting from semantically aligned interpolation in condition space, Interp3D enforces structural consistency via SLAT (Structured Latent)-guided structure interpolation, and finally transfers appearance details through fine-grained texture fusion. For comprehensive evaluations, we construct a dedicated dataset, Interp3DData, with graded difficulty levels and assess generation results from fidelity, transition smoothness, and plausibility. Both quantitative metrics and human studies demonstrate the significant advantages of our proposed approach over previous methods. Source code is available at https://github.com/xiaolul2/Interp3D.

