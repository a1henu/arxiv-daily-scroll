---
layout: default
title: MergeRec: Model Merging for Data-Isolated Cross-Domain Sequential Recommendation
---

# MergeRec: Model Merging for Data-Isolated Cross-Domain Sequential Recommendation
**arXiv**：[2601.01753v1](https://arxiv.org/abs/2601.01753) · [PDF](https://arxiv.org/pdf/2601.01753.pdf)  
**作者**：Hyunsoo Kim, Jaewan Moon, Seongmin Park, Jongwuk Lee  

**一句话要点**：提出MergeRec框架，通过模型合并解决数据隔离的跨域序列推荐问题。

**关键词**：跨域序列推荐, 模型合并, 数据隔离, 伪用户数据, 蒸馏损失, 通用推荐系统

## 3 点简述
- 核心问题：跨域推荐中数据隔离限制模型泛化，现有方法依赖重叠数据或忽略隐私约束。
- 方法要点：基于训练无关合并初始化、伪用户数据构建和协同合并优化，合成训练样本并融合推荐与蒸馏损失。
- 实验或效果：在Recall@10指标上平均提升达17.21%，显著增强未见域的泛化能力。

## 摘要（原文）

> Modern recommender systems trained on domain-specific data often struggle to generalize across multiple domains. Cross-domain sequential recommendation has emerged as a promising research direction to address this challenge; however, existing approaches face fundamental limitations, such as reliance on overlapping users or items across domains, or unrealistic assumptions that ignore privacy constraints. In this work, we propose a new framework, MergeRec, based on model merging under a new and realistic problem setting termed data-isolated cross-domain sequential recommendation, where raw user interaction data cannot be shared across domains. MergeRec consists of three key components: (1) merging initialization, (2) pseudo-user data construction, and (3) collaborative merging optimization. First, we initialize a merged model using training-free merging techniques. Next, we construct pseudo-user data by treating each item as a virtual sequence in each domain, enabling the synthesis of meaningful training samples without relying on real user interactions. Finally, we optimize domain-specific merging weights through a joint objective that combines a recommendation loss, which encourages the merged model to identify relevant items, and a distillation loss, which transfers collaborative filtering signals from the fine-tuned source models. Extensive experiments demonstrate that MergeRec not only preserves the strengths of the original models but also significantly enhances generalizability to unseen domains. Compared to conventional model merging methods, MergeRec consistently achieves superior performance, with average improvements of up to 17.21% in Recall@10, highlighting the potential of model merging as a scalable and effective approach for building universal recommender systems. The source code is available at https://github.com/DIALLab-SKKU/MergeRec.

