---
layout: default
title: TriCEGAR: A Trace-Driven Abstraction Mechanism for Agentic AI
---

# TriCEGAR: A Trace-Driven Abstraction Mechanism for Agentic AI
**arXiv**：[2601.22997v1](https://arxiv.org/abs/2601.22997) · [PDF](https://arxiv.org/pdf/2601.22997.pdf)  
**作者**：Roham Koohestani, Ateş Görpelioğlu, Egor Klimov, Burcu Kulahcioglu Ozkan, Maliheh Izadi  

**一句话要点**：提出TriCEGAR，一种基于执行日志的自动化状态抽象机制，以解决Agentic AI系统行为验证中的状态定义难题。

**关键词**：Agentic AI验证, 状态抽象自动化, 概率模型检查, 执行日志驱动, 行为MDP构建, 异常检测

## 3 点简述
- 核心问题：Agentic AI系统行为依赖非确定性环境和概率模型输出，现有验证方法需手动定义状态抽象，增加应用负担。
- 方法要点：TriCEGAR从执行日志自动学习谓词树作为状态抽象，支持在线构建行为MDP，并利用反例进行精化。
- 实验或效果：实现框架原生支持，包括事件捕获、MDP构建和概率模型检查，可计算成功概率上界和失败概率下界等界限。

## 摘要（原文）

> Agentic AI systems act through tools and evolve their behavior over long, stochastic interaction traces. This setting complicates assurance, because behavior depends on nondeterministic environments and probabilistic model outputs. Prior work introduced runtime verification for agentic AI via Dynamic Probabilistic Assurance (DPA), learning an MDP online and model checking quantitative properties. A key limitation is that developers must manually define the state abstraction, which couples verification to application-specific heuristics and increases adoption friction. This paper proposes TriCEGAR, a trace-driven abstraction mechanism that automates state construction from execution logs and supports online construction of an agent behavioral MDP. TriCEGAR represents abstractions as predicate trees learned from traces and refined using counterexamples. We describe a framework-native implementation that (i) captures typed agent lifecycle events, (ii) builds abstractions from traces, (iii) constructs an MDP, and (iv) performs probabilistic model checking to compute bounds such as Pmax(success) and Pmin(failure). We also show how run likelihoods enable anomaly detection as a guardrailing signal.

