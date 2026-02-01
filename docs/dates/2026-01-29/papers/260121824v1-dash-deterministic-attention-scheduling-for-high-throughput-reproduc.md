---
layout: default
title: DASH: Deterministic Attention Scheduling for High-throughput Reproducible LLM Training
---

# DASH: Deterministic Attention Scheduling for High-throughput Reproducible LLM Training
**arXiv**：[2601.21824v1](https://arxiv.org/abs/2601.21824) · [PDF](https://arxiv.org/pdf/2601.21824.pdf)  
**作者**：Xinwei Qiang, Hongmin Chen, Shixuan Sun, Jingwen Leng, Xin Liu, Minyi Guo  

**一句话要点**：提出DASH调度策略以解决确定性注意力训练中的性能损失问题

**关键词**：确定性训练, 注意力机制, 调度优化, 大语言模型, 可复现性

## 3 点简述
- 核心问题：确定性注意力训练因梯度累积串行化导致高达37.9%的吞吐量下降
- 方法要点：将确定性注意力反向传播建模为DAG调度问题，设计最小化关键路径长度的调度策略
- 实验或效果：在NVIDIA H800 GPU上，DASH将注意力反向传播吞吐量提升至基线1.28倍

## 摘要（原文）

> Determinism is indispensable for reproducibility in large language model (LLM) training, yet it often exacts a steep performance cost. In widely used attention implementations such as FlashAttention-3, the deterministic backward pass can incur up to a 37.9% throughput reduction relative to its non-deterministic counterpart, primarily because gradient accumulation operations must be serialized to guarantee numerical consistency. This performance loss stems from suboptimal scheduling of compute and gradient-reduction phases, leading to significant hardware underutilization.
>   To address this challenge, we formulate the backward pass of deterministic attention as a scheduling problem on a Directed Acyclic Graph (DAG) and derive schedules that minimize the critical path length. Building on this formulation, we present DASH (Deterministic Attention Scheduling for High-Throughput), which encapsulates two complementary scheduling strategies: (i) Descending Q-Tile Iteration, a reversed query-block traversal that shrinks pipeline stalls in causal attention, and (ii) Shift Scheduling, a theoretically optimal schedule within our DAG model that reduces pipeline stalls for both full and causal masks.
>   Our empirical evaluations on NVIDIA H800 GPUs demonstrate that DASH narrows the performance gap of deterministic attention. The proposed strategies improve the throughput of the attention backward pass by up to 1.28$\times$ compared to the baseline, significantly advancing the efficiency of reproducible LLM training.
>   Our code is open-sourced at https://github.com/SJTU-Liquid/deterministic-FA3.

