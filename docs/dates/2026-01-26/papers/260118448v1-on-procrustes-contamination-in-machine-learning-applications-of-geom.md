---
layout: default
title: On Procrustes Contamination in Machine Learning Applications of Geometric Morphometrics
---

# On Procrustes Contamination in Machine Learning Applications of Geometric Morphometrics
**arXiv**：[2601.18448v1](https://arxiv.org/abs/2601.18448) · [PDF](https://arxiv.org/pdf/2601.18448.pdf)  
**作者**：Lloyd Austin Courtenay  

**一句话要点**：提出测试集重对齐方法以解决几何形态测量学中Procrustes污染对机器学习模型的影响

**关键词**：几何形态测量学, Procrustes分析, 机器学习预处理, 统计依赖性, 空间自相关, 模型污染

## 3 点简述
- 核心问题：标准GPA预处理在数据分割后引入统计依赖性，污染下游预测模型。
- 方法要点：提出测试集向训练集重对齐的新程序，消除跨样本依赖性。
- 实验或效果：通过模拟揭示样本大小与地标空间的稳健关系，并分析空间自相关影响。

## 摘要（原文）

> Geometric morphometrics (GMM) is widely used to quantify shape variation, more recently serving as input for machine learning (ML) analyses. Standard practice aligns all specimens via Generalized Procrustes Analysis (GPA) prior to splitting data into training and test sets, potentially introducing statistical dependence and contaminating downstream predictive models. Here, the effects of GPA-induced contamination are formally characterised using controlled 2D and 3D simulations across varying sample sizes, landmark densities, and allometric patterns. A novel realignment procedure is proposed, whereby test specimens are aligned to the training set prior to model fitting, eliminating cross-sample dependency. Simulations reveal a robust "diagonal" in sample-size vs. landmark-space, reflecting the scaling of RMSE under isotropic variation, with slopes analytically derived from the degrees of freedom in Procrustes tangent space. The importance of spatial autocorrelation among landmarks is further demonstrated using linear and convolutional regression models, highlighting performance degradation when landmark relationships are ignored. This work establishes the need for careful preprocessing in ML applications of GMM, provides practical guidelines for realignment, and clarifies fundamental statistical constraints inherent to Procrustes shape space.

