---
layout: default
title: Locality-Attending Vision Transformer
---

# Locality-Attending Vision Transformer
**arXiv**：[2603.04892v1](https://arxiv.org/abs/2603.04892) · [PDF](https://arxiv.org/pdf/2603.04892.pdf)  
**作者**：Sina Hajimiri, Farzad Beizaee, Fereshteh Shakeri, Christian Desrosiers, Ismail Ben Ayed, Jose Dolz  

**一句话要点**：提出局部注意力视觉变换器，通过可学习高斯核调制自注意力以增强分割性能，同时保持分类能力。

**关键词**：视觉变换器, 局部注意力, 图像分割, 自注意力调制, 高斯核, 补丁表示

## 3 点简述
- 核心问题：视觉变换器的全局自注意力机制可能模糊分割任务所需的细粒度空间细节。
- 方法要点：使用可学习高斯核偏置注意力至邻近补丁，并优化补丁表示以学习更好的空间嵌入。
- 实验或效果：在三个基准测试中实现显著分割增益，如ADE20K上ViT Tiny和Base分别提升超过6%和4%，且不牺牲分类性能。

## 摘要（原文）

> Vision transformers have demonstrated remarkable success in classification by leveraging global self-attention to capture long-range dependencies. However, this same mechanism can obscure fine-grained spatial details crucial for tasks such as segmentation. In this work, we seek to enhance segmentation performance of vision transformers after standard image-level classification training. More specifically, we present a simple yet effective add-on that improves performance on segmentation tasks while retaining vision transformers' image-level recognition capabilities. In our approach, we modulate the self-attention with a learnable Gaussian kernel that biases the attention toward neighboring patches. We further refine the patch representations to learn better embeddings at patch positions. These modifications encourage tokens to focus on local surroundings and ensure meaningful representations at spatial positions, while still preserving the model's ability to incorporate global information. Experiments demonstrate the effectiveness of our modifications, evidenced by substantial segmentation gains on three benchmarks (e.g., over 6% and 4% on ADE20K for ViT Tiny and Base), without changing the training regime or sacrificing classification performance. The code is available at https://github.com/sinahmr/LocAtViT/.

