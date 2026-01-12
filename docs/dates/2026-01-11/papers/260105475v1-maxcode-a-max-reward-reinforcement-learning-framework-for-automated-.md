---
layout: default
title: MaxCode: A Max-Reward Reinforcement Learning Framework for Automated Code Optimization
---

# MaxCode: A Max-Reward Reinforcement Learning Framework for Automated Code Optimization
**arXiv**：[2601.05475v1](https://arxiv.org/abs/2601.05475) · [PDF](https://arxiv.org/pdf/2601.05475.pdf)  
**作者**：Jiefu Ou, Sapana Chaudhary, Kaj Bostrom, Nathaniel Weir, Shuai Zhang, Huzefa Rangwala, George Karypis  

**一句话要点**：提出MaxCode框架，基于最大奖励强化学习自动化代码优化，提升LLM在CUDA和C++代码的性能表现。

**关键词**：代码优化, 强化学习, 大语言模型, 自动化搜索, 性能提升, 自然语言处理

## 3 点简述
- 核心问题：LLM在优化代码时面临编写复杂优化代码和解释性能指标的挑战。
- 方法要点：统一搜索方法于最大奖励强化学习框架，集成自然语言批判模型和生成奖励模型增强观察与探索。
- 实验或效果：在KernelBench和PIE基准测试中，MaxCode在绝对加速值和相对加速排名上分别实现20.3%和10.1%的相对改进。

## 摘要（原文）

> Large Language Models (LLMs) demonstrate strong capabilities in general coding tasks but encounter two key challenges when optimizing code: (i) the complexity of writing optimized code (such as performant CUDA kernels and competition-level CPU code) requires expertise in systems, algorithms and specific languages and (ii) requires interpretation of performance metrics like timing and device utilization beyond binary correctness. In this work, we explore inference-time search algorithms that guide the LLM to discover better solutions through iterative refinement based on execution feedback. Our approach, called MaxCode unifies existing search methods under a max-reward reinforcement learning framework, making the observation and action-value functions modular for modification. To enhance the observation space, we integrate a natural language critique model that converts raw execution feedback into diagnostic insights about errors and performance bottlenecks, and the best-discounted reward seen so far. Together, these provide richer input to the code proposal function. To improve exploration during search, we train a generative reward-to-go model using action values from rollouts to rerank potential solutions. Testing on the KernelBench (CUDA) and PIE (C++) optimization benchmarks shows that MaxCode improves optimized code performance compared to baselines, achieving 20.3% and 10.1% relative improvements in absolute speedup value and relative speedup ranking, respectively.

