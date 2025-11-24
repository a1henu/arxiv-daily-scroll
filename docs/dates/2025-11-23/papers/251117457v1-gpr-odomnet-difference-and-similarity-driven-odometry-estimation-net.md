---
layout: default
title: GPR-OdomNet: Difference and Similarity-Driven Odometry Estimation Network for Ground Penetrating Radar-Based Localization
---

# GPR-OdomNet: Difference and Similarity-Driven Odometry Estimation Network for Ground Penetrating Radar-Based Localization
**arXiv**：[2511.17457v1](https://arxiv.org/abs/2511.17457) · [PDF](https://arxiv.org/pdf/2511.17457.pdf)  
**作者**：Huaichao Wang, Xuanxin Fan, Ji Liu, Haifeng Li, Dezhen Song  

**一句话要点**：提出GPR-OdomNet，利用B-scan图像相似与差异特征，提升探地雷达定位精度。

**关键词**：探地雷达定位, 里程计估计, B-scan图像处理, 神经网络, 多尺度特征提取, 相似性分析

## 3 点简述
- 核心问题：探地雷达B-scan图像差异小，现有方法距离估计不准确。
- 方法要点：神经网络提取多尺度特征，分析相似与差异以估计欧氏距离。
- 实验效果：在CMU-GPR数据集上，RMSE降低10.2%，优于现有方法。

## 摘要（原文）

> When performing robot/vehicle localization using ground penetrating radar (GPR) to handle adverse weather and environmental conditions, existing techniques often struggle to accurately estimate distances when processing B-scan images with minor distinctions. This study introduces a new neural network-based odometry method that leverages the similarity and difference features of GPR B-scan images for precise estimation of the Euclidean distances traveled between the B-scan images. The new custom neural network extracts multi-scale features from B-scan images taken at consecutive moments and then determines the Euclidean distance traveled by analyzing the similarities and differences between these features. To evaluate our method, an ablation study and comparison experiments have been conducted using the publicly available CMU-GPR dataset. The experimental results show that our method consistently outperforms state-of-the-art counterparts in all tests. Specifically, our method achieves a root mean square error (RMSE), and achieves an overall weighted RMSE of 0.449 m across all data sets, which is a 10.2\% reduction in RMSE when compared to the best state-of-the-art method.

