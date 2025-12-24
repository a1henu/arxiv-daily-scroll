---
layout: default
title: Machine Learning to Predict Digital Frustration from Clickstream Data
---

# Machine Learning to Predict Digital Frustration from Clickstream Data
**arXiv**：[2512.20438v1](https://arxiv.org/abs/2512.20438) · [PDF](https://arxiv.org/pdf/2512.20438.pdf)  
**作者**：Jibin Joseph  

**一句话要点**：提出基于点击流数据的机器学习方法，预测电子商务会话中的用户挫败感。

**关键词**：点击流分析, 用户挫败感预测, LSTM分类器, 电子商务会话, 机器学习应用

## 3 点简述
- 核心问题：用户在使用移动应用或网站时产生的挫败感可能导致销售损失和投诉，需从点击流数据中自动识别。
- 方法要点：定义挫败感规则（如愤怒爆发、来回导航），构建表格特征训练XGBoost，并使用事件序列训练LSTM分类器。
- 实验效果：LSTM模型表现最佳，准确率约91%，ROC AUC达0.9705，且仅需前20-30次交互即可可靠预测。

## 摘要（原文）

> Many businesses depend on their mobile apps and websites, so user frustration while trying to complete a task on these channels can cause lost sales and complaints. In this research, I use clickstream data from a real e-commerce site to predict whether a session is frustrated or not. Frustration is defined using certain rules based on rage bursts, back and forth navigation (U turns), cart churn, search struggle, and long wandering sessions, and applies these rules to 5.4 million raw clickstream events (304,881 sessions). From each session, I build tabular features and train standard classifier models. I also use the full event sequence to train a discriminative LSTM classifier. XGBoost reaches about 90% accuracy, ROC AUC of 0.9579, while the LSTM performs best with about 91% accuracy and a ROC AUC of 0.9705. Finally, the research shows that with only the first 20 to 30 interactions, the LSTM already predicts frustration reliably.

