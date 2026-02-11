---
layout: default
title: Towards Explainable Federated Learning: Understanding the Impact of Differential Privacy
---

# Towards Explainable Federated Learning: Understanding the Impact of Differential Privacy
**arXiv**：[2602.10100v1](https://arxiv.org/abs/2602.10100) · [PDF](https://arxiv.org/pdf/2602.10100.pdf)  
**作者**：Júlio Oliveira, Rodrigo Ferreira, André Riker, Glaucio H. S. Carvalho, Eirini Eleni Tsilopoulou  

**一句话要点**：提出FEXT-DP以结合联邦学习与差分隐私，并分析其对可解释性的影响。

**关键词**：联邦学习, 差分隐私, 可解释人工智能, 决策树, 隐私保护

## 3 点简述
- 核心问题：数据隐私与可解释性在机器学习中需兼顾，但差分隐私可能损害可解释性。
- 方法要点：基于决策树构建联邦学习系统FEXT-DP，并应用差分隐私增强隐私保护。
- 实验或效果：评估显示FEXT-DP在训练速度、均方误差和可解释性方面有改进。

## 摘要（原文）

> Data privacy and eXplainable Artificial Intelligence (XAI) are two important aspects for modern Machine Learning systems. To enhance data privacy, recent machine learning models have been designed as a Federated Learning (FL) system. On top of that, additional privacy layers can be added, via Differential Privacy (DP). On the other hand, to improve explainability, ML must consider more interpretable approaches with reduced number of features and less complex internal architecture. In this context, this paper aims to achieve a machine learning (ML) model that combines enhanced data privacy with explainability. So, we propose a FL solution, called Federated EXplainable Trees with Differential Privacy (FEXT-DP), that: (i) is based on Decision Trees, since they are lightweight and have superior explainability than neural networks-based FL systems; (ii) provides additional layer of data privacy protection applying Differential Privacy (DP) to the Tree-Based model. However, there is a side effect adding DP: it harms the explainability of the system. So, this paper also presents the impact of DP protection on the explainability of the ML model. The carried out performance assessment shows improvements of FEXT-DP in terms of a faster training, i.e., numbers of rounds, Mean Squared Error and explainability.

