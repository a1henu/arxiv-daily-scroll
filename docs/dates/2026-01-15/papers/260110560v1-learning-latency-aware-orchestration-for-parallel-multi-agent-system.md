---
layout: default
title: Learning Latency-Aware Orchestration for Parallel Multi-Agent Systems
---

# Learning Latency-Aware Orchestration for Parallel Multi-Agent Systems
**arXiv**：[2601.10560v1](https://arxiv.org/abs/2601.10560) · [PDF](https://arxiv.org/pdf/2601.10560.pdf)  
**作者**：Xi Shi, Mengxin Zheng, Qian Lou  

**一句话要点**：提出LAMaS框架以优化并行多智能体系统的延迟感知编排

**关键词**：多智能体系统, 延迟优化, 并行执行, 编排框架, 关键路径优化

## 3 点简述
- 核心问题：多智能体系统在并行执行时延迟高，现有方法多假设顺序执行，优化不足。
- 方法要点：基于学习的编排框架，显式监督延迟，优化关键执行路径，构建低延迟拓扑图。
- 实验或效果：在多个基准测试中，相比基线减少关键路径长度38-46%，保持或提升任务性能。

## 摘要（原文）

> Multi-agent systems (MAS) enable complex reasoning by coordinating multiple agents, but often incur high inference latency due to multi-step execution and repeated model invocations, severely limiting their scalability and usability in time-sensitive scenarios. Most existing approaches primarily optimize task performance and inference cost, and explicitly or implicitly assume sequential execution, making them less optimal for controlling latency under parallel execution. In this work, we investigate learning-based orchestration of multi-agent systems with explicit latency supervision under parallel execution. We propose Latency-Aware Multi-agent System (LAMaS), a latency-aware multi-agent orchestration framework that enables parallel execution and explicitly optimizes the critical execution path, allowing the controller to construct execution topology graphs with lower latency under parallel execution. Our experiments show that our approach reduces critical path length by 38-46% compared to the state-of-the-art baseline for multi-agent architecture search across multiple benchmarks, while maintaining or even improving task performance. These results highlight the importance of explicitly optimizing latency under parallel execution when designing efficient multi-agent systems. The code is available at https://github.com/xishi404/LAMaS

