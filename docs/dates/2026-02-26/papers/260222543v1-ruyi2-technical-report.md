---
layout: default
title: Ruyi2 Technical Report
---

# Ruyi2 Technical Report
**arXiv**：[2602.22543v1](https://arxiv.org/abs/2602.22543) · [PDF](https://arxiv.org/pdf/2602.22543.pdf)  
**作者**：Huan Song, Shuyu Tian, Junyi Hao, Minxiu Xu, Hongjun An, Yiliang Song, Jiawei Shao, Xuelong Li  

**一句话要点**：提出Ruyi2自适应模型以解决大语言模型部署成本与延迟问题

**关键词**：自适应计算, 家族模型, 3D并行训练, 大语言模型部署, 参数共享

## 3 点简述
- 核心问题：大语言模型面临高部署成本和延迟，需自适应计算策略。
- 方法要点：基于AI Flow框架，引入稳定家族模型，采用3D并行训练优化。
- 实验或效果：相比Ruyi提速2-3倍，性能媲美同规模Qwen3模型。

## 摘要（原文）

> Large Language Models (LLMs) face significant challenges regarding deployment costs and latency, necessitating adaptive computing strategies. Building upon the AI Flow framework, we introduce Ruyi2 as an evolution of our adaptive model series designed for efficient variable-depth computation. While early-exit architectures offer a viable efficiency-performance balance, the Ruyi model and existing methods often struggle with optimization complexity and compatibility with large-scale distributed training. To bridge this gap, Ruyi2 introduces a stable "Familial Model" based on Megatron-LM. By using 3D parallel training, it achieves a 2-3 times speedup over Ruyi, while performing comparably to same-sized Qwen3 models. These results confirm that family-based parameter sharing is a highly effective strategy, establishing a new "Train Once, Deploy Many" paradigm and providing a key reference for balancing architectural efficiency with high-performance capabilities.

