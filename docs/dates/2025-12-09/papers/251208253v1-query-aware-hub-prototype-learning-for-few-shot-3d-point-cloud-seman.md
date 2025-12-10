---
layout: default
title: Query-aware Hub Prototype Learning for Few-Shot 3D Point Cloud Semantic Segmentation
---

# Query-aware Hub Prototype Learning for Few-Shot 3D Point Cloud Semantic Segmentation
**arXiv**：[2512.08253v1](https://arxiv.org/abs/2512.08253) · [PDF](https://arxiv.org/pdf/2512.08253.pdf)  
**作者**：YiLin Zhou, Lili Wei, Zheming Xu, Ziyi Chen, Congyan Lang  

**一句话要点**：提出查询感知枢纽原型学习方法，以解决少样本三维点云语义分割中的原型偏差问题。

**关键词**：少样本学习, 三维点云语义分割, 原型学习, 查询感知, 枢纽原型, 对比损失

## 3 点简述
- 核心问题：现有基于度量的原型学习方法仅从支持集生成原型，忽略查询数据相关性，导致原型偏差和性能下降。
- 方法要点：通过枢纽原型生成模块构建二分图识别支持枢纽，生成查询相关原型；原型分布优化模块使用纯度加权对比损失优化原型表示。
- 实验或效果：在S3DIS和ScanNet数据集上实验显示，QHP方法显著超越现有方法，有效缩小原型与查询集间的语义差距。

## 摘要（原文）

> Few-shot 3D point cloud semantic segmentation (FS-3DSeg) aims to segment novel classes with only a few labeled samples. However, existing metric-based prototype learning methods generate prototypes solely from the support set, without considering their relevance to query data. This often results in prototype bias, where prototypes overfit support-specific characteristics and fail to generalize to the query distribution, especially in the presence of distribution shifts, which leads to degraded segmentation performance. To address this issue, we propose a novel Query-aware Hub Prototype (QHP) learning method that explicitly models semantic correlations between support and query sets. Specifically, we propose a Hub Prototype Generation (HPG) module that constructs a bipartite graph connecting query and support points, identifies frequently linked support hubs, and generates query-relevant prototypes that better capture cross-set semantics. To further mitigate the influence of bad hubs and ambiguous prototypes near class boundaries, we introduce a Prototype Distribution Optimization (PDO) module, which employs a purity-reweighted contrastive loss to refine prototype representations by pulling bad hubs and outlier prototypes closer to their corresponding class centers. Extensive experiments on S3DIS and ScanNet demonstrate that QHP achieves substantial performance gains over state-of-the-art methods, effectively narrowing the semantic gap between prototypes and query sets in FS-3DSeg.

