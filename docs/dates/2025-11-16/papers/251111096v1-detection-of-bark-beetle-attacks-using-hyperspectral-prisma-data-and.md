---
layout: default
title: Detection of Bark Beetle Attacks using Hyperspectral PRISMA Data and Few-Shot Learning
---

# Detection of Bark Beetle Attacks using Hyperspectral PRISMA Data and Few-Shot Learning
**arXiv**：[2511.11096v1](https://arxiv.org/abs/2511.11096) · [PDF](https://arxiv.org/pdf/2511.11096.pdf)  
**作者**：Mattia Ferrari, Giancarlo Papitto, Giorgio Deligios, Lorenzo Bruzzone  

**一句话要点**：提出基于对比学习和少样本学习的PRISMA高光谱数据方法以检测树皮甲虫侵害

**关键词**：高光谱遥感, 少样本学习, 对比学习, 树皮甲虫检测, 森林健康监测

## 3 点简述
- 核心问题：树皮甲虫侵害威胁针叶林健康，需高效监测方法。
- 方法要点：使用对比学习预训练一维CNN编码器，提取高光谱特征后结合支持向量回归。
- 实验或效果：在Dolomites地区实验，优于PRISMA原始波段和Sentinel-2数据。

## 摘要（原文）

> Bark beetle infestations represent a serious challenge for maintaining the health of coniferous forests. This paper proposes a few-shot learning approach leveraging contrastive learning to detect bark beetle infestations using satellite PRISMA hyperspectral data. The methodology is based on a contrastive learning framework to pre-train a one-dimensional CNN encoder, enabling the extraction of robust feature representations from hyperspectral data. These extracted features are subsequently utilized as input to support vector regression estimators, one for each class, trained on few labeled samples to estimate the proportions of healthy, attacked by bark beetle, and dead trees for each pixel. Experiments on the area of study in the Dolomites show that our method outperforms the use of original PRISMA spectral bands and of Sentinel-2 data. The results indicate that PRISMA hyperspectral data combined with few-shot learning offers significant advantages for forest health monitoring.

