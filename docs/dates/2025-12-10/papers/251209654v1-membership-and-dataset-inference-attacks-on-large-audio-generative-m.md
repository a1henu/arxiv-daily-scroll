---
layout: default
title: Membership and Dataset Inference Attacks on Large Audio Generative Models
---

# Membership and Dataset Inference Attacks on Large Audio Generative Models
**arXiv**：[2512.09654v1](https://arxiv.org/abs/2512.09654) · [PDF](https://arxiv.org/pdf/2512.09654.pdf)  
**作者**：Jakub Proboszcz, Paweł Kochanski, Karol Korszun, Donato Crisostomi, Giorgio Strano, Emanuele Rodolà, Kamil Deja, Jan Dubinski  

**一句话要点**：提出数据集推理攻击以评估音频生成模型训练数据版权归属

**关键词**：音频生成模型, 成员推理攻击, 数据集推理攻击, 版权保护, 训练数据验证

## 3 点简述
- 核心问题：验证音频生成模型是否使用特定艺术家的作品进行训练，以应对版权保护挑战。
- 方法要点：在成员推理攻击基础上，通过聚合多个样本证据，实施数据集推理攻击。
- 实验或效果：成员推理在大型数据集上效果有限，但数据集推理在音频领域成功，提供实用评估机制。

## 摘要（原文）

> Generative audio models, based on diffusion and autoregressive architectures, have advanced rapidly in both quality and expressiveness. This progress, however, raises pressing copyright concerns, as such models are often trained on vast corpora of artistic and commercial works. A central question is whether one can reliably verify if an artist's material was included in training, thereby providing a means for copyright holders to protect their content. In this work, we investigate the feasibility of such verification through membership inference attacks (MIA) on open-source generative audio models, which attempt to determine whether a specific audio sample was part of the training set. Our empirical results show that membership inference alone is of limited effectiveness at scale, as the per-sample membership signal is weak for models trained on large and diverse datasets. However, artists and media owners typically hold collections of works rather than isolated samples. Building on prior work in text and vision domains, in this work we focus on dataset inference (DI), which aggregates diverse membership evidence across multiple samples. We find that DI is successful in the audio domain, offering a more practical mechanism for assessing whether an artist's works contributed to model training. Our results suggest DI as a promising direction for copyright protection and dataset accountability in the era of large audio generative models.

