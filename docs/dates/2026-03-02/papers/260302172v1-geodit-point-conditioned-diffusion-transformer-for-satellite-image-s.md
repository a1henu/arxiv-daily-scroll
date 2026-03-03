---
layout: default
title: GeoDiT: Point-Conditioned Diffusion Transformer for Satellite Image Synthesis
---

# GeoDiT: Point-Conditioned Diffusion Transformer for Satellite Image Synthesis
**arXiv**：[2603.02172v1](https://arxiv.org/abs/2603.02172) · [PDF](https://arxiv.org/pdf/2603.02172.pdf)  
**作者**：Srikumar Sastry, Dan Cher, Brian Wei, Aayush Dhakal, Subash Khanal, Dev Gupta, Nathan Jacobs  

**一句话要点**：提出GeoDiT，一种基于点条件扩散Transformer的卫星图像生成模型，以解决像素级控制耗时且语义有限的问题。

**关键词**：卫星图像合成, 扩散Transformer, 点条件控制, 自适应注意力, 遥感生成模型

## 3 点简述
- 核心问题：现有卫星图像生成模型依赖像素级地图，获取耗时且语义控制有限。
- 方法要点：引入点条件框架，通过点空间位置和文本描述提供语义丰富控制，采用自适应局部注意力机制。
- 实验或效果：系统评估设计选择，实验显示GeoDiT超越现有遥感生成模型，性能优异。

## 摘要（原文）

> We introduce GeoDiT, a diffusion transformer designed for text-to-satellite image generation with point-based control. Existing controlled satellite image generative models often require pixel-level maps that are time-consuming to acquire, yet semantically limited. To address this limitation, we introduce a novel point-based conditioning framework that controls the generation process through the spatial location of the points and the textual description associated with each point, providing semantically rich control signals. This approach enables flexible, annotation-friendly, and computationally simple inference for satellite image generation. To this end, we introduce an adaptive local attention mechanism that effectively regularizes the attention scores based on the input point queries. We systematically evaluate various domain-specific design choices for training GeoDiT, including the selection of satellite image representation for alignment and geolocation representation for conditioning. Our experiments demonstrate that GeoDiT achieves impressive generation performance, surpassing the state-of-the-art remote sensing generative models.

