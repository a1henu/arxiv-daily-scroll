---
layout: default
title: M3Net: A Multi-Metric Mixture of Experts Network Digital Twin with Graph Neural Networks
---

# M3Net: A Multi-Metric Mixture of Experts Network Digital Twin with Graph Neural Networks
**arXiv**：[2512.09797v1](https://arxiv.org/abs/2512.09797) · [PDF](https://arxiv.org/pdf/2512.09797.pdf)  
**作者**：Blessed Guda, Carlee Joe-Wong  

**一句话要点**：提出M3Net网络数字孪生模型，利用图神经网络和专家混合架构预测多性能指标以优化网络管理。

**关键词**：网络数字孪生, 图神经网络, 专家混合模型, 多性能指标预测, 网络管理优化

## 3 点简述
- 核心问题：5G/6G网络应用需求多样，传统网络建模方法在准确性和可扩展性上难以平衡。
- 方法要点：采用图神经网络和专家混合架构，从扩展的网络状态数据中估计多个性能指标。
- 实验或效果：显著提升流延迟预测准确性，MAPE从20.06%降至17.39%，并在抖动和丢包率预测上达到高准确度。

## 摘要（原文）

> The rise of 5G/6G network technologies promises to enable applications like autonomous vehicles and virtual reality, resulting in a significant increase in connected devices and necessarily complicating network management. Even worse, these applications often have strict, yet heterogeneous, performance requirements across metrics like latency and reliability. Much recent work has thus focused on developing the ability to predict network performance. However, traditional methods for network modeling, like discrete event simulators and emulation, often fail to balance accuracy and scalability. Network Digital Twins (NDTs), augmented by machine learning, present a viable solution by creating virtual replicas of physical networks for real- time simulation and analysis. State-of-the-art models, however, fall short of full-fledged NDTs, as they often focus only on a single performance metric or simulated network data. We introduce M3Net, a Multi-Metric Mixture-of-experts (MoE) NDT that uses a graph neural network architecture to estimate multiple performance metrics from an expanded set of network state data in a range of scenarios. We show that M3Net significantly enhances the accuracy of flow delay predictions by reducing the MAPE (Mean Absolute Percentage Error) from 20.06% to 17.39%, while also achieving 66.47% and 78.7% accuracy on jitter and packets dropped for each flow

