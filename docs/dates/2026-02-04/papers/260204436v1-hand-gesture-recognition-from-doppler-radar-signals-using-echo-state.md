---
layout: default
title: Hand Gesture Recognition from Doppler Radar Signals Using Echo State Networks
---

# Hand Gesture Recognition from Doppler Radar Signals Using Echo State Networks
**arXiv**：[2602.04436v1](https://arxiv.org/abs/2602.04436) · [PDF](https://arxiv.org/pdf/2602.04436.pdf)  
**作者**：Towa Sano, Gouhei Tanaka  

**一句话要点**：提出基于回声状态网络的多普勒雷达手势识别方法，以降低计算成本并提升资源受限环境下的性能。

**关键词**：手势识别, 多普勒雷达, 回声状态网络, 轻量计算, 时空特征, 时频分析

## 3 点简述
- 核心问题：基于多普勒雷达的手势识别在车载和机器人系统中需轻量高效，但现有深度学习方法计算成本高。
- 方法要点：使用FMCW雷达信号生成特征图，通过回声状态网络处理时空和时频模式，结合多种分类器进行识别。
- 实验或效果：在Soli和Dop-NET数据集上优于现有方法，多储层并行处理有效提升识别性能，计算成本低。

## 摘要（原文）

> Hand gesture recognition (HGR) is a fundamental technology in human computer interaction (HCI).In particular, HGR based on Doppler radar signals is suited for in-vehicle interfaces and robotic systems, necessitating lightweight and computationally efficient recognition techniques. However, conventional deep learning-based methods still suffer from high computational costs. To address this issue, we propose an Echo State Network (ESN) approach for radar-based HGR, using frequency-modulated-continuous-wave (FMCW) radar signals. Raw radar data is first converted into feature maps, such as range-time and Doppler-time maps, which are then fed into one or more recurrent neural network-based reservoirs. The obtained reservoir states are processed by readout classifiers, including ridge regression, support vector machines, and random forests. Comparative experiments demonstrate that our method outperforms existing approaches on an 11-class HGR task using the Soli dataset and surpasses existing deep learning models on a 4-class HGR task using the Dop-NET dataset. The results indicate that parallel processing using multi-reservoir ESNs are effective for recognizing temporal patterns from the multiple different feature maps in the time-space and time-frequency domains. Our ESN approaches achieve high recognition performance with low computational cost in HGR, showing great potential for more advanced HCI technologies, especially in resource-constrained environments.

