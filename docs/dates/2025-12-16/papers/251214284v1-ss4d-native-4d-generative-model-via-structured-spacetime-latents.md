---
layout: default
title: SS4D: Native 4D Generative Model via Structured Spacetime Latents
---

# SS4D: Native 4D Generative Model via Structured Spacetime Latents
**arXiv**：[2512.14284v1](https://arxiv.org/abs/2512.14284) · [PDF](https://arxiv.org/pdf/2512.14284.pdf)  
**作者**：Zhibing Li, Mengchen Zhang, Tong Wu, Jing Tan, Jiaqi Wang, Dahua Lin  

**一句话要点**：提出SS4D原生4D生成模型，通过结构化时空潜在变量从单目视频合成动态3D对象

**关键词**：4D生成模型, 结构化时空潜在变量, 单目视频合成, 时间一致性, 因子化4D卷积, 动态3D对象

## 3 点简述
- 核心问题：现有方法依赖3D或视频生成模型优化构建4D表示，导致保真度、时间一致性和结构一致性不足
- 方法要点：基于预训练单图到3D模型增强空间一致性，引入时间层确保时间一致性，使用因子化4D卷积和时间下采样压缩潜在序列
- 实验或效果：实现高保真、时间连贯和结构一致的动态3D对象生成，支持长视频序列高效训练和推理

## 摘要（原文）

> We present SS4D, a native 4D generative model that synthesizes dynamic 3D objects directly from monocular video. Unlike prior approaches that construct 4D representations by optimizing over 3D or video generative models, we train a generator directly on 4D data, achieving high fidelity, temporal coherence, and structural consistency. At the core of our method is a compressed set of structured spacetime latents. Specifically, (1) To address the scarcity of 4D training data, we build on a pre-trained single-image-to-3D model, preserving strong spatial consistency. (2) Temporal consistency is enforced by introducing dedicated temporal layers that reason across frames. (3) To support efficient training and inference over long video sequences, we compress the latent sequence along the temporal axis using factorized 4D convolutions and temporal downsampling blocks. In addition, we employ a carefully designed training strategy to enhance robustness against occlusion

