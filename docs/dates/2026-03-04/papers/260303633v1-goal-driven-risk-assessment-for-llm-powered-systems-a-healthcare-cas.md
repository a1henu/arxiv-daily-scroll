---
layout: default
title: Goal-Driven Risk Assessment for LLM-Powered Systems: A Healthcare Case Study
---

# Goal-Driven Risk Assessment for LLM-Powered Systems: A Healthcare Case Study
**arXiv**：[2603.03633v1](https://arxiv.org/abs/2603.03633) · [PDF](https://arxiv.org/pdf/2603.03633.pdf)  
**作者**：Neha Nagaraja, Hayretdin Bahsi  

**一句话要点**：提出目标驱动风险评估方法，以解决LLM医疗系统中威胁建模模糊的问题。

**关键词**：LLM风险评估, 攻击树, 医疗系统安全, 威胁建模, 目标驱动方法

## 3 点简述
- 核心问题：LLM系统威胁建模抽象，难以评估风险优先级。
- 方法要点：使用攻击树结构化威胁，结合攻击向量和路径。
- 实验或效果：在LLM医疗代理案例中演示，整合传统与新型攻击。

## 摘要（原文）

> While incorporating LLMs into systems offers significant benefits in critical application areas such as healthcare, new security challenges emerge due to the potential cyber kill chain cycles that combine adversarial model, prompt injection and conventional cyber attacks. Threat modeling methods enable the system designers to identify potential cyber threats and the relevant mitigations during the early stages of development. Although the cyber security community has extensive experience in applying these methods to software-based systems, the elicited threats are usually abstract and vague, limiting their effectiveness for conducting proper likelihood and impact assessments for risk prioritization, especially in complex systems with novel attacks surfaces, such as those involving LLMs. In this study, we propose a structured, goal driven risk assessment approach that contextualizes the threats with detailed attack vectors, preconditions, and attack paths through the use of attack trees. We demonstrate the proposed approach on a case study with an LLM agent-based healthcare system. This study harmonizes the state-of-the-art attacks to LLMs with conventional ones and presents possible attack paths applicable to similar systems. By providing a structured risk assessment, this study makes a significant contribution to the literature and advances the secure-by-design practices in LLM-based systems.

