---
layout: default
title: Motion Attribution for Video Generation
---

# Motion Attribution for Video Generation
**arXiv**：[2601.08828v1](https://arxiv.org/abs/2601.08828) · [PDF](https://arxiv.org/pdf/2601.08828.pdf)  
**作者**：Xindi Wu, Despoina Paschalidou, Jun Gao, Antonio Torralba, Laura Leal-Taixé, Olga Russakovsky, Sanja Fidler, Jonathan Lorraine  

**一句话要点**：提出Motive框架以解决视频生成中数据对运动影响的理解问题

**关键词**：视频生成, 运动归因, 数据归因, 梯度方法, 时间动态, 数据筛选

## 3 点简述
- 核心问题：视频生成模型中数据如何影响运动动态尚不明确
- 方法要点：基于梯度的运动中心数据归因框架，通过运动加权损失掩码分离时间动态
- 实验或效果：在VBench上提升运动平滑度和动态度，人类偏好胜率达74.1%

## 摘要（原文）

> Despite the rapid progress of video generation models, the role of data in influencing motion is poorly understood. We present Motive (MOTIon attribution for Video gEneration), a motion-centric, gradient-based data attribution framework that scales to modern, large, high-quality video datasets and models. We use this to study which fine-tuning clips improve or degrade temporal dynamics. Motive isolates temporal dynamics from static appearance via motion-weighted loss masks, yielding efficient and scalable motion-specific influence computation. On text-to-video models, Motive identifies clips that strongly affect motion and guides data curation that improves temporal consistency and physical plausibility. With Motive-selected high-influence data, our method improves both motion smoothness and dynamic degree on VBench, achieving a 74.1% human preference win rate compared with the pretrained base model. To our knowledge, this is the first framework to attribute motion rather than visual appearance in video generative models and to use it to curate fine-tuning data.

