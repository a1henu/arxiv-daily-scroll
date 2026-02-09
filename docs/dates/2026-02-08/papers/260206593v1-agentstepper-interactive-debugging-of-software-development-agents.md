---
layout: default
title: AgentStepper: Interactive Debugging of Software Development Agents
---

# AgentStepper: Interactive Debugging of Software Development Agents
**arXiv**：[2602.06593v1](https://arxiv.org/abs/2602.06593) · [PDF](https://arxiv.org/pdf/2602.06593.pdf)  
**作者**：Robert Hutter, Michael Pradel  

**一句话要点**：提出AgentStepper交互式调试器以解决基于LLM的软件开发代理调试难题

**关键词**：软件开发代理, 交互式调试, LLM轨迹分析, 软件工程工具, 用户研究

## 3 点简述
- 核心问题：基于LLM的软件开发代理调试困难，缺乏可理解的中间过程展示
- 方法要点：将代理轨迹表示为结构化对话，支持断点、逐步执行和实时编辑
- 实验或效果：集成到现有代理需少量代码修改，用户研究显示提升轨迹理解和错误识别能力

## 摘要（原文）

> Software development agents powered by large language models (LLMs) have shown great promise in automating tasks like environment setup, issue solving, and program repair. Unfortunately, understanding and debugging such agents remain challenging due to their complex and dynamic nature. Developers must reason about trajectories of LLM queries, tool calls, and code modifications, but current techniques reveal little of this intermediate process in a comprehensible format. The key insight of this paper is that debugging software development agents shares many similarities with conventional debugging of software programs, yet requires a higher level of abstraction that raises the level from low-level implementation details to high-level agent actions. Drawing on this insight, we introduce AgentStepper, the first interactive debugger for LLM-based software engineering agents. AgentStepper enables developers to inspect, control, and interactively manipulate agent trajectories. AgentStepper represents trajectories as structured conversations among an LLM, the agent program, and tools. It supports breakpoints, stepwise execution, and live editing of prompts and tool invocations, while capturing and displaying intermediate repository-level code changes. Our evaluation applies AgentStepper to three state-of-the-art software development agents, ExecutionAgent, SWE-Agent, and RepairAgent, showing that integrating the approach into existing agents requires minor code changes (39-42 edited lines). Moreover, we report on a user study with twelve participants, indicating that AgentStepper improves the ability of participants to interpret trajectories (64% vs. 67% mean performance) and identify bugs in the agent's implementation (17% vs. 60% success rate), while reducing perceived workload (e.g., frustration reduced from 5.4/7.0 to 2.4/7.0) compared to conventional tools.

