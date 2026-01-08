---
layout: default
title: Physically Consistent Machine Learning for Melting Temperature Prediction of Refractory High-Entropy Alloys
---

# Physically Consistent Machine Learning for Melting Temperature Prediction of Refractory High-Entropy Alloys
**arXiv**：[2601.03801v1](https://arxiv.org/abs/2601.03801) · [PDF](https://arxiv.org/pdf/2601.03801.pdf)  
**作者**：Mohd Hasnain  

**一句话要点**：提出基于XGBoost的物理一致机器学习模型，用于预测难熔高熵合金的熔化温度。

**关键词**：熔化温度预测, 高熵合金, 机器学习, 物理一致性, 梯度提升决策树, 元素特征

## 3 点简述
- 核心问题：传统CALPHAD或DFT方法预测多组分合金熔化温度计算成本高。
- 方法要点：使用梯度提升决策树，基于元素属性特征避免数据泄露，确保物理一致性。
- 实验或效果：模型在验证集上R²达0.948，相对误差约5%，并成功捕获VEC规则下的相变点。

## 摘要（原文）

> Predicting the melting temperature (Tm) of multi-component and high-entropy alloys (HEAs) is critical for high-temperature applications but computationally expensive using traditional CALPHAD or DFT methods. In this work, we develop a gradient-boosted decision tree (XGBoost) model to predict Tm for complex alloys based on elemental properties. To ensure physical consistency, we address the issue of data leakage by excluding temperature-dependent thermodynamic descriptors (such as Gibbs free energy of mixing) and instead rely on physically motivated elemental features. The optimized model achieves a coefficient of determination (R2) of 0.948 and a Mean Squared Error (MSE) of 9928 which is about 5% relative error for HEAs on a validation set of approximately 1300 compositions. Crucially, we validate the model using the Valence Electron Concentration (VEC) rule. Without explicit constraints during training, the model successfully captures the known stability transition between BCC and FCC phases at a VEC of approximately 6.87. These results demonstrate that data-driven models, when properly feature-engineered, can capture fundamental metallurgical principles for rapid alloy screening.

