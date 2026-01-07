---
layout: default
title: Domain Generalization for Time Series: Enhancing Drilling Regression Models for Stick-Slip Index Prediction
---

# Domain Generalization for Time Series: Enhancing Drilling Regression Models for Stick-Slip Index Prediction
**arXiv**：[2601.02884v1](https://arxiv.org/abs/2601.02884) · [PDF](https://arxiv.org/pdf/2601.02884.pdf)  
**作者**：Hana Yahia, Bruno Figliuzzi, Florent Di Meglio, Laurent Gerbaud, Stephane Menand, Mohamed Mahjoub  

**一句话要点**：比较对抗域泛化与不变风险最小化方法，提升钻井时间序列回归模型在未知井的粘滑指数预测泛化能力

**关键词**：时间序列分析, 域泛化, 钻井工程, 回归模型, 对抗训练, 不变风险最小化

## 3 点简述
- 核心问题：钻井时间序列数据存在域偏移，模型在训练井上表现良好，但在未知井上泛化能力不足，影响粘滑指数预测准确性。
- 方法要点：采用对抗域泛化（ADG）和不变风险最小化（IRM）技术，结合网格搜索优化超参数，并评估迁移学习（TL）对性能的改进效果。
- 实验或效果：ADG和IRM模型相比基线分别提升10%和8%性能，严重事件检测率从20%提高到60%，ADG略优于IRM，迁移学习进一步改善结果。

## 摘要（原文）

> This paper provides a comprehensive comparison of domain generalization techniques applied to time series data within a drilling context, focusing on the prediction of a continuous Stick-Slip Index (SSI), a critical metric for assessing torsional downhole vibrations at the drill bit. The study aims to develop a robust regression model that can generalize across domains by training on 60 second labeled sequences of 1 Hz surface drilling data to predict the SSI. The model is tested in wells that are different from those used during training. To fine-tune the model architecture, a grid search approach is employed to optimize key hyperparameters. A comparative analysis of the Adversarial Domain Generalization (ADG), Invariant Risk Minimization (IRM) and baseline models is presented, along with an evaluation of the effectiveness of transfer learning (TL) in improving model performance. The ADG and IRM models achieve performance improvements of 10% and 8%, respectively, over the baseline model. Most importantly, severe events are detected 60% of the time, against 20% for the baseline model. Overall, the results indicate that both ADG and IRM models surpass the baseline, with the ADG model exhibiting a slight advantage over the IRM model. Additionally, applying TL to a pre-trained model further improves performance. Our findings demonstrate the potential of domain generalization approaches in drilling applications, with ADG emerging as the most effective approach.

