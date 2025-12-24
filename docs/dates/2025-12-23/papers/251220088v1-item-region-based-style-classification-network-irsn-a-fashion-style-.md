---
layout: default
title: Item Region-based Style Classification Network (IRSN): A Fashion Style Classifier Based on Domain Knowledge of Fashion Experts
---

# Item Region-based Style Classification Network (IRSN): A Fashion Style Classifier Based on Domain Knowledge of Fashion Experts
**arXiv**：[2512.20088v1](https://arxiv.org/abs/2512.20088) · [PDF](https://arxiv.org/pdf/2512.20088.pdf)  
**作者**：Jinyoung Choi, Youngchae Kwon, Injung Kim  

**一句话要点**：提出基于物品区域的风格分类网络（IRSN），通过分析物品特征及其组合来提升时尚风格分类精度。

**关键词**：时尚风格分类, 物品区域分析, 门控特征融合, 双骨干架构, 视觉相似性

## 3 点简述
- 时尚风格分类因类内视觉差异大和类间相似性高而具挑战性。
- IRSN使用物品区域池化和门控特征融合，结合双骨干架构提取全局与物品特征。
- 在多个数据集上，IRSN平均提升分类准确率6.9%-7.6%，最高达15.1%。

## 摘要（原文）

> Fashion style classification is a challenging task because of the large visual variation within the same style and the existence of visually similar styles.
>   Styles are expressed not only by the global appearance, but also by the attributes of individual items and their combinations.
>   In this study, we propose an item region-based fashion style classification network (IRSN) to effectively classify fashion styles by analyzing item-specific features and their combinations in addition to global features.
>   IRSN extracts features of each item region using item region pooling (IRP), analyzes them separately, and combines them using gated feature fusion (GFF).
>   In addition, we improve the feature extractor by applying a dual-backbone architecture that combines a domain-specific feature extractor and a general feature extractor pre-trained with a large-scale image-text dataset.
>   In experiments, applying IRSN to six widely-used backbones, including EfficientNet, ConvNeXt, and Swin Transformer, improved style classification accuracy by an average of 6.9% and a maximum of 14.5% on the FashionStyle14 dataset and by an average of 7.6% and a maximum of 15.1% on the ShowniqV3 dataset. Visualization analysis also supports that the IRSN models are better than the baseline models at capturing differences between similar style classes.

