---
layout: default
title: MAUNet-Light: A Concise MAUNet Architecture for Bias Correction and Downscaling of Precipitation Estimates
---

# MAUNet-Light: A Concise MAUNet Architecture for Bias Correction and Downscaling of Precipitation Estimates
**arXiv**：[2602.12980v1](https://arxiv.org/abs/2602.12980) · [PDF](https://arxiv.org/pdf/2602.12980.pdf)  
**作者**：Sumanta Chandra Mishra Sharma, Adway Mitra, Auroop Ratan Ganguly  

**一句话要点**：提出MAUNet-Light轻量架构，用于降水估计的偏差校正与降尺度

**关键词**：降水估计, 偏差校正, 降尺度, 轻量神经网络, 知识蒸馏, MAUNet

## 3 点简述
- 降水卫星数据与模型存在系统性偏差，需校正与降尺度以匹配地面观测
- 基于师生学习范式，从MAUNet迁移知识，设计轻量网络MAUNet-Light
- 在减少计算需求的同时，保持与先进方法相当的精度

## 摘要（原文）

> Satellite-derived data products and climate model simulations of geophysical variables like precipitation, often exhibit systematic biases compared to in-situ measurements. Bias correction and spatial downscaling are fundamental components to develop operational weather forecast systems, as they seek to improve the consistency between coarse-resolution climate model simulations or satellite-based estimates and ground-based observations. In recent years, deep learning-based models have been increasingly replaced traditional statistical methods to generate high-resolution, bias free projections of climate variables. For example, Max-Average U-Net (MAUNet) architecture has been demonstrated for its ability to downscale precipitation estimates. The versatility and adaptability of these neural models make them highly effective across a range of applications, though this often come at the cost of high computational and memory requirements. The aim of this research is to develop light-weight neural network architectures for both bias correction and downscaling of precipitation, for which the teacher-student based learning paradigm is explored. This research demonstrates the adaptability of MAUNet to the task of bias correction, and further introduces a compact, lightweight neural network architecture termed MAUNet-Light.The proposed MAUNet-Light model is developed by transferring knowledge from the trained MAUNet, and it is designed to perform both downscaling and bias correction with reduced computational requirements without any significant loss in accuracy compared to state-of-the-art.

