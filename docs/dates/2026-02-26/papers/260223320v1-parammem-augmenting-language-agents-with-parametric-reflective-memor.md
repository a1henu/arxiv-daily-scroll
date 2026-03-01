---
layout: default
title: ParamMem: Augmenting Language Agents with Parametric Reflective Memory
---

# ParamMem: Augmenting Language Agents with Parametric Reflective Memory
**arXiv**：[2602.23320v1](https://arxiv.org/abs/2602.23320) · [PDF](https://arxiv.org/pdf/2602.23320.pdf)  
**作者**：Tianjun Yao, Yongqiang Chen, Yujia Zheng, Pan Li, Zhiqiang Shen, Kun Zhang  

**一句话要点**：提出ParamMem参数化记忆模块以增强语言代理的反思多样性，提升推理性能。

**关键词**：语言代理, 参数化记忆, 反思多样性, 温度采样, 推理增强, 自改进

## 3 点简述
- 核心问题：语言代理自我反思常产生重复输出，限制推理性能。
- 方法要点：引入参数化记忆模块，编码跨样本反思模式，通过温度控制采样生成多样反思。
- 实验或效果：在代码生成、数学推理和多跳问答任务中优于基线，支持弱到强迁移和自改进。

## 摘要（原文）

> Self-reflection enables language agents to iteratively refine solutions, yet often produces repetitive outputs that limit reasoning performance. Recent studies have attempted to address this limitation through various approaches, among which increasing reflective diversity has shown promise. Our empirical analysis reveals a strong positive correlation between reflective diversity and task success, further motivating the need for diverse reflection signals. We introduce ParamMem, a parametric memory module that encodes cross-sample reflection patterns into model parameters, enabling diverse reflection generation through temperature-controlled sampling. Building on this module, we propose ParamAgent, a reflection-based agent framework that integrates parametric memory with episodic and cross-sample memory. Extensive experiments on code generation, mathematical reasoning, and multi-hop question answering demonstrate consistent improvements over state-of-the-art baselines. Further analysis reveals that ParamMem is sample-efficient, enables weak-to-strong transfer across model scales, and supports self-improvement without reliance on stronger external model, highlighting the potential of ParamMem as an effective component for enhancing language agents.

