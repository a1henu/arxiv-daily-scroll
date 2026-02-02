---
layout: default
title: HeaPA: Difficulty-Aware Heap Sampling and On-Policy Query Augmentation for LLM Reinforcement Learning
---

# HeaPA: Difficulty-Aware Heap Sampling and On-Policy Query Augmentation for LLM Reinforcement Learning
**arXiv**：[2601.22448v1](https://arxiv.org/abs/2601.22448) · [PDF](https://arxiv.org/pdf/2601.22448.pdf)  
**作者**：Weiqi Wang, Xin Liu, Binxuan Huang, Hejie Cui, Rongzhi Zhang, Changlong Yu, Shuowei Jin, Jingfeng Yang, Qingyu Yin, Zhengyang Wang, Zheng Li, Yifan Gao, Priyanka Nigam, Bing Yin, Lihong Li, Yangqiu Song  

**一句话要点**：提出HeaPA方法以提升LLM强化学习在推理任务中的效率，通过动态采样与查询增强。

**关键词**：强化学习, 大语言模型, 采样效率, 查询增强, 动态提示池, 异步验证

## 3 点简述
- 核心问题：RLVR训练中，静态提示池导致采样效率低下，浪费计算资源于已解决或不可及的提示。
- 方法要点：采用堆采样追踪能力边界，通过轻量异步验证进行策略内查询增强，动态维护有界池。
- 实验或效果：在多个基准测试中，HeaPA提高准确性，减少计算量，同时保持训练时间可比。

## 摘要（原文）

> RLVR is now a standard way to train LLMs on reasoning tasks with verifiable outcomes, but when rollout generation dominates the cost, efficiency depends heavily on which prompts you sample and when. In practice, prompt pools are often static or only loosely tied to the model's learning progress, so uniform sampling can't keep up with the shifting capability frontier and ends up wasting rollouts on prompts that are already solved or still out of reach. Existing approaches improve efficiency through filtering, curricula, adaptive rollout allocation, or teacher guidance, but they typically assume a fixed pool-which makes it hard to support stable on-policy pool growth-or they add extra teacher cost and latency. We introduce HeaPA (Heap Sampling and On-Policy Query Augmentation), which maintains a bounded, evolving pool, tracks the frontier using heap-based boundary sampling, expands the pool via on-policy augmentation with lightweight asynchronous validation, and stabilizes correlated queries through topology-aware re-estimation of pool statistics and controlled reinsertion. Across two training corpora, two training recipes, and seven benchmarks, HeaPA consistently improves accuracy and reaches target performance with fewer computations while keeping wall-clock time comparable. Our analyses suggest these gains come from frontier-focused sampling and on-policy pool growth, with the benefits becoming larger as model scale increases. Our code is available at https://github.com/horizon-rl/HeaPA.

