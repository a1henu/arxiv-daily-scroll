---
layout: default
title: Entropy-Enhanced Conformal Features from Ricci Flow for Robust Alzheimer's Disease Classification
---

# Entropy-Enhanced Conformal Features from Ricci Flow for Robust Alzheimer's Disease Classification
**arXiv**：[2510.18396v1](https://arxiv.org/abs/2510.18396) · [PDF](https://arxiv.org/pdf/2510.18396.pdf)  
**作者**：F. Ahmadi, B. Bidabad, H. Nasiri  

**一句话要点**：提出基于Ricci流和熵的局部表面特征方法，用于阿尔茨海默病分类

**关键词**：脑影像分析, 共形几何, 熵特征, 阿尔茨海默病分类, Ricci流, 机器学习分类

## 3 点简述
- 核心问题：阿尔茨海默病导致皮质萎缩，需从脑影像中准确分类患者与健康人
- 方法要点：使用Ricci流计算共形参数化特征，结合Shannon熵构建紧凑特征向量
- 实验或效果：在ADNI数据集上，MLP和逻辑回归分类器达到98.62%准确率和F1分数

## 摘要（原文）

> Background and Objective: In brain imaging, geometric surface models are
> essential for analyzing the 3D shapes of anatomical structures. Alzheimer's
> disease (AD) is associated with significant cortical atrophy, making such shape
> analysis a valuable diagnostic tool. The objective of this study is to
> introduce and validate a novel local surface representation method for the
> automated and accurate diagnosis of AD. Methods: The study utilizes T1-weighted
> MRI scans from 160 participants (80 AD patients and 80 healthy controls) from
> the Alzheimer's Disease Neuroimaging Initiative (ADNI). Cortical surface models
> were reconstructed from the MRI data using Freesurfer. Key geometric attributes
> were computed from the 3D meshes. Area distortion and conformal factor were
> derived using Ricci flow for conformal parameterization, while Gaussian
> curvature was calculated directly from the mesh geometry. Shannon entropy was
> applied to these three features to create compact and informative feature
> vectors. The feature vectors were used to train and evaluate a suite of
> classifiers (e.g. XGBoost, MLP, Logistic Regression, etc.). Results:
> Statistical significance of performance differences between classifiers was
> evaluated using paired Welch's t-test. The method proved highly effective in
> distinguishing AD patients from healthy controls. The Multi-Layer Perceptron
> (MLP) and Logistic Regression classifiers outperformed all others, achieving an
> accuracy and F$_1$ Score of 98.62%. Conclusions: This study confirms that the
> entropy of conformally-derived geometric features provides a powerful and
> robust metric for cortical morphometry. The high classification accuracy
> underscores the method's potential to enhance the study and diagnosis of
> Alzheimer's disease, offering a straightforward yet powerful tool for clinical
> research applications.

