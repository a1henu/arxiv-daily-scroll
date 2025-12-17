---
layout: default
title: Hybrid Ensemble Method for Detecting Cyber-Attacks in Water Distribution Systems Using the BATADAL Dataset
---

# Hybrid Ensemble Method for Detecting Cyber-Attacks in Water Distribution Systems Using the BATADAL Dataset
**arXiv**：[2512.14422v1](https://arxiv.org/abs/2512.14422) · [PDF](https://arxiv.org/pdf/2512.14422.pdf)  
**作者**：Waqas Ahmed  

**一句话要点**：提出混合集成方法以检测供水系统中的网络攻击，利用BATADAL数据集提升检测能力。

**关键词**：网络攻击检测, 混合集成学习, BATADAL数据集, 时间序列分析, 类别不平衡处理

## 3 点简述
- 核心问题：BATADAL数据集存在类别不平衡、多变量时间依赖和隐蔽攻击等挑战。
- 方法要点：结合随机森林、XGBoost和LSTM，采用平均和堆叠集成，使用SMOTE处理不平衡。
- 实验或效果：混合堆叠集成在攻击类上F1=0.7205，AUC=0.9826，表现最佳。

## 摘要（原文）

> The cybersecurity of Industrial Control Systems that manage critical infrastructure such as Water Distribution Systems has become increasingly important as digital connectivity expands. BATADAL benchmark data is a good source of testing intrusion detection techniques, but it presents several important problems, such as imbalance in the number of classes, multivariate time dependence, and stealthy attacks. We consider a hybrid ensemble learning model that will enhance the detection ability of cyber-attacks in WDS by using the complementary capabilities of machine learning and deep learning models. Three base learners, namely, Random Forest , eXtreme Gradient Boosting , and Long Short-Term Memory network, have been strictly compared and seven ensemble types using simple averaged and stacked learning with a logistic regression meta-learner. Random Forest analysis identified top predictors turned into temporal and statistical features, and Synthetic Minority Oversampling Technique (SMOTE) was used to overcome the class imbalance issue. The analyics indicates that the single Long Short-Term Memory network model is of poor performance (F1 = 0.000, AUC = 0.4460), but tree-based models, especially eXtreme Gradient Boosting, perform well (F1 = 0.7470, AUC=0.9684). The hybrid stacked ensemble of Random Forest , eXtreme Gradient Boosting , and Long Short-Term Memory network scored the highest, with the attack class of 0.7205 with an F1-score and a AUC of 0.9826 indicating that the heterogeneous stacking between model precision and generalization can work. The proposed framework establishes a robust and scalable solution for cyber-attack detection in time-dependent industrial systems, integrating temporal learning and ensemble diversity to support the secure operation of critical infrastructure.

