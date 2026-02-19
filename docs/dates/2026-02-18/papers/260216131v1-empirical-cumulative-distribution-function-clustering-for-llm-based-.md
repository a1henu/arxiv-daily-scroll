---
layout: default
title: Empirical Cumulative Distribution Function Clustering for LLM-based Agent System Analysis
---

# Empirical Cumulative Distribution Function Clustering for LLM-based Agent System Analysis
**arXiv**：[2602.16131v1](https://arxiv.org/abs/2602.16131) · [PDF](https://arxiv.org/pdf/2602.16131.pdf)  
**作者**：Chihiro Watanabe, Jingyu Sun  

**一句话要点**：提出基于经验累积分布函数的评估框架与聚类方法，以分析LLM代理系统的响应质量分布。

**关键词**：LLM代理评估, 经验累积分布函数, 响应质量分析, 聚类方法, 余弦相似度, k-medoids算法

## 3 点简述
- 核心问题：传统评估方法如多数投票可能掩盖LLM代理响应的质量分布特性。
- 方法要点：使用响应与参考答案余弦相似度的经验累积分布函数进行细粒度评估，并基于距离和k-medoids算法对ECDF聚类。
- 实验或效果：在QA数据集上验证ECDF能区分相似最终精度但不同质量分布的代理设置，聚类揭示温度、人设和问题主题的影响。

## 摘要（原文）

> Large language models (LLMs) are increasingly used as agents to solve complex tasks such as question answering (QA), scientific debate, and software development. A standard evaluation procedure aggregates multiple responses from LLM agents into a single final answer, often via majority voting, and compares it against reference answers. However, this process can obscure the quality and distributional characteristics of the original responses. In this paper, we propose a novel evaluation framework based on the empirical cumulative distribution function (ECDF) of cosine similarities between generated responses and reference answers. This enables a more nuanced assessment of response quality beyond exact match metrics. To analyze the response distributions across different agent configurations, we further introduce a clustering method for ECDFs using their distances and the $k$-medoids algorithm. Our experiments on a QA dataset demonstrate that ECDFs can distinguish between agent settings with similar final accuracies but different quality distributions. The clustering analysis also reveals interpretable group structures in the responses, offering insights into the impact of temperature, persona, and question topics.

