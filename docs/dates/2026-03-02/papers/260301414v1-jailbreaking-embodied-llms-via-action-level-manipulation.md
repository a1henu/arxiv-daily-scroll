---
layout: default
title: Jailbreaking Embodied LLMs via Action-level Manipulation
---

# Jailbreaking Embodied LLMs via Action-level Manipulation
**arXiv**：[2603.01414v1](https://arxiv.org/abs/2603.01414) · [PDF](https://arxiv.org/pdf/2603.01414.pdf)  
**作者**：Xinyu Huang, Qiang Yang, Leming Shen, Zijing Ma, Yuanqing Zheng  

**一句话要点**：提出Blindfold框架，通过动作级操纵攻击具身LLM，揭示语言安全与物理后果的错位。

**关键词**：具身大语言模型, 动作级攻击, 对抗代理规划, 物理安全, 机器人控制, 自动化攻击框架

## 3 点简述
- 核心问题：具身LLM存在语言安全与物理后果的错位，语义无害指令可能导致危险物理效应。
- 方法要点：采用对抗代理规划策略，在本地代理LLM上执行动作级操纵，结合噪声注入和规则验证器。
- 实验或效果：在模拟器和真实机器人上评估，攻击成功率比SOTA基线高最多53%。

## 摘要（原文）

> Embodied Large Language Models (LLMs) enable AI agents to interact with the physical world through natural language instructions and actions. However, beyond the language-level risks inherent to LLMs themselves, embodied LLMs with real-world actuation introduce a new vulnerability: instructions that appear semantically benign may still lead to dangerous real-world consequences, revealing a fundamental misalignment between linguistic security and physical outcomes. In this paper, we introduce Blindfold, an automated attack framework that leverages the limited causal reasoning capabilities of embodied LLMs in real-world action contexts. Rather than iterative trial-and-error jailbreaking of black-box embodied LLMs, Blindfold adopts an Adversarial Proxy Planning strategy: it compromises a local surrogate LLM to perform action-level manipulations that appear semantically safe but could result in harmful physical effects when executed. Blindfold further conceals key malicious actions by injecting carefully crafted noise to evade detection by defense mechanisms, and it incorporates a rule-based verifier to improve the attack executability. Evaluations on both embodied AI simulators and a real-world 6DoF robotic arm show that Blindfold achieves up to 53% higher attack success rates than SOTA baselines, highlighting the urgent need to move beyond surface-level language censorship and toward consequence-aware defense mechanisms to secure embodied LLMs.

