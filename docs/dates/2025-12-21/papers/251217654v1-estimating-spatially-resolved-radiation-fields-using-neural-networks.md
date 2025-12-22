---
layout: default
title: Estimating Spatially Resolved Radiation Fields Using Neural Networks
---

# Estimating Spatially Resolved Radiation Fields Using Neural Networks
**arXiv**：[2512.17654v1](https://arxiv.org/abs/2512.17654) · [PDF](https://arxiv.org/pdf/2512.17654.pdf)  
**作者**：Felix Lehner, Pasquale Lombardo, Susana Castillo, Oliver Hupe, Marcus Magnor  

**一句话要点**：提出基于神经网络的辐射场空间分布估计方法，用于医疗辐射防护剂量学。

**关键词**：辐射防护剂量学, 神经网络估计, 蒙特卡洛模拟, 空间分布重建, 医疗辐射场

## 3 点简述
- 核心问题：估计医疗辐射场（如介入放射学）中散射辐射的空间分布，以支持剂量学评估。
- 方法要点：使用Geant4蒙特卡洛模拟生成合成数据集，评估卷积和全连接神经网络架构。
- 实验或效果：通过三个复杂度递增的数据集验证网络设计，开源数据集和训练流程。

## 摘要（原文）

> We present an in-depth analysis on how to build and train neural networks to estimate the spatial distribution of scattered radiation fields for radiation protection dosimetry in medical radiation fields, such as those found in Interventional Radiology and Cardiology. Therefore, we present three different synthetically generated datasets with increasing complexity for training, using a Monte-Carlo Simulation application based on Geant4. On those datasets, we evaluate convolutional and fully connected architectures of neural networks to demonstrate which design decisions work well for reconstructing the fluence and spectra distributions over the spatial domain of such radiation fields. All used datasets as well as our training pipeline are published as open source in separate repositories.

