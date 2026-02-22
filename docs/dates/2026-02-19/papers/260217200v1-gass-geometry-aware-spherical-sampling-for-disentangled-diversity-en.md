---
layout: default
title: GASS: Geometry-Aware Spherical Sampling for Disentangled Diversity Enhancement in Text-to-Image Generation
---

# GASS: Geometry-Aware Spherical Sampling for Disentangled Diversity Enhancement in Text-to-Image Generation
**arXiv**：[2602.17200v1](https://arxiv.org/abs/2602.17200) · [PDF](https://arxiv.org/pdf/2602.17200.pdf)  
**作者**：Ye Zhu, Kaleb S. Newman, Johannes F. Lutzeyer, Adriana Romero-Soriano, Michal Drozdzal, Olga Russakovsky  

**一句话要点**：提出几何感知球面采样以增强文本到图像生成中的解耦多样性

**关键词**：文本到图像生成, 多样性增强, 几何感知采样, 解耦表示, 扩散模型, CLIP嵌入

## 3 点简述
- 核心问题：文本到图像生成模型缺乏多样性，可能放大社会偏见。
- 方法要点：通过CLIP嵌入分解，沿文本相关和无关方向控制变化，提升几何投影分散度。
- 实验或效果：在不同骨干模型和基准上验证，增强多样性同时保持图像保真度和语义对齐。

## 摘要（原文）

> Despite high semantic alignment, modern text-to-image (T2I) generative models still struggle to synthesize diverse images from a given prompt. This lack of diversity not only restricts user choice, but also risks amplifying societal biases. In this work, we enhance the T2I diversity through a geometric lens. Unlike most existing methods that rely primarily on entropy-based guidance to increase sample dissimilarity, we introduce Geometry-Aware Spherical Sampling (GASS) to enhance diversity by explicitly controlling both prompt-dependent and prompt-independent sources of variation. Specifically, we decompose the diversity measure in CLIP embeddings using two orthogonal directions: the text embedding, which captures semantic variation related to the prompt, and an identified orthogonal direction that captures prompt-independent variation (e.g., backgrounds). Based on this decomposition, GASS increases the geometric projection spread of generated image embeddings along both axes and guides the T2I sampling process via expanded predictions along the generation trajectory. Our experiments on different frozen T2I backbones (U-Net and DiT, diffusion and flow) and benchmarks demonstrate the effectiveness of disentangled diversity enhancement with minimal impact on image fidelity and semantic alignment.

