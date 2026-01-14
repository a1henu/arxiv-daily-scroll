---
layout: default
title: A brain-inspired information fusion method for enhancing robot GPS outages navigation
---

# A brain-inspired information fusion method for enhancing robot GPS outages navigation
**arXiv**：[2601.08244v1](https://arxiv.org/abs/2601.08244) · [PDF](https://arxiv.org/pdf/2601.08244.pdf)  
**作者**：Yaohua Liu, Hengjun Zhang, Binkai Ou  

**一句话要点**：提出脑启发的GPS/INS融合网络以增强机器人GPS中断时的导航性能

**关键词**：GPS/INS融合, 脉冲神经网络, 机器人导航, 时空特征提取, 惯性测量单元

## 3 点简述
- 核心问题：低成本惯性导航系统在GPS中断时因传感器偏差和噪声导致导航精度快速下降。
- 方法要点：基于脉冲神经网络，结合脉冲Transformer和编码器提取IMU信号的时空特征，建模车辆运动关系。
- 实验或效果：通过实地测试和公开数据集验证，相比传统深度学习方法，在长时间GPS中断下实现更高精度和可靠性。

## 摘要（原文）

> Low-cost inertial navigation systems (INS) are prone to sensor biases and measurement noise, which lead to rapid degradation of navigation accuracy during global positioning system (GPS) outages. To address this challenge and improve positioning continuity in GPS-denied environments, this paper proposes a brain-inspired GPS/INS fusion network (BGFN) based on spiking neural networks (SNNs). The BGFN architecture integrates a spiking Transformer with a spiking encoder to simultaneously extract spatial features from inertial measurement unit (IMU) signals and capture their temporal dynamics. By modeling the relationship between vehicle attitude, specific force, angular rate, and GPS-derived position increments, the network leverages both current and historical IMU data to estimate vehicle motion. The effectiveness of the proposed method is evaluated through real-world field tests and experiments on public datasets. Compared to conventional deep learning approaches, the results demonstrate that BGFN achieves higher accuracy and enhanced reliability in navigation performance, particularly under prolonged GPS outages.

