---
layout: default
title: Prediction of Cellular Malignancy Using Electrical Impedance Signatures and Supervised Machine Learning
---

# Prediction of Cellular Malignancy Using Electrical Impedance Signatures and Supervised Machine Learning
**arXiv**：[2601.04478v1](https://arxiv.org/abs/2601.04478) · [PDF](https://arxiv.org/pdf/2601.04478.pdf)  
**作者**：Shadeeb Hossain  

**一句话要点**：利用细胞电阻抗特征与监督机器学习预测细胞恶性程度

**关键词**：细胞电阻抗, 监督机器学习, 随机森林, 生物电特性, 诊断分类

## 3 点简述
- 核心问题：健康与恶性细胞的生物电特性（如相对介电常数、电导率）在频率上存在显著差异，可用于诊断分类。
- 方法要点：系统综述33篇文献，编译生物电参数数据集，并应用随机森林、支持向量机和K近邻算法进行预测建模。
- 实验或效果：随机森林在最大深度4和100个估计器下达到约90%的准确率，KNN和SVM的F1分数分别约为78%和76.5%。

## 摘要（原文）

> Bioelectrical properties of cells such as relative permittivity, conductivity, and characteristic time constants vary significantly between healthy and malignant cells across different frequencies. These distinctions provide a promising foundation for diagnostic and classification applications. This study systematically reviewed 33 scholarly articles to compile datasets of quantitative bioelectric parameters and evaluated their utility in predictive modeling. Three supervised machine learning algorithms- Random Forest (RF), Support Vector Machine (SVM), and K-Nearest Neighbor (KNN) were implemented and tuned using key hyperparameters to assess classification performance. Model effectiveness was evaluated using accuracy and F1 score as performance metrics. Results demonstrate that Random Forest achieved the highest predictive accuracy of ~ 90% when configured with a maximum depth of 4 and 100 estimators. These findings highlight the potential of integrating bioelectrical property analysis with machine learning for improved diagnostic decision-making. Similarly, for KNN and SVM, the F1 score peaked at approximately 78% and 76.5%, respectively. Future work will explore incorporating additional discriminative features, leveraging stimulated datasets, and optimizing hyperparameter through advanced search strategies. Ultimately, hardware prototype with embedded micro-electrodes and real-time control systems could pave the path for practical diagnostic tools capable of in-situ cell classification.

