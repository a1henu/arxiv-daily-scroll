---
layout: default
title: Active Learning for Planet Habitability Classification under Extreme Class Imbalance
---

# Active Learning for Planet Habitability Classification under Extreme Class Imbalance
**arXiv**：[2602.23666v1](https://arxiv.org/abs/2602.23666) · [PDF](https://arxiv.org/pdf/2602.23666.pdf)  
**作者**：R. I. El-Kholy, Z. M. Hayman  

**一句话要点**：提出基于主动学习的行星宜居性分类方法，以解决极端类别不平衡下的标签效率问题。

**关键词**：主动学习, 行星宜居性分类, 类别不平衡, 梯度提升决策树, 不确定性采样, 系外行星数据集

## 3 点简述
- 核心问题：系外行星目录规模增大且异质性高，宜居行星极端稀缺，标签不完整，导致系统评估困难。
- 方法要点：构建统一数据集，建立基于梯度提升决策树的监督基线，并嵌入基于不确定性的主动学习框架进行查询优化。
- 实验或效果：主动学习显著减少所需标签实例数量，接近监督性能，并通过集成模型识别出单个候选行星用于后续研究。

## 摘要（原文）

> The increasing size and heterogeneity of exoplanet catalogs have made systematic habitability assessment challenging, particularly given the extreme scarcity of potentially habitable planets and the evolving nature of their labels. In this study, we explore the use of pool-based active learning to improve the efficiency of habitability classification under realistic observational constraints. We construct a unified dataset from the Habitable World Catalog and the NASA Exoplanet Archive and formulate habitability assessment as a binary classification problem. A supervised baseline based on gradient-boosted decision trees is established and optimized for recall in order to prioritize the identification of rare potentially habitable planets. This model is then embedded within an active learning framework, where uncertainty-based margin sampling is compared against random querying across multiple runs and labeling budgets. We find that active learning substantially reduces the number of labeled instances required to approach supervised performance, demonstrating clear gains in label efficiency. To connect these results to a practical astronomical use case, we aggregate predictions from independently trained active-learning models into an ensemble and use the resulting mean probabilities and uncertainties to rank planets originally labeled as non-habitable. This procedure identifies a single robust candidate for further study, illustrating how active learning can support conservative, uncertainty-aware prioritization of follow-up targets rather than speculative reclassification. Our results indicate that active learning provides a principled framework for guiding habitability studies in data regimes characterized by label imbalance, incomplete information, and limited observational resources.

