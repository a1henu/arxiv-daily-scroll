---
layout: default
title: Counterfactual Fairness with Graph Uncertainty
---

# Counterfactual Fairness with Graph Uncertainty
**arXiv**：[2601.03203v1](https://arxiv.org/abs/2601.03203) · [PDF](https://arxiv.org/pdf/2601.03203.pdf)  
**作者**：Davi Valério, Chrysoula Zerva, Mariana Pinto, Ricardo Santos, André Carreiro  

**一句话要点**：提出CF-GU以在因果图不确定场景下评估机器学习模型偏差

**关键词**：反事实公平性, 因果图不确定性, 偏差评估, 因果发现, 机器学习审计

## 3 点简述
- 核心问题：反事实公平性审计依赖单一因果图，但真实场景中因果图常不确定。
- 方法要点：通过因果发现算法生成多个有向无环图，用香农熵量化图不确定性，提供置信区间。
- 实验效果：在合成和真实数据上验证，能高置信度识别已知偏差，支持不同领域知识假设下的审计。

## 摘要（原文）

> Evaluating machine learning (ML) model bias is key to building trustworthy and robust ML systems. Counterfactual Fairness (CF) audits allow the measurement of bias of ML models with a causal framework, yet their conclusions rely on a single causal graph that is rarely known with certainty in real-world scenarios. We propose CF with Graph Uncertainty (CF-GU), a bias evaluation procedure that incorporates the uncertainty of specifying a causal graph into CF. CF-GU (i) bootstraps a Causal Discovery algorithm under domain knowledge constraints to produce a bag of plausible Directed Acyclic Graphs (DAGs), (ii) quantifies graph uncertainty with the normalized Shannon entropy, and (iii) provides confidence bounds on CF metrics. Experiments on synthetic data show how contrasting domain knowledge assumptions support or refute audits of CF, while experiments on real-world data (COMPAS and Adult datasets) pinpoint well-known biases with high confidence, even when supplied with minimal domain knowledge constraints.

