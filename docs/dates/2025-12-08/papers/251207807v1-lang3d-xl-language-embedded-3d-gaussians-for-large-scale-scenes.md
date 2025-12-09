---
layout: default
title: Lang3D-XL: Language Embedded 3D Gaussians for Large-scale Scenes
---

# Lang3D-XL: Language Embedded 3D Gaussians for Large-scale Scenes
**arXiv**：[2512.07807v1](https://arxiv.org/abs/2512.07807) · [PDF](https://arxiv.org/pdf/2512.07807.pdf)  
**作者**：Shai Krakovsky, Gal Fiebelman, Sagie Benaim, Hadar Averbuch-Elor  

**一句话要点**：提出Lang3D-XL方法，通过低维语义瓶颈特征和哈希编码器解决大规模场景中语言嵌入3D高斯的效率与语义对齐问题。

**关键词**：语言嵌入3D高斯, 大规模场景理解, 语义特征对齐, 哈希编码器, 效率优化, 多模态推理

## 3 点简述
- 核心问题：现有特征蒸馏方法在大规模互联网数据上因语义特征错位和内存运行时效率低下而难以有效学习。
- 方法要点：引入极低维语义瓶颈特征，结合多分辨率哈希编码器提升效率；使用Attenuated Downsampler模块和正则化处理语义错位。
- 实验或效果：在HolyScenes数据集上评估，性能与效率均超越现有方法。

## 摘要（原文）

> Embedding a language field in a 3D representation enables richer semantic understanding of spatial environments by linking geometry with descriptive meaning. This allows for a more intuitive human-computer interaction, enabling querying or editing scenes using natural language, and could potentially improve tasks like scene retrieval, navigation, and multimodal reasoning. While such capabilities could be transformative, in particular for large-scale scenes, we find that recent feature distillation approaches cannot effectively learn over massive Internet data due to challenges in semantic feature misalignment and inefficiency in memory and runtime. To this end, we propose a novel approach to address these challenges. First, we introduce extremely low-dimensional semantic bottleneck features as part of the underlying 3D Gaussian representation. These are processed by rendering and passing them through a multi-resolution, feature-based, hash encoder. This significantly improves efficiency both in runtime and GPU memory. Second, we introduce an Attenuated Downsampler module and propose several regularizations addressing the semantic misalignment of ground truth 2D features. We evaluate our method on the in-the-wild HolyScenes dataset and demonstrate that it surpasses existing approaches in both performance and efficiency.

