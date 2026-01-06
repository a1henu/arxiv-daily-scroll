---
layout: default
title: Streaming Hallucination Detection in Long Chain-of-Thought Reasoning
---

# Streaming Hallucination Detection in Long Chain-of-Thought Reasoning
**arXiv**：[2601.02170v1](https://arxiv.org/abs/2601.02170) · [PDF](https://arxiv.org/pdf/2601.02170.pdf)  
**作者**：Haolang Lu, Minghui Pan, Ripeng Li, Guoshun Nan, Jialin Zhuang, Zijie Zhao, Zhongxiang Sun, Kun Wang, Yang Liu  

**一句话要点**：提出流式幻觉检测方法以解决长思维链推理中的幻觉传播问题

**关键词**：长思维链推理, 幻觉检测, 流式处理, 状态演化追踪, 实时监控

## 3 点简述
- 核心问题：长思维链推理中幻觉以潜在状态演化并跨步骤传播，而非一次性错误事件
- 方法要点：将步骤级幻觉判断视为局部观测，引入累积前缀级信号追踪全局推理状态演化
- 实验或效果：实现流式检测，提供实时、可解释的证据，未知具体性能指标

## 摘要（原文）

> Long chain-of-thought (CoT) reasoning improves the performance of large language models, yet hallucinations in such settings often emerge subtly and propagate across reasoning steps. We suggest that hallucination in long CoT reasoning is better understood as an evolving latent state rather than a one-off erroneous event. Accordingly, we treat step-level hallucination judgments as local observations and introduce a cumulative prefix-level hallucination signal that tracks the global evolution of the reasoning state over the entire trajectory. Overall, our approach enables streaming hallucination detection in long CoT reasoning, providing real-time, interpretable evidence.

