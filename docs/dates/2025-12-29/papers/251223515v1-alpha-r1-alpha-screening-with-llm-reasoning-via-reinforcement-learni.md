---
layout: default
title: Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning
---

# Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning
**arXiv**：[2512.23515v1](https://arxiv.org/abs/2512.23515) · [PDF](https://arxiv.org/pdf/2512.23515.pdf)  
**作者**：Zuoyou Jiang, Li Zhao, Rui Sun, Ruohan Sun, Zhongjian Li, Jing Li, Daxin Jiang, Zuo Bai, Cheng Hua  

**一句话要点**：提出Alpha-R1，通过强化学习训练LLM推理模型，用于非平稳市场中的上下文感知Alpha筛选。

**关键词**：Alpha筛选, 强化学习, 大语言模型推理, 非平稳市场, 因子逻辑

## 3 点简述
- 核心问题：非平稳市场中信号衰减和制度转换挑战数据驱动策略，传统方法依赖历史相关性难以泛化。
- 方法要点：训练8B参数推理模型，结合因子逻辑和实时新闻进行经济推理，选择性激活或停用因子。
- 实验或效果：在多个资产池中实证显示，Alpha-R1优于基准策略，对Alpha衰减具有更强鲁棒性。

## 摘要（原文）

> Signal decay and regime shifts pose recurring challenges for data-driven investment strategies in non-stationary markets. Conventional time-series and machine learning approaches, which rely primarily on historical correlations, often struggle to generalize when the economic environment changes. While large language models (LLMs) offer strong capabilities for processing unstructured information, their potential to support quantitative factor screening through explicit economic reasoning remains underexplored. Existing factor-based methods typically reduce alphas to numerical time series, overlooking the semantic rationale that determines when a factor is economically relevant. We propose Alpha-R1, an 8B-parameter reasoning model trained via reinforcement learning for context-aware alpha screening. Alpha-R1 reasons over factor logic and real-time news to evaluate alpha relevance under changing market conditions, selectively activating or deactivating factors based on contextual consistency. Empirical results across multiple asset pools show that Alpha-R1 consistently outperforms benchmark strategies and exhibits improved robustness to alpha decay. The full implementation and resources are available at https://github.com/FinStep-AI/Alpha-R1.

