---
layout: default
title: HiMAP-Travel: Hierarchical Multi-Agent Planning for Long-Horizon Constrained Travel
---

# HiMAP-Travel: Hierarchical Multi-Agent Planning for Long-Horizon Constrained Travel
**arXiv**：[2603.04750v1](https://arxiv.org/abs/2603.04750) · [PDF](https://arxiv.org/pdf/2603.04750.pdf)  
**作者**：The Viet Bui, Wenjun Li, Yong Liu  

**一句话要点**：提出HiMAP-Travel分层多智能体框架以解决长时程约束旅行规划问题

**关键词**：长时程规划, 多智能体系统, 旅行规划, 约束优化, 并行执行

## 3 点简述
- 核心问题：序列LLM智能体在长时程规划中易偏离预算和多样性等硬约束
- 方法要点：采用战略协调与并行日级执行分层结构，结合事务监控和协商协议
- 实验或效果：在TravelPlanner上超越基线8.67个百分点，并行化降低延迟2.5倍

## 摘要（原文）

> Sequential LLM agents fail on long-horizon planning with hard constraints like budgets and diversity requirements. As planning progresses and context grows, these agents drift from global constraints. We propose HiMAP-Travel, a hierarchical multi-agent framework that splits planning into strategic coordination and parallel day-level execution. A Coordinator allocates resources across days, while Day Executors plan independently in parallel. Three key mechanisms enable this: a transactional monitor enforcing budget and uniqueness constraints across parallel agents, a bargaining protocol allowing agents to reject infeasible sub-goals and trigger re-planning, and a single policy trained with GRPO that powers all agents through role conditioning. On TravelPlanner, HiMAP-Travel with Qwen3-8B achieves 52.78% validation and 52.65% test Final Pass Rate (FPR). In a controlled comparison with identical model, training, and tools, it outperforms the sequential DeepTravel baseline by +8.67~pp. It also surpasses ATLAS by +17.65~pp and MTP by +10.0~pp. On FlexTravelBench multi-turn scenarios, it achieves 44.34% (2-turn) and 37.42% (3-turn) FPR while reducing latency 2.5x through parallelization.

