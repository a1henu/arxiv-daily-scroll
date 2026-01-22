---
layout: default
title: FlowSSC: Universal Generative Monocular Semantic Scene Completion via One-Step Latent Diffusion
---

# FlowSSC: Universal Generative Monocular Semantic Scene Completion via One-Step Latent Diffusion
**arXiv**：[2601.15250v1](https://arxiv.org/abs/2601.15250) · [PDF](https://arxiv.org/pdf/2601.15250.pdf)  
**作者**：Zichen Xi, Hao-Xiang Chen, Nan Xue, Hongyu Yan, Qi-Yuan Feng, Levent Burak Kara, Joaquim Jorge, Qun-Ce Xu  

**一句话要点**：提出FlowSSC，通过一步潜在扩散实现单目语义场景补全的通用生成框架。

**关键词**：语义场景补全, 单目视觉, 生成模型, 潜在扩散, 实时推理, 三平面表示

## 3 点简述
- 核心问题：单目RGB图像语义场景补全因遮挡区域推断模糊而具挑战性，现有前馈方法难以生成合理细节。
- 方法要点：采用条件生成框架，结合捷径流匹配在紧凑三平面潜在空间中实现一步高保真生成，支持实时推理。
- 实验或效果：在SemanticKITTI上达到最先进性能，显著超越基线，可提升现有方法效果。

## 摘要（原文）

> Semantic Scene Completion (SSC) from monocular RGB images is a fundamental yet challenging task due to the inherent ambiguity of inferring occluded 3D geometry from a single view. While feed-forward methods have made progress, they often struggle to generate plausible details in occluded regions and preserve the fundamental spatial relationships of objects. Such accurate generative reasoning capability for the entire 3D space is critical in real-world applications. In this paper, we present FlowSSC, the first generative framework applied directly to monocular semantic scene completion. FlowSSC treats the SSC task as a conditional generation problem and can seamlessly integrate with existing feed-forward SSC methods to significantly boost their performance. To achieve real-time inference without compromising quality, we introduce Shortcut Flow-matching that operates in a compact triplane latent space. Unlike standard diffusion models that require hundreds of steps, our method utilizes a shortcut mechanism to achieve high-fidelity generation in a single step, enabling practical deployment in autonomous systems. Extensive experiments on SemanticKITTI demonstrate that FlowSSC achieves state-of-the-art performance, significantly outperforming existing baselines.

