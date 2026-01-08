---
layout: default
title: CloudMatch: Weak-to-Strong Consistency Learning for Semi-Supervised Cloud Detection
---

# CloudMatch: Weak-to-Strong Consistency Learning for Semi-Supervised Cloud Detection
**arXiv**：[2601.03528v1](https://arxiv.org/abs/2601.03528) · [PDF](https://arxiv.org/pdf/2601.03528.pdf)  
**作者**：Jiayi Zhao, Changlu Chen, Jingsheng Li, Tianxiang Xue, Kun Zhan  

**一句话要点**：提出CloudMatch框架，通过视图一致性学习和场景混合增强解决半监督云检测问题。

**关键词**：半监督学习, 云检测, 视图一致性学习, 场景混合增强, 遥感图像处理

## 3 点简述
- 核心问题：像素级标注成本高，半监督学习利用未标注遥感图像进行云检测。
- 方法要点：生成弱增强和强增强视图，结合场景间和场景内混合，强制预测一致性以捕捉云模式多样性。
- 实验或效果：实验显示CloudMatch性能良好，能有效利用未标注数据提升检测能力。

## 摘要（原文）

> Due to the high cost of annotating accurate pixel-level labels, semi-supervised learning has emerged as a promising approach for cloud detection. In this paper, we propose CloudMatch, a semi-supervised framework that effectively leverages unlabeled remote sensing imagery through view-consistency learning combined with scene-mixing augmentations. An observation behind CloudMatch is that cloud patterns exhibit structural diversity and contextual variability across different scenes and within the same scene category. Our key insight is that enforcing prediction consistency across diversely augmented views, incorporating both inter-scene and intra-scene mixing, enables the model to capture the structural diversity and contextual richness of cloud patterns. Specifically, CloudMatch generates one weakly augmented view along with two complementary strongly augmented views for each unlabeled image: one integrates inter-scene patches to simulate contextual variety, while the other employs intra-scene mixing to preserve semantic coherence. This approach guides pseudolabel generation and enhances generalization. Extensive experiments show that CloudMatch achieves good performance, demonstrating its capability to utilize unlabeled data efficiently and advance semi-supervised cloud detection.

