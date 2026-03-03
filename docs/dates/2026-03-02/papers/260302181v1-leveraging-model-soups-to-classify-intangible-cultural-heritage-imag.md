---
layout: default
title: Leveraging Model Soups to Classify Intangible Cultural Heritage Images from the Mekong Delta
---

# Leveraging Model Soups to Classify Intangible Cultural Heritage Images from the Mekong Delta
**arXiv**：[2603.02181v1](https://arxiv.org/abs/2603.02181) · [PDF](https://arxiv.org/pdf/2603.02181.pdf)  
**作者**：Quoc-Khang Tran, Minh-Thien Nguyen, Nguyen-Khang Pham  

**一句话要点**：提出结合CoAtNet与模型汤的框架，以提升湄公河三角洲非物质文化遗产图像分类的泛化能力。

**关键词**：非物质文化遗产图像分类, 模型汤, CoAtNet, 权重空间集成, 偏差-方差分解, 低资源学习

## 3 点简述
- 针对非物质文化遗产图像分类中数据稀缺、类间相似度高和领域异质性等挑战。
- 采用CoAtNet架构融合卷积与自注意力，并应用贪婪和均匀汤策略进行轻量级权重空间集成。
- 在ICH-17数据集上实现72.36%的top-1准确率，优于ResNet-50等基线模型，并通过偏差-方差分解分析集成效果。

## 摘要（原文）

> The classification of Intangible Cultural Heritage (ICH) images in the Mekong Delta poses unique challenges due to limited annotated data, high visual similarity among classes, and domain heterogeneity. In such low-resource settings, conventional deep learning models often suffer from high variance or overfit to spurious correlations, leading to poor generalization. To address these limitations, we propose a robust framework that integrates the hybrid CoAtNet architecture with model soups, a lightweight weight-space ensembling technique that averages checkpoints from a single training trajectory without increasing inference cost. CoAtNet captures both local and global patterns through stage-wise fusion of convolution and self-attention. We apply two ensembling strategies - greedy and uniform soup - to selectively combine diverse checkpoints into a final model. Beyond performance improvements, we analyze the ensembling effect through the lens of bias-variance decomposition. Our findings show that model soups reduces variance by stabilizing predictions across diverse model snapshots, while introducing minimal additional bias. Furthermore, using cross-entropy-based distance metrics and Multidimensional Scaling (MDS), we show that model soups selects geometrically diverse checkpoints, unlike Soft Voting, which blends redundant models centered in output space. Evaluated on the ICH-17 dataset (7,406 images across 17 classes), our approach achieves state-of-the-art results with 72.36% top-1 accuracy and 69.28% macro F1-score, outperforming strong baselines including ResNet-50, DenseNet-121, and ViT. These results underscore that diversity-aware checkpoint averaging provides a principled and efficient way to reduce variance and enhance generalization in culturally rich, data-scarce classification tasks.

