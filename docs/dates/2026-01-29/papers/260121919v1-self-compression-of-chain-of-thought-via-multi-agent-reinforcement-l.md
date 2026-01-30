---
layout: default
title: Self-Compression of Chain-of-Thought via Multi-Agent Reinforcement Learning
---

# Self-Compression of Chain-of-Thought via Multi-Agent Reinforcement Learning
**arXiv**：[2601.21919v1](https://arxiv.org/abs/2601.21919) · [PDF](https://arxiv.org/pdf/2601.21919.pdf)  
**作者**：Yiqun Chen, Jinyuan Feng, Wei Yang, Meizhi Zhong, Zhengliang Shi, Rui Li, Xiaochi Wei, Yan Gao, Yi Wu, Yao Hu, Zhiqiang Pu, Jiaxin Mao  

**一句话要点**：提出多智能体强化学习框架SCMA，通过选择性压缩冗余推理块来优化大型推理模型的推理效率与准确性。

**关键词**：推理压缩, 多智能体强化学习, 大型推理模型, 冗余检测, 重要性加权, 协同优化

## 3 点简述
- 核心问题：冗余推理导致推理开销大，影响大型推理模型的交互体验与部署效率。
- 方法要点：采用多智能体强化学习框架，包括分割、评分和推理智能体，协同定义重要性加权长度惩罚。
- 实验或效果：在多个模型规模上，SCMA减少响应长度11.1%至39.0%，同时提升准确性4.33%至10.02%。

## 摘要（原文）

> The inference overhead induced by redundant reasoning undermines the interactive experience and severely bottlenecks the deployment of Large Reasoning Models. Existing reinforcement learning (RL)-based solutions tackle this problem by coupling a length penalty with outcome-based rewards. This simplistic reward weighting struggles to reconcile brevity with accuracy, as enforcing brevity may compromise critical reasoning logic. In this work, we address this limitation by proposing a multi-agent RL framework that selectively penalizes redundant chunks, while preserving essential reasoning logic. Our framework, Self-Compression via MARL (SCMA), instantiates redundancy detection and evaluation through two specialized agents: \textbf{a Segmentation Agent} for decomposing the reasoning process into logical chunks, and \textbf{a Scoring Agent} for quantifying the significance of each chunk. The Segmentation and Scoring agents collaboratively define an importance-weighted length penalty during training, incentivizing \textbf{a Reasoning Agent} to prioritize essential logic without introducing inference overhead during deployment. Empirical evaluations across model scales demonstrate that SCMA reduces response length by 11.1\% to 39.0\% while boosting accuracy by 4.33\% to 10.02\%. Furthermore, ablation studies and qualitative analysis validate that the synergistic optimization within the MARL framework fosters emergent behaviors, yielding more powerful LRMs compared to vanilla RL paradigms.

