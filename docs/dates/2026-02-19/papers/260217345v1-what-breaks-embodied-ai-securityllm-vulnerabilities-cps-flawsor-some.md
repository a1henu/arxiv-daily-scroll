---
layout: default
title: What Breaks Embodied AI Security:LLM Vulnerabilities, CPS Flaws,or Something Else?
---

# What Breaks Embodied AI Security:LLM Vulnerabilities, CPS Flaws,or Something Else?
**arXiv**：[2602.17345v1](https://arxiv.org/abs/2602.17345) · [PDF](https://arxiv.org/pdf/2602.17345.pdf)  
**作者**：Boyang Ma, Hechuan Guo, Peizhuo Lv, Minghui Xu, Xuelong Dai, YeChao Zhang, Yijun Yang, Yue Zhang  

**一句话要点**：提出系统级失配视角以解释具身AI安全漏洞，超越LLM与CPS传统分析框架

**关键词**：具身AI安全, 系统级失配, 物理风险推理, 感知-决策-行动循环, 安全非组合性

## 3 点简述
- 核心问题：具身AI安全失效常源于系统级失配，而非孤立模型缺陷或传统CPS攻击
- 方法要点：识别四个核心洞察，如语义正确性不保证物理安全、小误差在感知-决策-行动循环中放大
- 实验或效果：基于调查分析，强调需转向系统级物理风险推理以提升安全

## 摘要（原文）

> Embodied AI systems (e.g., autonomous vehicles, service robots, and LLM-driven interactive agents) are rapidly transitioning from controlled environments to safety critical real-world deployments. Unlike disembodied AI, failures in embodied intelligence lead to irreversible physical consequences, raising fundamental questions about security, safety, and reliability. While existing research predominantly analyzes embodied AI through the lenses of Large Language Model (LLM) vulnerabilities or classical Cyber-Physical System (CPS) failures, this survey argues that these perspectives are individually insufficient to explain many observed breakdowns in modern embodied systems. We posit that a significant class of failures arises from embodiment-induced system-level mismatches, rather than from isolated model flaws or traditional CPS attacks. Specifically, we identify four core insights that explain why embodied AI is fundamentally harder to secure: (i) semantic correctness does not imply physical safety, as language-level reasoning abstracts away geometry, dynamics, and contact constraints; (ii) identical actions can lead to drastically different outcomes across physical states due to nonlinear dynamics and state uncertainty; (iii) small errors propagate and amplify across tightly coupled perception-decision-action loops; and (iv) safety is not compositional across time or system layers, enabling locally safe decisions to accumulate into globally unsafe behavior. These insights suggest that securing embodied AI requires moving beyond component-level defenses toward system-level reasoning about physical risk, uncertainty, and failure propagation.

