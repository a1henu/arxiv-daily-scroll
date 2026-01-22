---
layout: default
title: INFA-Guard: Mitigating Malicious Propagation via Infection-Aware Safeguarding in LLM-Based Multi-Agent Systems
---

# INFA-Guard: Mitigating Malicious Propagation via Infection-Aware Safeguarding in LLM-Based Multi-Agent Systems
**arXiv**：[2601.14667v1](https://arxiv.org/abs/2601.14667) · [PDF](https://arxiv.org/pdf/2601.14667.pdf)  
**作者**：Yijin Zhou, Xiaoya Lu, Dongrui Liu, Junchi Yan, Jing Shao  

**一句话要点**：提出INFA-Guard框架以缓解基于LLM的多智能体系统中恶意传播问题

**关键词**：多智能体系统, 恶意传播防御, 感染感知检测, 拓扑约束, 攻击成功率降低, 跨模型鲁棒性

## 3 点简述
- 核心问题：传统防御方法无法区分攻击智能体和被感染智能体，导致恶意传播难以控制。
- 方法要点：通过感染感知检测和拓扑约束，精准定位攻击源和感染范围，并替换攻击者、修复被感染者。
- 实验或效果：实验显示INFA-Guard平均降低攻击成功率33%，具有跨模型鲁棒性和高成本效益。

## 摘要（原文）

> The rapid advancement of Large Language Model (LLM)-based Multi-Agent Systems (MAS) has introduced significant security vulnerabilities, where malicious influence can propagate virally through inter-agent communication. Conventional safeguards often rely on a binary paradigm that strictly distinguishes between benign and attack agents, failing to account for infected agents i.e., benign entities converted by attack agents. In this paper, we propose Infection-Aware Guard, INFA-Guard, a novel defense framework that explicitly identifies and addresses infected agents as a distinct threat category. By leveraging infection-aware detection and topological constraints, INFA-Guard accurately localizes attack sources and infected ranges. During remediation, INFA-Guard replaces attackers and rehabilitates infected ones, avoiding malicious propagation while preserving topological integrity. Extensive experiments demonstrate that INFA-Guard achieves state-of-the-art performance, reducing the Attack Success Rate (ASR) by an average of 33%, while exhibiting cross-model robustness, superior topological generalization, and high cost-effectiveness.

