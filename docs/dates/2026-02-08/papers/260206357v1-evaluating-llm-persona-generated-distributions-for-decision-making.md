---
layout: default
title: Evaluating LLM-persona Generated Distributions for Decision-making
---

# Evaluating LLM-persona Generated Distributions for Decision-making
**arXiv**：[2602.06357v1](https://arxiv.org/abs/2602.06357) · [PDF](https://arxiv.org/pdf/2602.06357.pdf)  
**作者**：Jackie Baek, Yunhan Chen, Ziyu Chi, Will Ma  

**一句话要点**：提出基于决策质量的评估指标，验证LLM生成分布在低数据场景下的实用性。

**关键词**：LLM生成分布, 决策评估, 低数据场景, 定价优化, 分布质量

## 3 点简述
- 核心问题：评估LLM生成分布对下游决策的支持效果，如定价优化。
- 方法要点：引入LLM-SAA方法，通过决策诱导指标替代传统分布距离度量。
- 实验或效果：在选品、定价和报童问题中，LLM分布在低数据场景下表现实用。

## 摘要（原文）

> LLMs can generate a wealth of data, ranging from simulated personas imitating human valuations and preferences, to demand forecasts based on world knowledge. But how well do such LLM-generated distributions support downstream decision-making? For example, when pricing a new product, a firm could prompt an LLM to simulate how much consumers are willing to pay based on a product description, but how useful is the resulting distribution for optimizing the price? We refer to this approach as LLM-SAA, in which an LLM is used to construct an estimated distribution and the decision is then optimized under that distribution. In this paper, we study metrics to evaluate the quality of these LLM-generated distributions, based on the decisions they induce. Taking three canonical decision-making problems (assortment optimization, pricing, and newsvendor) as examples, we find that LLM-generated distributions are practically useful, especially in low-data regimes. We also show that decision-agnostic metrics such as Wasserstein distance can be misleading when evaluating these distributions for decision-making.

