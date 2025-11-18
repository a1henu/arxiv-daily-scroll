---
layout: default
title: Large Language Models Meet Extreme Multi-label Classification: Scaling and Multi-modal Framework
---

# Large Language Models Meet Extreme Multi-label Classification: Scaling and Multi-modal Framework
**arXiv**：[2511.13189v1](https://arxiv.org/abs/2511.13189) · [PDF](https://arxiv.org/pdf/2511.13189.pdf)  
**作者**：Diego Ortego, Marlon Rodríguez, Mario Almagro, Kunal Dahiya, David Jiménez, Juan C. SanMiguel  

**一句话要点**：提出ViXML框架以解决极端多标签分类中的效率与性能平衡问题。

**关键词**：极端多标签分类, 多模态学习, 解码器模型, 视觉增强, 效率优化

## 3 点简述
- 核心问题：极端多标签分类需在超大标签空间中平衡效率与性能。
- 方法要点：结合解码器模型和视觉信息，通过单图像嵌入集成多模态能力。
- 实验或效果：在多个数据集上超越现有方法，P@1提升最高达8.21%。

## 摘要（原文）

> Foundation models have revolutionized artificial intelligence across numerous domains, yet their transformative potential remains largely untapped in Extreme Multi-label Classification (XMC). Queries in XMC are associated with relevant labels from extremely large label spaces, where it is critical to strike a balance between efficiency and performance. Therefore, many recent approaches efficiently pose XMC as a maximum inner product search between embeddings learned from small encoder-only transformer architectures. In this paper, we address two important aspects in XMC: how to effectively harness larger decoder-only models, and how to exploit visual information while maintaining computational efficiency. We demonstrate that both play a critical role in XMC separately and can be combined for improved performance. We show that a few billion-size decoder can deliver substantial improvements while keeping computational overhead manageable. Furthermore, our Vision-enhanced eXtreme Multi-label Learning framework (ViXML) efficiently integrates foundation vision models by pooling a single embedding per image. This limits computational growth while unlocking multi-modal capabilities. Remarkably, ViXML with small encoders outperforms text-only decoder in most cases, showing that an image is worth billions of parameters. Finally, we present an extension of existing text-only datasets to exploit visual metadata and make them available for future benchmarking. Comprehensive experiments across four public text-only datasets and their corresponding image enhanced versions validate our proposals' effectiveness, surpassing previous state-of-the-art by up to +8.21\% in P@1 on the largest dataset. ViXML's code is available at https://github.com/DiegoOrtego/vixml.

