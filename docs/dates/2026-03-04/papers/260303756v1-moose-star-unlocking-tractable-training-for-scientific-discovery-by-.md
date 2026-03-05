---
layout: default
title: MOOSE-Star: Unlocking Tractable Training for Scientific Discovery by Breaking the Complexity Barrier
---

# MOOSE-Star: Unlocking Tractable Training for Scientific Discovery by Breaking the Complexity Barrier
**arXiv**：[2603.03756v1](https://arxiv.org/abs/2603.03756) · [PDF](https://arxiv.org/pdf/2603.03756.pdf)  
**作者**：Zonglin Yang, Lidong Bing  

**一句话要点**：提出MOOSE-Star框架以解决科学发现中生成推理过程直接训练的复杂性障碍

**关键词**：科学发现, 生成推理训练, 复杂性降低, 分层搜索, 数据集构建, 测试时间扩展

## 3 点简述
- 核心问题：直接训练P(h\|b)因组合复杂性（O(N^k)）而数学上不可行
- 方法要点：通过分解子任务、动机引导分层搜索和有界组合，将复杂度降至对数级
- 实验或效果：在TOMATO-Star数据集上训练，展示连续测试时间扩展，避免复杂度墙

## 摘要（原文）

> While large language models (LLMs) show promise in scientific discovery, existing research focuses on inference or feedback-driven training, leaving the direct modeling of the generative reasoning process, $P(\text{hypothesis}\|\text{background})$ ($P(h\|b)$), unexplored. We demonstrate that directly training $P(h\|b)$ is mathematically intractable due to the combinatorial complexity ($O(N^k)$) inherent in retrieving and composing inspirations from a vast knowledge base. To break this barrier, we introduce MOOSE-Star, a unified framework enabling tractable training and scalable inference. In the best case, MOOSE-Star reduces complexity from exponential to logarithmic ($O(\log N)$) by (1) training on decomposed subtasks derived from the probabilistic equation of discovery, (2) employing motivation-guided hierarchical search to enable logarithmic retrieval and prune irrelevant subspaces, and (3) utilizing bounded composition for robustness against retrieval noise. To facilitate this, we release TOMATO-Star, a dataset of 108,717 decomposed papers (38,400 GPU hours) for training. Furthermore, we show that while brute-force sampling hits a ''complexity wall,'' MOOSE-Star exhibits continuous test-time scaling.

