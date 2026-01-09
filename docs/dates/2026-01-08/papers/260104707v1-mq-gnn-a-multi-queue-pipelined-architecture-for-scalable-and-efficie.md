---
layout: default
title: MQ-GNN: A Multi-Queue Pipelined Architecture for Scalable and Efficient GNN Training
---

# MQ-GNN: A Multi-Queue Pipelined Architecture for Scalable and Efficient GNN Training
**arXiv**：[2601.04707v1](https://arxiv.org/abs/2601.04707) · [PDF](https://arxiv.org/pdf/2601.04707.pdf)  
**作者**：Irfan Ullah, Young-Koo Lee  

**一句话要点**：提出MQ-GNN多队列流水线框架以解决多GPU图神经网络训练中的可扩展性和效率问题

**关键词**：图神经网络训练, 多GPU并行, 异步梯度更新, 流水线架构, 可扩展性优化

## 3 点简述
- 核心问题：图神经网络训练存在小批量生成低效、数据传输瓶颈和GPU间同步成本高的问题
- 方法要点：引入RaCoM实现异步梯度共享和模型更新，结合全局邻居采样与缓存及自适应队列大小策略
- 实验或效果：在四个大规模数据集上，MQ-GNN实现最高4.6倍训练加速和30%GPU利用率提升，同时保持准确率

## 摘要（原文）

> Graph Neural Networks (GNNs) are powerful tools for learning graph-structured data, but their scalability is hindered by inefficient mini-batch generation, data transfer bottlenecks, and costly inter-GPU synchronization. Existing training frameworks fail to overlap these stages, leading to suboptimal resource utilization. This paper proposes MQ-GNN, a multi-queue pipelined framework that maximizes training efficiency by interleaving GNN training stages and optimizing resource utilization. MQ-GNN introduces Ready-to-Update Asynchronous Consistent Model (RaCoM), which enables asynchronous gradient sharing and model updates while ensuring global consistency through adaptive periodic synchronization. Additionally, it employs global neighbor sampling with caching to reduce data transfer overhead and an adaptive queue-sizing strategy to balance computation and memory efficiency. Experiments on four large-scale datasets and ten baseline models demonstrate that MQ-GNN achieves up to \boldmath $\bm{4.6\,\times}$ faster training time and 30% improved GPU utilization while maintaining competitive accuracy. These results establish MQ-GNN as a scalable and efficient solution for multi-GPU GNN training.

