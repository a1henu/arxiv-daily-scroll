---
layout: default
title: CoShadow: Multi-Object Shadow Generation for Image Compositing via Diffusion Model
---

# CoShadow: Multi-Object Shadow Generation for Image Compositing via Diffusion Model
**arXiv**：[2603.02743v1](https://arxiv.org/abs/2603.02743) · [PDF](https://arxiv.org/pdf/2603.02743.pdf)  
**作者**：Waqas Ahmed, Dean Diepeveen, Ferdous Sohel  

**一句话要点**：提出CoShadow方法，基于扩散模型解决多对象图像合成中的阴影生成问题

**关键词**：阴影生成, 图像合成, 扩散模型, 多对象处理, 注意力机制

## 3 点简述
- 核心问题：现有方法难以生成多对象合成时的物理一致阴影，限制了图像合成的真实感
- 方法要点：利用预训练扩散模型，结合图像特征和文本编码，通过交叉注意力和对齐损失实现多对象阴影生成
- 实验或效果：在DESOBAv2数据集上验证，在单对象和多对象设置中均达到先进性能

## 摘要（原文）

> Realistic shadow generation is crucial for achieving seamless image compositing, yet existing methods primarily focus on single-object insertion and often fail to generalize when multiple foreground objects are composited into a background scene. In practice, however, modern compositing pipelines and real-world applications often insert multiple objects simultaneously, necessitating shadows that are jointly consistent in terms of geometry, attachment, and location. In this paper, we address the under-explored problem of multi-object shadow generation, aiming to synthesize physically plausible shadows for multiple inserted objects. Our approach exploits the multimodal capabilities of a pre-trained text-to-image diffusion model. An image pathway injects dense, multi-scale features to provide fine-grained spatial guidance, while a text-based pathway encodes per-object shadow bounding boxes as learned positional tokens and fuses them via cross-attention. An attention-alignment loss further grounds these tokens to their corresponding shadow regions. To support this task, we augment the DESOBAv2 dataset by constructing composite scenes with multiple inserted objects and automatically derive prompts combining object category and shadow positioning information. Experimental results demonstrate that our method achieves state-of-the-art performance in both single and multi-object shadow generation settings.

