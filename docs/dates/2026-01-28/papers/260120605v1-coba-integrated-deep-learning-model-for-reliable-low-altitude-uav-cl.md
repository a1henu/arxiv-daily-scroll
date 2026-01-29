---
layout: default
title: CoBA: Integrated Deep Learning Model for Reliable Low-Altitude UAV Classification in mmWave Radio Networks
---

# CoBA: Integrated Deep Learning Model for Reliable Low-Altitude UAV Classification in mmWave Radio Networks
**arXiv**：[2601.20605v1](https://arxiv.org/abs/2601.20605) · [PDF](https://arxiv.org/pdf/2601.20605.pdf)  
**作者**：Junaid Sajid, Ivo Müürsepp, Luca Reggiani, Davide Scazzoli, Federico Francesco Luigi Mariani, Maurizio Magarini, Rizwan Ahmad, Muhammad Mahtab Alam  

**一句话要点**：提出CoBA深度学习模型，利用5G毫米波测量实现低空无人机在授权与受限空域的分类。

**关键词**：无人机分类, 毫米波通信, 深度学习模型, 时空模式分析, 5G网络

## 3 点简述
- 核心问题：毫米波环境下低空无人机在授权与受限空域的分类挑战，需处理复杂传播和信号变化。
- 方法要点：集成CNN、BiLSTM和注意力机制，捕获无人机无线电测量的时空模式。
- 实验或效果：基于5G毫米波网络数据集，CoBA在准确率上显著优于传统机器学习和指纹基准模型。

## 摘要（原文）

> Uncrewed Aerial Vehicles (UAVs) are increasingly used in civilian and industrial applications, making secure low-altitude operations crucial. In dense mmWave environments, accurately classifying low-altitude UAVs as either inside authorized or restricted airspaces remains challenging, requiring models that handle complex propagation and signal variability. This paper proposes a deep learning model, referred to as CoBA, which stands for integrated Convolutional Neural Network (CNN), Bidirectional Long Short-Term Memory (BiLSTM), and Attention which leverages Fifth Generation (5G) millimeter-wave (mmWave) radio measurements to classify UAV operations in authorized and restricted airspaces at low altitude. The proposed CoBA model integrates convolutional, bidirectional recurrent, and attention layers to capture both spatial and temporal patterns in UAV radio measurements. To validate the model, a dedicated dataset is collected using the 5G mmWave network at TalTech, with controlled low altitude UAV flights in authorized and restricted scenarios. The model is evaluated against conventional ML models and a fingerprinting-based benchmark. Experimental results show that CoBA achieves superior accuracy, significantly outperforming all baseline models and demonstrating its potential for reliable and regulated UAV airspace monitoring.

