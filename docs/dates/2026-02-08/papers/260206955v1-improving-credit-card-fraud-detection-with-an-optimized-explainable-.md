---
layout: default
title: Improving Credit Card Fraud Detection with an Optimized Explainable Boosting Machine
---

# Improving Credit Card Fraud Detection with an Optimized Explainable Boosting Machine
**arXiv**：[2602.06955v1](https://arxiv.org/abs/2602.06955) · [PDF](https://arxiv.org/pdf/2602.06955.pdf)  
**作者**：Reza E. Fazel, Arash Bakhtiary, Siavash A. Bigdeli  

**一句话要点**：提出优化可解释提升机以解决信用卡欺诈检测中的类别不平衡问题

**关键词**：信用卡欺诈检测, 可解释提升机, 类别不平衡, 超参数优化, 特征选择, ROC-AUC

## 3 点简述
- 核心问题：类别不平衡影响信用卡欺诈检测的预测可靠性
- 方法要点：基于可解释提升机，通过超参数调优、特征选择和预处理优化提升性能
- 实验或效果：在基准数据上ROC-AUC达0.983，优于基线模型和传统方法

## 摘要（原文）

> Addressing class imbalance is a central challenge in credit card fraud detection, as it directly impacts predictive reliability in real-world financial systems. To overcome this, the study proposes an enhanced workflow based on the Explainable Boosting Machine (EBM)-a transparent, state-of-the-art implementation of the GA2M algorithm-optimized through systematic hyperparameter tuning, feature selection, and preprocessing refinement. Rather than relying on conventional sampling techniques that may introduce bias or cause information loss, the optimized EBM achieves an effective balance between accuracy and interpretability, enabling precise detection of fraudulent transactions while providing actionable insights into feature importance and interaction effects. Furthermore, the Taguchi method is employed to optimize both the sequence of data scalers and model hyperparameters, ensuring robust, reproducible, and systematically validated performance improvements. Experimental evaluation on benchmark credit card data yields an ROC-AUC of 0.983, surpassing prior EBM baselines (0.975) and outperforming Logistic Regression, Random Forest, XGBoost, and Decision Tree models. These results highlight the potential of interpretable machine learning and data-driven optimization for advancing trustworthy fraud analytics in financial systems.

