---
layout: default
title: SearchGym: Bootstrapping Real-World Search Agents via Cost-Effective and High-Fidelity Environment Simulation
---

# SearchGym: Bootstrapping Real-World Search Agents via Cost-Effective and High-Fidelity Environment Simulation
**arXiv**：[2601.14615v1](https://arxiv.org/abs/2601.14615) · [PDF](https://arxiv.org/pdf/2601.14615.pdf)  
**作者**：Xichen Zhang, Ziyi He, Yinghao Zhu, Sitong Wu, Shaozuo Yu, Meng Chu, Wenhu Zhang, Haoru Tan, Jiaya Jia  

**一句话要点**：提出SearchGym模拟环境以低成本高保真地训练搜索代理

**关键词**：搜索代理, 强化学习, 模拟环境, 知识图谱, 课程学习, Sim-to-Real泛化

## 3 点简述
- 核心问题：训练搜索代理时，实时Web API成本高，静态数据对齐噪声导致奖励信号失真。
- 方法要点：构建可验证知识图谱和对齐文档语料库，确保任务可解，并采用课程学习优化策略。
- 实验或效果：在Llama和Qwen模型上验证Sim-to-Real泛化，Qwen2.5-7B-Base在九个基准上平均超越基线10.6%。

## 摘要（原文）

> Search agents have emerged as a pivotal paradigm for solving open-ended, knowledge-intensive reasoning tasks. However, training these agents via Reinforcement Learning (RL) faces a critical dilemma: interacting with live commercial Web APIs is prohibitively expensive, while relying on static data snapshots often introduces noise due to data misalignment. This misalignment generates corrupted reward signals that destabilize training by penalizing correct reasoning or rewarding hallucination. To address this, we propose SearchGym, a simulation environment designed to bootstrap robust search agents. SearchGym employs a rigorous generative pipeline to construct a verifiable knowledge graph and an aligned document corpus, ensuring that every reasoning task is factually grounded and strictly solvable. Building on this controllable environment, we introduce SearchGym-RL, a curriculum learning methodology that progressively optimizes agent policies through purified feedback, evolving from basic interactions to complex, long-horizon planning. Extensive experiments across the Llama and Qwen families demonstrate strong Sim-to-Real generalization. Notably, our Qwen2.5-7B-Base model trained within SearchGym surpasses the web-enhanced ASearcher baseline across nine diverse benchmarks by an average relative margin of 10.6%. Our results validate that high-fidelity simulation serves as a scalable and highly cost-effective methodology for developing capable search agents.

