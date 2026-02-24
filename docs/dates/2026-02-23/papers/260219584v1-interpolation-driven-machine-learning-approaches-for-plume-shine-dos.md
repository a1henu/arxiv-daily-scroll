---
layout: default
title: Interpolation-Driven Machine Learning Approaches for Plume Shine Dose Estimation: A Comparison of XGBoost, Random Forest, and TabNet
---

# Interpolation-Driven Machine Learning Approaches for Plume Shine Dose Estimation: A Comparison of XGBoost, Random Forest, and TabNet
**arXiv**：[2602.19584v1](https://arxiv.org/abs/2602.19584) · [PDF](https://arxiv.org/pdf/2602.19584.pdf)  
**作者**：Biswajit Sadhu, Kalpak Gupte, Trijit Sadhu, S. Anand  

**一句话要点**：提出插值辅助机器学习框架，用于快速准确估计羽流照射剂量，比较XGBoost、随机森林和TabNet性能。

**关键词**：羽流照射剂量估计, 插值辅助机器学习, XGBoost, 随机森林, TabNet, 可解释性分析

## 3 点简述
- 核心问题：辐射剂量评估中机器学习应用受限，羽流照射剂量计算昂贵，需高效替代方法。
- 方法要点：使用pyDOSEIA生成离散数据集，通过形状保持插值增强数据，评估树基模型和深度学习模型。
- 实验或效果：插值数据提升所有模型精度，XGBoost表现最佳，可解释性分析揭示特征利用差异。

## 摘要（原文）

> Despite the success of machine learning (ML) in surrogate modeling, its use in radiation dose assessment is limited by safety-critical constraints, scarce training-ready data, and challenges in selecting suitable architectures for physics-dominated systems. Within this context, rapid and accurate plume shine dose estimation serves as a practical test case, as it is critical for nuclear facility safety assessment and radiological emergency response, while conventional photon-transport-based calculations remain computationally expensive. In this work, an interpolation-assisted ML framework was developed using discrete dose datasets generated with the pyDOSEIA suite for 17 gamma-emitting radionuclides across varying downwind distances, release heights, and atmospheric stability categories. The datasets were augmented using shape-preserving interpolation to construct dense, high-resolution training data. Two tree-based ML models (Random Forest and XGBoost) and one deep learning (DL) model (TabNet) were evaluated to examine predictive performance and sensitivity to dataset resolution. All models showed higher prediction accuracy with the interpolated high-resolution dataset than with the discrete data; however, XGBoost consistently achieved the highest accuracy. Interpretability analysis using permutation importance (tree-based models) and attention-based feature attribution (TabNet) revealed that performance differences stem from how the models utilize input features. Tree-based models focus mainly on dominant geometry-dispersion features (release height, stability category, and downwind distance), treating radionuclide identity as a secondary input, whereas TabNet distributes attention more broadly across multiple variables. For practical deployment, a web-based GUI was developed for interactive scenario evaluation and transparent comparison with photon-transport reference calculations.

