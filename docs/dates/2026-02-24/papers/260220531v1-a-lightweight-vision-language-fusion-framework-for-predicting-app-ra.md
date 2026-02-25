---
layout: default
title: A Lightweight Vision-Language Fusion Framework for Predicting App Ratings from User Interfaces and Metadata
---

# A Lightweight Vision-Language Fusion Framework for Predicting App Ratings from User Interfaces and Metadata
**arXiv**：[2602.20531v1](https://arxiv.org/abs/2602.20531) · [PDF](https://arxiv.org/pdf/2602.20531.pdf)  
**作者**：Azrin Sultana, Firoz Ahmed  

**一句话要点**：提出轻量级视觉-语言融合框架，结合UI布局与语义信息预测应用评分

**关键词**：应用评分预测, 视觉-语言融合, 轻量级框架, 多模态学习, 边缘计算

## 3 点简述
- 核心问题：现有应用评分预测模型多依赖文本或UI特征，忽略多模态信息融合。
- 方法要点：使用MobileNetV3提取UI视觉特征，DistilBERT提取文本特征，通过门控融合模块整合。
- 实验效果：模型在多项指标上表现优异，如MAE为0.1060，R2为0.8529，支持边缘设备部署。

## 摘要（原文）

> App ratings are among the most significant indicators of the quality, usability, and overall user satisfaction of mobile applications. However, existing app rating prediction models are largely limited to textual data or user interface (UI) features, overlooking the importance of jointly leveraging UI and semantic information. To address these limitations, this study proposes a lightweight vision--language framework that integrates both mobile UI and semantic information for app rating prediction. The framework combines MobileNetV3 to extract visual features from UI layouts and DistilBERT to extract textual features. These multimodal features are fused through a gated fusion module with Swish activations, followed by a multilayer perceptron (MLP) regression head. The proposed model is evaluated using mean absolute error (MAE), root mean square error (RMSE), mean squared error (MSE), coefficient of determination (R2), and Pearson correlation. After training for 20 epochs, the model achieves an MAE of 0.1060, an RMSE of 0.1433, an MSE of 0.0205, an R2 of 0.8529, and a Pearson correlation of 0.9251. Extensive ablation studies further demonstrate the effectiveness of different combinations of visual and textual encoders. Overall, the proposed lightweight framework provides valuable insights for developers and end users, supports sustainable app development, and enables efficient deployment on edge devices.

