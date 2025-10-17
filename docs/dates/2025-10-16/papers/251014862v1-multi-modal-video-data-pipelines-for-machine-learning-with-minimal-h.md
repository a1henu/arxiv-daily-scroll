---
layout: default
title: Multi-modal video data-pipelines for machine learning with minimal human supervision
---

# Multi-modal video data-pipelines for machine learning with minimal human supervision
**arXiv**：[2510.14862v1](https://arxiv.org/abs/2510.14862) · [PDF](https://arxiv.org/pdf/2510.14862.pdf)  
**作者**：Mihai-Cristian Pîrvu, Marius Leordeanu  

**一句话要点**：提出多模态视频数据流水线，实现无监督机器学习，应用于实时语义分割。

**关键词**：多模态学习, 无监督数据流水线, 模型蒸馏, 实时语义分割, 视频分析

## 3 点简述
- 核心问题：传统机器学习模型多为单模态，难以全面理解真实世界。
- 方法要点：使用预训练专家和自主数据流水线，结合PHG-MAE模型处理多模态数据。
- 实验或效果：蒸馏后模型参数<1M，性能媲美300M参数模型，部署于实时语义分割。

## 摘要（原文）

> The real-world is inherently multi-modal at its core. Our tools observe and
> take snapshots of it, in digital form, such as videos or sounds, however much
> of it is lost. Similarly for actions and information passing between humans,
> languages are used as a written form of communication. Traditionally, Machine
> Learning models have been unimodal (i.e. rgb -> semantic or text ->
> sentiment_class). Recent trends go towards bi-modality, where images and text
> are learned together, however, in order to truly understand the world, we need
> to integrate all these independent modalities. In this work we try to combine
> as many visual modalities as we can using little to no human supervision. In
> order to do this, we use pre-trained experts and procedural combinations
> between them on top of raw videos using a fully autonomous data-pipeline, which
> we also open-source. We then make use of PHG-MAE, a model specifically designed
> to leverage multi-modal data. We show that this model which was efficiently
> distilled into a low-parameter (<1M) can have competitive results compared to
> models of ~300M parameters. We deploy this model and analyze the use-case of
> real-time semantic segmentation from handheld devices or webcams on commodity
> hardware. Finally, we deploy other off-the-shelf models using the same
> framework, such as DPT for near real-time depth estimation.

