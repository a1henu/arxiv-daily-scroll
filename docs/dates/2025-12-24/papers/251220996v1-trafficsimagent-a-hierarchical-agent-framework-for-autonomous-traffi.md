---
layout: default
title: TrafficSimAgent: A Hierarchical Agent Framework for Autonomous Traffic Simulation with MCP Control
---

# TrafficSimAgent: A Hierarchical Agent Framework for Autonomous Traffic Simulation with MCP Control
**arXiv**：[2512.20996v1](https://arxiv.org/abs/2512.20996) · [PDF](https://arxiv.org/pdf/2512.20996.pdf)  
**作者**：Yuwei Du, Jun Zhang, Jie Feng, Zhicheng Liu, Jian Yuan, Yong Li  

**一句话要点**：提出TrafficSimAgent分层代理框架，基于LLM和MCP控制解决通用交通模拟任务中的实验设计与决策优化问题。

**关键词**：交通模拟, 分层代理框架, LLM代理, MCP控制, 实验设计优化, 自主决策

## 3 点简述
- 核心问题：现有交通模拟平台如SUMO和MATSim对非专业用户门槛高，实验设计和应用困难。
- 方法要点：采用分层代理框架，高层代理理解自然语言指令并规划工作流，低层代理基于实时交通条件优化基础元素动作。
- 实验或效果：多场景实验显示，框架能有效执行模拟，在模糊指令下仍产生合理结果，性能优于其他系统和SOTA LLM方法。

## 摘要（原文）

> Traffic simulation is important for transportation optimization and policy making. While existing simulators such as SUMO and MATSim offer fully-featured platforms and utilities, users without too much knowledge about these platforms often face significant challenges when conducting experiments from scratch and applying them to their daily work. To solve this challenge, we propose TrafficSimAgent, an LLM-based agent framework that serves as an expert in experiment design and decision optimization for general-purpose traffic simulation tasks. The framework facilitates execution through cross-level collaboration among expert agents: high-level expert agents comprehend natural language instructions with high flexibility, plan the overall experiment workflow, and invoke corresponding MCP-compatible tools on demand; meanwhile, low-level expert agents select optimal action plans for fundamental elements based on real-time traffic conditions. Extensive experiments across multiple scenarios show that TrafficSimAgent effectively executes simulations under various conditions and consistently produces reasonable outcomes even when user instructions are ambiguous. Besides, the carefully designed expert-level autonomous decision-driven optimization in TrafficSimAgent yields superior performance when compared with other systems and SOTA LLM based methods.

