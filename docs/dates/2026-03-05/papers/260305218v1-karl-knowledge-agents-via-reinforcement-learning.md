---
layout: default
title: KARL: Knowledge Agents via Reinforcement Learning
---

# KARL: Knowledge Agents via Reinforcement Learning
**arXiv**：[2603.05218v1](https://arxiv.org/abs/2603.05218) · [PDF](https://arxiv.org/pdf/2603.05218.pdf)  
**作者**：Jonathan D. Chang, Andrew Drozdov, Shubham Toshniwal, Owen Oertell, Alexander Trott, Jacob Portes, Abhay Gupta, Pallavi Koppol, Ashutosh Baheti, Sean Kulinski, Ivan Zhou, Irene Dea, Krista Opsahl-Ong, Simon Favreau-Lessard, Sean Owen, Jose Javier Gonzalez Ortiz, Arnav Singhvi, Xabi Andrade, Cindy Wang, Kartik Sreenivasan, Sam Havens, Jialu Liu, Peyton DeNiro, Wen Sun, Michael Bendersky, Jonathan Frankle  

**一句话要点**：提出KARL系统，通过强化学习训练企业搜索代理，在多样化搜索任务中实现最优性能。

**关键词**：企业搜索代理, 强化学习, 多任务训练, 合成数据生成, 评估套件, 泛化能力

## 3 点简述
- 核心问题：企业搜索任务多样且难以验证，需高效代理处理。
- 方法要点：开发KARLBench评估套件，结合多任务强化学习与合成数据生成。
- 实验或效果：在成本-质量和延迟-质量权衡上优于Claude 4.6和GPT 5.2，泛化能力强。

## 摘要（原文）

> We present a system for training enterprise search agents via reinforcement learning that achieves state-of-the-art performance across a diverse suite of hard-to-verify agentic search tasks. Our work makes four core contributions. First, we introduce KARLBench, a multi-capability evaluation suite spanning six distinct search regimes, including constraint-driven entity search, cross-document report synthesis, tabular numerical reasoning, exhaustive entity retrieval, procedural reasoning over technical documentation, and fact aggregation over internal enterprise notes. Second, we show that models trained across heterogeneous search behaviors generalize substantially better than those optimized for any single benchmark. Third, we develop an agentic synthesis pipeline that employs long-horizon reasoning and tool use to generate diverse, grounded, and high-quality training data, with iterative bootstrapping from increasingly capable models. Fourth, we propose a new post-training paradigm based on iterative large-batch off-policy RL that is sample efficient, robust to train-inference engine discrepancies, and naturally extends to multi-task training with out-of-distribution generalization. Compared to Claude 4.6 and GPT 5.2, KARL is Pareto-optimal on KARLBench across cost-quality and latency-quality trade-offs, including tasks that were out-of-distribution during training. With sufficient test-time compute, it surpasses the strongest closed models. These results show that tailored synthetic data in combination with multi-task reinforcement learning enables cost-efficient and high-performing knowledge agents for grounded reasoning.

