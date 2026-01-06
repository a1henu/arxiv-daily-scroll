---
layout: default
title: Car Drag Coefficient Prediction from 3D Point Clouds Using a Slice-Based Surrogate Model
---

# Car Drag Coefficient Prediction from 3D Point Clouds Using a Slice-Based Surrogate Model
**arXiv**：[2601.02112v1](https://arxiv.org/abs/2601.02112) · [PDF](https://arxiv.org/pdf/2601.02112.pdf)  
**作者**：Utkarsh Singh, Absaar Ali, Adarsh Roy  

**一句话要点**：提出基于切片处理的轻量级代理模型，用于从3D点云预测汽车风阻系数，以加速早期设计迭代。

**关键词**：风阻系数预测, 3D点云处理, 切片序列建模, 轻量级代理模型, 汽车空气动力学

## 3 点简述
- 核心问题：传统CFD和风洞测试资源密集，阻碍汽车空气动力学设计的快速迭代。
- 方法要点：将3D车辆点云沿流向轴分解为切片序列，用PointNet2D编码后通过双向LSTM处理。
- 实验或效果：在DrivAerNet++数据集上实现高精度预测（R²>0.9528），推理时间约0.025秒/样本。

## 摘要（原文）

> The automotive industry's pursuit of enhanced fuel economy and performance necessitates efficient aerodynamic design. However, traditional evaluation methods such as computational fluid dynamics (CFD) and wind tunnel testing are resource intensive, hindering rapid iteration in the early design stages. Machine learning-based surrogate models offer a promising alternative, yet many existing approaches suffer from high computational complexity, limited interpretability, or insufficient accuracy for detailed geometric inputs. This paper introduces a novel lightweight surrogate model for the prediction of the aerodynamic drag coefficient (Cd) based on a sequential slice-wise processing of the geometry of the 3D vehicle. Inspired by medical imaging, 3D point clouds of vehicles are decomposed into an ordered sequence of 2D cross-sectional slices along the stream-wise axis. Each slice is encoded by a lightweight PointNet2D module, and the sequence of slice embeddings is processed by a bidirectional LSTM to capture longitudinal geometric evolution. The model, trained and evaluated on the DrivAerNet++ dataset, achieves a high coefficient of determination (R^2 > 0.9528) and a low mean absolute error (MAE approx 6.046 x 10^{-3}) in Cd prediction. With an inference time of approximately 0.025 seconds per sample on a consumer-grade GPU, our approach provides fast, accurate, and interpretable aerodynamic feedback, facilitating more agile and informed automotive design exploration.

