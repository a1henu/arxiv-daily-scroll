---
layout: default
title: A Contrastive Learning Framework Empowered by Attention-based Feature Adaptation for Street-View Image Classification
---

# A Contrastive Learning Framework Empowered by Attention-based Feature Adaptation for Street-View Image Classification
**arXiv**：[2602.16590v1](https://arxiv.org/abs/2602.16590) · [PDF](https://arxiv.org/pdf/2602.16590.pdf)  
**作者**：Qi You, Yitai Cheng, Zichao Zeng, James Haworth  

**一句话要点**：提出CLIP-MHAdapter，通过多头自注意力增强特征适应，提升街景图像属性分类性能。

**关键词**：街景图像分类, 对比学习, 特征适应, 多头自注意力, 轻量模型

## 3 点简述
- 问题：现有CLIP适应方法依赖全局嵌入，难以捕捉街景中细粒度局部属性。
- 方法：在轻量CLIP适应范式中添加带多头自注意力的瓶颈MLP，建模补丁间依赖关系。
- 效果：在Global StreetScapes数据集上，以约140万参数实现SOTA或竞争性准确率，计算成本低。

## 摘要（原文）

> Street-view image attribute classification is a vital downstream task of image classification, enabling applications such as autonomous driving, urban analytics, and high-definition map construction. It remains computationally demanding whether training from scratch, initialising from pre-trained weights, or fine-tuning large models. Although pre-trained vision-language models such as CLIP offer rich image representations, existing adaptation or fine-tuning methods often rely on their global image embeddings, limiting their ability to capture fine-grained, localised attributes essential in complex, cluttered street scenes. To address this, we propose CLIP-MHAdapter, a variant of the current lightweight CLIP adaptation paradigm that appends a bottleneck MLP equipped with multi-head self-attention operating on patch tokens to model inter-patch dependencies. With approximately 1.4 million trainable parameters, CLIP-MHAdapter achieves superior or competitive accuracy across eight attribute classification tasks on the Global StreetScapes dataset, attaining new state-of-the-art results while maintaining low computational cost. The code is available at https://github.com/SpaceTimeLab/CLIP-MHAdapter.

