---
layout: default
title: Decentralized Intent-Based Multi-Robot Task Planner with LLM Oracles on Hyperledger Fabric
---

# Decentralized Intent-Based Multi-Robot Task Planner with LLM Oracles on Hyperledger Fabric
**arXiv**：[2602.08421v1](https://arxiv.org/abs/2602.08421) · [PDF](https://arxiv.org/pdf/2602.08421.pdf)  
**作者**：Farhad Keramat, Salma Salimi, Tomi Westerlund  

**一句话要点**：提出基于LLM预言机的去中心化多机器人任务规划器，以解决机器人任务规划中的聚合方法不足问题。

**关键词**：多机器人系统, 任务规划, LLM预言机, 去中心化架构, Hyperledger Fabric, 访问控制

## 3 点简述
- 核心问题：现有LLM预言机聚合方法依赖语义相似性，不适用于需考虑任务时序的机器人规划。
- 方法要点：设计新聚合方法用于机器人任务规划，并基于Hyperledger Fabric构建去中心化多机器人基础设施。
- 实验或效果：创建SkillChain-RTD基准，实验显示架构可行且新聚合方法优于现有方法。

## 摘要（原文）

> Large language models (LLMs) have opened new opportunities for transforming natural language user intents into executable actions. This capability enables embodied AI agents to perform complex tasks, without involvement of an expert, making human-robot interaction (HRI) more convenient. However these developments raise significant security and privacy challenges such as self-preferencing, where a single LLM service provider dominates the market and uses this power to promote their own preferences. LLM oracles have been recently proposed as a mechanism to decentralize LLMs by executing multiple LLMs from different vendors and aggregating their outputs to obtain a more reliable and trustworthy final result. However, the accuracy of these approaches highly depends on the aggregation method. The current aggregation methods mostly use semantic similarity between various LLM outputs, not suitable for robotic task planning, where the temporal order of tasks is important. To fill the gap, we propose an LLM oracle with a new aggregation method for robotic task planning. In addition, we propose a decentralized multi-robot infrastructure based on Hyperledger Fabric that can host the proposed oracle. The proposed infrastructure enables users to express their natural language intent to the system, which then can be decomposed into subtasks. These subtasks require coordinating different robots from different vendors, while enforcing fine-grained access control management on the data. To evaluate our methodology, we created the SkillChain-RTD benchmark made it publicly available. Our experimental results demonstrate the feasibility of the proposed architecture, and the proposed aggregation method outperforms other aggregation methods currently in use.

