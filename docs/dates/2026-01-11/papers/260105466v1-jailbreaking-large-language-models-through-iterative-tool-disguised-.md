---
layout: default
title: Jailbreaking Large Language Models through Iterative Tool-Disguised Attacks via Reinforcement Learning
---

# Jailbreaking Large Language Models through Iterative Tool-Disguised Attacks via Reinforcement Learning
**arXiv**：[2601.05466v1](https://arxiv.org/abs/2601.05466) · [PDF](https://arxiv.org/pdf/2601.05466.pdf)  
**作者**：Zhaoqi Wang, Zijian Zhang, Daqing He, Pengtao Kou, Xin Li, Jiamou Liu, Jincheng An, Yong Liu  

**一句话要点**：提出iMIST方法，通过强化学习驱动的迭代工具伪装攻击，以解决大语言模型越狱漏洞问题。

**关键词**：大语言模型越狱, 工具伪装攻击, 强化学习优化, 交互式对话, 安全漏洞评估

## 3 点简述
- 核心问题：大语言模型易受越狱攻击，现有防御机制不足以应对复杂对抗策略。
- 方法要点：iMIST伪装恶意查询为工具调用，结合交互式渐进优化算法动态提升响应危害性。
- 实验或效果：在广泛使用的模型上，iMIST实现更高攻击效果，同时保持低拒绝率。

## 摘要（原文）

> Large language models (LLMs) have demonstrated remarkable capabilities across diverse applications, however, they remain critically vulnerable to jailbreak attacks that elicit harmful responses violating human values and safety guidelines. Despite extensive research on defense mechanisms, existing safeguards prove insufficient against sophisticated adversarial strategies. In this work, we propose iMIST (\underline{i}nteractive \underline{M}ulti-step \underline{P}rogre\underline{s}sive \underline{T}ool-disguised Jailbreak Attack), a novel adaptive jailbreak method that synergistically exploits vulnerabilities in current defense mechanisms. iMIST disguises malicious queries as normal tool invocations to bypass content filters, while simultaneously introducing an interactive progressive optimization algorithm that dynamically escalates response harmfulness through multi-turn dialogues guided by real-time harmfulness assessment. Our experiments on widely-used models demonstrate that iMIST achieves higher attack effectiveness, while maintaining low rejection rates. These results reveal critical vulnerabilities in current LLM safety mechanisms and underscore the urgent need for more robust defense strategies.

