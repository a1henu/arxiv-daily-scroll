---
layout: default
title: Intracoronary Optical Coherence Tomography Image Processing and Vessel Classification Using Machine Learning
---

# Intracoronary Optical Coherence Tomography Image Processing and Vessel Classification Using Machine Learning
**arXiv**：[2602.15579v1](https://arxiv.org/abs/2602.15579) · [PDF](https://arxiv.org/pdf/2602.15579.pdf)  
**作者**：Amal Lahchim, Lambros Athanasiou  

**一句话要点**：提出基于机器学习的全自动管道，用于冠状动脉OCT图像的血管分割与分类。

**关键词**：冠状动脉OCT, 血管分割, 机器学习分类, 图像预处理, 导丝伪影去除, 临床决策支持

## 3 点简述
- 核心问题：冠状动脉OCT图像存在噪声、成像伪影和组织结构复杂，影响血管分析。
- 方法要点：集成图像预处理、导丝伪影去除、极坐标转换、K-means聚类和局部特征提取，训练Logistic回归与SVM分类器。
- 实验或效果：在像素级分类中达到高达1.00的精确率、召回率和F1分数，总体准确率为99.68%。

## 摘要（原文）

> Intracoronary Optical Coherence Tomography (OCT) enables high-resolution visualization of coronary vessel anatomy but presents challenges due to noise, imaging artifacts, and complex tissue structures. This paper proposes a fully automated pipeline for vessel segmentation and classification in OCT images using machine learning techniques. The proposed method integrates image preprocessing, guidewire artifact removal, polar-to-Cartesian transformation, unsupervised K-means clustering, and local feature extraction. These features are used to train Logistic Regression and Support Vector Machine classifiers for pixel-wise vessel classification. Experimental results demonstrate excellent performance, achieving precision, recall, and F1-score values up to 1.00 and overall classification accuracy of 99.68%. The proposed approach provides accurate vessel boundary detection while maintaining low computational complexity and requiring minimal manual annotation. This method offers a reliable and efficient solution for automated OCT image analysis and has potential applications in clinical decision support and real-time medical image processing.

