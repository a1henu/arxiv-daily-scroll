---
layout: default
title: MM-TS: Multi-Modal Temperature and Margin Schedules for Contrastive Learning with Long-Tail Data
---

# MM-TS: Multi-Modal Temperature and Margin Schedules for Contrastive Learning with Long-Tail Data
**arXiv**：[2603.08202v1](https://arxiv.org/abs/2603.08202) · [PDF](https://arxiv.org/pdf/2603.08202.pdf)  
**作者**：Siarhei Sheludzko, Dhimitrios Duka, Bernt Schiele, Hilde Kuehne, Anna Kukleva  

**一句话要点**：提出多模态温度与边界调度方法，以优化长尾数据下的对比学习性能

**关键词**：多模态对比学习, 温度调度, 长尾分布, 最大边界框架, 图像-语言对齐, 视频-语言对齐

## 3 点简述
- 针对多模态对比学习中温度参数固定问题，提出动态温度调度机制
- 结合样本局部分布调整温度，密集簇样本用更高温度以保持语义结构
- 在四个图像-视频语言数据集上验证，提升性能并达到新最优结果

## 摘要（原文）

> Contrastive learning has become a fundamental approach in both uni-modal and multi-modal frameworks. This learning paradigm pulls positive pairs of samples closer while pushing negatives apart. In the uni-modal setting (e.g., image-based learning), previous research has shown that the strength of these forces can be controlled through the temperature parameter. In this work, we propose Multi-Modal Temperature and Margin Schedules (MM-TS), extending the concept of uni-modal temperature scheduling to multi-modal contrastive learning. Our method dynamically adjusts the temperature in the contrastive loss during training, modulating the attraction and repulsion forces in the multi-modal setting. Additionally, recognizing that standard multi-modal datasets often follow imbalanced, long-tail distributions, we adapt the temperature based on the local distribution of each training sample. Specifically, samples from dense clusters are assigned a higher temperature to better preserve their semantic structure. Furthermore, we demonstrate that temperature scheduling can be effectively integrated within a max-margin framework, thereby unifying the two predominant approaches in multi-modal contrastive learning: InfoNCE loss and max-margin objective. We evaluate our approach on four widely used image- and video-language datasets, Flickr30K, MSCOCO, EPIC-KITCHENS-100, and YouCook2, and show that our dynamic temperature and margin schedules improve performance and lead to new state-of-the-art results in the field.

