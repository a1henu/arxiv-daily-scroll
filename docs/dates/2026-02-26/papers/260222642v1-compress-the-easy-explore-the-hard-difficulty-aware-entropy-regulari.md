---
layout: default
title: Compress the Easy, Explore the Hard: Difficulty-Aware Entropy Regularization for Efficient LLM Reasoning
---

# Compress the Easy, Explore the Hard: Difficulty-Aware Entropy Regularization for Efficient LLM Reasoning
**arXiv**：[2602.22642v1](https://arxiv.org/abs/2602.22642) · [PDF](https://arxiv.org/pdf/2602.22642.pdf)  
**作者**：Qin-Wen Luo, Sheng Ren, Xiang Chen, Rui Liu, Jun Fang, Naiqiang Tan, Sheng-Jun Huang  

**一句话要点**：提出难度感知熵正则化方法CEEH，以解决LLM推理中压缩与探索的平衡问题

**关键词**：大语言模型推理, 思维链压缩, 难度感知学习, 熵正则化, 强化学习优化

## 3 点简述
- 核心问题：现有推理压缩方法易导致熵崩溃，牺牲推理能力换取简短性
- 方法要点：动态评估问题难度，对困难问题保持探索空间，对简单问题进行压缩
- 实验效果：在六个基准测试中保持准确率的同时显著缩短响应长度

## 摘要（原文）

> Chain-of-Thought (CoT) has substantially empowered Large Language Models (LLMs) to tackle complex reasoning tasks, yet the verbose nature of explicit reasoning steps incurs prohibitive inference latency and computational costs, limiting real-world deployment. While existing compression methods - ranging from self-training to Reinforcement Learning (RL) with length constraints - attempt to mitigate this, they often sacrifice reasoning capability for brevity. We identify a critical failure mode in these approaches: explicitly optimizing for shorter trajectories triggers rapid entropy collapse, which prematurely shrinks the exploration space and stifles the discovery of valid reasoning paths, particularly for challenging questions requiring extensive deduction. To address this issue, we propose Compress responses for Easy questions and Explore Hard ones (CEEH), a difficulty-aware approach to RL-based efficient reasoning. CEEH dynamically assesses instance difficulty to apply selective entropy regularization: it preserves a diverse search space for currently hard questions to ensure robustness, while permitting aggressive compression on easier instances where the reasoning path is well-established. In addition, we introduce a dynamic optimal-length penalty anchored to the historically shortest correct response, which effectively counteracts entropy-induced length inflation and stabilizes the reward signal. Across six reasoning benchmarks, CEEH consistently reduces response length while maintaining accuracy comparable to the base model, and improves Pass@k relative to length-only optimization.

