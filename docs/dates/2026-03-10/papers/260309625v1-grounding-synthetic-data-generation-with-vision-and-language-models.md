---
layout: default
title: Grounding Synthetic Data Generation With Vision and Language Models
---

# Grounding Synthetic Data Generation With Vision and Language Models
**arXiv**：[2603.09625v1](https://arxiv.org/abs/2603.09625) · [PDF](https://arxiv.org/pdf/2603.09625.pdf)  
**作者**：Ümit Mert Çağlar, Alptekin Temizel  

**一句话要点**：提出基于视觉语言模型的合成数据增强框架，以提升遥感图像分割与描述任务性能。

**关键词**：合成数据增强, 遥感图像处理, 视觉语言模型, 语义分割, 图像描述, 数据集基准

## 3 点简述
- 现有合成数据评估指标依赖潜在特征相似性，难以解释且与下游任务贡献不总相关。
- 结合生成模型、语义分割和图像描述，构建可解释的合成数据增强与评估框架。
- 实验表明，增强数据训练模型优于仅用真实数据的基线，并发布大规模数据集ARAS400k。

## 摘要（原文）

> Deep learning models benefit from increasing data diversity and volume, motivating synthetic data augmentation to improve existing datasets. However, existing evaluation metrics for synthetic data typically calculate latent feature similarity, which is difficult to interpret and does not always correlate with the contribution to downstream tasks.
>   We propose a vision-language grounded framework for interpretable synthetic data augmentation and evaluation in remote sensing. Our approach combines generative models, semantic segmentation and image captioning with vision and language models. Based on this framework, we introduce ARAS400k: A large-scale Remote sensing dataset Augmented with Synthetic data for segmentation and captioning, containing 100k real images and 300k synthetic images, each paired with segmentation maps and descriptions.
>   ARAS400k enables the automated evaluation of synthetic data by analyzing semantic composition, minimizing caption redundancy, and verifying cross-modal consistency between visual structures and language descriptions. Experimental results indicate that while models trained exclusively on synthetic data reach competitive performance levels, those trained with augmented data (a combination of real and synthetic images) consistently outperform real-data baselines. Consequently, this work establishes a scalable benchmark for remote sensing tasks, specifically in semantic segmentation and image captioning. The dataset is available at zenodo.org/records/18890661 and the code base at github.com/caglarmert/ARAS400k.

