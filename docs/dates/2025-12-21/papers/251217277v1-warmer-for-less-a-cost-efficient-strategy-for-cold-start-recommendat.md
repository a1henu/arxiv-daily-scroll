---
layout: default
title: Warmer for Less: A Cost-Efficient Strategy for Cold-Start Recommendations at Pinterest
---

# Warmer for Less: A Cost-Efficient Strategy for Cold-Start Recommendations at Pinterest
**arXiv**：[2512.17277v1](https://arxiv.org/abs/2512.17277) · [PDF](https://arxiv.org/pdf/2512.17277.pdf)  
**作者**：Saeed Ebrahimi, Weijie Jiang, Jaewon Yang, Olafur Gudmundsson, Yucheng Tu, Huizhong Duan  

**一句话要点**：提出轻量级策略以解决Pinterest冷启动推荐的成本效率问题

**关键词**：冷启动推荐, 工业级推荐系统, 成本效率优化, 特征增强, 分数正则化, 数据稀疏性处理

## 3 点简述
- 核心问题：冷启动物品在工业级推荐系统中面临计算约束、特征重要性低、预测分数偏差和标签稀疏性挑战。
- 方法要点：采用残差连接提升非历史特征重要性，引入分数正则化调整预测偏差，应用流形混合缓解数据稀疏性，整体参数仅增5%。
- 实验或效果：部署后提升新鲜内容参与度10%，不影响整体参与度和成本，服务超5.7亿用户。

## 摘要（原文）

> Pinterest is a leading visual discovery platform where recommender systems (RecSys) are key to delivering relevant, engaging, and fresh content to our users. In this paper, we study the problem of improving RecSys model predictions for cold-start (CS) items, which appear infrequently in the training data. Although this problem is well-studied in academia, few studies have addressed its root causes effectively at the scale of a platform like Pinterest. By investigating live traffic data, we identified several challenges of the CS problem and developed a corresponding solution for each: First, industrial-scale RecSys models must operate under tight computational constraints. Since CS items are a minority, any related improvements must be highly cost-efficient. To address this, our solutions were designed to be lightweight, collectively increasing the total parameters by only 5%. Second, CS items are represented only by non-historical (e.g., content or attribute) features, which models often treat as less important. To elevate their significance, we introduce a residual connection for the non-historical features. Third, CS items tend to receive lower prediction scores compared to non-CS items, reducing their likelihood of being surfaced. We mitigate this by incorporating a score regularization term into the model. Fourth, the labels associated with CS items are sparse, making it difficult for the model to learn from them. We apply the manifold mixup technique to address this data sparsity. Implemented together, our methods increased fresh content engagement at Pinterest by 10% without negatively impacting overall engagement and cost, and have been deployed to serve over 570 million users on Pinterest.

