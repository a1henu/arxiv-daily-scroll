---
layout: default
title: InsertAnywhere: Bridging 4D Scene Geometry and Diffusion Models for Realistic Video Object Insertion
---

# InsertAnywhere: Bridging 4D Scene Geometry and Diffusion Models for Realistic Video Object Insertion
**arXiv**：[2512.17504v1](https://arxiv.org/abs/2512.17504) · [PDF](https://arxiv.org/pdf/2512.17504.pdf)  
**作者**：Hoiyeong Jin, Hyojin Jang, Jeongho Kim, Junha Hyung, Kinam Kim, Dongjin Kim, Huijin Choi, Hyeonji Kim, Jaegul Choo  

**一句话要点**：提出InsertAnywhere框架，通过4D场景几何与扩散模型实现真实视频对象插入

**关键词**：视频对象插入, 4D场景几何, 扩散模型, 遮挡一致性, 光照合成, 合成数据集

## 3 点简述
- 核心问题：现有视频对象插入方法在4D场景理解和遮挡光照处理上不足，导致不真实
- 方法要点：结合4D感知掩码生成和扩散模型，实现几何一致的对象放置与外观合成
- 实验或效果：在ROSE++数据集上验证，优于现有研究及商业模型，提升视觉一致性

## 摘要（原文）

> Recent advances in diffusion-based video generation have opened new possibilities for controllable video editing, yet realistic video object insertion (VOI) remains challenging due to limited 4D scene understanding and inadequate handling of occlusion and lighting effects. We present InsertAnywhere, a new VOI framework that achieves geometrically consistent object placement and appearance-faithful video synthesis. Our method begins with a 4D aware mask generation module that reconstructs the scene geometry and propagates user specified object placement across frames while maintaining temporal coherence and occlusion consistency. Building upon this spatial foundation, we extend a diffusion based video generation model to jointly synthesize the inserted object and its surrounding local variations such as illumination and shading. To enable supervised training, we introduce ROSE++, an illumination aware synthetic dataset constructed by transforming the ROSE object removal dataset into triplets of object removed video, object present video, and a VLM generated reference image. Through extensive experiments, we demonstrate that our framework produces geometrically plausible and visually coherent object insertions across diverse real world scenarios, significantly outperforming existing research and commercial models.

