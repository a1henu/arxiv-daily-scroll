---
layout: default
title: WideSeek-R1: Exploring Width Scaling for Broad Information Seeking via Multi-Agent Reinforcement Learning
---

# WideSeek-R1: Exploring Width Scaling for Broad Information Seeking via Multi-Agent Reinforcement Learning
**arXiv**：[2602.04634v1](https://arxiv.org/abs/2602.04634) · [PDF](https://arxiv.org/pdf/2602.04634.pdf)  
**作者**：Zelai Xu, Zhexuan Xu, Ruize Zhang, Chunyang Zhu, Shi Yu, Weilin Liu, Quanlu Zhang, Wenbo Ding, Chao Yu, Yu Wang  

**一句话要点**：提出WideSeek-R1框架，通过多智能体强化学习实现宽度扩展以解决广泛信息搜索任务

**关键词**：多智能体系统, 宽度扩展, 强化学习, 信息搜索, 并行执行, 智能体编排

## 3 点简述
- 核心问题：现有多智能体系统依赖手工工作流，难以有效并行化处理广泛信息搜索任务
- 方法要点：采用主智能体-子智能体框架，通过多智能体强化学习协同优化可扩展编排与并行执行
- 实验或效果：在WideSearch基准上，4B参数模型达到40.0%项目F1分数，性能与671B单智能体模型相当

## 摘要（原文）

> Recent advancements in Large Language Models (LLMs) have largely focused on depth scaling, where a single agent solves long-horizon problems with multi-turn reasoning and tool use. However, as tasks grow broader, the key bottleneck shifts from individual competence to organizational capability. In this work, we explore a complementary dimension of width scaling with multi-agent systems to address broad information seeking. Existing multi-agent systems often rely on hand-crafted workflows and turn-taking interactions that fail to parallelize work effectively. To bridge this gap, we propose WideSeek-R1, a lead-agent-subagent framework trained via multi-agent reinforcement learning (MARL) to synergize scalable orchestration and parallel execution. By utilizing a shared LLM with isolated contexts and specialized tools, WideSeek-R1 jointly optimizes the lead agent and parallel subagents on a curated dataset of 20k broad information-seeking tasks. Extensive experiments show that WideSeek-R1-4B achieves an item F1 score of 40.0% on the WideSearch benchmark, which is comparable to the performance of single-agent DeepSeek-R1-671B. Furthermore, WideSeek-R1-4B exhibits consistent performance gains as the number of parallel subagents increases, highlighting the effectiveness of width scaling.

