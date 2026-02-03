---
layout: default
title: TRIP-Bench: A Benchmark for Long-Horizon Interactive Agents in Real-World Scenarios
---

# TRIP-Bench: A Benchmark for Long-Horizon Interactive Agents in Real-World Scenarios
**arXiv**：[2602.01675v1](https://arxiv.org/abs/2602.01675) · [PDF](https://arxiv.org/pdf/2602.01675.pdf)  
**作者**：Yuanzhe Shen, Zisu Huang, Zhengyuan Wang, Muzhao Tian, Zhengkang Guo, Chenyang Zhang, Shuaiyu Zhou, Zengjie Hu, Dailin Li, Jingwen Xu, Kaimin Wang, Wenhao Liu, Tianlong Li, Fengpeng Yue, Feng Hong, Cao Liu, Ke Zeng  

**一句话要点**：提出TRIP-Bench基准与GTPO方法以提升长时程交互智能体在真实旅行规划场景中的性能。

**关键词**：长时程交互智能体, 旅行规划基准, 多工具推理, 在线强化学习, 自动化评估

## 3 点简述
- 现有基准在长时程交互中低估了全局约束、多工具协调和用户行为适应等挑战。
- TRIP-Bench基于真实旅行数据，提供工具和需求，支持自动化评估，包含难度分级。
- 实验显示先进模型在简单子集成功率≤50%，GTPO方法提升约束满足和交互鲁棒性。

## 摘要（原文）

> As LLM-based agents are deployed in increasingly complex real-world settings, existing benchmarks underrepresent key challenges such as enforcing global constraints, coordinating multi-tool reasoning, and adapting to evolving user behavior over long, multi-turn interactions. To bridge this gap, we introduce \textbf{TRIP-Bench}, a long-horizon benchmark grounded in realistic travel-planning scenarios. TRIP-Bench leverages real-world data, offers 18 curated tools and 40+ travel requirements, and supports automated evaluation. It includes splits of varying difficulty; the hard split emphasizes long and ambiguous interactions, style shifts, feasibility changes, and iterative version revision. Dialogues span up to 15 user turns, can involve 150+ tool calls, and may exceed 200k tokens of context. Experiments show that even advanced models achieve at most 50\% success on the easy split, with performance dropping below 10\% on hard subsets. We further propose \textbf{GTPO}, an online multi-turn reinforcement learning method with specialized reward normalization and reward differencing. Applied to Qwen2.5-32B-Instruct, GTPO improves constraint satisfaction and interaction robustness, outperforming Gemini-3-Pro in our evaluation. We expect TRIP-Bench to advance practical long-horizon interactive agents, and GTPO to provide an effective online RL recipe for robust long-horizon training.

