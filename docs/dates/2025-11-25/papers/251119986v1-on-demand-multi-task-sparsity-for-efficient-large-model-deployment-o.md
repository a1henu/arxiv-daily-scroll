---
layout: default
title: On-Demand Multi-Task Sparsity for Efficient Large-Model Deployment on Edge Devices
---

# On-Demand Multi-Task Sparsity for Efficient Large-Model Deployment on Edge Devices
**arXiv**：[2511.19986v1](https://arxiv.org/abs/2511.19986) · [PDF](https://arxiv.org/pdf/2511.19986.pdf)  
**作者**：Lianming Huang, Haibo Hu, Qiao Li, Nan Guan, Chun Jason Xue  

**一句话要点**：提出按需多任务稀疏框架以最小化边缘设备任务切换开销

**关键词**：边缘计算, 模型稀疏化, 多任务学习, 参数复用, 任务切换优化

## 3 点简述
- 核心问题：传统稀疏方法忽略任务切换时的I/O开销，导致冷启动延迟
- 方法要点：将权重分解为可重用块单元，跨任务对齐稀疏结构以最大化参数复用
- 实验效果：在自动驾驶平台测试，任务切换加速平均超过6.6倍

## 摘要（原文）

> Sparsity is essential for deploying large models on resource constrained edge platforms. However, optimizing sparsity patterns for individual tasks in isolation ignores the significant I/O overhead incurred during frequent task switching. We introduce an on-demand multi-task sparsity framework specifically designed to minimize switching costs by maximizing parameter reuse. Unlike monolithic approaches, we decompose weights into reusable block-granular units and align sparse structures across tasks to maximize overlap. By dynamically loading only the small differential set of blocks required for the next task, our method effectively mitigates the cold-start latency inherent in traditional monolithic approaches.Experiments on a real-world autonomous driving platform demonstrate that our framework achieves superior switching efficiency, accelerating task switching by over 6.6X on average compared to existing sparsity methods.

