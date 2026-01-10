---
layout: default
title: Prediction of Cellular Malignancy Using Electrical Impedance Signatures and Supervised Machine Learning
---

# Prediction of Cellular Malignancy Using Electrical Impedance Signatures and Supervised Machine Learning
**arXiv**：[2601.04478v1](https://arxiv.org/abs/2601.04478) · [PDF](https://arxiv.org/pdf/2601.04478.pdf)  
**作者**：Shadeeb Hossain  

**一句话要点**：利用细胞电阻抗特征与监督机器学习预测细胞恶性程度

**关键词**：细胞电阻抗, 监督机器学习, 随机森林, 生物电特性, 分类性能, 诊断工具

## 3 点简述
- 核心问题：健康与恶性细胞的生物电特性差异为诊断提供基础，但需系统评估其预测性能。
- 方法要点：综述33篇文献构建数据集，应用随机森林、支持向量机和K近邻算法进行模型调优。
- 实验或效果：随机森林在特定超参数下达到约90%准确率，优于其他算法，突显集成生物电分析与机器学习的潜力。

## 摘要（原文）

> Bioelectrical properties of cells such as relative permittivity, conductivity, and characteristic time constants vary significantly between healthy and malignant cells across different frequencies. These distinctions provide a promising foundation for diagnostic and classification applications. This study systematically reviewed 33 scholarly articles to compile datasets of quantitative bioelectric parameters and evaluated their utility in predictive modeling. Three supervised machine learning algorithms- Random Forest (RF), Support Vector Machine (SVM), and K-Nearest Neighbor (KNN) were implemented and tuned using key hyperparameters to assess classification performance. Model effectiveness was evaluated using accuracy and F1 score as performance metrics. Results demonstrate that Random Forest achieved the highest predictive accuracy of ~ 90% when configured with a maximum depth of 4 and 100 estimators. These findings highlight the potential of integrating bioelectrical property analysis with machine learning for improved diagnostic decision-making. Similarly, for KNN and SVM, the F1 score peaked at approximately 78% and 76.5%, respectively. Future work will explore incorporating additional discriminative features, leveraging stimulated datasets, and optimizing hyperparameter through advanced search strategies. Ultimately, hardware prototype with embedded micro-electrodes and real-time control systems could pave the path for practical diagnostic tools capable of in-situ cell classification.

