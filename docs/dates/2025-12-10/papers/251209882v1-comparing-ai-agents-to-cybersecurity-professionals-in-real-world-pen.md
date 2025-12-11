---
layout: default
title: Comparing AI Agents to Cybersecurity Professionals in Real-World Penetration Testing
---

# Comparing AI Agents to Cybersecurity Professionals in Real-World Penetration Testing
**arXiv**：[2512.09882v1](https://arxiv.org/abs/2512.09882) · [PDF](https://arxiv.org/pdf/2512.09882.pdf)  
**作者**：Justin W. Lin, Eliot Krzysztof Jones, Donovan Julian Jasper, Ethan Jun-shen Ho, Anna Wu, Arnold Tianyi Yang, Neil Perry, Andy Zou, Matt Fredrikson, J. Zico Kolter, Percy Liang, Dan Boneh, Daniel E. Ho  

**一句话要点**：提出ARTEMIS多智能体框架，在真实企业环境中评估AI与人类网络安全专家的渗透测试性能。

**关键词**：AI智能体, 渗透测试, 网络安全评估, 多智能体框架, 漏洞发现

## 3 点简述
- 核心问题：首次在真实企业环境中全面评估AI智能体与人类网络安全专家的渗透测试能力对比。
- 方法要点：ARTEMIS采用动态提示生成、任意子智能体和自动漏洞分类的多智能体框架。
- 实验或效果：ARTEMIS在8000主机网络中排名第二，发现9个有效漏洞，优于9/10人类参与者，但存在高误报率和GUI任务困难。

## 摘要（原文）

> We present the first comprehensive evaluation of AI agents against human cybersecurity professionals in a live enterprise environment. We evaluate ten cybersecurity professionals alongside six existing AI agents and ARTEMIS, our new agent scaffold, on a large university network consisting of ~8,000 hosts across 12 subnets. ARTEMIS is a multi-agent framework featuring dynamic prompt generation, arbitrary sub-agents, and automatic vulnerability triaging. In our comparative study, ARTEMIS placed second overall, discovering 9 valid vulnerabilities with an 82% valid submission rate and outperforming 9 of 10 human participants. While existing scaffolds such as Codex and CyAgent underperformed relative to most human participants, ARTEMIS demonstrated technical sophistication and submission quality comparable to the strongest participants. We observe that AI agents offer advantages in systematic enumeration, parallel exploitation, and cost -- certain ARTEMIS variants cost $18/hour versus $60/hour for professional penetration testers. We also identify key capability gaps: AI agents exhibit higher false-positive rates and struggle with GUI-based tasks.

