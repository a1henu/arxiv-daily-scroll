---
layout: default
title: BOAD: Discovering Hierarchical Software Engineering Agents via Bandit Optimization
---

# BOAD: Discovering Hierarchical Software Engineering Agents via Bandit Optimization
**arXiv**：[2512.23631v1](https://arxiv.org/abs/2512.23631) · [PDF](https://arxiv.org/pdf/2512.23631.pdf)  
**作者**：Iris Xu, Guangtao Zeng, Zexue He, Charles Jin, Aldo Pareja, Dan Gutfreund, Chuang Gan, Zhang-Wei Hong  

**一句话要点**：提出BOAD框架，通过多臂老虎机优化自动发现分层软件工程代理以解决长视野任务泛化问题

**关键词**：软件工程代理, 分层多代理系统, 多臂老虎机优化, 长视野任务, 代码修复, 泛化能力

## 3 点简述
- 核心问题：大语言模型在长视野、分布外软件工程任务中泛化能力不足，单代理设计易导致无关上下文干扰和虚假相关
- 方法要点：将代理设计为协调子代理的编排器，利用多臂老虎机建模子代理选择，高效探索分层结构
- 实验或效果：在SWE-bench-Verified上优于单代理和手动多代理系统，在SWE-bench-Live上36B系统排名第二，超越GPT-4等大模型

## 摘要（原文）

> Large language models (LLMs) have shown strong reasoning and coding capabilities, yet they struggle to generalize to real-world software engineering (SWE) problems that are long-horizon and out of distribution. Existing systems often rely on a single agent to handle the entire workflow-interpreting issues, navigating large codebases, and implementing fixes-within one reasoning chain. Such monolithic designs force the model to retain irrelevant context, leading to spurious correlations and poor generalization. Motivated by how human engineers decompose complex problems, we propose structuring SWE agents as orchestrators coordinating specialized sub-agents for sub-tasks such as localization, editing, and validation. The challenge lies in discovering effective hierarchies automatically: as the number of sub-agents grows, the search space becomes combinatorial, and it is difficult to attribute credit to individual sub-agents within a team. We address these challenges by formulating hierarchy discovery as a multi-armed bandit (MAB) problem, where each arm represents a candidate sub-agent and the reward measures its helpfulness when collaborating with others. This framework, termed Bandit Optimization for Agent Design (BOAD), enables efficient exploration of sub-agent designs under limited evaluation budgets. On SWE-bench-Verified, BOAD outperforms single-agent and manually designed multi-agent systems. On SWE-bench-Live, featuring more recent and out-of-distribution issues, our 36B system ranks second on the leaderboard at the time of evaluation, surpassing larger models such as GPT-4 and Claude. These results demonstrate that automatically discovered hierarchical multi-agent systems significantly improve generalization on challenging long-horizon SWE tasks. Code is available at https://github.com/iamxjy/BOAD-SWE-Agent.

