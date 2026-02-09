---
layout: default
title: Gold Exploration using Representations from a Multispectral Autoencoder
---

# Gold Exploration using Representations from a Multispectral Autoencoder
**arXiv**：[2602.06748v1](https://arxiv.org/abs/2602.06748) · [PDF](https://arxiv.org/pdf/2602.06748.pdf)  
**作者**：Argyro Tsandalidou, Konstantinos Dogeas, Eleftheria Tetoula Tsonga, Elisavet Parselia, Georgios Tsimiklis, George Arvanitakis  

**一句话要点**：提出基于多光谱自编码器表征的金矿勘探框架，利用卫星图像提升识别精度。

**关键词**：金矿勘探, 多光谱图像, 自编码器, 表征学习, 卫星遥感, XGBoost分类

## 3 点简述
- 核心问题：现场矿物勘探数据成本高且有限，需利用卫星图像进行大规模金矿前景测绘。
- 方法要点：使用预训练自编码器Isometric从多光谱Sentinel-2图像学习表征，结合XGBoost分类器识别金矿区域。
- 实验或效果：在63个图像数据集上，patch级准确率从0.51提升至0.68，图像级准确率从0.55提升至0.73。

## 摘要（原文）

> Satellite imagery is employed for large-scale prospectivity mapping due to the high cost and typically limited availability of on-site mineral exploration data. In this work, we present a proof-of-concept framework that leverages generative representations learned from multispectral Sentinel-2 imagery to identify gold-bearing regions from space. An autoencoder foundation model, called Isometric, which is pretrained on the large-scale FalconSpace-S2 v1.0 dataset, produces information-dense spectral-spatial representations that serve as inputs to a lightweight XGBoost classifier. We compare this representation-based approach with a raw spectral input baseline using a dataset of 63 Sentinel-2 images from known gold and non-gold locations. The proposed method improves patch-level accuracy from 0.51 to 0.68 and image-level accuracy from 0.55 to 0.73, demonstrating that generative embeddings capture transferable mineralogical patterns even with limited labeled data. These results highlight the potential of foundation-model representations to make mineral exploration more efficient, scalable, and globally applicable.

