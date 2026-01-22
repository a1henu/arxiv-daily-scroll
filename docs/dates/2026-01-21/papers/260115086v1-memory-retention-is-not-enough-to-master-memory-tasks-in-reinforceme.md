---
layout: default
title: Memory Retention Is Not Enough to Master Memory Tasks in Reinforcement Learning
---

# Memory Retention Is Not Enough to Master Memory Tasks in Reinforcement Learning
**arXiv**：[2601.15086v1](https://arxiv.org/abs/2601.15086) · [PDF](https://arxiv.org/pdf/2601.15086.pdf)  
**作者**：Oleg Shchendrigin, Egor Cherepanov, Alexey K. Kovalev, Aleksandr I. Panov  

**一句话要点**：提出记忆重写基准以解决强化学习中记忆稳定与自适应更新的平衡问题

**关键词**：强化学习, 记忆重写, 部分可观测性, 基准测试, 记忆架构, 自适应更新

## 3 点简述
- 核心问题：现有强化学习基准和记忆增强代理主要关注记忆保留，忽视记忆重写能力
- 方法要点：引入部分可观测性下的持续记忆更新基准，比较循环、基于Transformer和结构化记忆架构
- 实验或效果：经典循环模型在记忆重写任务中表现更灵活稳健，而结构化记忆和Transformer代理在非平凡保留案例中常失败

## 摘要（原文）

> Effective decision-making in the real world depends on memory that is both stable and adaptive: environments change over time, and agents must retain relevant information over long horizons while also updating or overwriting outdated content when circumstances shift. Existing Reinforcement Learning (RL) benchmarks and memory-augmented agents focus primarily on retention, leaving the equally critical ability of memory rewriting largely unexplored. To address this gap, we introduce a benchmark that explicitly tests continual memory updating under partial observability, i.e. the natural setting where an agent must rely on memory rather than current observations, and use it to compare recurrent, transformer-based, and structured memory architectures. Our experiments reveal that classic recurrent models, despite their simplicity, demonstrate greater flexibility and robustness in memory rewriting tasks than modern structured memories, which succeed only under narrow conditions, and transformer-based agents, which often fail beyond trivial retention cases. These findings expose a fundamental limitation of current approaches and emphasize the necessity of memory mechanisms that balance stable retention with adaptive updating. Our work highlights this overlooked challenge, introduces benchmarks to evaluate it, and offers insights for designing future RL agents with explicit and trainable forgetting mechanisms. Code: https://quartz-admirer.github.io/Memory-Rewriting/

