---
layout: default
title: I2E: Real-Time Image-to-Event Conversion for High-Performance Spiking Neural Networks
---

# I2E: Real-Time Image-to-Event Conversion for High-Performance Spiking Neural Networks
**arXiv**：[2511.08065v1](https://arxiv.org/abs/2511.08065) · [PDF](https://arxiv.org/pdf/2511.08065.pdf)  
**作者**：Ruichen Ma, Liwei Meng, Guanchao Qiao, Ning Ning, Yang Liu, Shaogang Hu  

**一句话要点**：提出I2E框架将静态图像转换为事件流，以解决脉冲神经网络数据稀缺问题。

**关键词**：图像到事件转换, 脉冲神经网络, 数据增强, 神经形态工程, 合成事件数据, 高通量模拟

## 3 点简述
- 核心问题：脉冲神经网络因事件流数据稀缺而应用受限。
- 方法要点：通过模拟微扫视眼动，使用并行卷积实现高速图像到事件流转换。
- 实验或效果：在ImageNet上达到60.50%准确率，CIFAR10-DVS上达92.5%，验证合成数据有效性。

## 摘要（原文）

> Spiking neural networks (SNNs) promise highly energy-efficient computing, but their adoption is hindered by a critical scarcity of event-stream data. This work introduces I2E, an algorithmic framework that resolves this bottleneck by converting static images into high-fidelity event streams. By simulating microsaccadic eye movements with a highly parallelized convolution, I2E achieves a conversion speed over 300x faster than prior methods, uniquely enabling on-the-fly data augmentation for SNN training. The framework's effectiveness is demonstrated on large-scale benchmarks. An SNN trained on the generated I2E-ImageNet dataset achieves a state-of-the-art accuracy of 60.50%. Critically, this work establishes a powerful sim-to-real paradigm where pre-training on synthetic I2E data and fine-tuning on the real-world CIFAR10-DVS dataset yields an unprecedented accuracy of 92.5%. This result validates that synthetic event data can serve as a high-fidelity proxy for real sensor data, bridging a long-standing gap in neuromorphic engineering. By providing a scalable solution to the data problem, I2E offers a foundational toolkit for developing high-performance neuromorphic systems. The open-source algorithm and all generated datasets are provided to accelerate research in the field.

