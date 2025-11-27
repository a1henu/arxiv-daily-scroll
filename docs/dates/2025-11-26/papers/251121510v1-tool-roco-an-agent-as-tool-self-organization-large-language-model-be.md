---
layout: default
title: Tool-RoCo: An Agent-as-Tool Self-organization Large Language Model Benchmark in Multi-robot Cooperation
---

# Tool-RoCo: An Agent-as-Tool Self-organization Large Language Model Benchmark in Multi-robot Cooperation
**arXiv**：[2511.21510v1](https://arxiv.org/abs/2511.21510) · [PDF](https://arxiv.org/pdf/2511.21510.pdf)  
**作者**：Ke Zhang, Xiaoning Zhao, Ce Zheng, Jiahong Ning, Dandan Zhu, Wenqi Zhang, Chen Sun, Toshiharu Sugawara  

**一句话要点**：提出Tool-RoCo基准以评估大语言模型在多机器人合作中的自组织能力

**关键词**：多智能体合作, 大语言模型基准, 自组织评估, 工具使用, 机器人协作, 智能体自主性

## 3 点简述
- 核心问题：现有LLM多智能体系统依赖预定义编排，忽视智能体自主性。
- 方法要点：引入合作工具，通过工具使用评估多智能体合作与自组织。
- 实验效果：结果显示合作工具使用率低，激活工具占比高，揭示LLM自适应协调不足。

## 摘要（原文）

> This study proposes Tool-RoCo, a novel benchmark for evaluating large language models (LLMs) in long-term multi-agent cooperation based on RoCo, a multi-robot cooperative benchmark. Recent research on LLM-based multi-agent systems has relied on predefined orchestration, while ignoring agent autonomy. Tool-RoCo treats other agents as tools and introduces cooperative tools, leveraging tool usage to evaluate multi-agent cooperation and self-organization. Tool usage means that each agent (LLM) selects a tool from a candidate set based on the current state, receives feedback, and adjusts its selection in subsequent rounds. To evaluate different autonomy levels, we propose four LLM paradigms: (1) centralized cooperation, where a single LLM allocates tools to all agents; (2) centralized self-organization, where a central LLM autonomously activates agents while keeping others inactive; (3) decentralized cooperation, where each agent has its own LLM and calls tools based on local information; and (4) self-organization, where a randomly chosen initial agent can request collaboration, activating additional agents via tool calls. Tool-RoCo includes three multi-robot tasks, SORT, PACK, and CABINET, to measure format and parameter accuracy and agent coordination through tool usage. The results using several LLMs showed that cooperative tools accounted for only 7.09% of all tools, indicating that LLM-based agents rarely invoked others as assistants. Moreover, activation tools accounted for 96.42%, suggesting that current LLMs tend to maintain active agents while seldom deactivating them for adaptive coordination. Tool-RoCo provides a systematic benchmark to evaluate LLM autonomy and cooperation in multi-agent tasks. Code and Demo: https://github.com/ColaZhang22/Tool-Roco

