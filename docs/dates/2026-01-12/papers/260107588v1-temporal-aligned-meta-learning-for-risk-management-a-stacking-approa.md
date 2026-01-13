---
layout: default
title: Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring
---

# Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring
**arXiv**：[2601.07588v1](https://arxiv.org/abs/2601.07588) · [PDF](https://arxiv.org/pdf/2601.07588.pdf)  
**作者**：O. Didkovskyi, A. Vidali, N. Jean, G. Le Pera  

**一句话要点**：提出时序对齐元学习框架，通过堆叠方法解决意大利中小企业信用评分中的时间错位问题

**关键词**：信用评分, 元学习, 时序对齐, 堆叠方法, 中小企业风险, 违约概率建模

## 3 点简述
- 核心问题：信用评分模型因财务报表发布日期延迟和异步数据源导致时间错位，影响风险评估准确性。
- 方法要点：采用两步时序分解，先基于静态模型估计年度违约概率，再用高频行为数据建模月度演化，并通过堆叠架构聚合多评分系统。
- 实验或效果：实证验证显示框架能有效捕捉信用风险随时间演化，提升时间一致性和预测稳定性，优于标准集成方法。

## 摘要（原文）

> This paper presents a meta-learning framework for credit risk assessment of Italian Small and Medium Enterprises (SMEs) that explicitly addresses the temporal misalignment of credit scoring models.
>   The approach aligns financial statement reference dates with evaluation dates, mitigating bias arising from publication delays and asynchronous data sources. It is based on a two-step temporal decomposition that at first estimates annual probabilities of default (PDs) anchored to balance-sheet reference dates (December 31st) through a static model. Then it models the monthly evolution of PDs using higher-frequency behavioral data. Finally, we employ stacking-based architecture to aggregate multiple scoring systems, each capturing complementary aspects of default risk, into a unified predictive model. In this way, first level model outputs are treated as learned representations that encode non-linear relationships in financial and behavioral indicators, allowing integration of new expert-based features without retraining base models. This design provides a coherent and interpretable solution to challenges typical of low-default environments, including heterogeneous default definitions and reporting delays. Empirical validation shows that the framework effectively captures credit risk evolution over time, improving temporal consistency and predictive stability relative to standard ensemble methods.

