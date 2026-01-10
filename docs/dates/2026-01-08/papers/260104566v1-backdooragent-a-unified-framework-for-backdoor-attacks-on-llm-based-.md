---
layout: default
title: BackdoorAgent: A Unified Framework for Backdoor Attacks on LLM-based Agents
---

# BackdoorAgent: A Unified Framework for Backdoor Attacks on LLM-based Agents
**arXiv**：[2601.04566v1](https://arxiv.org/abs/2601.04566) · [PDF](https://arxiv.org/pdf/2601.04566.pdf)  
**作者**：Yunhao Feng, Yige Li, Yutao Wu, Yingshui Tan, Yanming Guo, Yifan Ding, Kun Zhai, Xingjun Ma, Yugang Jiang  

**一句话要点**：提出BackdoorAgent框架，统一分析LLM智能体工作流中的后门攻击威胁。

**关键词**：后门攻击, LLM智能体, 工作流安全, 触发传播, 基准测试, 多模态代理

## 3 点简述
- 核心问题：现有研究孤立分析后门攻击，缺乏从智能体视角理解跨阶段触发传播。
- 方法要点：构建模块化框架，将攻击面分为规划、记忆和工具使用三阶段进行系统分析。
- 实验或效果：在标准化基准上验证单阶段触发器可跨步持久传播，如GPT骨干中记忆攻击触发率达77.97%。

## 摘要（原文）

> Large language model (LLM) agents execute tasks through multi-step workflows that combine planning, memory, and tool use. While this design enables autonomy, it also expands the attack surface for backdoor threats. Backdoor triggers injected into specific stages of an agent workflow can persist through multiple intermediate states and adversely influence downstream outputs. However, existing studies remain fragmented and typically analyze individual attack vectors in isolation, leaving the cross-stage interaction and propagation of backdoor triggers poorly understood from an agent-centric perspective. To fill this gap, we propose \textbf{BackdoorAgent}, a modular and stage-aware framework that provides a unified, agent-centric view of backdoor threats in LLM agents. BackdoorAgent structures the attack surface into three functional stages of agentic workflows, including \textbf{planning attacks}, \textbf{memory attacks}, and \textbf{tool-use attacks}, and instruments agent execution to enable systematic analysis of trigger activation and propagation across different stages. Building on this framework, we construct a standardized benchmark spanning four representative agent applications: \textbf{Agent QA}, \textbf{Agent Code}, \textbf{Agent Web}, and \textbf{Agent Drive}, covering both language-only and multimodal settings. Our empirical analysis shows that \textit{triggers implanted at a single stage can persist across multiple steps and propagate through intermediate states.} For instance, when using a GPT-based backbone, we observe trigger persistence in 43.58\% of planning attacks, 77.97\% of memory attacks, and 60.28\% of tool-stage attacks, highlighting the vulnerabilities of the agentic workflow itself to backdoor threats. To facilitate reproducibility and future research, our code and benchmark are publicly available at GitHub.

