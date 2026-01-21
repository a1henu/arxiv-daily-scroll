---
layout: default
title: Efficient Coordination with the System-Level Shared State: An Embodied-AI Native Modular Framework
---

# Efficient Coordination with the System-Level Shared State: An Embodied-AI Native Modular Framework
**arXiv**：[2601.13945v1](https://arxiv.org/abs/2601.13945) · [PDF](https://arxiv.org/pdf/2601.13945.pdf)  
**作者**：Yixuan Deng, Tongrun Wu, Donghao Wu, Zeyu Wei, Jiayuan Wang, Zhenglong Sun, Yuqing Tang, Xiaoqiang Ji  

**一句话要点**：提出ANCHOR框架以解决具身AI系统模块化部署中的耦合与鲁棒性问题

**关键词**：具身AI, 模块化框架, 系统级共享状态, 鲁棒性, 闭环系统, 自动恢复

## 3 点简述
- 核心问题：现有具身AI系统部分解耦导致接口漂移、模块干扰和脆弱恢复
- 方法要点：ANCHOR通过标准化共享状态和通信总线实现显式解耦与可检查闭环
- 实验或效果：验证闭环可行性，分析延迟分布，并展示崩溃后自动恢复能力

## 摘要（原文）

> As Embodied AI systems move from research prototypes to real world deployments, they tend to evolve rapidly while remaining reliable under workload changes and partial failures. In practice, many deployments are only partially decoupled: middleware moves messages, but shared context and feedback semantics are implicit, causing interface drift, cross-module interference, and brittle recovery at scale. We present ANCHOR, a modular framework that makes decoupling and robustness explicit system-level primitives. ANCHOR separates (i) Canonical Records, an evolvable contract for the standardized shared state, from (ii) a communication bus for many-to-many dissemination and feedback-oriented coordination, forming an inspectable end-to-end loop. We validate closed-loop feasibility on a de-identified workflow instantiation, characterize latency distributions under varying payload sizes and publish rates, and demonstrate automatic stream resumption after hard crashes and restarts even with shared-memory loss. Overall, ANCHOR turns ad-hoc integration glue into explicit contracts, enabling controlled degradation under load and self-healing recovery for scalable deployment of closed-loop AI systems.

