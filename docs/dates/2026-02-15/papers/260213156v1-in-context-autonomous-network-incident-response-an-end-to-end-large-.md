---
layout: default
title: In-Context Autonomous Network Incident Response: An End-to-End Large Language Model Agent Approach
---

# In-Context Autonomous Network Incident Response: An End-to-End Large Language Model Agent Approach
**arXiv**：[2602.13156v1](https://arxiv.org/abs/2602.13156) · [PDF](https://arxiv.org/pdf/2602.13156.pdf)  
**作者**：Yiran Gao, Kim Hammar, Tao Li  

**一句话要点**：提出基于大型语言模型的端到端自主网络事件响应代理，利用上下文学习实现快速恢复。

**关键词**：网络事件响应, 大型语言模型代理, 上下文学习, 端到端系统, 自主适应

## 3 点简述
- 核心问题：传统强化学习方法需手工建模模拟器，抑制原始日志语义，难以适应快速演变的网络攻击。
- 方法要点：集成感知、推理、规划和行动功能于轻量级LLM，通过微调和思维链推理处理日志并生成响应。
- 实验或效果：在文献事件日志评估中，恢复速度比前沿LLM快达23%，无需建模且可在商用硬件运行。

## 摘要（原文）

> Rapidly evolving cyberattacks demand incident response systems that can autonomously learn and adapt to changing threats. Prior work has extensively explored the reinforcement learning approach, which involves learning response strategies through extensive simulation of the incident. While this approach can be effective, it requires handcrafted modeling of the simulator and suppresses useful semantics from raw system logs and alerts. To address these limitations, we propose to leverage large language models' (LLM) pre-trained security knowledge and in-context learning to create an end-to-end agentic solution for incident response planning. Specifically, our agent integrates four functionalities, perception, reasoning, planning, and action, into one lightweight LLM (14b model). Through fine-tuning and chain-of-thought reasoning, our LLM agent is capable of processing system logs and inferring the underlying network state (perception), updating its conjecture of attack models (reasoning), simulating consequences under different response strategies (planning), and generating an effective response (action). By comparing LLM-simulated outcomes with actual observations, the LLM agent repeatedly refines its attack conjecture and corresponding response, thereby demonstrating in-context adaptation. Our agentic approach is free of modeling and can run on commodity hardware. When evaluated on incident logs reported in the literature, our agent achieves recovery up to 23% faster than those of frontier LLMs.

