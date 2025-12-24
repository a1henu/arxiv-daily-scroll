---
layout: default
title: High Dimensional Data Decomposition for Anomaly Detection of Textured Images
---

# High Dimensional Data Decomposition for Anomaly Detection of Textured Images
**arXiv**：[2512.20432v1](https://arxiv.org/abs/2512.20432) · [PDF](https://arxiv.org/pdf/2512.20432.pdf)  
**作者**：Ji Song, Xing Wang, Jianguo Wu, Xiaowei Yue  

**一句话要点**：提出纹理基集成平滑分解方法，以解决纹理图像中异常检测的误识别和数据集依赖问题。

**关键词**：纹理图像异常检测, 高维数据分解, 准周期性建模, 纹理基函数学习, 稀疏异常检测

## 3 点简述
- 核心问题：传统方法在纹理缺陷图像上存在误识别、鲁棒性低和依赖大规模结构化数据集的局限性。
- 方法要点：基于准周期性理论，通过纹理基函数学习提取准周期纹理模式，并利用其作为先验知识进行高精度异常检测。
- 实验或效果：在仿真和真实数据集上超越基准，减少误识别、降低训练数据需求，并提升异常检测性能。

## 摘要（原文）

> In the realm of diverse high-dimensional data, images play a significant role across various processes of manufacturing systems where efficient image anomaly detection has emerged as a core technology of utmost importance. However, when applied to textured defect images, conventional anomaly detection methods have limitations including non-negligible misidentification, low robustness, and excessive reliance on large-scale and structured datasets. This paper proposes a texture basis integrated smooth decomposition (TBSD) approach, which is targeted at efficient anomaly detection in textured images with smooth backgrounds and sparse anomalies. Mathematical formulation of quasi-periodicity and its theoretical properties are investigated for image texture estimation. TBSD method consists of two principal processes: the first process learns the texture basis functions to effectively extract quasi-periodic texture patterns; the subsequent anomaly detection process utilizes that texture basis as prior knowledge to prevent texture misidentification and capture potential anomalies with high accuracy.The proposed method surpasses benchmarks with less misidentification, smaller training dataset requirement, and superior anomaly detection performance on both simulation and real-world datasets.

