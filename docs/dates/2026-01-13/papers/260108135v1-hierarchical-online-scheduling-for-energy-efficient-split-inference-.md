---
layout: default
title: Hierarchical Online-Scheduling for Energy-Efficient Split Inference with Progressive Transmission
---

# Hierarchical Online-Scheduling for Energy-Efficient Split Inference with Progressive Transmission
**arXiv**：[2601.08135v1](https://arxiv.org/abs/2601.08135) · [PDF](https://arxiv.org/pdf/2601.08135.pdf)  
**作者**：Zengzipeng Tang, Yuxuan Sun, Wei Chen, Jianwen Ding, Bo Ai, Yulin Shao  

**一句话要点**：提出ENACHI框架，通过分层调度与渐进传输优化设备-边缘协同推理的能效与精度

**关键词**：设备-边缘协同推理, 分层调度, 渐进传输, 能效优化, 在线决策

## 3 点简述
- 核心问题：任务级调度与包级信道动态不匹配，导致资源利用效率低
- 方法要点：开发基于Lyapunov的两层框架，结合任务级决策与包级渐进传输
- 实验或效果：在ImageNet上优于基准方法，在严格时延下精度提升43.12%，能耗降低62.13%

## 摘要（原文）

> Device-edge collaborative inference with Deep Neural Networks (DNNs) faces fundamental trade-offs among accuracy, latency and energy consumption. Current scheduling exhibits two drawbacks: a granularity mismatch between coarse, task-level decisions and fine-grained, packet-level channel dynamics, and insufficient awareness of per-task complexity. Consequently, scheduling solely at the task level leads to inefficient resource utilization. This paper proposes a novel ENergy-ACcuracy Hierarchical optimization framework for split Inference, named ENACHI, that jointly optimizes task- and packet-level scheduling to maximize accuracy under energy and delay constraints. A two-tier Lyapunov-based framework is developed for ENACHI, with a progressive transmission technique further integrated to enhance adaptivity. At the task level, an outer drift-plus-penalty loop makes online decisions for DNN partitioning and bandwidth allocation, and establishes a reference power budget to manage the long-term energy-accuracy trade-off. At the packet level, an uncertainty-aware progressive transmission mechanism is employed to adaptively manage per-sample task complexity. This is integrated with a nested inner control loop implementing a novel reference-tracking policy, which dynamically adjusts per-slot transmit power to adapt to fluctuating channel conditions. Experiments on ImageNet dataset demonstrate that ENACHI outperforms state-of-the-art benchmarks under varying deadlines and bandwidths, achieving a 43.12\% gain in inference accuracy with a 62.13\% reduction in energy consumption under stringent deadlines, and exhibits high scalability by maintaining stable energy consumption in congested multi-user scenarios.

