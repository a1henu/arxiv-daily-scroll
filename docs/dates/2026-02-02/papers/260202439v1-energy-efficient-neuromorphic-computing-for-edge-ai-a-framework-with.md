---
layout: default
title: Energy-Efficient Neuromorphic Computing for Edge AI: A Framework with Adaptive Spiking Neural Networks and Hardware-Aware Optimization
---

# Energy-Efficient Neuromorphic Computing for Edge AI: A Framework with Adaptive Spiking Neural Networks and Hardware-Aware Optimization
**arXiv**：[2602.02439v1](https://arxiv.org/abs/2602.02439) · [PDF](https://arxiv.org/pdf/2602.02439.pdf)  
**作者**：Olaf Yunus Laitinen Imanov, Derya Umut Kulali, Taner Yilmaz, Duygu Erisken, Rana Irem Turhan  

**一句话要点**：提出NeuEdge框架，结合自适应脉冲神经网络与硬件感知优化，以解决边缘AI中能效与延迟问题。

**关键词**：边缘AI, 脉冲神经网络, 硬件感知优化, 能效计算, 自适应阈值, 实时推理

## 3 点简述
- 核心问题：边缘AI部署面临脉冲神经网络训练难、硬件映射开销大及时间动态敏感等挑战。
- 方法要点：采用混合时间编码方案和硬件感知训练，自适应调整神经元阈值以降低能耗。
- 实验或效果：在视觉和音频基准测试中实现高精度与低延迟，无人机案例显示显著节能效果。

## 摘要（原文）

> Edge AI applications increasingly require ultra-low-power, low-latency inference. Neuromorphic computing based on event-driven spiking neural networks (SNNs) offers an attractive path, but practical deployment on resource-constrained devices is limited by training difficulty, hardware-mapping overheads, and sensitivity to temporal dynamics. We present NeuEdge, a framework that combines adaptive SNN models with hardware-aware optimization for edge deployment. NeuEdge uses a temporal coding scheme that blends rate and spike-timing patterns to reduce spike activity while preserving accuracy, and a hardware-aware training procedure that co-optimizes network structure and on-chip placement to improve utilization on neuromorphic processors. An adaptive threshold mechanism adjusts neuron excitability from input statistics, reducing energy consumption without degrading performance. Across standard vision and audio benchmarks, NeuEdge achieves 91-96% accuracy with up to 2.3 ms inference latency on edge hardware and an estimated 847 GOp/s/W energy efficiency. A case study on an autonomous-drone workload shows up to 312x energy savings relative to conventional deep neural networks while maintaining real-time operation.

