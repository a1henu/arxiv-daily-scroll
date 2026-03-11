---
layout: default
title: No evaluation without fair representation : Impact of label and selection bias on the evaluation, performance and mitigation of classification models
---

# No evaluation without fair representation : Impact of label and selection bias on the evaluation, performance and mitigation of classification models
**arXiv**：[2603.09662v1](https://arxiv.org/abs/2603.09662) · [PDF](https://arxiv.org/pdf/2603.09662.pdf)  
**作者**：Magali Legast, Toon Calders, François Fouss  

**一句话要点**：提出偏置与评估框架，分析标签和选择偏置对分类模型评估与缓解方法的影响

**关键词**：偏置分析, 分类模型评估, 公平机器学习, 标签偏置, 选择偏置, 偏置缓解方法

## 3 点简述
- 核心问题：标签和选择偏置在机器学习数据集中的不同影响被低估，影响模型评估与公平性
- 方法要点：引入偏置与评估框架，在低歧视真实数据中可控引入偏置，独立分析各偏置类型
- 实验或效果：实证显示偏置类型影响模型性能与缓解方法效果，无偏测试集下公平性与准确性无权衡

## 摘要（原文）

> Bias can be introduced in diverse ways in machine learning datasets, for example via selection or label bias. Although these bias types in themselves have an influence on important aspects of fair machine learning, their different impact has been understudied. In this work, we empirically analyze the effect of label bias and several subtypes of selection bias on the evaluation of classification models, on their performance, and on the effectiveness of bias mitigation methods. We also introduce a biasing and evaluation framework that allows to model fair worlds and their biased counterparts through the introduction of controlled bias in real-life datasets with low discrimination. Using our framework, we empirically analyze the impact of each bias type independently, while obtaining a more representative evaluation of models and mitigation methods than with the traditional use of a subset of biased data as test set. Our results highlight different factors that influence how impactful bias is on model performance. They also show an absence of trade-off between fairness and accuracy, and between individual and group fairness, when models are evaluated on a test set that does not exhibit unwanted bias. They furthermore indicate that the performance of bias mitigation methods is influenced by the type of bias present in the data. Our findings call for future work to develop more accurate evaluations of prediction models and fairness interventions, but also to better understand other types of bias, more complex scenarios involving the combination of different bias types, and other factors that impact the efficiency of the mitigation methods, such as dataset characteristics.

