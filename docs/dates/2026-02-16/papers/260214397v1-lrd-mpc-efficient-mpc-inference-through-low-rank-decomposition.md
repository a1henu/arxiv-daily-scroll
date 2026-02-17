---
layout: default
title: LRD-MPC: Efficient MPC Inference through Low-rank Decomposition
---

# LRD-MPC: Efficient MPC Inference through Low-rank Decomposition
**arXiv**：[2602.14397v1](https://arxiv.org/abs/2602.14397) · [PDF](https://arxiv.org/pdf/2602.14397.pdf)  
**作者**：Tingting Tang, Yongqin Wang, Murali Annavaram  

**一句话要点**：提出LRD-MPC，通过低秩分解优化安全多方计算中的推理效率

**关键词**：安全多方计算, 低秩分解, 机器学习推理, 通信优化, 计算效率, 隐私保护

## 3 点简述
- 核心问题：MPC在机器学习推理中因矩阵乘法导致高计算和通信开销
- 方法要点：利用低秩分解减少矩阵乘法规模，结合截断跳过和线性层拼接优化
- 实验效果：在n-PC和3-PC协议中分别实现最高25%和33%加速，显著降低能耗

## 摘要（原文）

> Secure Multi-party Computation (MPC) enables untrusted parties to jointly compute a function without revealing their inputs. Its application to machine learning (ML) has gained significant attention, particularly for secure inference services deployed across multiple cloud virtual machines (VMs), where each VM acts as an MPC party. Model providers secret-share model weights, and users secret-share inputs, ensuring that each server operates only on random shares. While MPC provides strong cryptographic guarantees, it incurs substantial computational and communication overhead. Deep neural networks rely heavily on convolutional and fully connected layers, which require costly matrix multiplications in MPC. To reduce this cost, we propose leveraging low-rank decomposition (LRD) for linear layers, replacing one large matrix multiplication with two smaller ones. Each matrix multiplication in MPC incurs a round of communication, meaning decomposing one matrix multiplication into two leads to an additional communication round. Second, the added matrix multiplication requires an additional truncation step to maintain numerical precision. Since truncation itself requires communication and computation, these overheads can offset the gains from decomposition. To address this, we introduce two complementary optimizations: truncation skipping and efficient linear layer concatenation. Truncation skipping removes the extra truncation induced by LRD, while linear layer concatenation pipelines operations to hide the additional communication round. Together, these techniques mitigate the main overheads of LRD in MPC and improve overall efficiency. Our approach is broadly applicable across MPC protocols. Experiments show up to 25% speedup in n-PC and 33% in 3-PC protocols over full-rank baselines, along with up to 52% GPU energy savings and 88% reduction in offline-phase latency.

