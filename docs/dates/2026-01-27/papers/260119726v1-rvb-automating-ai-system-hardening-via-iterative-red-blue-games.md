---
layout: default
title: RvB: Automating AI System Hardening via Iterative Red-Blue Games
---

# RvB: Automating AI System Hardening via Iterative Red-Blue Games
**arXiv**：[2601.19726v1](https://arxiv.org/abs/2601.19726) · [PDF](https://arxiv.org/pdf/2601.19726.pdf)  
**作者**：Lige Huang, Zicheng Liu, Jie Zhang, Lewen Yan, Dongrui Liu, Jing Shao  

**一句话要点**：提出RvB框架以自动化AI系统强化，通过红蓝对抗游戏实现动态迭代防御优化。

**关键词**：AI安全, 对抗性游戏, 系统强化, 动态防御, 免训练优化

## 3 点简述
- 核心问题：AI安全缺乏统一框架，难以动态迭代适应对抗性攻击。
- 方法要点：设计免训练、顺序、不完全信息游戏，红队暴露漏洞，蓝队学习防御方案。
- 实验或效果：在代码加固和护栏优化任务中，防御成功率分别达90%和45%，假阳性率接近0%。

## 摘要（原文）

> The dual offensive and defensive utility of Large Language Models (LLMs) highlights a critical gap in AI security: the lack of unified frameworks for dynamic, iterative adversarial adaptation hardening. To bridge this gap, we propose the Red Team vs. Blue Team (RvB) framework, formulated as a training-free, sequential, imperfect-information game. In this process, the Red Team exposes vulnerabilities, driving the Blue Team to learning effective solutions without parameter updates. We validate our framework across two challenging domains: dynamic code hardening against CVEs and guardrail optimization against jailbreaks. Our empirical results show that this interaction compels the Blue Team to learn fundamental defensive principles, leading to robust remediations that are not merely overfitted to specific exploits. RvB achieves Defense Success Rates of 90\% and 45\% across the respective tasks while maintaining near 0\% False Positive Rates, significantly surpassing baselines. This work establishes the iterative adversarial interaction framework as a practical paradigm that automates the continuous hardening of AI systems.

