---
layout: default
title: DendroNN: Dendrocentric Neural Networks for Energy-Efficient Classification of Event-Based Data
---

# DendroNN: Dendrocentric Neural Networks for Energy-Efficient Classification of Event-Based Data
**arXiv**：[2603.09274v1](https://arxiv.org/abs/2603.09274) · [PDF](https://arxiv.org/pdf/2603.09274.pdf)  
**作者**：Jann Krausse, Zhe Su, Kyrus Mama, Maryada, Klaus Knobloch, Giacomo Indiveri, Jürgen Becker  

**一句话要点**：提出DendroNN以解决事件数据分类中能效与时间解码精度的平衡问题

**关键词**：事件驱动计算, 脉冲神经网络, 树突计算, 硬件效率, 时空特征, 音频分类

## 3 点简述
- 核心问题：前馈脉冲神经网络在事件数据分类中时间解码精度低，依赖延迟或循环降低硬件效率
- 方法要点：基于树突序列检测机制，引入DendroNN识别时空特征，通过重连训练非可微序列
- 实验或效果：在事件时间序列数据集上实现竞争性精度，硬件架构比先进神经形态硬件能效提升高达4倍

## 摘要（原文）

> Spatiotemporal information is at the core of diverse sensory processing and computational tasks. Feed-forward spiking neural networks can be used to solve these tasks while offering potential benefits in terms of energy efficiency by computing event-based. However, they have trouble decoding temporal information with high accuracy. Thus, they commonly resort to recurrence or delays to enhance their temporal computing ability which, however, bring downsides in terms of hardware-efficiency. In the brain, dendrites are computational powerhouses that just recently started to be acknowledged in such machine learning systems. In this work, we focus on a sequence detection mechanism present in branches of dendrites and translate it into a novel type of neural network by introducing a dendrocentric neural network, DendroNN. DendroNNs identify unique incoming spike sequences as spatiotemporal features. This work further introduces a rewiring phase to train the non-differentiable spike sequences without the use of gradients. During the rewiring, the network memorizes frequently occurring sequences and additionally discards those that do not contribute any discriminative information. The networks display competitive accuracies across various event-based time series datasets. We also propose an asynchronous digital hardware architecture using a time-wheel mechanism that builds on the event-driven design of DendroNNs, eliminating per-step global updates typical of delay- or recurrence-based models. By leveraging a DendroNN's dynamic and static sparsity along with intrinsic quantization, it achieves up to 4x higher efficiency than state-of-the-art neuromorphic hardware at comparable accuracy on the same audio classification task, demonstrating its suitability for spatiotemporal event-based computing. This work offers a novel approach to low-power spatiotemporal processing on event-driven hardware.

