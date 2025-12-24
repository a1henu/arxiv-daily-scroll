---
layout: default
title: Simplifying Multi-Task Architectures Through Task-Specific Normalization
---

# Simplifying Multi-Task Architectures Through Task-Specific Normalization
**arXiv**：[2512.20420v1](https://arxiv.org/abs/2512.20420) · [PDF](https://arxiv.org/pdf/2512.20420.pdf)  
**作者**：Mihai Suteu, Ovidiu Serban  

**一句话要点**：提出任务特定归一化以简化多任务学习架构，提升性能与效率

**关键词**：多任务学习, 任务特定归一化, 参数效率, 架构简化, 可解释性分析, 深度学习

## 3 点简述
- 多任务学习中共享归一化层导致任务干扰与资源平衡困难
- 用任务特定归一化替代共享归一化，无需复杂模块即可实现竞争性性能
- 在多个数据集上验证，TSσBN提高稳定性与参数效率，并提供可解释性分析

## 摘要（原文）

> Multi-task learning (MTL) aims to leverage shared knowledge across tasks to improve generalization and parameter efficiency, yet balancing resources and mitigating interference remain open challenges. Architectural solutions often introduce elaborate task-specific modules or routing schemes, increasing complexity and overhead. In this work, we show that normalization layers alone are sufficient to address many of these challenges. Simply replacing shared normalization with task-specific variants already yields competitive performance, questioning the need for complex designs. Building on this insight, we propose Task-Specific Sigmoid Batch Normalization (TS$σ$BN), a lightweight mechanism that enables tasks to softly allocate network capacity while fully sharing feature extractors. TS$σ$BN improves stability across CNNs and Transformers, matching or exceeding performance on NYUv2, Cityscapes, CelebA, and PascalContext, while remaining highly parameter-efficient. Moreover, its learned gates provide a natural framework for analyzing MTL dynamics, offering interpretable insights into capacity allocation, filter specialization, and task relationships. Our findings suggest that complex MTL architectures may be unnecessary and that task-specific normalization offers a simple, interpretable, and efficient alternative.

