---
layout: default
title: Deep Learning for Metabolic Rate Estimation from Biosignals: A Comparative Study of Architectures and Signal Selection
---

# Deep Learning for Metabolic Rate Estimation from Biosignals: A Comparative Study of Architectures and Signal Selection
**arXiv**：[2511.09276v1](https://arxiv.org/abs/2511.09276) · [PDF](https://arxiv.org/pdf/2511.09276.pdf)  
**作者**：Sarvenaz Babakhani, David Remy, Alina Roitberg  

**一句话要点**：系统评估深度学习架构与信号选择对代谢率估计的影响，发现分钟通气量最有效。

**关键词**：代谢率估计, 深度学习架构, 生理信号选择, Transformer模型, 能量消耗预测

## 3 点简述
- 核心问题：从生理信号估计代谢率，传统方法为主，深度学习角色未明。
- 方法要点：比较经典与神经架构，分析单信号、信号对和分组输入。
- 实验或效果：Transformer模型在分钟通气量上RMSE最低，活动强度影响误差。

## 摘要（原文）

> Energy expenditure estimation aims to infer human metabolic rate from physiological signals such as heart rate, respiration, or accelerometer data, and has been studied primarily with classical regression methods. The few existing deep learning approaches rarely disentangle the role of neural architecture from that of signal choice. In this work, we systematically evaluate both aspects. We compare classical baselines with newer neural architectures across single signals, signal pairs, and grouped sensor inputs for diverse physical activities. Our results show that minute ventilation is the most predictive individual signal, with a transformer model achieving the lowest root mean square error (RMSE) of 0.87 W/kg across all activities. Paired and grouped signals, such as those from the Hexoskin smart shirt (five signals), offer good alternatives for faster models like CNN and ResNet with attention. Per-activity evaluation revealed mixed outcomes: notably better results in low-intensity activities (RMSE down to 0.29 W/kg; NRMSE = 0.04), while higher-intensity tasks showed larger RMSE but more comparable normalized errors. Finally, subject-level analysis highlights strong inter-individual variability, motivating the need for adaptive modeling strategies. Our code and models will be publicly available at https://github.com/Sarvibabakhani/deeplearning-biosignals-ee .

