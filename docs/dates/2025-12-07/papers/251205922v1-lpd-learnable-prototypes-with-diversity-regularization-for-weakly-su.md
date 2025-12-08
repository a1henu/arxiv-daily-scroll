---
layout: default
title: LPD: Learnable Prototypes with Diversity Regularization for Weakly Supervised Histopathology Segmentation
---

# LPD: Learnable Prototypes with Diversity Regularization for Weakly Supervised Histopathology Segmentation
**arXiv**：[2512.05922v1](https://arxiv.org/abs/2512.05922) · [PDF](https://arxiv.org/pdf/2512.05922.pdf)  
**作者**：Khang Le, Anh Mai Vu, Thi Kim Trang Vo, Ha Thach, Ngoc Bui Lam Quang, Thanh-Huy Nguyen, Minh H. N. Le, Zhu Han, Chandra Mohan, Hien Van Nguyen  

**一句话要点**：提出可学习原型与多样性正则化框架，以解决组织病理学弱监督分割中的类内异质性问题。

**关键词**：弱监督语义分割, 组织病理学图像, 可学习原型, 多样性正则化, 单阶段框架, 类内异质性

## 3 点简述
- 核心问题：弱监督组织病理学分割面临类间同质、类内异质和CAM区域收缩，现有两阶段方法效率低且效果受限。
- 方法要点：设计免聚类单阶段框架，通过可学习原型和多样性正则化增强类内形态覆盖，避免超参数敏感。
- 实验或效果：在BCSS-WSSS上实现SOTA性能，mIoU和mDice超越先前方法，分割图边界更清晰且误标减少。

## 摘要（原文）

> Weakly supervised semantic segmentation (WSSS) in histopathology reduces pixel-level labeling by learning from image-level labels, but it is hindered by inter-class homogeneity, intra-class heterogeneity, and CAM-induced region shrinkage (global pooling-based class activation maps whose activations highlight only the most distinctive areas and miss nearby class regions). Recent works address these challenges by constructing a clustering prototype bank and then refining masks in a separate stage; however, such two-stage pipelines are costly, sensitive to hyperparameters, and decouple prototype discovery from segmentation learning, limiting their effectiveness and efficiency. We propose a cluster-free, one-stage learnable-prototype framework with diversity regularization to enhance morphological intra-class heterogeneity coverage. Our approach achieves state-of-the-art (SOTA) performance on BCSS-WSSS, outperforming prior methods in mIoU and mDice. Qualitative segmentation maps show sharper boundaries and fewer mislabels, and activation heatmaps further reveal that, compared with clustering-based prototypes, our learnable prototypes cover more diverse and complementary regions within each class, providing consistent qualitative evidence for their effectiveness.

