---
layout: default
title: CoCo-Fed: A Unified Framework for Memory- and Communication-Efficient Federated Learning at the Wireless Edge
---

# CoCo-Fed: A Unified Framework for Memory- and Communication-Efficient Federated Learning at the Wireless Edge
**arXiv**：[2601.00549v1](https://arxiv.org/abs/2601.00549) · [PDF](https://arxiv.org/pdf/2601.00549.pdf)  
**作者**：Zhiheng Guo, Zhaoyang Liu, Zihan Cen, Chenyuan Feng, Xinghua Sun, Xiang Chen, Tony Q. S. Quek, Xijun Wang  

**一句话要点**：提出CoCo-Fed框架以解决无线边缘联邦学习中内存与通信效率瓶颈

**关键词**：联邦学习, 无线边缘计算, 内存优化, 通信压缩, O-RAN架构, 非独立同分布学习

## 3 点简述
- 核心问题：O-RAN中大规模神经网络部署面临本地内存不足和回程带宽饱和的挑战
- 方法要点：本地采用双维度梯度降维优化，全局基于正交子空间叠加传输协议
- 实验或效果：在到达角估计任务中，非独立同分布下显著提升效率并保持收敛

## 摘要（原文）

> The deployment of large-scale neural networks within the Open Radio Access Network (O-RAN) architecture is pivotal for enabling native edge intelligence. However, this paradigm faces two critical bottlenecks: the prohibitive memory footprint required for local training on resource-constrained gNBs, and the saturation of bandwidth-limited backhaul links during the global aggregation of high-dimensional model updates. To address these challenges, we propose CoCo-Fed, a novel Compression and Combination-based Federated learning framework that unifies local memory efficiency and global communication reduction. Locally, CoCo-Fed breaks the memory wall by performing a double-dimension down-projection of gradients, adapting the optimizer to operate on low-rank structures without introducing additional inference parameters/latency. Globally, we introduce a transmission protocol based on orthogonal subspace superposition, where layer-wise updates are projected and superimposed into a single consolidated matrix per gNB, drastically reducing the backhaul traffic. Beyond empirical designs, we establish a rigorous theoretical foundation, proving the convergence of CoCo-Fed even under unsupervised learning conditions suitable for wireless sensing tasks. Extensive simulations on an angle-of-arrival estimation task demonstrate that CoCo-Fed significantly outperforms state-of-the-art baselines in both memory and communication efficiency while maintaining robust convergence under non-IID settings.

