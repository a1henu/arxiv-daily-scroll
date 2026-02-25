---
layout: default
title: Motivation is Something You Need
---

# Motivation is Something You Need
**arXiv**：[2602.21064v1](https://arxiv.org/abs/2602.21064) · [PDF](https://arxiv.org/pdf/2602.21064.pdf)  
**作者**：Mehdi Acheli, Walid Gaaloul  

**一句话要点**：提出基于情感神经科学的双模型训练框架，以提升图像分类性能并降低训练成本。

**关键词**：情感神经科学, 双模型训练, 图像分类, 动机状态, 权重共享, 计算效率

## 3 点简述
- 核心问题：传统训练方法可能效率低，难以平衡模型性能与计算成本。
- 方法要点：设计小基础模型与间歇激活的大动机模型，模拟大脑寻求状态以增强认知。
- 实验或效果：在图像分类任务中，交替训练提升基础模型，动机模型数据少但性能可超越独立训练。

## 摘要（原文）

> This work introduces a novel training paradigm that draws from affective neuroscience. Inspired by the interplay of emotions and cognition in the human brain and more specifically the SEEKING motivational state, we design a dual-model framework where a smaller base model is trained continuously, while a larger motivated model is activated intermittently during predefined "motivation conditions". The framework mimics the emotional state of high curiosity and anticipation of reward in which broader brain regions are recruited to enhance cognitive performance. Exploiting scalable architectures where larger models extend smaller ones, our method enables shared weight updates and selective expansion of network capacity during noteworthy training steps. Empirical evaluation on the image classification task demonstrates that, not only does the alternating training scheme efficiently and effectively enhance the base model compared to a traditional scheme, in some cases, the motivational model also surpasses its standalone counterpart despite seeing less data per epoch. This opens the possibility of simultaneously training two models tailored to different deployment constraints with competitive or superior performance while keeping training cost lower than when training the larger model.

