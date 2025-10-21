---
layout: default
title: CaMiT: A Time-Aware Car Model Dataset for Classification and Generation
---

# CaMiT: A Time-Aware Car Model Dataset for Classification and Generation
**arXiv**：[2510.17626v1](https://arxiv.org/abs/2510.17626) · [PDF](https://arxiv.org/pdf/2510.17626.pdf)  
**作者**：Frédéric LIN, Biruk Abere Ambaw, Adrian Popescu, Hejer Ammar, Romaric Audigier, Hervé Le Borgne  

**一句话要点**：提出CaMiT数据集以解决汽车模型随时间演变的视觉识别与生成问题

**关键词**：时间感知数据集, 细粒度分类, 持续学习, 图像生成, 汽车模型识别

## 3 点简述
- 核心问题：AI系统需适应视觉环境随时间变化，尤其在对象外观演变的领域
- 方法要点：引入时间增量分类和生成策略，提升模型对新兴、演变和消失类的鲁棒性
- 实验或效果：静态预训练资源高效，时间增量方法改善跨年测试准确性

## 摘要（原文）

> AI systems must adapt to evolving visual environments, especially in domains
> where object appearances change over time. We introduce Car Models in Time
> (CaMiT), a fine-grained dataset capturing the temporal evolution of car models,
> a representative class of technological artifacts. CaMiT includes 787K labeled
> samples of 190 car models (2007-2023) and 5.1M unlabeled samples (2005-2023),
> supporting both supervised and self-supervised learning. Static pretraining on
> in-domain data achieves competitive performance with large-scale generalist
> models while being more resource-efficient, yet accuracy declines when models
> are tested across years. To address this, we propose a time-incremental
> classification setting, a realistic continual learning scenario with emerging,
> evolving, and disappearing classes. We evaluate two strategies:
> time-incremental pretraining, which updates the backbone, and time-incremental
> classifier learning, which updates only the final layer, both improving
> temporal robustness. Finally, we explore time-aware image generation that
> leverages temporal metadata during training, yielding more realistic outputs.
> CaMiT offers a rich benchmark for studying temporal adaptation in fine-grained
> visual recognition and generation.

