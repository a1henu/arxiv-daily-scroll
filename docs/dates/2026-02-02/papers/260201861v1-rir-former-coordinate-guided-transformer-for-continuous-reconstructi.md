---
layout: default
title: RIR-Former: Coordinate-Guided Transformer for Continuous Reconstruction of Room Impulse Responses
---

# RIR-Former: Coordinate-Guided Transformer for Continuous Reconstruction of Room Impulse Responses
**arXiv**：[2602.01861v1](https://arxiv.org/abs/2602.01861) · [PDF](https://arxiv.org/pdf/2602.01861.pdf)  
**作者**：Shaoheng Xu, Chunyi Sun, Jihui, Zhang, Prasanga N. Samarasinghe, Thushara D. Abhayapala  

**一句话要点**：提出RIR-Former，一种基于坐标引导Transformer的模型，用于连续重建房间脉冲响应。

**关键词**：房间脉冲响应重建, Transformer模型, 坐标编码, 声学信号处理, 稀疏数据插值

## 3 点简述
- 核心问题：密集测量房间脉冲响应不切实际，需从稀疏数据重建。
- 方法要点：引入正弦编码模块整合麦克风位置信息，设计分段多分支解码器处理早期反射和晚期混响。
- 实验或效果：在多种模拟声学环境中，NMSE和余弦距离指标优于现有基线，支持任意阵列位置插值。

## 摘要（原文）

> Room impulse responses (RIRs) are essential for many acoustic signal processing tasks, yet measuring them densely across space is often impractical. In this work, we propose RIR-Former, a grid-free, one-step feed-forward model for RIR reconstruction. By introducing a sinusoidal encoding module into a transformer backbone, our method effectively incorporates microphone position information, enabling interpolation at arbitrary array locations. Furthermore, a segmented multi-branch decoder is designed to separately handle early reflections and late reverberation, improving reconstruction across the entire RIR. Experiments on diverse simulated acoustic environments demonstrate that RIR-Former consistently outperforms state-of-the-art baselines in terms of normalized mean square error (NMSE) and cosine distance (CD), under varying missing rates and array configurations. These results highlight the potential of our approach for practical deployment and motivate future work on scaling from randomly spaced linear arrays to complex array geometries, dynamic acoustic scenes, and real-world environments.

