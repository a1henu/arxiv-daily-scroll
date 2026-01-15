---
layout: default
title: Hidden States as Early Signals: Step-level Trace Evaluation and Pruning for Efficient Test-Time Scaling
---

# Hidden States as Early Signals: Step-level Trace Evaluation and Pruning for Efficient Test-Time Scaling
**arXiv**：[2601.09093v1](https://arxiv.org/abs/2601.09093) · [PDF](https://arxiv.org/pdf/2601.09093.pdf)  
**作者**：Zhixiang Liang, Beichen Huang, Zheng Wang, Minjia Zhang  

**一句话要点**：提出STEP框架，利用隐藏状态评估推理步骤，动态剪枝以降低大语言模型测试时扩展的延迟。

**关键词**：大语言模型, 推理加速, 动态剪枝, 隐藏状态评估, 测试时扩展, GPU内存优化

## 3 点简述
- 核心问题：大语言模型测试时扩展中，长推理轨迹和多采样导致高计算开销和延迟。
- 方法要点：训练轻量级步骤评分器，基于隐藏状态评估推理质量，设计GPU内存感知的动态剪枝策略。
- 实验或效果：在推理基准测试中，平均降低延迟45%-70%，同时提高推理准确性。

## 摘要（原文）

> Large Language Models (LLMs) can enhance reasoning capabilities through test-time scaling by generating multiple traces. However, the combination of lengthy reasoning traces with multiple sampling introduces substantial computation and high end-to-end latency. Prior work on accelerating this process has relied on similarity-based or confidence-based pruning, but these signals do not reliably indicate trace quality. To address these limitations, we propose STEP: Step-level Trace Evaluation and Pruning, a novel pruning framework that evaluates reasoning steps using hidden states and dynamically prunes unpromising traces during generation. We train a lightweight step scorer to estimate trace quality, and design a GPU memory-aware pruning strategy that triggers pruning as the GPU memory is saturated by KV cache to reduce end-to-end latency. Experiments across challenging reasoning benchmarks demonstrate that STEP reduces end-to-end inference latency by 45%-70% on average compared to self-consistency while also improving reasoning accuracy. Our code is released at: https://github.com/Supercomputing-System-AI-Lab/STEP

