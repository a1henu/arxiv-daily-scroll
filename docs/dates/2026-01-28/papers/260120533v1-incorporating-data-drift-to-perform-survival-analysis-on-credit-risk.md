---
layout: default
title: Incorporating data drift to perform survival analysis on credit risk
---

# Incorporating data drift to perform survival analysis on credit risk
**arXiv**：[2601.20533v1](https://arxiv.org/abs/2601.20533) · [PDF](https://arxiv.org/pdf/2601.20533.pdf)  
**作者**：Jianwei Peng, Stefan Lessmann  

**一句话要点**：提出动态联合建模框架以提升信用风险生存分析在数据漂移下的鲁棒性

**关键词**：信用风险建模, 生存分析, 数据漂移, 动态联合模型, 抵押贷款数据集

## 3 点简述
- 核心问题：传统生存分析假设数据生成过程平稳，但抵押贷款组合面临多种数据漂移影响。
- 方法要点：集成纵向行为标记与离散时间风险模型，结合地标独热编码和等渗校准。
- 实验或效果：在模拟漂移场景中，模型在区分度和校准上优于经典方法，验证了设计优越性。

## 摘要（原文）

> Survival analysis has become a standard approach for modelling time to default by time-varying covariates in credit risk. Unlike most existing methods that implicitly assume a stationary data-generating process, in practise, mortgage portfolios are exposed to various forms of data drift caused by changing borrower behaviour, macroeconomic conditions, policy regimes and so on. This study investigates the impact of data drift on survival-based credit risk models and proposes a dynamic joint modelling framework to improve robustness under non-stationary environments. The proposed model integrates a longitudinal behavioural marker derived from balance dynamics with a discrete-time hazard formulation, combined with landmark one-hot encoding and isotonic calibration. Three types of data drift (sudden, incremental and recurring) are simulated and analysed on mortgage loan datasets from Freddie Mac. Experiments and corresponding evidence show that the proposed landmark-based joint model consistently outperforms classical survival models, tree-based drift-adaptive learners and gradient boosting methods in terms of discrimination and calibration across all drift scenarios, which confirms the superiority of our model design.

