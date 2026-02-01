---
layout: default
title: Temporal Sepsis Modeling: a Fully Interpretable Relational Way
---

# Temporal Sepsis Modeling: a Fully Interpretable Relational Way
**arXiv**：[2601.21747v1](https://arxiv.org/abs/2601.21747) · [PDF](https://arxiv.org/pdf/2601.21747.pdf)  
**作者**：Vincent Lemaire, Nédra Meloulli, Pierre Jaquet  

**一句话要点**：提出基于关系数据建模的时序脓毒症预测框架，以增强模型可解释性。

**关键词**：脓毒症预测, 关系数据建模, 时序分析, 可解释机器学习, 医疗数据挖掘

## 3 点简述
- 核心问题：脓毒症预测中深度学习模型缺乏可解释性且忽略患者亚表型。
- 方法要点：将时序医疗数据视为关系模式，通过命题化技术构建可解释特征，使用选择性朴素贝叶斯分类器。
- 实验或效果：验证了方法的有效性和极强可解释性，包括单变量、全局、局部和反事实解释。

## 摘要（原文）

> Sepsis remains one of the most complex and heterogeneous syndromes in intensive care, characterized by diverse physiological trajectories and variable responses to treatment. While deep learning models perform well in the early prediction of sepsis, they often lack interpretability and ignore latent patient sub-phenotypes. In this work, we propose a machine learning framework by opening up a new avenue for addressing this issue: a relational approach. Temporal data from electronic medical records (EMRs) are viewed as multivariate patient logs and represented in a relational data schema. Then, a propositionalisation technique (based on classic aggregation/selection functions from the field of relational data) is applied to construct interpretable features to "flatten" the data. Finally, the flattened data is classified using a selective naive Bayesian classifier. Experimental validation demonstrates the relevance of the suggested approach as well as its extreme interpretability. The interpretation is fourfold: univariate, global, local, and counterfactual.

