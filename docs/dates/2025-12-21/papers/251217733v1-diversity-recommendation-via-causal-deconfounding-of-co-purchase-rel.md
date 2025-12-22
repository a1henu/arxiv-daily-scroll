---
layout: default
title: Diversity Recommendation via Causal Deconfounding of Co-purchase Relations and Counterfactual Exposure
---

# Diversity Recommendation via Causal Deconfounding of Co-purchase Relations and Counterfactual Exposure
**arXiv**：[2512.17733v1](https://arxiv.org/abs/2512.17733) · [PDF](https://arxiv.org/pdf/2512.17733.pdf)  
**作者**：Jingmao Zhang, Zhiting Zhao, Yunqi Lin, Jianghong Ma, Tianjun Wei, Haijun Zhang, Xiaofeng Zhang  

**一句话要点**：提出Cadence框架，通过因果去混杂和反事实曝光增强推荐多样性

**关键词**：推荐系统, 因果推断, 多样性推荐, 去混杂, 反事实曝光, 物品图

## 3 点简述
- 问题：现有方法依赖共现关系，易受物品流行度和用户属性偏差影响，且多样性研究不足。
- 方法：计算无偏非对称共购关系构建去混杂物品图，并模拟高曝光场景以提升多样性。
- 效果：在真实数据集上，在多样性和准确性上均优于现有模型，验证了有效性和可迁移性。

## 摘要（原文）

> Beyond user-item modeling, item-to-item relationships are increasingly used to enhance recommendation. However, common methods largely rely on co-occurrence, making them prone to item popularity bias and user attributes, which degrades embedding quality and performance. Meanwhile, although diversity is acknowledged as a key aspect of recommendation quality, existing research offers limited attention to it, with a notable lack of causal perspectives and theoretical grounding. To address these challenges, we propose Cadence: Diversity Recommendation via Causal Deconfounding of Co-purchase Relations and Counterfactual Exposure - a plug-and-play framework built upon LightGCN as the backbone, primarily designed to enhance recommendation diversity while preserving accuracy. First, we compute the Unbiased Asymmetric Co-purchase Relationship (UACR) between items - excluding item popularity and user attributes - to construct a deconfounded directed item graph, with an aggregation mechanism to refine embeddings. Second, we leverage UACR to identify diverse categories of items that exhibit strong causal relevance to a user's interacted items but have not yet been engaged with. We then simulate their behavior under high-exposure scenarios, thereby significantly enhancing recommendation diversity while preserving relevance. Extensive experiments on real-world datasets demonstrate that our method consistently outperforms state-of-the-art diversity models in both diversity and accuracy, and further validates its effectiveness, transferability, and efficiency over baselines.

