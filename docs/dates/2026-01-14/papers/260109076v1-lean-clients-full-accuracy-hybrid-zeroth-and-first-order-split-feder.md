---
layout: default
title: Lean Clients, Full Accuracy: Hybrid Zeroth- and First-Order Split Federated Learning
---

# Lean Clients, Full Accuracy: Hybrid Zeroth- and First-Order Split Federated Learning
**arXiv**：[2601.09076v1](https://arxiv.org/abs/2601.09076) · [PDF](https://arxiv.org/pdf/2601.09076.pdf)  
**作者**：Zhoubin Kou, Zihan Chen, Jing Yang, Cong Shen  

**一句话要点**：提出HERON-SFL混合优化框架，以解决分割联邦学习中客户端计算资源受限问题

**关键词**：分割联邦学习, 零阶优化, 混合优化, 资源受限设备, 模型训练扩展

## 3 点简述
- 核心问题：分割联邦学习中客户端反向传播计算成本高，限制模型规模扩展
- 方法要点：客户端采用零阶优化近似梯度，服务器保留一阶优化，结合辅助网络减少通信
- 实验或效果：在ResNet和语言模型任务中，匹配基准精度，降低客户端峰值内存和计算成本

## 摘要（原文）

> Split Federated Learning (SFL) enables collaborative training between resource-constrained edge devices and a compute-rich server. Communication overhead is a central issue in SFL and can be mitigated with auxiliary networks. Yet, the fundamental client-side computation challenge remains, as back-propagation requires substantial memory and computation costs, severely limiting the scale of models that edge devices can support. To enable more resource-efficient client computation and reduce the client-server communication, we propose HERON-SFL, a novel hybrid optimization framework that integrates zeroth-order (ZO) optimization for local client training while retaining first-order (FO) optimization on the server. With the assistance of auxiliary networks, ZO updates enable clients to approximate local gradients using perturbed forward-only evaluations per step, eliminating memory-intensive activation caching and avoiding explicit gradient computation in the traditional training process. Leveraging the low effective rank assumption, we theoretically prove that HERON-SFL's convergence rate is independent of model dimensionality, addressing a key scalability concern common to ZO algorithms. Empirically, on ResNet training and language model (LM) fine-tuning tasks, HERON-SFL matches benchmark accuracy while reducing client peak memory by up to 64% and client-side compute cost by up to 33% per step, substantially expanding the range of models that can be trained or adapted on resource-limited devices.

