---
layout: default
title: GenZ: Foundational models as latent variable generators within traditional statistical models
---

# GenZ: Foundational models as latent variable generators within traditional statistical models
**arXiv**：[2512.24834v1](https://arxiv.org/abs/2512.24834) · [PDF](https://arxiv.org/pdf/2512.24834.pdf)  
**作者**：Marko Jojic, Nebojsa Jojic  

**一句话要点**：提出GenZ模型，通过可解释语义特征桥接基础模型与传统统计模型，应用于房价预测和电影推荐场景。

**关键词**：语义特征发现, 广义EM算法, 混合建模, 房价预测, 协同过滤, 可解释性

## 3 点简述
- 核心问题：基础模型难以捕获数据集特定模式，影响预测任务准确性。
- 方法要点：采用广义EM算法，迭代发现语义特征描述符，并优化统计模型参数。
- 实验效果：在房价预测中显著优于GPT-5基线，电影推荐中仅凭语义描述匹配传统协同过滤性能。

## 摘要（原文）

> We present GenZ, a hybrid model that bridges foundational models and statistical modeling through interpretable semantic features. While large language models possess broad domain knowledge, they often fail to capture dataset-specific patterns critical for prediction tasks. Our approach addresses this by discovering semantic feature descriptions through an iterative process that contrasts groups of items identified via statistical modeling errors, rather than relying solely on the foundational model's domain understanding. We formulate this as a generalized EM algorithm that jointly optimizes semantic feature descriptors and statistical model parameters. The method prompts a frozen foundational model to classify items based on discovered features, treating these judgments as noisy observations of latent binary features that predict real-valued targets through learned statistical relationships. We demonstrate the approach on two domains: house price prediction (hedonic regression) and cold-start collaborative filtering for movie recommendations. On house prices, our model achieves 12\% median relative error using discovered semantic features from multimodal listing data, substantially outperforming a GPT-5 baseline (38\% error) that relies on the LLM's general domain knowledge. For Netflix movie embeddings, our model predicts collaborative filtering representations with 0.59 cosine similarity purely from semantic descriptions -- matching the performance that would require approximately 4000 user ratings through traditional collaborative filtering. The discovered features reveal dataset-specific patterns (e.g., architectural details predicting local housing markets, franchise membership predicting user preferences) that diverge from the model's domain knowledge alone.

