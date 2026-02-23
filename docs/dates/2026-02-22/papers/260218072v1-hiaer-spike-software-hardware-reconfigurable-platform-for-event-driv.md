---
layout: default
title: HiAER-Spike Software-Hardware Reconfigurable Platform for Event-Driven Neuromorphic Computing at Scale
---

# HiAER-Spike Software-Hardware Reconfigurable Platform for Event-Driven Neuromorphic Computing at Scale
**arXiv**：[2602.18072v1](https://arxiv.org/abs/2602.18072) · [PDF](https://arxiv.org/pdf/2602.18072.pdf)  
**作者**：Gwenevere Frank, Gopabandhu Hota, Keli Wang, Christopher Deng, Krish Arora, Diana Vins, Abhinav Uppal, Omowuyi Olajide, Kenneth Yoshimoto, Qingbo Wang, Mari Yamaoka, Johannes Leugering, Stephen Deiss, Leif Gibb, Gert Cauwenberghs  

**一句话要点**：提出HiAER-Spike软硬件可重构平台，用于大规模事件驱动神经形态计算

**关键词**：神经形态计算, 脉冲神经网络, 事件驱动架构, 软硬件协同设计, 分层地址事件路由, 大规模并行处理

## 3 点简述
- 核心问题：大规模脉冲神经网络执行需高效处理稀疏连接与活动，支持边缘与云计算
- 方法要点：采用模块化软硬件协同设计，优化分层地址事件路由和内存效率
- 实验或效果：在CIFAR-10、DVS手势等任务中展示事件驱动视觉能力，支持1.6亿神经元实时处理

## 摘要（原文）

> In this work, we present HiAER-Spike, a modular, reconfigurable, event-driven neuromorphic computing platform designed to execute large spiking neural networks with up to 160 million neurons and 40 billion synapses - roughly twice the neurons of a mouse brain at faster than real time. This system, assembled at the UC San Diego Supercomputer Center, comprises a co-designed hard- and software stack that is optimized for run-time massively parallel processing and hierarchical address-event routing (HiAER) of spikes while promoting memory-efficient network storage and execution. The architecture efficiently handles both sparse connectivity and sparse activity for robust and low-latency event-driven inference for both edge and cloud computing. A Python programming interface to HiAER-Spike, agnostic to hardware-level detail, shields the user from complexity in the configuration and execution of general spiking neural networks with minimal constraints in topology. The system is made easily available over a web portal for use by the wider community. In the following, we provide an overview of the hard- and software stack, explain the underlying design principles, demonstrate some of the system's capabilities and solicit feedback from the broader neuromorphic community. Examples are shown demonstrating HiAER-Spike's capabilities for event-driven vision on benchmark CIFAR-10, DVS event-based gesture, MNIST, and Pong tasks.

