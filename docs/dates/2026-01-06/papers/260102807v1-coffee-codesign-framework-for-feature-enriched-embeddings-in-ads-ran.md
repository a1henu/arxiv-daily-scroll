---
layout: default
title: COFFEE: COdesign Framework for Feature Enriched Embeddings in Ads-Ranking Systems
---

# COFFEE: COdesign Framework for Feature Enriched Embeddings in Ads-Ranking Systems
**arXiv**：[2601.02807v1](https://arxiv.org/abs/2601.02807) · [PDF](https://arxiv.org/pdf/2601.02807.pdf)  
**作者**：Sohini Roychowdhury, Doris Wang, Qian Ge, Joy Mu, Srihari Reddy  

**一句话要点**：提出COFFEE框架以增强广告排序系统中的用户-广告表示，通过多源数据融合提升预测性能。

**关键词**：广告排序系统, 用户表示增强, 多源数据融合, 序列建模, 点击率预测, 缩放定律

## 3 点简述
- 核心问题：广告推荐系统需整合多样数据源以准确评估用户兴趣，但现有方法在表示新鲜度和复杂性上受限。
- 方法要点：设计三维框架，包括事件源多样性、用户历史长度和数据属性增强，不增加推理复杂度。
- 实验或效果：相比有机来源，广告曝光源AUC提升1.56-2倍，CTR预测AUC提高0.56%，优化序列缩放分辨率。

## 摘要（原文）

> Diverse and enriched data sources are essential for commercial ads-recommendation models to accurately assess user interest both before and after engagement with content. While extended user-engagement histories can improve the prediction of user interests, it is equally important to embed activity sequences from multiple sources to ensure freshness of user and ad-representations, following scaling law principles. In this paper, we present a novel three-dimensional framework for enhancing user-ad representations without increasing model inference or serving complexity. The first dimension examines the impact of incorporating diverse event sources, the second considers the benefits of longer user histories, and the third focuses on enriching data with additional event attributes and multi-modal embeddings. We assess the return on investment (ROI) of our source enrichment framework by comparing organic user engagement sources, such as content viewing, with ad-impression sources. The proposed method can boost the area under curve (AUC) and the slope of scaling curves for ad-impression sources by 1.56 to 2 times compared to organic usage sources even for short online-sequence lengths of 100 to 10K. Additionally, click-through rate (CTR) prediction improves by 0.56% AUC over the baseline production ad-recommendation system when using enriched ad-impression event sources, leading to improved sequence scaling resolutions for longer and offline user-ad representations.

