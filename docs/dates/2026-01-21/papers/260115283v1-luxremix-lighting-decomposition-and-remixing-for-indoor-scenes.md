---
layout: default
title: LuxRemix: Lighting Decomposition and Remixing for Indoor Scenes
---

# LuxRemix: Lighting Decomposition and Remixing for Indoor Scenes
**arXiv**：[2601.15283v1](https://arxiv.org/abs/2601.15283) · [PDF](https://arxiv.org/pdf/2601.15283.pdf)  
**作者**：Ruofan Liang, Norman Müller, Ethan Weber, Duncan Zauss, Nandita Vijaykumar, Peter Kontschieder, Christian Richardt  

**一句话要点**：提出LuxRemix方法，基于单次多视角捕获实现室内场景的交互式光照编辑。

**关键词**：光照分解, 交互式编辑, 室内场景, 多视角协调, 3D高斯泼溅

## 3 点简述
- 核心问题：从单次多视角捕获中分解室内复杂光照，实现独立光源控制。
- 方法要点：利用生成式图像光照分解模型，结合多视角光照协调与可重光照3D高斯泼溅表示。
- 实验或效果：在合成和真实数据集上评估，展示高真实感光照分解与实时交互编辑效果。

## 摘要（原文）

> We present a novel approach for interactive light editing in indoor scenes from a single multi-view scene capture. Our method leverages a generative image-based light decomposition model that factorizes complex indoor scene illumination into its constituent light sources. This factorization enables independent manipulation of individual light sources, specifically allowing control over their state (on/off), chromaticity, and intensity. We further introduce multi-view lighting harmonization to ensure consistent propagation of the lighting decomposition across all scene views. This is integrated into a relightable 3D Gaussian splatting representation, providing real-time interactive control over the individual light sources. Our results demonstrate highly photorealistic lighting decomposition and relighting outcomes across diverse indoor scenes. We evaluate our method on both synthetic and real-world datasets and provide a quantitative and qualitative comparison to state-of-the-art techniques. For video results and interactive demos, see https://luxremix.github.io.

