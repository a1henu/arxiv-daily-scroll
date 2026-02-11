---
layout: default
title: Linear Model Extraction via Factual and Counterfactual Queries
---

# Linear Model Extraction via Factual and Counterfactual Queries
**arXiv**：[2602.09748v1](https://arxiv.org/abs/2602.09748) · [PDF](https://arxiv.org/pdf/2602.09748.pdf)  
**作者**：Daan Otto, Jannis Kurtz, Dick den Hertog, Ilker Birbil  

**一句话要点**：提出基于事实与反事实查询的线性模型提取方法，分析查询数量与距离函数对模型安全性的影响。

**关键词**：模型提取攻击, 线性模型, 反事实查询, 距离函数, 安全性分析

## 3 点简述
- 研究模型提取攻击，结合事实与反事实查询揭示黑盒线性模型参数。
- 推导查询已知决策的分类区域数学公式，无需恢复模型参数。
- 分析不同距离函数下反事实查询所需数量，显示单次查询可提取完整模型。

## 摘要（原文）

> In model extraction attacks, the goal is to reveal the parameters of a black-box machine learning model by querying the model for a selected set of data points. Due to an increasing demand for explanations, this may involve counterfactual queries besides the typically considered factual queries. In this work, we consider linear models and three types of queries: factual, counterfactual, and robust counterfactual. First, for an arbitrary set of queries, we derive novel mathematical formulations for the classification regions for which the decision of the unknown model is known, without recovering any of the model parameters. Second, we derive bounds on the number of queries needed to extract the model's parameters for (robust) counterfactual queries under arbitrary norm-based distances. We show that the full model can be recovered using just a single counterfactual query when differentiable distance measures are employed. In contrast, when using polyhedral distances for instance, the number of required queries grows linearly with the dimension of the data space. For robust counterfactuals, the latter number of queries doubles. Consequently, the applied distance function and robustness of counterfactuals have a significant impact on the model's security.

