---
layout: default
title: Align then Adapt: Rethinking Parameter-Efficient Transfer Learning in 4D Perception
---

# Align then Adapt: Rethinking Parameter-Efficient Transfer Learning in 4D Perception
**arXiv**：[2602.23069v1](https://arxiv.org/abs/2602.23069) · [PDF](https://arxiv.org/pdf/2602.23069.pdf)  
**作者**：Yiding Sun, Jihua Zhu, Haozhe Cheng, Chaoyi Lu, Zhichuan Yang, Lin Chen, Yaonan Wang  

**一句话要点**：提出PointATA范式以解决3D预训练模型向4D感知任务迁移时的过拟合与模态差距问题

**关键词**：点云视频理解, 参数高效迁移学习, 模态对齐, 时序建模, 4D感知

## 3 点简述
- 核心问题：3D与4D数据集分布差异导致迁移能力受限，存在过拟合和模态差距
- 方法要点：分两阶段设计，先对齐分布缓解模态差距，再适配增强时序建模能力
- 实验或效果：在动作识别和语义分割任务上达到或超越全微调模型，参数效率高

## 摘要（原文）

> Point cloud video understanding is critical for robotics as it accurately encodes motion and scene interaction. We recognize that 4D datasets are far scarcer than 3D ones, which hampers the scalability of self-supervised 4D models. A promising alternative is to transfer 3D pre-trained models to 4D perception tasks. However, rigorous empirical analysis reveals two critical limitations that impede transfer capability: overfitting and the modality gap. To overcome these challenges, we develop a novel "Align then Adapt" (PointATA) paradigm that decomposes parameter-efficient transfer learning into two sequential stages. Optimal-transport theory is employed to quantify the distributional discrepancy between 3D and 4D datasets, enabling our proposed point align embedder to be trained in Stage 1 to alleviate the underlying modality gap. To mitigate overfitting, an efficient point-video adapter and a spatial-context encoder are integrated into the frozen 3D backbone to enhance temporal modeling capacity in Stage 2. Notably, with the above engineering-oriented designs, PointATA enables a pre-trained 3D model without temporal knowledge to reason about dynamic video content at a smaller parameter cost compared to previous work. Extensive experiments show that PointATA can match or even outperform strong full fine-tuning models, whilst enjoying the advantage of parameter efficiency, e.g. 97.21 \% accuracy on 3D action recognition, $+8.7 \%$ on 4 D action segmentation, and 84.06\% on 4D semantic segmentation.

