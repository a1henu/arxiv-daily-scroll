---
layout: default
title: TEXTRIX: Latent Attribute Grid for Native Texture Generation and Beyond
---

# TEXTRIX: Latent Attribute Grid for Native Texture Generation and Beyond
**arXiv**：[2512.02993v1](https://arxiv.org/abs/2512.02993) · [PDF](https://arxiv.org/pdf/2512.02993.pdf)  
**作者**：Yifei Zeng, Yajie Bao, Jiachen Qian, Shuang Wu, Youtian Lin, Hao Zhu, Buyu Li, Feihu Zhang, Xun Cao, Yao Yao  

**一句话要点**：提出TEXTRIX框架，通过潜在属性网格和稀疏注意力扩散Transformer，实现高保真原生3D纹理生成与精确分割。

**关键词**：3D纹理生成, 潜在属性网格, 扩散Transformer, 稀疏注意力, 3D分割, 原生表示

## 3 点简述
- 核心问题：现有3D纹理生成方法依赖多视图融合，易导致视图不一致和表面覆盖不全，限制保真度和完整性。
- 方法要点：构建潜在3D属性网格，采用稀疏注意力扩散Transformer，直接在体积空间着色，避免多视图融合的局限性。
- 实验或效果：在纹理生成和3D部件分割任务上达到先进性能，生成无缝高保真纹理和精确边界的分割结果。

## 摘要（原文）

> Prevailing 3D texture generation methods, which often rely on multi-view fusion, are frequently hindered by inter-view inconsistencies and incomplete coverage of complex surfaces, limiting the fidelity and completeness of the generated content. To overcome these challenges, we introduce TEXTRIX, a native 3D attribute generation framework for high-fidelity texture synthesis and downstream applications such as precise 3D part segmentation. Our approach constructs a latent 3D attribute grid and leverages a Diffusion Transformer equipped with sparse attention, enabling direct coloring of 3D models in volumetric space and fundamentally avoiding the limitations of multi-view fusion. Built upon this native representation, the framework naturally extends to high-precision 3D segmentation by training the same architecture to predict semantic attributes on the grid. Extensive experiments demonstrate state-of-the-art performance on both tasks, producing seamless, high-fidelity textures and accurate 3D part segmentation with precise boundaries.

