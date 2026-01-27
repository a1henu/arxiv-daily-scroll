---
layout: default
title: FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learning
---

# FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learning
**arXiv**：[2601.18150v1](https://arxiv.org/abs/2601.18150) · [PDF](https://arxiv.org/pdf/2601.18150.pdf)  
**作者**：Zhaopeng Qiu, Shuang Yu, Jingqi Zhang, Shuai Zhang, Xue Huang, Jingyi Yang, Junjie Lai  

**一句话要点**：提出FP8-RL低精度栈以解决LLM强化学习中rollout阶段的计算与内存瓶颈问题

**关键词**：低精度计算, 强化学习, 大语言模型, KV缓存优化, 训练-推理不匹配, 块状量化

## 3 点简述
- 核心问题：LLM强化学习中rollout阶段因长序列导致注意力与KV缓存内存成为性能瓶颈，且FP8应用面临权重变化和训练-推理不匹配的挑战
- 方法要点：采用块状FP8量化实现W8A8线性层rollout，扩展FP8至KV缓存以缓解长上下文内存压力，并基于重要性采样校正缓解不匹配
- 实验或效果：在密集和MoE模型上实现高达44%的rollout吞吐量提升，同时保持与BF16基线相当的学习行为

## 摘要（原文）

> Reinforcement learning (RL) for large language models (LLMs) is increasingly bottlenecked by rollout (generation), where long output sequence lengths make attention and KV-cache memory dominate end-to-end step time. FP8 offers an attractive lever for accelerating RL by reducing compute cost and memory traffic during rollout, but applying FP8 in RL introduces unique engineering and algorithmic challenges: policy weights change every step (requiring repeated quantization and weight synchronization into the inference engine) and low-precision rollouts can deviate from the higher-precision policy assumed by the trainer, causing train-inference mismatch and potential instability. This report presents a practical FP8 rollout stack for LLM RL, implemented in the veRL ecosystem with support for common training backends (e.g., FSDP/Megatron-LM) and inference engines (e.g., vLLM/SGLang). We (i) enable FP8 W8A8 linear-layer rollout using blockwise FP8 quantization, (ii) extend FP8 to KV-cache to remove long-context memory bottlenecks via per-step QKV scale recalibration, and (iii) mitigate mismatch using importance-sampling-based rollout correction (token-level TIS/MIS variants). Across dense and MoE models, these techniques deliver up to 44% rollout throughput gains while preserving learning behavior comparable to BF16 baselines.

