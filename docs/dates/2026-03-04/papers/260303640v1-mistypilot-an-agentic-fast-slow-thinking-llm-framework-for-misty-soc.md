---
layout: default
title: MistyPilot: An Agentic Fast-Slow Thinking LLM Framework for Misty Social Robots
---

# MistyPilot: An Agentic Fast-Slow Thinking LLM Framework for Misty Social Robots
**arXiv**：[2603.03640v1](https://arxiv.org/abs/2603.03640) · [PDF](https://arxiv.org/pdf/2603.03640.pdf)  
**作者**：Xiao Wang, Lu Dong, Jingchen Sun, Ifeoma Nwogu, Srirangaraj Setlur, Venu Govindaraju  

**一句话要点**：提出MistyPilot框架以解决社交机器人中用户指令解释与工具执行的挑战

**关键词**：社交机器人, 工具选择与编排, 快慢思维范式, 情感对齐, 基准数据集

## 3 点简述
- 核心问题：用户无编程经验时难以解释高级指令、选择配置工具并可靠执行
- 方法要点：集成物理交互代理与社会智能代理，采用快慢思维范式提升效率
- 实验或效果：通过五个基准数据集评估，在路由正确性、任务完成度等方面表现有效

## 摘要（原文）

> With the availability of open APIs in social robots, it has become easier to customize general-purpose tools to meet users' needs. However, interpreting high-level user instructions, selecting and configuring appropriate tools, and executing them reliably remain challenging for users without programming experience. To address these challenges, we introduce MistyPilot, an agentic LLM-driven framework for autonomous tool selection, orchestration, and parameter configuration. MistyPilot comprises two core components: a Physically Interactive Agent (PIA) and a Socially Intelligent Agent (SIA). The PIA enables robust sensor-triggered and tool-driven task execution, while the SIA generates socially intelligent and emotionally aligned dialogue. MistyPilot further integrates a fast-slow thinking paradigm to capture user preferences, reduce latency, and improve task efficiency. To comprehensively evaluate MistyPilot, we contribute five benchmark datasets. Extensive experiments demonstrate the effectiveness of our framework in routing correctness, task completeness, fast-slow thinking retrieval efficiency, tool scalability,and emotion alignment. All code, datasets, and experimental videos will be made publicly available on the project webpage.

