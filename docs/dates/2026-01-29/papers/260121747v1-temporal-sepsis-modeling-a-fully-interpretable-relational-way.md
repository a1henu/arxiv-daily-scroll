---
layout: default
title: Temporal Sepsis Modeling: a Fully Interpretable Relational Way
---

# Temporal Sepsis Modeling: a Fully Interpretable Relational Way
**arXiv**：[2601.21747v1](https://arxiv.org/abs/2601.21747) · [PDF](https://arxiv.org/pdf/2601.21747.pdf)  
**作者**：Vincent Lemaire, Nédra Meloulli, Pierre Jaquet  

**一句话要点**：提出基于关系数据建模的败血症时序预测框架，以提升模型可解释性。

**关键词**：败血症预测, 时序数据建模, 关系数据, 可解释机器学习, 命题化, 朴素贝叶斯分类

## 3 点简述
- 败血症预测中深度学习模型可解释性差且忽略患者亚型。
- 采用关系数据模式表示时序数据，通过命题化构建可解释特征。
- 实验验证了方法的有效性和四重可解释性（单变量、全局、局部、反事实）。

## 摘要（原文）

> Sepsis remains one of the most complex and heterogeneous syndromes in intensive care, characterized by diverse physiological trajectories and variable responses to treatment. While deep learning models perform well in the early prediction of sepsis, they often lack interpretability and ignore latent patient sub-phenotypes. In this work, we propose a machine learning framework by opening up a new avenue for addressing this issue: a relational approach. Temporal data from electronic medical records (EMRs) are viewed as multivariate patient logs and represented in a relational data schema. Then, a propositionalisation technique (based on classic aggregation/selection functions from the field of relational data) is applied to construct interpretable features to "flatten" the data. Finally, the flattened data is classified using a selective naive Bayesian classifier. Experimental validation demonstrates the relevance of the suggested approach as well as its extreme interpretability. The interpretation is fourfold: univariate, global, local, and counterfactual.

