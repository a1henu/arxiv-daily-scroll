---
layout: default
title: From Hawkes Processes to Attention: Time-Modulated Mechanisms for Event Sequences
---

# From Hawkes Processes to Attention: Time-Modulated Mechanisms for Event Sequences
**arXiv**：[2601.09220v1](https://arxiv.org/abs/2601.09220) · [PDF](https://arxiv.org/pdf/2601.09220.pdf)  
**作者**：Xinzi Tan, Kejian Zhang, Junhan Yu, Doudou Zhou  

**一句话要点**：提出Hawkes Attention以解决标记时间点过程中异质时间效应建模不足的问题

**关键词**：标记时间点过程, Hawkes Attention, 时间调制机制, 事件序列建模, Transformer改进

## 3 点简述
- 现有Transformer方法在标记时间点过程中依赖共享或参数化衰减结构，难以捕捉异质和类型特定时间效应
- 从多元Hawkes过程理论推导Hawkes Attention，使用可学习的每类型神经核调制查询、键和值投影，统一事件时间和内容交互
- 实验表明方法在标记时间点过程和时序预测等任务中优于基线，能学习时间相关行为和类型特定激发模式

## 摘要（原文）

> Marked Temporal Point Processes (MTPPs) arise naturally in medical, social, commercial, and financial domains. However, existing Transformer-based methods mostly inject temporal information only via positional encodings, relying on shared or parametric decay structures, which limits their ability to capture heterogeneous and type-specific temporal effects. Inspired by this observation, we derive a novel attention operator called Hawkes Attention from the multivariate Hawkes process theory for MTPP, using learnable per-type neural kernels to modulate query, key and value projections, thereby replacing the corresponding parts in the traditional attention. Benefited from the design, Hawkes Attention unifies event timing and content interaction, learning both the time-relevant behavior and type-specific excitation patterns from the data. The experimental results show that our method achieves better performance compared to the baselines. In addition to the general MTPP, our attention mechanism can also be easily applied to specific temporal structures, such as time series forecasting.

