---
layout: default
title: Tiny Recursive Control: Iterative Reasoning for Efficient Optimal Control
---

# Tiny Recursive Control: Iterative Reasoning for Efficient Optimal Control
**arXiv**：[2512.16824v1](https://arxiv.org/abs/2512.16824) · [PDF](https://arxiv.org/pdf/2512.16824.pdf)  
**作者**：Amit Jain, Richard Linares  

**一句话要点**：提出Tiny Recursive Control，通过迭代推理实现嵌入式系统高效最优控制

**关键词**：递归控制, 最优控制, 嵌入式系统, 神经网络架构, 迭代推理, 航空航天应用

## 3 点简述
- 问题：神经网络控制器参数庞大，不适用于功率和延迟受限的嵌入式航空航天系统。
- 方法：基于迭代深度而非参数数量的递归架构，使用紧凑网络通过两级层次潜在结构重复优化控制序列。
- 效果：在非线性控制任务中实现近最优成本，推理时间毫秒级，内存低于10MB，比语言模型基线小两个数量级。

## 摘要（原文）

> Neural network controllers increasingly demand millions of parameters, and language model approaches push into the billions. For embedded aerospace systems with strict power and latency constraints, this scaling is prohibitive. We present Tiny Recursive Control (TRC), a neural architecture based on a counterintuitive principle: capacity can emerge from iteration depth rather than parameter count. TRC applies compact networks (approximately 1.5M parameters) repeatedly through a two-level hierarchical latent structure, refining control sequences by simulating trajectories and correcting based on tracking error. Because the same weights process every refinement step, adding iterations increases computation without increasing memory. We evaluate TRC on nonlinear control problems including oscillator stabilization and powered descent with fuel constraints. Across these domains, TRC achieves near-optimal control costs while requiring only millisecond-scale inference on GPU and under 10~MB memory, two orders of magnitude smaller than language model baselines. These results demonstrate that recursive reasoning, previously confined to discrete tasks, transfers effectively to continuous control synthesis.

