---
layout: default
title: FedMomentum: Preserving LoRA Training Momentum in Federated Fine-Tuning
---

# FedMomentum: Preserving LoRA Training Momentum in Federated Fine-Tuning
**arXiv**：[2603.08014v1](https://arxiv.org/abs/2603.08014) · [PDF](https://arxiv.org/pdf/2603.08014.pdf)  
**作者**：Peishen Yan, Yang Hua, Hao Wang, Jiaru Zhang, Xiaoyu Wu, Tao Song, Haibing Guan  

**一句话要点**：提出FedMomentum以解决联邦微调中LoRA训练动量丢失问题

**关键词**：联邦学习, 低秩适应, 训练动量, 奇异值分解, 大语言模型微调

## 3 点简述
- 核心问题：LoRA模块在联邦聚合时因数学不正确导致噪声或结构表达受限，训练动量丢失。
- 方法要点：通过SVD结构化聚合LoRA更新，保留主导更新方向并重构低秩模块，维持训练动量。
- 实验或效果：在多项任务中，FedMomentum在收敛速度和最终准确率上优于现有方法。

## 摘要（原文）

> Federated fine-tuning of large language models (LLMs) with low-rank adaptation (LoRA) offers a communication-efficient and privacy-preserving solution for task-specific adaptation. Naive aggregation of LoRA modules introduces noise due to mathematical incorrectness when averaging the downsampling and upsampling matrices independently. However, existing noise-free aggregation strategies inevitably compromise the structural expressiveness of LoRA, limiting its ability to retain client-specific adaptations by either improperly reconstructing the low-rank structure or excluding partially trainable components. We identify this problem as loss of training momentum, where LoRA updates fail to accumulate effectively across rounds, resulting in slower convergence and suboptimal performance. To address this, we propose FedMomentum, a novel framework that enables structured and momentum-preserving LoRA aggregation via singular value decomposition (SVD). Specifically, after aggregating low-rank updates in a mathematically correct manner, FedMomentum applies SVD to extract the dominant components that capture the main update directions. These components are used to reconstruct the LoRA modules with the same rank, while residual components can be retained and later merged into the backbone to preserve semantic information and ensure robustness. Extensive experiments across multiple tasks demonstrate that FedMomentum consistently outperforms prior state-of-the-art methods in convergence speed and final accuracy.

