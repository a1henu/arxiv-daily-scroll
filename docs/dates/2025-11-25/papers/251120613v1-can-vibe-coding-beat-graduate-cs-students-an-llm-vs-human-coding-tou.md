---
layout: default
title: Can Vibe Coding Beat Graduate CS Students? An LLM vs. Human Coding Tournament on Market-driven Strategic Planning
---

# Can Vibe Coding Beat Graduate CS Students? An LLM vs. Human Coding Tournament on Market-driven Strategic Planning
**arXiv**：[2511.20613v1](https://arxiv.org/abs/2511.20613) · [PDF](https://arxiv.org/pdf/2511.20613.pdf)  
**作者**：Panayiotis Danassis, Naman Goel  

**一句话要点**：提出多代理推理基准评估LLM代码生成，发现人类代码在物流优化中更优

**关键词**：大语言模型, 代码生成基准, 多代理系统, 物流优化, 战略规划

## 3 点简述
- 核心问题：现有基准低估LLM在规划与战略交互代码生成中的能力
- 方法要点：基于物流优化问题构建多代理基准，结合拍卖与路由
- 实验效果：人类代码代理在比赛中表现优于多数LLM生成代理

## 摘要（原文）

> The rapid proliferation of Large Language Models (LLMs) has revolutionized AI-assisted code generation. This rapid development of LLMs has outpaced our ability to properly benchmark them. Prevailing benchmarks emphasize unit-test pass rates and syntactic correctness. Such metrics understate the difficulty of many real-world problems that require planning, optimization, and strategic interaction. We introduce a multi-agent reasoning-driven benchmark based on a real-world logistics optimization problem (Auction, Pickup, and Delivery Problem) that couples competitive auctions with capacity-constrained routing. The benchmark requires building agents that can (i) bid strategically under uncertainty and (ii) optimize planners that deliver tasks while maximizing profit. We evaluate 40 LLM-coded agents (by a wide range of state-of-the-art LLMs under multiple prompting methodologies, including vibe coding) against 17 human-coded agents developed before the advent of LLMs. Our results over 12 double all-play-all tournaments and $\sim 40$k matches demonstrate (i) a clear superiority of human(graduate students)-coded agents: the top 5 spots are consistently won by human-coded agents, (ii) the majority of LLM-coded agents (33 out of 40) are beaten by very simple baselines, and (iii) given the best human solution as an input and prompted to improve upon, the best performing LLM makes the solution significantly worse instead of improving it. Our results highlight a gap in LLMs' ability to produce code that works competitively in the real-world, and motivate new evaluations that emphasize reasoning-driven code synthesis in real-world scenarios.

