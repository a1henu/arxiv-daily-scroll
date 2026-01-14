---
layout: default
title: Reducing Compute Waste in LLMs through Kernel-Level DVFS
---

# Reducing Compute Waste in LLMs through Kernel-Level DVFS
**arXiv**：[2601.08539v1](https://arxiv.org/abs/2601.08539) · [PDF](https://arxiv.org/pdf/2601.08539.pdf)  
**作者**：Jeffrey Spaan, Kuan-Hsun Chen, Ana-Lucia Varbanescu  

**一句话要点**：提出细粒度核级DVFS以减少大语言模型操作中的计算浪费

**关键词**：大语言模型, 动态电压频率调整, 能效优化, 核级调度, 计算浪费减少, GPU加速

## 3 点简述
- 核心问题：AI数据中心能耗增长成为瓶颈，现有DVFS方法节能但导致显著性能下降
- 方法要点：采用细粒度核级DVFS探索新频率配置，优于传统pass或迭代级方案
- 实验或效果：在GPT-3训练中节能14.6%，仅慢0.6%，且适用于数据和张量并行

## 摘要（原文）

> The rapid growth of AI has fueled the expansion of accelerator- or GPU-based data centers. However, the rising operational energy consumption has emerged as a critical bottleneck and a major sustainability concern. Dynamic Voltage and Frequency Scaling (DVFS) is a well-known technique used to reduce energy consumption, and thus improve energy-efficiency, since it requires little effort and works with existing hardware. Reducing the energy consumption of training and inference of Large Language Models (LLMs) through DVFS or power capping is feasible: related work has shown energy savings can be significant, but at the cost of significant slowdowns. In this work, we focus on reducing waste in LLM operations: i.e., reducing energy consumption without losing performance. We propose a fine-grained, kernel-level, DVFS approach that explores new frequency configurations, and prove these save more energy than previous, pass- or iteration-level solutions. For example, for a GPT-3 training run, a pass-level approach could reduce energy consumption by 2% (without losing performance), while our kernel-level approach saves as much as 14.6% (with a 0.6% slowdown). We further investigate the effect of data and tensor parallelism, and show our discovered clock frequencies translate well for both. We conclude that kernel-level DVFS is a suitable technique to reduce waste in LLM operations, providing significant energy savings with negligible slow-down.

