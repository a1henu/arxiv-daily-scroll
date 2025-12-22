---
layout: default
title: M2RU: Memristive Minion Recurrent Unit for Continual Learning at the Edge
---

# M2RU: Memristive Minion Recurrent Unit for Continual Learning at the Edge
**arXiv**：[2512.17299v1](https://arxiv.org/abs/2512.17299) · [PDF](https://arxiv.org/pdf/2512.17299.pdf)  
**作者**：Abdullah M. Zyarah, Dhireesha Kudithipudi  

**一句话要点**：提出M2RU混合信号架构，实现边缘设备上的高效持续学习与时间处理。

**关键词**：持续学习, 边缘计算, 混合信号架构, 循环神经网络, 能效优化, 时间处理

## 3 点简述
- 边缘持续学习面临能耗高和数据移动频繁的挑战。
- M2RU集成加权比特流和体验回放机制，支持片上持续学习。
- 实验显示能效提升29倍，在顺序任务中保持接近软件基线的准确率。

## 摘要（原文）

> Continual learning on edge platforms remains challenging because recurrent networks depend on energy-intensive training procedures and frequent data movement that are impractical for embedded deployments. This work introduces M2RU, a mixed-signal architecture that implements the minion recurrent unit for efficient temporal processing with on-chip continual learning. The architecture integrates weighted-bit streaming, which enables multi-bit digital inputs to be processed in crossbars without high-resolution conversion, and an experience replay mechanism that stabilizes learning under domain shifts. M2RU achieves 15 GOPS at 48.62 mW, corresponding to 312 GOPS per watt, and maintains accuracy within 5 percent of software baselines on sequential MNIST and CIFAR-10 tasks. Compared with a CMOS digital design, the accelerator provides 29X improvement in energy efficiency. Device-aware analysis shows an expected operational lifetime of 12.2 years under continual learning workloads. These results establish M2RU as a scalable and energy-efficient platform for real-time adaptation in edge-level temporal intelligence.

