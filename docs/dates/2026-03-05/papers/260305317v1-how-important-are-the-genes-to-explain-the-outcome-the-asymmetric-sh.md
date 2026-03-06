---
layout: default
title: How important are the genes to explain the outcome - the asymmetric Shapley value as an honest importance metric for high-dimensional features
---

# How important are the genes to explain the outcome - the asymmetric Shapley value as an honest importance metric for high-dimensional features
**arXiv**：[2603.05317v1](https://arxiv.org/abs/2603.05317) · [PDF](https://arxiv.org/pdf/2603.05317.pdf)  
**作者**：Mark A. van de Wiel, Jeroen Goedhart, Martin Jullum, Kjersti Aas  

**一句话要点**：提出非对称Shapley值作为高维特征重要性度量，用于临床预测模型

**关键词**：特征重要性, 非对称Shapley值, 临床预测, 高维特征, 可解释性

## 3 点简述
- 核心问题：传统方法评估高维特征重要性时忽略共线性和依赖方向性
- 方法要点：引入非对称Shapley值，量化混合维度模型中特征贡献
- 实验或效果：应用于结直肠癌无进展生存期预测，提供局部和全局解释

## 摘要（原文）

> In clinical prediction settings the importance of a high-dimensional feature like genomics is often assessed by evaluating the change in predictive performance when adding it to a set of traditional clinical variables. This approach is questionable, because it does not account for collinearity nor known directionality of dependencies between variables. We suggest to use asymmetric Shapley values as a more suitable alternative to quantify feature importance in the context of a mixed-dimensional prediction model. We focus on a setting that is particularly relevant in clinical prediction: disease state as a mediating variable for genomic effects, with additional confounders for which the direction of effects may be unknown. We derive efficient algorithms to compute local and global asymmetric Shapley values for this setting. The former are shown to be very useful for inference, whereas the latter provide interpretation by decomposing any predictive performance metric into contributions of the features. Throughout, we illustrate our framework by a leading example: the prediction of progression-free survival for colorectal cancer patients.

