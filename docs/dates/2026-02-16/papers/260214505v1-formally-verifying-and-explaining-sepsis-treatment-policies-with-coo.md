---
layout: default
title: Formally Verifying and Explaining Sepsis Treatment Policies with COOL-MC
---

# Formally Verifying and Explaining Sepsis Treatment Policies with COOL-MC
**arXiv**：[2602.14505v1](https://arxiv.org/abs/2602.14505) · [PDF](https://arxiv.org/pdf/2602.14505.pdf)  
**作者**：Dennis Gross  

**一句话要点**：提出COOL-MC工具，通过形式化验证与可解释性分析优化脓毒症治疗策略

**关键词**：形式化验证, 强化学习策略, 可解释性分析, 脓毒症治疗, 模型检查, 医疗决策

## 3 点简述
- 核心问题：强化学习策略在医疗决策中不透明且难以验证，传统模型检查器在大规模MDP中不可行。
- 方法要点：COOL-MC构建策略诱导的可达状态空间，集成PCTL查询和可解释性方法，实现高效验证与决策分析。
- 实验或效果：在ICU-Sepsis MDP基准上验证策略安全边界，揭示策略依赖历史剂量而非患者实时状态的弱点。

## 摘要（原文）

> Safe and interpretable sequential decision-making is critical in healthcare, yet reinforcement learning (RL) policies for sepsis treatment optimization remain opaque and difficult to verify. Standard probabilistic model checkers operate on the full state space, which becomes infeasible for larger MDPs, and cannot explain why a learned policy makes particular decisions. COOL-MC wraps the model checker Storm but adds three key capabilities: it constructs only the reachable state space induced by a trained policy, yielding a smaller discrete-time Markov chain amenable to verification even when full-MDP analysis is intractable; it automatically labels states with clinically meaningful atomic propositions; and it integrates explainability methods with probabilistic computation tree logic (PCTL) queries to reveal which features drive decisions across treatment trajectories. We demonstrate COOL-MC's capabilities on the ICU-Sepsis MDP, a benchmark derived from approximately 17,000 sepsis patient records, which serves as a case study for applying COOL-MC to the formal analysis of sepsis treatment policies. Our analysis establishes hard bounds via full MDP verification, trains a safe RL policy that achieves optimal survival probability, and analyzes its behavior via PCTL verification and explainability on the induced DTMC. This reveals, for instance, that our trained policy relies predominantly on prior dosing history rather than the patient's evolving condition, a weakness that is invisible to standard evaluation but is exposed by COOL-MC's integration of formal verification and explainability. Our results illustrate how COOL-MC could serve as a tool for clinicians to investigate and debug sepsis treatment policies before deployment.

