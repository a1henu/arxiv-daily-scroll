---
layout: default
title: Adaptive and Balanced Re-initialization for Long-timescale Continual Test-time Domain Adaptation
---

# Adaptive and Balanced Re-initialization for Long-timescale Continual Test-time Domain Adaptation
**arXiv**：[2602.06328v1](https://arxiv.org/abs/2602.06328) · [PDF](https://arxiv.org/pdf/2602.06328.pdf)  
**作者**：Yanshuo Wang, Jinguang Tong, Jun Lan, Weiqiang Wang, Huijia Zhu, Haoxing Chen, Xuesong Li, Jie Hong  

**一句话要点**：提出自适应平衡重初始化方法以解决长时持续测试时域适应问题

**关键词**：持续测试时域适应, 长时域适应, 重初始化策略, 标签翻转分析, 自适应间隔, 模型性能保持

## 3 点简述
- 核心问题：模型在长期非平稳环境中性能下降，需保持长期适应能力
- 方法要点：基于标签翻转轨迹模式，自适应调整权重重初始化间隔
- 实验或效果：在多个CTTA基准测试中验证，实现优越性能

## 摘要（原文）

> Continual test-time domain adaptation (CTTA) aims to adjust models so that they can perform well over time across non-stationary environments. While previous methods have made considerable efforts to optimize the adaptation process, a crucial question remains: Can the model adapt to continually changing environments over a long time? In this work, we explore facilitating better CTTA in the long run using a re-initialization (or reset) based method. First, we observe that the long-term performance is associated with the trajectory pattern in label flip. Based on this observed correlation, we propose a simple yet effective policy, Adaptive-and-Balanced Re-initialization (ABR), towards preserving the model's long-term performance. In particular, ABR performs weight re-initialization using adaptive intervals. The adaptive interval is determined based on the change in label flip. The proposed method is validated on extensive CTTA benchmarks, achieving superior performance.

