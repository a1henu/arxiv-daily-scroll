---
layout: default
title: PRISM: Parametrically Refactoring Inference for Speculative Sampling Draft Models
---

# PRISM: Parametrically Refactoring Inference for Speculative Sampling Draft Models
**arXiv**：[2602.01762v1](https://arxiv.org/abs/2602.01762) · [PDF](https://arxiv.org/pdf/2602.01762.pdf)  
**作者**：Xuliang Wang, Yuetao Chen, Maochan Zhen, Fang Liu, Xinzhou Zheng, Xingwu Liu, Hong Xu, Ming Li  

**一句话要点**：提出PRISM架构以解决推测解码中草稿模型计算开销与质量权衡问题

**关键词**：推测解码, 草稿模型, 推理加速, 参数重构, 计算解耦

## 3 点简述
- 核心问题：大语言模型自回归解码慢，推测解码中草稿模型参数增大导致计算开销高
- 方法要点：通过参数化重构草稿模型计算路径，解耦模型容量与推理成本
- 实验或效果：PRISM在保持低延迟下实现高接受长度，解码吞吐量提升超2.6倍

## 摘要（原文）

> Large Language Models (LLMs), constrained by their auto-regressive nature, suffer from slow decoding. Speculative decoding methods have emerged as a promising solution to accelerate LLM decoding, attracting attention from both systems and AI research communities. Recently, the pursuit of better draft quality has driven a trend toward parametrically larger draft models, which inevitably introduces substantial computational overhead. While existing work attempts to balance the trade-off between prediction accuracy and compute latency, we address this fundamental dilemma through architectural innovation.
>   We propose PRISM, which disaggregates the computation of each predictive step across different parameter sets, refactoring the computational pathways of draft models to successfully decouple model capacity from inference cost. Through extensive experiments, we demonstrate that PRISM outperforms all existing draft architectures, achieving exceptional acceptance lengths while maintaining minimal draft latency for superior end-to-end speedup. We also re-examine scaling laws with PRISM, revealing that PRISM scales more effectively with expanding data volumes than other draft architectures. Through rigorous and fair comparison, we show that PRISM boosts the decoding throughput of an already highly optimized inference engine by more than 2.6x.

