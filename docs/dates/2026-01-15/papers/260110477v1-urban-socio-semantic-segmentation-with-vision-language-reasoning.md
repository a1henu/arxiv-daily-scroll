---
layout: default
title: Urban Socio-Semantic Segmentation with Vision-Language Reasoning
---

# Urban Socio-Semantic Segmentation with Vision-Language Reasoning
**arXiv**：[2601.10477v1](https://arxiv.org/abs/2601.10477) · [PDF](https://arxiv.org/pdf/2601.10477.pdf)  
**作者**：Yu Wang, Yi Wang, Rui Dai, Yujie Wang, Kaikui Liu, Xiangxiang Chu, Yansheng Li  

**一句话要点**：提出SocioReasoner框架，通过视觉语言推理解决卫星图像中社会语义实体分割问题。

**关键词**：社会语义分割, 视觉语言推理, 卫星图像分析, 强化学习优化, 零样本泛化

## 3 点简述
- 核心问题：现有分割模型难以处理卫星图像中的社会语义类别（如学校、公园）。
- 方法要点：引入SocioSeg数据集，并设计SocioReasoner框架，通过跨模态识别和多阶段推理模拟人类标注过程。
- 实验或效果：实验显示方法优于先进模型，并具有强零样本泛化能力。

## 摘要（原文）

> As hubs of human activity, urban surfaces consist of a wealth of semantic entities. Segmenting these various entities from satellite imagery is crucial for a range of downstream applications. Current advanced segmentation models can reliably segment entities defined by physical attributes (e.g., buildings, water bodies) but still struggle with socially defined categories (e.g., schools, parks). In this work, we achieve socio-semantic segmentation by vision-language model reasoning. To facilitate this, we introduce the Urban Socio-Semantic Segmentation dataset named SocioSeg, a new resource comprising satellite imagery, digital maps, and pixel-level labels of social semantic entities organized in a hierarchical structure. Additionally, we propose a novel vision-language reasoning framework called SocioReasoner that simulates the human process of identifying and annotating social semantic entities via cross-modal recognition and multi-stage reasoning. We employ reinforcement learning to optimize this non-differentiable process and elicit the reasoning capabilities of the vision-language model. Experiments demonstrate our approach's gains over state-of-the-art models and strong zero-shot generalization. Our dataset and code are available in https://github.com/AMAP-ML/SocioReasoner.

