---
layout: default
title: CNN-LSTM Hybrid Architecture for Over-the-Air Automatic Modulation Classification Using SDR
---

# CNN-LSTM Hybrid Architecture for Over-the-Air Automatic Modulation Classification Using SDR
**arXiv**：[2511.21040v1](https://arxiv.org/abs/2511.21040) · [PDF](https://arxiv.org/pdf/2511.21040.pdf)  
**作者**：Dinanath Padhya, Krishna Acharya, Bipul Kumar Dahal, Dinesh Baniya Kshatri  

**一句话要点**：提出CNN-LSTM混合架构以解决无线通信中的自动调制分类问题

**关键词**：自动调制分类, CNN-LSTM混合架构, 软件定义无线电, 信号特征提取, 频谱管理, 认知无线电

## 3 点简述
- 自动调制分类是认知无线电等系统的核心技术，需识别未知调制方案
- 结合CNN提取空间特征和LSTM捕获时序依赖，处理复杂时变信号
- 实验在OTA信号上验证，模型准确率达93.48%，AUC-ROC显示强判别力

## 摘要（原文）

> Automatic Modulation Classification (AMC) is a core technology for future wireless communication systems, enabling the identification of modulation schemes without prior knowledge. This capability is essential for applications in cognitive radio, spectrum monitoring, and intelligent communication networks. We propose an AMC system based on a hybrid Convolutional Neural Network (CNN) and Long Short-Term Memory (LSTM) architecture, integrated with a Software Defined Radio (SDR) platform. The proposed architecture leverages CNNs for spatial feature extraction and LSTMs for capturing temporal dependencies, enabling efficient handling of complex, time-varying communication signals. The system's practical ability was demonstrated by identifying over-the-air (OTA) signals from a custom-built FM transmitter alongside other modulation schemes. The system was trained on a hybrid dataset combining the RadioML2018 dataset with a custom-generated dataset, featuring samples at Signal-to-Noise Ratios (SNRs) from 0 to 30dB. System performance was evaluated using accuracy, precision, recall, F1 score, and the Area Under the Receiver Operating Characteristic Curve (AUC-ROC). The optimized model achieved 93.48% accuracy, 93.53% precision, 93.48% recall, and an F1 score of 93.45%. The AUC-ROC analysis confirmed the model's discriminative power, even in noisy conditions. This paper's experimental results validate the effectiveness of the hybrid CNN-LSTM architecture for AMC, suggesting its potential application in adaptive spectrum management and advanced cognitive radio systems.

