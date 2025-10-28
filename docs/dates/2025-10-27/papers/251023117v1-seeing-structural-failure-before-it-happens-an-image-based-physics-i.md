---
layout: default
title: Seeing Structural Failure Before it Happens: An Image-Based Physics-Informed Neural Network (PINN) for Spaghetti Bridge Load Prediction
---

# Seeing Structural Failure Before it Happens: An Image-Based Physics-Informed Neural Network (PINN) for Spaghetti Bridge Load Prediction
**arXiv**：[2510.23117v1](https://arxiv.org/abs/2510.23117) · [PDF](https://arxiv.org/pdf/2510.23117.pdf)  
**作者**：Omer Jauhar Khan, Sudais Khan, Hafeez Anwar  

**一句话要点**：提出物理信息神经网络以预测意大利面桥梁承重，辅助结构失效分析。

**关键词**：物理信息神经网络, 结构工程预测, 意大利面桥梁, 计算机视觉, 失效分析, 深度学习

## 3 点简述
- 核心问题：在数据有限下预测简化结构模型的承重和失效模式。
- 方法要点：结合物理约束与深度学习，引入新型PIKAN架构。
- 实验或效果：在15座桥梁数据集上，R²达0.9603，MAE为10.50单位。

## 摘要（原文）

> Physics Informed Neural Networks (PINNs) are gaining attention for their
> ability to embed physical laws into deep learning models, which is particularly
> useful in structural engineering tasks with limited data. This paper aims to
> explore the use of PINNs to predict the weight of small scale spaghetti
> bridges, a task relevant to understanding load limits and potential failure
> modes in simplified structural models. Our proposed framework incorporates
> physics-based constraints to the prediction model for improved performance. In
> addition to standard PINNs, we introduce a novel architecture named Physics
> Informed Kolmogorov Arnold Network (PIKAN), which blends universal function
> approximation theory with physical insights. The structural parameters provided
> as input to the model are collected either manually or through computer vision
> methods. Our dataset includes 15 real bridges, augmented to 100 samples, and
> our best model achieves an $R^2$ score of 0.9603 and a mean absolute error
> (MAE) of 10.50 units. From applied perspective, we also provide a web based
> interface for parameter entry and prediction. These results show that PINNs can
> offer reliable estimates of structural weight, even with limited data, and may
> help inform early stage failure analysis in lightweight bridge designs.
>   The complete data and code are available at
> https://github.com/OmerJauhar/PINNS-For-Spaghetti-Bridges.

