---
layout: default
title: LLMServingSim 2.0: A Unified Simulator for Heterogeneous and Disaggregated LLM Serving Infrastructure
---

# LLMServingSim 2.0: A Unified Simulator for Heterogeneous and Disaggregated LLM Serving Infrastructure
**arXiv**：[2602.23036v1](https://arxiv.org/abs/2602.23036) · [PDF](https://arxiv.org/pdf/2602.23036.pdf)  
**作者**：Jaehong Cho, Hyunmin Choi, Guseul Heo, Jongse Park  

**一句话要点**：提出LLMServingSim 2.0统一模拟器，以建模异构与解耦LLM服务基础设施中的运行时硬件-软件交互。

**关键词**：LLM服务模拟, 异构硬件建模, 解耦系统, 运行时交互, 系统级仿真, 性能分析

## 3 点简述
- 核心问题：现有模拟器缺乏统一框架，难以联合建模异构硬件与解耦服务技术间的运行时交互。
- 方法要点：嵌入服务决策与硬件行为到单一运行时循环，支持基于配置的扩展集成，实现交互感知建模。
- 实验或效果：验证显示平均误差0.97%，模拟时间约10分钟，为硬件创新与服务系统设计提供实用桥梁。

## 摘要（原文）

> Large language model (LLM) serving infrastructures are undergoing a shift toward heterogeneity and disaggregation. Modern deployments increasingly integrate diverse accelerators and near-memory processing technologies, introducing significant hardware heterogeneity, while system software increasingly separates computation, memory, and model components across distributed resources to improve scalability and efficiency. As a result, LLM serving performance is no longer determined by hardware or software choices in isolation, but by their runtime interaction through scheduling, data movement, and interconnect behavior. However, understanding these interactions remains challenging, as existing simulators lack the ability to jointly model heterogeneous hardware and disaggregated serving techniques within a unified, runtime-driven framework.
>   This paper presents LLMServingSim 2.0, a unified system-level simulator designed to make runtime-driven hardware-software interactions in heterogeneous and disaggregated LLM serving infrastructures explicit and analyzable. LLMServingSim 2.0 embeds serving decisions and hardware behavior into a single runtime loop, enabling interaction-aware modeling of batching, routing, offloading, memory, and power. The simulator supports extensible integration of emerging accelerators and memory systems through profile-based modeling, while capturing dynamic serving behavior and system-level effects. We validate LLMServingSim 2.0 against real deployments, showing that it reproduces key performance, memory, and power metrics with an average error of 0.97%, while maintaining simulation times of around 10 minutes even for complex configurations. These results demonstrate that LLMServingSim 2.0 provides a practical bridge between hardware innovation and serving-system design, enabling systematic exploration and co-design for next-generation LLM serving infrastructures.

