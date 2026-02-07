---
layout: default
title: UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents
---

# UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents
**arXiv**：[2602.05832v1](https://arxiv.org/abs/2602.05832) · [PDF](https://arxiv.org/pdf/2602.05832.pdf)  
**作者**：Han Xiao, Guozhi Wang, Hao Wang, Shilong Liu, Yuxiang Chai, Yue Pan, Yufeng Zhou, Xiaoxin Chen, Yafei Wen, Hongsheng Li  

**一句话要点**：提出UI-Mem框架以解决移动GUI在线强化学习中的经验转移与信用分配问题

**关键词**：在线强化学习, 移动GUI代理, 经验记忆, 分层采样, 自进化学习, 跨任务泛化

## 3 点简述
- 核心问题：在线强化学习在长视野任务中信用分配低效，且缺乏跨任务经验转移导致重复错误。
- 方法要点：引入分层经验记忆存储结构化知识，通过分层组采样注入指导，并利用自进化循环更新记忆。
- 实验或效果：在在线GUI基准测试中显著优于传统基线，展现出对未见应用的强泛化能力。

## 摘要（原文）

> Online Reinforcement Learning (RL) offers a promising paradigm for enhancing GUI agents through direct environment interaction. However, its effectiveness is severely hindered by inefficient credit assignment in long-horizon tasks and repetitive errors across tasks due to the lack of experience transfer. To address these challenges, we propose UI-Mem, a novel framework that enhances GUI online RL with a Hierarchical Experience Memory. Unlike traditional replay buffers, our memory accumulates structured knowledge, including high-level workflows, subtask skills, and failure patterns. These experiences are stored as parameterized templates that enable cross-task and cross-application transfer. To effectively integrate memory guidance into online RL, we introduce Stratified Group Sampling, which injects varying levels of guidance across trajectories within each rollout group to maintain outcome diversity, driving the unguided policy toward internalizing guided behaviors. Furthermore, a Self-Evolving Loop continuously abstracts novel strategies and errors to keep the memory aligned with the agent's evolving policy. Experiments on online GUI benchmarks demonstrate that UI-Mem significantly outperforms traditional RL baselines and static reuse strategies, with strong generalization to unseen applications. Project page: https://ui-mem.github.io

