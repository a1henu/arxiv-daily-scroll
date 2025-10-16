---
layout: default
title: Unsupervised Domain Adaptation via Content Alignment for Hippocampus Segmentation
---

# Unsupervised Domain Adaptation via Content Alignment for Hippocampus Segmentation
**arXiv**：[2510.13075v1](https://arxiv.org/abs/2510.13075) · [PDF](https://arxiv.org/pdf/2510.13075.pdf)  
**作者**：Hoda Kalabizadeh, Ludovica Griffanti, Pak-Hei Yeung, Ana I. L. Namburete, Nicola K. Dinsdale, Konstantinos Kamnitsas  

**一句话要点**：提出基于内容对齐的无监督域适应框架，用于跨域海马体分割

**关键词**：无监督域适应, 海马体分割, 可变形图像配准, 医学图像分析, MRI域偏移

## 3 点简述
- 核心问题：医学图像分割模型因域偏移（风格和内容变化）在跨数据集部署时性能下降
- 方法要点：结合z归一化风格协调和双向可变形图像配准，联合训练配准、分割和判别器网络
- 实验或效果：在合成和真实MRI数据集上验证，Dice分数相对标准方法提升高达15%

## 摘要（原文）

> Deep learning models for medical image segmentation often struggle when
> deployed across different datasets due to domain shifts - variations in both
> image appearance, known as style, and population-dependent anatomical
> characteristics, referred to as content. This paper presents a novel
> unsupervised domain adaptation framework that directly addresses domain shifts
> encountered in cross-domain hippocampus segmentation from MRI, with specific
> emphasis on content variations. Our approach combines efficient style
> harmonisation through z-normalisation with a bidirectional deformable image
> registration (DIR) strategy. The DIR network is jointly trained with
> segmentation and discriminator networks to guide the registration with respect
> to a region of interest and generate anatomically plausible transformations
> that align source images to the target domain. We validate our approach through
> comprehensive evaluations on both a synthetic dataset using Morpho-MNIST (for
> controlled validation of core principles) and three MRI hippocampus datasets
> representing populations with varying degrees of atrophy. Across all
> experiments, our method outperforms existing baselines. For hippocampus
> segmentation, when transferring from young, healthy populations to clinical
> dementia patients, our framework achieves up to 15% relative improvement in
> Dice score compared to standard augmentation methods, with the largest gains
> observed in scenarios with substantial content shift. These results highlight
> the efficacy of our approach for accurate hippocampus segmentation across
> diverse populations.

