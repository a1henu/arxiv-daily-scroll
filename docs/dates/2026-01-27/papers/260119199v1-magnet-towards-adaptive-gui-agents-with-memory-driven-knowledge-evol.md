---
layout: default
title: MAGNET: Towards Adaptive GUI Agents with Memory-Driven Knowledge Evolution
---

# MAGNET: Towards Adaptive GUI Agents with Memory-Driven Knowledge Evolution
**arXiv**：[2601.19199v1](https://arxiv.org/abs/2601.19199) · [PDF](https://arxiv.org/pdf/2601.19199.pdf)  
**作者**：Libo Sun, Jiwen Zhang, Siyuan Wang, Zhongyu Wei  

**一句话要点**：提出MAGNET框架，通过双级记忆机制解决移动GUI代理在界面更新中的适应性问题。

**关键词**：移动GUI代理, 记忆驱动适应, 双级记忆机制, 动态记忆进化, 界面更新鲁棒性, 任务意图稳定性

## 3 点简述
- 核心问题：移动GUI代理因界面频繁更新导致基于历史数据的训练失效，尽管功能语义和任务意图保持稳定。
- 方法要点：引入双级记忆（静态记忆和过程记忆），结合动态记忆进化机制，优先更新常用知识以增强适应能力。
- 实验或效果：在线AndroidWorld基准测试显示性能显著提升，离线测试在分布偏移下保持稳定增益，验证了框架的有效性。

## 摘要（原文）

> Mobile GUI agents powered by large foundation models enable autonomous task execution, but frequent updates altering UI appearance and reorganizing workflows cause agents trained on historical data to fail. Despite surface changes, functional semantics and task intents remain fundamentally stable. Building on this insight, we introduce MAGNET, a memory-driven adaptive agent framework with dual-level memory: stationary memory linking diverse visual features to stable functional semantics for robust action grounding and procedural memory capturing stable task intents across varying workflows. We propose a dynamic memory evolution mechanism that continuously refines both memories by prioritizing frequently accessed knowledge. Online benchmark AndroidWorld evaluations show substantial improvements over baselines, while offline benchmarks confirm consistent gains under distribution shifts. These results validate that leveraging stable structures across interface changes improves agent performance and generalization in evolving software environments.

