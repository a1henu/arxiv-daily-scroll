---
layout: default
title: ScaleSim: Serving Large-Scale Multi-Agent Simulation with Invocation Distance-Based Memory Management
---

# ScaleSim: Serving Large-Scale Multi-Agent Simulation with Invocation Distance-Based Memory Management
**arXiv**：[2601.21473v1](https://arxiv.org/abs/2601.21473) · [PDF](https://arxiv.org/pdf/2601.21473.pdf)  
**作者**：Zaifeng Pan, Yipeng Shen, Zhengding Hu, Zhuang Wang, Aninda Manocha, Zheng Wang, Zhongkai Yu, Yue Guan, Yufei Ding  

**一句话要点**：提出ScaleSim系统，基于调用距离管理内存以支持大规模多智能体模拟的LLM服务。

**关键词**：多智能体模拟, LLM服务系统, 内存管理, 调用距离, GPU优化

## 3 点简述
- 核心问题：多智能体模拟中GPU内存压力大，因每个智能体需维护私有状态，导致扩展困难。
- 方法要点：引入调用距离抽象，预测智能体LLM请求顺序，实现主动预取和基于优先级的逐出。
- 实验或效果：在模拟基准测试中，相比SGLang实现最高1.74倍加速，提升内存效率。

## 摘要（原文）

> LLM-based multi-agent simulations are increasingly adopted across application domains, but remain difficult to scale due to GPU memory pressure. Each agent maintains private GPU-resident states, including models, prefix caches, and adapters, which quickly exhaust device memory as the agent count grows. We identify two key properties of these workloads: sparse agent activation and an estimable agent invocation order. Based on an analysis of representative workload classes, we introduce invocation distance, a unified abstraction that estimates the relative order in which agents will issue future LLM requests. Leveraging this abstraction, we present ScaleSim, a memory-efficient LLM serving system for large-scale multi-agent simulations. ScaleSim enables proactive prefetching and priority-based eviction, supports diverse agent-specific memory through a modular interface, and achieves up to 1.74x speedup over SGLang on simulation benchmarks.

