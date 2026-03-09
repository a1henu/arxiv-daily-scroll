---
layout: default
title: Skeleton-to-Image Encoding: Enabling Skeleton Representation Learning via Vision-Pretrained Models
---

# Skeleton-to-Image Encoding: Enabling Skeleton Representation Learning via Vision-Pretrained Models
**arXiv**：[2603.05963v1](https://arxiv.org/abs/2603.05963) · [PDF](https://arxiv.org/pdf/2603.05963.pdf)  
**作者**：Siyuan Yang, Jun Liu, Hao Cheng, Chong Wang, Shijian Lu, Hedvig Kjellstrom, Weisi Lin, Alex C. Kot  

**一句话要点**：提出Skeleton-to-Image Encoding，通过骨架转图像表示，实现基于视觉预训练模型的骨架表示学习。

**关键词**：骨架表示学习, 视觉预训练模型, 自监督学习, 异构骨架数据, 动作识别

## 3 点简述
- 核心问题：3D骨架数据与视觉模型格式差异大，且缺乏大规模数据集，难以直接应用预训练模型。
- 方法要点：将骨架序列按身体部位语义分区排列，转换为标准化图像，统一处理异构骨架数据。
- 实验或效果：在NTU-60、NTU-120和PKU-MMD数据集上验证了自监督骨架表示学习的有效性和泛化性。

## 摘要（原文）

> Recent advances in large-scale pretrained vision models have demonstrated impressive capabilities across a wide range of downstream tasks, including cross-modal and multi-modal scenarios. However, their direct application to 3D human skeleton data remains challenging due to fundamental differences in data format. Moreover, the scarcity of large-scale skeleton datasets and the need to incorporate skeleton data into multi-modal action recognition without introducing additional model branches present significant research opportunities. To address these challenges, we introduce Skeleton-to-Image Encoding (S2I), a novel representation that transforms skeleton sequences into image-like data by partitioning and arranging joints based on body-part semantics and resizing to standardized image dimensions. This encoding enables, for the first time, the use of powerful vision-pretrained models for self-supervised skeleton representation learning, effectively transferring rich visual-domain knowledge to skeleton analysis. While existing skeleton methods often design models tailored to specific, homogeneous skeleton formats, they overlook the structural heterogeneity that naturally arises from diverse data sources. In contrast, our S2I representation offers a unified image-like format that naturally accommodates heterogeneous skeleton data. Extensive experiments on NTU-60, NTU-120, and PKU-MMD demonstrate the effectiveness and generalizability of our method for self-supervised skeleton representation learning, including under challenging cross-format evaluation settings.

