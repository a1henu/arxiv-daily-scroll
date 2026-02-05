---
layout: default
title: Performative Learning Theory
---

# Performative Learning Theory
**arXiv**：[2602.04402v1](https://arxiv.org/abs/2602.04402) · [PDF](https://arxiv.org/pdf/2602.04402.pdf)  
**作者**：Julian Rodemann, Unai Fischer-Abaigar, James Bailie, Krikamol Muandet  

**一句话要点**：提出表演性学习理论，分析预测影响数据时的泛化界限，应用于失业培训分配案例。

**关键词**：表演性预测, 泛化理论, Wasserstein距离, 学习理论, 统计学习, 案例研究

## 3 点简述
- 研究表演性预测对样本和总体的影响，探讨模型泛化能力。
- 在Wasserstein空间中建立min-max和min-min风险泛函，证明泛化界限。
- 通过德国劳动力市场数据案例，验证理论在失业培训分配中的应用效果。

## 摘要（原文）

> Performative predictions influence the very outcomes they aim to forecast. We study performative predictions that affect a sample (e.g., only existing users of an app) and/or the whole population (e.g., all potential app users). This raises the question of how well models generalize under performativity. For example, how well can we draw insights about new app users based on existing users when both of them react to the app's predictions? We address this question by embedding performative predictions into statistical learning theory. We prove generalization bounds under performative effects on the sample, on the population, and on both. A key intuition behind our proofs is that in the worst case, the population negates predictions, while the sample deceptively fulfills them. We cast such self-negating and self-fulfilling predictions as min-max and min-min risk functionals in Wasserstein space, respectively. Our analysis reveals a fundamental trade-off between performatively changing the world and learning from it: the more a model affects data, the less it can learn from it. Moreover, our analysis results in a surprising insight on how to improve generalization guarantees by retraining on performatively distorted samples. We illustrate our bounds in a case study on prediction-informed assignments of unemployed German residents to job trainings, drawing upon administrative labor market records from 1975 to 2017 in Germany.

