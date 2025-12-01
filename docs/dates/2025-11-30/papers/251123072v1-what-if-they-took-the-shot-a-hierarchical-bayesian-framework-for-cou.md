---
layout: default
title: What If They Took the Shot? A Hierarchical Bayesian Framework for Counterfactual Expected Goals
---

# What If They Took the Shot? A Hierarchical Bayesian Framework for Counterfactual Expected Goals
**arXiv**：[2511.23072v1](https://arxiv.org/abs/2511.23072) · [PDF](https://arxiv.org/pdf/2511.23072.pdf)  
**作者**：Mikayil Mahmudlu, Oktay Karakuş, Hasan Arkadaş  

**一句话要点**：提出分层贝叶斯框架以量化球员特异性效应，解决预期进球估计中球员同质化问题。

**关键词**：分层贝叶斯模型, 预期进球估计, 球员特异性效应, 反事实分析, 足球数据分析

## 3 点简述
- 核心问题：标准预期进球模型忽略球员个体差异，导致估计偏差。
- 方法要点：结合贝叶斯逻辑回归与专家先验，构建分层模型稳定球员级估计。
- 实验或效果：模型减少后验不确定性，外部验证R2达0.833，支持反事实分析。

## 摘要（原文）

> This study develops a hierarchical Bayesian framework that integrates expert domain knowledge to quantify player-specific effects in expected goals (xG) estimation, addressing a limitation of standard models that treat all players as identical finishers. Using 9,970 shots from StatsBomb's 2015-16 data and Football Manager 2017 ratings, we combine Bayesian logistic regression with informed priors to stabilise player-level estimates, especially for players with few shots. The hierarchical model reduces posterior uncertainty relative to weak priors and achieves strong external validity: hierarchical and baseline predictions correlate at R2 = 0.75, while an XGBoost benchmark validated against StatsBomb xG reaches R2 = 0.833. The model uncovers interpretable specialisation profiles, including one-on-one finishing (Aguero, Suarez, Belotti, Immobile, Martial), long-range shooting (Pogba), and first-touch execution (Insigne, Salah, Gameiro). It also identifies latent ability in underperforming players such as Immobile and Belotti. The framework supports counterfactual "what-if" analysis by reallocating shots between players under identical contexts. Case studies show that Sansone would generate +2.2 xG from Berardi's chances, driven largely by high-pressure situations, while Vardy-Giroud substitutions reveal strong asymmetry: replacing Vardy with Giroud results in a large decline (about -7 xG), whereas the reverse substitution has only a small effect (about -1 xG). This work provides an uncertainty-aware tool for player evaluation, recruitment, and tactical planning, and offers a general approach for domains where individual skill and contextual factors jointly shape performance.

