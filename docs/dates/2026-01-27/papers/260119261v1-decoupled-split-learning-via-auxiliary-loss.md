---
layout: default
title: Decoupled Split Learning via Auxiliary Loss
---

# Decoupled Split Learning via Auxiliary Loss
**arXiv**：[2601.19261v1](https://arxiv.org/abs/2601.19261) · [PDF](https://arxiv.org/pdf/2601.19261.pdf)  
**作者**：Anower Zihad, Felix Owino, Haibo Yang, Ming Tang, Chao Huang  

**一句话要点**：提出基于辅助损失的解耦分割学习，以降低分割学习的通信和内存开销。

**关键词**：分割学习, 解耦训练, 辅助损失, 通信优化, 内存效率

## 3 点简述
- 传统分割学习依赖端到端反向传播，导致高通信和内存开销。
- 方法通过辅助分类器提供本地损失信号，实现客户端和服务器半独立训练。
- 在CIFAR数据集上验证，性能与标准方法相当，通信减少50%，内存降低达58%。

## 摘要（原文）

> Split learning is a distributed training paradigm where a neural network is partitioned between clients and a server, which allows data to remain at the client while only intermediate activations are shared. Traditional split learning relies on end-to-end backpropagation across the client-server split point. This incurs a large communication overhead (i.e., forward activations and backward gradients need to be exchanged every iteration) and significant memory use (for storing activations and gradients). In this paper, we develop a beyond-backpropagation training method for split learning. In this approach, the client and server train their model partitions semi-independently, using local loss signals instead of propagated gradients. In particular, the client's network is augmented with a small auxiliary classifier at the split point to provide a local error signal, while the server trains on the client's transmitted activations using the true loss function. This decoupling removes the need to send backward gradients, which cuts communication costs roughly in half and also reduces memory overhead (as each side only stores local activations for its own backward pass). We evaluate our approach on CIFAR-10 and CIFAR-100. Our experiments show two key results. First, the proposed approach achieves performance on par with standard split learning that uses backpropagation. Second, it significantly reduces communication (of transmitting activations/gradient) by 50% and peak memory usage by up to 58%.

