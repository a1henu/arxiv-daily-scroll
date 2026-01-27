---
layout: default
title: Structural Gender Bias in Credit Scoring: Proxy Leakage
---

# Structural Gender Bias in Credit Scoring: Proxy Leakage
**arXiv**：[2601.18342v1](https://arxiv.org/abs/2601.18342) · [PDF](https://arxiv.org/pdf/2601.18342.pdf)  
**作者**：Navya SD, Sreekanth D, SS Uma Sankari  

**一句话要点**：揭示信用评分中结构性性别偏见，挑战公平性盲视，提出因果建模方法

**关键词**：信用评分, 算法偏见, 公平性审计, SHAP解释, 对抗建模, 金融AI

## 3 点简述
- 核心问题：机器学习信用评估中，移除敏感属性后仍存在结构性性别偏见，传统公平性审计不足。
- 方法要点：使用SHAP识别非敏感特征（如婚姻状况、年龄）作为性别代理，采用对抗逆建模量化泄漏。
- 实验或效果：在台湾信用违约数据集中，从非敏感特征重建性别属性ROC AUC达0.65，证明偏见嵌入模型。

## 摘要（原文）

> As financial institutions increasingly adopt machine learning for credit risk assessment, the persistence of algorithmic bias remains a critical barrier to equitable financial inclusion. This study provides a comprehensive audit of structural gender bias within the Taiwan Credit Default dataset, specifically challenging the prevailing doctrine of "fairness through blindness." Despite the removal of explicit protected attributes and the application of industry standard fairness interventions, our results demonstrate that gendered predictive signals remain deeply embedded within non-sensitive features. Utilizing SHAP (SHapley Additive exPlanations), we identify that variables such as Marital Status, Age, and Credit Limit function as potent proxies for gender, allowing models to maintain discriminatory pathways while appearing statistically fair. To mathematically quantify this leakage, we employ an adversarial inverse modeling framework. Our findings reveal that the protected gender attribute can be reconstructed from purely non-sensitive financial features with an ROC AUC score of 0.65, demonstrating that traditional fairness audits are insufficient for detecting implicit structural bias. These results advocate for a shift from surface-level statistical parity toward causal-aware modeling and structural accountability in financial AI.

