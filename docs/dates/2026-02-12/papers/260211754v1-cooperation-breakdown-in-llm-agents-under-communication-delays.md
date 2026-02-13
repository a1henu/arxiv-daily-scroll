---
layout: default
title: Cooperation Breakdown in LLM Agents Under Communication Delays
---

# Cooperation Breakdown in LLM Agents Under Communication Delays
**arXiv**：[2602.11754v1](https://arxiv.org/abs/2602.11754) · [PDF](https://arxiv.org/pdf/2602.11754.pdf)  
**作者**：Keita Nishimoto, Kimitaka Asatani, Ichiro Sakata  

**一句话要点**：提出FLCOA框架分析通信延迟对LLM多智能体合作的影响

**关键词**：多智能体系统, 通信延迟, 合作博弈, LLM智能体, 模拟实验

## 3 点简述
- 核心问题：LLM多智能体系统在真实世界通信延迟下合作可能崩溃
- 方法要点：引入带通信延迟的连续囚徒困境模拟LLM智能体行为
- 实验效果：延迟增加导致利用行为，过度延迟减少利用，呈现U形关系

## 摘要（原文）

> LLM-based multi-agent systems (LLM-MAS), in which autonomous AI agents cooperate to solve tasks, are gaining increasing attention. For such systems to be deployed in society, agents must be able to establish cooperation and coordination under real-world computational and communication constraints. We propose the FLCOA framework (Five Layers for Cooperation/Coordination among Autonomous Agents) to conceptualize how cooperation and coordination emerge in groups of autonomous agents, and highlight that the influence of lower-layer factors - especially computational and communication resources - has been largely overlooked. To examine the effect of communication delay, we introduce a Continuous Prisoner's Dilemma with Communication Delay and conduct simulations with LLM-based agents. As delay increases, agents begin to exploit slower responses even without explicit instructions. Interestingly, excessive delay reduces cycles of exploitation, yielding a U-shaped relationship between delay magnitude and mutual cooperation. These results suggest that fostering cooperation requires attention not only to high-level institutional design but also to lower-layer factors such as communication delay and resource allocation, pointing to new directions for MAS research.

