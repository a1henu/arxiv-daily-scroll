---
layout: default
title: Explaining AutoClustering: Uncovering Meta-Feature Contribution in AutoML for Clustering
---

# Explaining AutoClustering: Uncovering Meta-Feature Contribution in AutoML for Clustering
**arXiv**：[2602.18348v1](https://arxiv.org/abs/2602.18348) · [PDF](https://arxiv.org/pdf/2602.18348.pdf)  
**作者**：Matheus Camilo da Silva, Leonardo Arrighi, Ana Carolina Lorena, Sylvio Barbon Junior  

**一句话要点**：研究AutoClustering中元特征贡献的解释性，以提升无监督学习自动化的决策透明度

**关键词**：AutoClustering, 元学习解释性, 元特征分析, SHAP, 无监督学习自动化, 决策透明度

## 3 点简述
- 核心问题：AutoClustering系统推荐难以解释，元特征影响不透明，限制可靠性和改进诊断
- 方法要点：综述22种方法并分类元特征，应用全局和局部解释技术分析元模型特征重要性
- 实验或效果：发现元特征相关性模式，识别当前元学习策略的结构弱点，提供可解释AutoML设计指导

## 摘要（原文）

> AutoClustering methods aim to automate unsupervised learning tasks, including algorithm selection (AS), hyperparameter optimization (HPO), and pipeline synthesis (PS), by often leveraging meta-learning over dataset meta-features. While these systems often achieve strong performance, their recommendations are often difficult to justify: the influence of dataset meta-features on algorithm and hyperparameter choices is typically not exposed, limiting reliability, bias diagnostics, and efficient meta-feature engineering. This limits reliability and diagnostic insight for further improvements. In this work, we investigate the explainability of the meta-models in AutoClustering. We first review 22 existing methods and organize their meta-features into a structured taxonomy. We then apply a global explainability technique (i.e., Decision Predicate Graphs) to assess feature importance within meta-models from selected frameworks. Finally, we use local explainability tools such as SHAP (SHapley Additive exPlanations) to analyse specific clustering decisions. Our findings highlight consistent patterns in meta-feature relevance, identify structural weaknesses in current meta-learning strategies that can distort recommendations, and provide actionable guidance for more interpretable Automated Machine Learning (AutoML) design. This study therefore offers a practical foundation for increasing decision transparency in unsupervised learning automation.

