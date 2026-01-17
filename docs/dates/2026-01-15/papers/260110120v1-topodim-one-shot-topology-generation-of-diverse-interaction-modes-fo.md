---
layout: default
title: TopoDIM: One-shot Topology Generation of Diverse Interaction Modes for Multi-Agent Systems
---

# TopoDIM: One-shot Topology Generation of Diverse Interaction Modes for Multi-Agent Systems
**arXiv**：[2601.10120v1](https://arxiv.org/abs/2601.10120) · [PDF](https://arxiv.org/pdf/2601.10120.pdf)  
**作者**：Rui Sun, Jie Ding, Chenghua Gong, Tianjun Gu, Yihang Jiang, Juyuan Zhang, Liming Pan, Linyuan Lü  

**一句话要点**：提出TopoDIM框架，通过一次性生成多样化交互拓扑，优化基于LLM的多智能体系统通信效率与性能。

**关键词**：多智能体系统, 通信拓扑优化, 一次性生成, 去中心化执行, 异构智能体交互, 令牌效率

## 3 点简述
- 核心问题：现有基于时空交互范式的多智能体系统通信拓扑优化方法存在高延迟和高计算成本问题。
- 方法要点：TopoDIM采用去中心化执行，使智能体自主构建异构通信，无需迭代协调，实现一次性拓扑生成。
- 实验或效果：实验显示，TopoDIM在减少总令牌消耗46.41%的同时，平均性能提升1.50%，并展现强适应性。

## 摘要（原文）

> Optimizing communication topology in LLM-based multi-agent system is critical for enabling collective intelligence. Existing methods mainly rely on spatio-temporal interaction paradigms, where the sequential execution of multi-round dialogues incurs high latency and computation. Motivated by the recent insights that evaluation and debate mechanisms can improve problem-solving in multi-agent systems, we propose TopoDIM, a framework for one-shot Topology generation with Diverse Interaction Modes. Designed for decentralized execution to enhance adaptability and privacy, TopoDIM enables agents to autonomously construct heterogeneous communication without iterative coordination, achieving token efficiency and improved task performance. Experiments demonstrate that TopoDIM reduces total token consumption by 46.41% while improving average performance by 1.50% over state-of-the-art methods. Moreover, the framework exhibits strong adaptability in organizing communication among heterogeneous agents. Code is available at: https://anonymous.4open.science/r/TopoDIM-8D35/

