---
layout: default
title: BAPO: Boundary-Aware Policy Optimization for Reliable Agentic Search
---

# BAPO: Boundary-Aware Policy Optimization for Reliable Agentic Search
**arXiv**：[2601.11037v1](https://arxiv.org/abs/2601.11037) · [PDF](https://arxiv.org/pdf/2601.11037.pdf)  
**作者**：Shiyu Liu, Yongjing Yin, Jianhao Yan, Yunbo Tang, Qinggang Zhang, Bei Li, Xin Chen, Jingang Wang, Xunliang Cai, Jinsong Su  

**一句话要点**：提出边界感知策略优化以提升基于强化学习的代理搜索可靠性

**关键词**：强化学习, 代理搜索, 边界感知, 可靠性优化, 奖励设计

## 3 点简述
- 核心问题：基于强化学习的代理搜索在证据不足或推理达到极限时缺乏可靠性，很少承认未知。
- 方法要点：引入基于组的边界感知奖励和自适应奖励调制器，鼓励在推理极限时响应未知，避免早期探索中利用未知作为捷径。
- 实验或效果：在四个基准测试中，BAPO显著增强了代理搜索的整体可靠性。

## 摘要（原文）

> RL-based agentic search enables LLMs to solve complex questions via dynamic planning and external search. While this approach significantly enhances accuracy with agent policies optimized via large-scale reinforcement learning, we identify a critical gap in reliability: these agents fail to recognize their reasoning boundaries and rarely admit ``I DON'T KNOW'' (IDK) even when evidence is insufficient or reasoning reaches its limit. The lack of reliability often leads to plausible but unreliable answers, introducing significant risks in many real-world scenarios. To this end, we propose Boundary-Aware Policy Optimization (BAPO), a novel RL framework designed to cultivate reliable boundary awareness without compromising accuracy. BAPO introduces two key components: (i) a group-based boundary-aware reward that encourages an IDK response only when the reasoning reaches its limit, and (ii) an adaptive reward modulator that strategically suspends this reward during early exploration, preventing the model from exploiting IDK as a shortcut. Extensive experiments on four benchmarks demonstrate that BAPO substantially enhances the overall reliability of agentic search.

