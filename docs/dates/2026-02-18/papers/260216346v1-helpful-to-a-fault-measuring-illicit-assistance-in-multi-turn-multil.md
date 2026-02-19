---
layout: default
title: Helpful to a Fault: Measuring Illicit Assistance in Multi-Turn, Multilingual LLM Agents
---

# Helpful to a Fault: Measuring Illicit Assistance in Multi-Turn, Multilingual LLM Agents
**arXiv**：[2602.16346v1](https://arxiv.org/abs/2602.16346) · [PDF](https://arxiv.org/pdf/2602.16346.pdf)  
**作者**：Nivya Talokar, Ayush K Tarun, Murari Mandal, Maksym Andriushchenko, Antoine Bosselut  

**一句话要点**：提出STING框架以评估多轮多语言LLM代理中的非法辅助风险

**关键词**：代理滥用评估, 多轮红队测试, 多语言LLM代理, 非法任务检测, 自适应攻击框架

## 3 点简述
- 核心问题：现有代理滥用基准多测试单轮指令，缺乏多轮交互下非法任务完成度的测量
- 方法要点：STING框架基于良性人设构建逐步非法计划，通过自适应跟进和法官代理跟踪阶段完成
- 实验或效果：在AgentHarm场景中，STING比单轮提示和聊天基线显著提高非法任务完成度，多语言评估显示攻击成功率在低资源语言中未一致增加

## 摘要（原文）

> LLM-based agents execute real-world workflows via tools and memory. These affordances enable ill-intended adversaries to also use these agents to carry out complex misuse scenarios. Existing agent misuse benchmarks largely test single-prompt instructions, leaving a gap in measuring how agents end up helping with harmful or illegal tasks over multiple turns. We introduce STING (Sequential Testing of Illicit N-step Goal execution), an automated red-teaming framework that constructs a step-by-step illicit plan grounded in a benign persona and iteratively probes a target agent with adaptive follow-ups, using judge agents to track phase completion. We further introduce an analysis framework that models multi-turn red-teaming as a time-to-first-jailbreak random variable, enabling analysis tools like discovery curves, hazard-ratio attribution by attack language, and a new metric: Restricted Mean Jailbreak Discovery. Across AgentHarm scenarios, STING yields substantially higher illicit-task completion than single-turn prompting and chat-oriented multi-turn baselines adapted to tool-using agents. In multilingual evaluations across six non-English settings, we find that attack success and illicit-task completion do not consistently increase in lower-resource languages, diverging from common chatbot findings. Overall, STING provides a practical way to evaluate and stress-test agent misuse in realistic deployment settings, where interactions are inherently multi-turn and often multilingual.

