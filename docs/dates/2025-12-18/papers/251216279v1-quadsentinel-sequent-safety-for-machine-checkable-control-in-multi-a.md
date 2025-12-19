---
layout: default
title: QuadSentinel: Sequent Safety for Machine-Checkable Control in Multi-agent Systems
---

# QuadSentinel: Sequent Safety for Machine-Checkable Control in Multi-agent Systems
**arXiv**：[2512.16279v1](https://arxiv.org/abs/2512.16279) · [PDF](https://arxiv.org/pdf/2512.16279.pdf)  
**作者**：Yiliu Yang, Yilei Jiang, Qunzhong Wang, Yingshui Tan, Xiaoyong Zhu, Sherman S. M. Chow, Bo Zheng, Xiangyu Yue  

**一句话要点**：提出QuadSentinel以解决多智能体系统中基于大语言模型的安全策略机器可检查与在线执行问题

**关键词**：多智能体系统, 安全策略, 机器可检查规则, 在线执行, 大语言模型, 智能体安全

## 3 点简述
- 核心问题：自然语言安全策略模糊且依赖上下文，难以映射为机器可检查规则，导致运行时执行不可靠
- 方法要点：将安全策略表达为sequent，通过四智能体守卫（状态跟踪器、策略验证器、威胁监视器、裁判）编译为基于可观测状态谓词的机器可检查规则并在线执行
- 实验或效果：在ST-WebAgentBench和AgentHarm基准上，QuadSentinel提高了护栏准确性和规则召回率，同时减少误报，优于单智能体基线

## 摘要（原文）

> Safety risks arise as large language model-based agents solve complex tasks with tools, multi-step plans, and inter-agent messages. However, deployer-written policies in natural language are ambiguous and context dependent, so they map poorly to machine-checkable rules, and runtime enforcement is unreliable. Expressing safety policies as sequents, we propose \textsc{QuadSentinel}, a four-agent guard (state tracker, policy verifier, threat watcher, and referee) that compiles these policies into machine-checkable rules built from predicates over observable state and enforces them online. Referee logic plus an efficient top-$k$ predicate updater keeps costs low by prioritizing checks and resolving conflicts hierarchically. Measured on ST-WebAgentBench (ICML CUA~'25) and AgentHarm (ICLR~'25), \textsc{QuadSentinel} improves guardrail accuracy and rule recall while reducing false positives. Against single-agent baselines such as ShieldAgent (ICML~'25), it yields better overall safety control. Near-term deployments can adopt this pattern without modifying core agents by keeping policies separate and machine-checkable. Our code will be made publicly available at https://github.com/yyiliu/QuadSentinel.

