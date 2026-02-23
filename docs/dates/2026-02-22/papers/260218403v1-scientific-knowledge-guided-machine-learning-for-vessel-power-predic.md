---
layout: default
title: Scientific Knowledge-Guided Machine Learning for Vessel Power Prediction: A Comparative Study
---

# Scientific Knowledge-Guided Machine Learning for Vessel Power Prediction: A Comparative Study
**arXiv**：[2602.18403v1](https://arxiv.org/abs/2602.18403) · [PDF](https://arxiv.org/pdf/2602.18403.pdf)  
**作者**：Orfeas Bourchas, George Papalambrou  

**一句话要点**：提出基于科学知识的混合建模框架，用于船舶功率预测以提升泛化能力

**关键词**：船舶功率预测, 混合建模, 物理知识引导, 残差学习, 泛化能力, 性能优化

## 3 点简述
- 核心问题：传统机器学习方法在船舶功率预测中难以遵循螺旋桨定律，导致训练范围外泛化差
- 方法要点：结合物理基线模型与数据驱动残差学习，约束机器学习任务为残差修正
- 实验或效果：在稀疏数据区域优于纯数据驱动基线，保持密集区域性能，验证了框架有效性

## 摘要（原文）

> Accurate prediction of main engine power is essential for vessel performance optimization, fuel efficiency, and compliance with emission regulations. Conventional machine learning approaches, such as Support Vector Machines, variants of Artificial Neural Networks (ANNs), and tree-based methods like Random Forests, Extra Tree Regressors, and XGBoost, can capture nonlinearities but often struggle to respect the fundamental propeller law relationship between power and speed, resulting in poor extrapolation outside the training envelope. This study introduces a hybrid modeling framework that integrates physics-based knowledge from sea trials with data-driven residual learning. The baseline component, derived from calm-water power curves of the form $P = cV^n$, captures the dominant power-speed dependence, while another, nonlinear, regressor is then trained to predict the residual power, representing deviations caused by environmental and operational conditions. By constraining the machine learning task to residual corrections, the hybrid model simplifies learning, improves generalization, and ensures consistency with the underlying physics. In this study, an XGBoost, a simple Neural Network, and a Physics-Informed Neural Network (PINN) coupled with the baseline component were compared to identical models without the baseline component. Validation on in-service data demonstrates that the hybrid model consistently outperformed a pure data-driven baseline in sparse data regions while maintaining similar performance in populated ones. The proposed framework provides a practical and computationally efficient tool for vessel performance monitoring, with applications in weather routing, trim optimization, and energy efficiency planning.

