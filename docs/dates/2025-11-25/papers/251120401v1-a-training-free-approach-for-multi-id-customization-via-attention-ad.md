---
layout: default
title: A Training-Free Approach for Multi-ID Customization via Attention Adjustment and Spatial Control
---

# A Training-Free Approach for Multi-ID Customization via Attention Adjustment and Spatial Control
**arXiv**：[2511.20401v1](https://arxiv.org/abs/2511.20401) · [PDF](https://arxiv.org/pdf/2511.20401.pdf)  
**作者**：Jiawei Lin, Guanlong Jiao, Jianjin Xu  

**一句话要点**：提出MultiID方法以无训练方式解决多ID定制中的复制粘贴和文本控制问题

**关键词**：多ID定制, 注意力调整, 空间控制, 训练免费方法, 图像生成

## 3 点简述
- 核心问题：多ID定制存在复制粘贴导致质量低和文本控制性差的问题
- 方法要点：使用ID解耦交叉注意力机制和空间控制策略增强生成质量
- 实验或效果：在IDBench基准上表现优于或可比训练方法，验证有效性

## 摘要（原文）

> Multi-ID customization is an interesting topic in computer vision and attracts considerable attention recently. Given the ID images of multiple individuals, its purpose is to generate a customized image that seamlessly integrates them while preserving their respective identities. Compared to single-ID customization, multi-ID customization is much more difficult and poses two major challenges. First, since the multi-ID customization model is trained to reconstruct an image from the cropped person regions, it often encounters the copy-paste issue during inference, leading to lower quality. Second, the model also suffers from inferior text controllability. The generated result simply combines multiple persons into one image, regardless of whether it is aligned with the input text. In this work, we propose MultiID to tackle this challenging task in a training-free manner. Since the existing single-ID customization models have less copy-paste issue, our key idea is to adapt these models to achieve multi-ID customization. To this end, we present an ID-decoupled cross-attention mechanism, injecting distinct ID embeddings into the corresponding image regions and thus generating multi-ID outputs. To enhance the generation controllability, we introduce three critical strategies, namely the local prompt, depth-guided spatial control, and extended self-attention, making the results more consistent with the text prompts and ID images. We also carefully build a benchmark, called IDBench, for evaluation. The extensive qualitative and quantitative results demonstrate the effectiveness of MultiID in solving the aforementioned two challenges. Its performance is comparable or even better than the training-based multi-ID customization methods.

