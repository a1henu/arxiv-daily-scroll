---
layout: default
title: Vision Foundation Models in Agriculture: Toward Domain-Specific Adaptation for Weed Herbicide Trials Assessment
---

# Vision Foundation Models in Agriculture: Toward Domain-Specific Adaptation for Weed Herbicide Trials Assessment
**arXiv**：[2511.04288v1](https://arxiv.org/abs/2511.04288) · [PDF](https://arxiv.org/pdf/2511.04288.pdf)  
**作者**：Leire Benito-Del-Valle, Artzai Picón, Daniel Mugica, Manuel Ramos, Eva Portillo, Javier Romero, Carlos Javier Jimenez, Ramón Navarra-Mestre  

**一句话要点**：提出领域自适应视觉基础模型以解决农业除草剂试验中物种识别与损伤评估问题

**关键词**：视觉基础模型, 农业视觉, 自监督学习, 领域自适应, 除草剂试验, 图像分类

## 3 点简述
- 核心问题：通用视觉基础模型在农业领域对物种和损伤类型的细粒度识别性能受限
- 方法要点：采用自监督学习在农业数据集上训练，优化模型表示以适应除草剂试验图像
- 实验或效果：在物种识别和损伤分类中F1分数显著提升，并在未见条件下表现更优，减少标注需求

## 摘要（原文）

> Herbicide field trials require accurate identification of plant species and
> assessment of herbicide-induced damage across diverse environments. While
> general-purpose vision foundation models have shown promising results in
> complex visual domains, their performance can be limited in agriculture, where
> fine-grained distinctions between species and damage types are critical.
>   In this work, we adapt a general-purpose vision foundation model to herbicide
> trial characterization. Trained using a self-supervised learning approach on a
> large, curated agricultural dataset, the model learns rich and transferable
> representations optimized for herbicide trials images.
>   Our domain-specific model significantly outperforms the best general-purpose
> foundation model in both species identification (F1 score improvement from 0.91
> to 0.94) and damage classification (from 0.26 to 0.33). Under unseen conditions
> (new locations and other time), it achieves even greater gains (species
> identification from 0.56 to 0.66; damage classification from 0.17 to 0.27). In
> domain-shift scenarios, such as drone imagery, it maintains strong performance
> (species classification from 0.49 to 0.60).
>   Additionally, we show that domain-specific pretraining enhances segmentation
> accuracy, particularly in low-annotation regimes. An annotation-efficiency
> analysis reveals that, under unseen conditions, the domain-specific model
> achieves 5.4% higher F1 score than the general-purpose model, while using 80%
> fewer labeled samples.
>   These results demonstrate the generalization capabilities of domain-specific
> foundation models and their potential to significantly reduce manual annotation
> efforts, offering a scalable and automated solution for herbicide trial
> analysis.

