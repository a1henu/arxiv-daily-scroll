---
layout: default
title: ALRM: Agentic LLM for Robotic Manipulation
---

# ALRM: Agentic LLM for Robotic Manipulation
**arXiv**：[2601.19510v1](https://arxiv.org/abs/2601.19510) · [PDF](https://arxiv.org/pdf/2601.19510.pdf)  
**作者**：Vitor Gaboardi dos Santos, Ibrahim Khadraoui, Ibrahim Farhat, Hamza Yous, Samy Teffahi, Hakim Hacid  

**一句话要点**：提出ALRM框架以解决LLM在机器人操作中缺乏模块化代理执行和系统评估的问题

**关键词**：机器人操作, 大语言模型, 代理框架, 模拟基准, 代码即策略, 工具即策略

## 3 点简述
- 核心问题：现有LLM方法在机器人控制中缺乏模块化代理执行机制，且基准测试未系统评估多步推理和语言多样性
- 方法要点：ALRM集成策略生成与代理执行，通过ReAct式推理循环支持代码即策略和工具即策略两种模式
- 实验或效果：在包含56个任务的模拟基准上测试十个LLM，显示ALRM可扩展、可解释，Claude-4.1-Opus和Falcon-H1-7B表现最佳

## 摘要（原文）

> Large Language Models (LLMs) have recently empowered agentic frameworks to exhibit advanced reasoning and planning capabilities. However, their integration in robotic control pipelines remains limited in two aspects: (1) prior \ac{llm}-based approaches often lack modular, agentic execution mechanisms, limiting their ability to plan, reflect on outcomes, and revise actions in a closed-loop manner; and (2) existing benchmarks for manipulation tasks focus on low-level control and do not systematically evaluate multistep reasoning and linguistic variation. In this paper, we propose Agentic LLM for Robot Manipulation (ALRM), an LLM-driven agentic framework for robotic manipulation. ALRM integrates policy generation with agentic execution through a ReAct-style reasoning loop, supporting two complementary modes: Code-asPolicy (CaP) for direct executable control code generation, and Tool-as-Policy (TaP) for iterative planning and tool-based action execution. To enable systematic evaluation, we also introduce a novel simulation benchmark comprising 56 tasks across multiple environments, capturing linguistically diverse instructions. Experiments with ten LLMs demonstrate that ALRM provides a scalable, interpretable, and modular approach for bridging natural language reasoning with reliable robotic execution. Results reveal Claude-4.1-Opus as the top closed-source model and Falcon-H1-7B as the top open-source model under CaP.

