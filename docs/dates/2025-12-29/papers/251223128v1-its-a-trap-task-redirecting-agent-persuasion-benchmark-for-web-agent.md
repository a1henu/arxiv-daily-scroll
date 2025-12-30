---
layout: default
title: It's a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents
---

# It's a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents
**arXiv**：[2512.23128v1](https://arxiv.org/abs/2512.23128) · [PDF](https://arxiv.org/pdf/2512.23128.pdf)  
**作者**：Karolina Korgul, Yushi Yang, Arkadiusz Drohomirecki, Piotr Błaszczyk, Will Howard, Lukas Aichberger, Chris Russell, Philip H. S. Torr, Adam Mahdi, Adel Bibi  

**一句话要点**：提出TRAP基准以评估基于大语言模型的Web代理在真实任务中受提示注入攻击的脆弱性。

**关键词**：Web代理安全, 提示注入攻击, 任务重定向基准, 社会工程框架, 大语言模型评估, 心理驱动漏洞

## 3 点简述
- 核心问题：Web代理依赖动态内容，易受隐藏于界面元素的对抗性提示注入攻击，导致任务重定向。
- 方法要点：引入TRAP基准，包含模块化社会工程注入框架，在高保真网站克隆上进行受控实验。
- 实验或效果：在六个前沿模型中，代理平均25%任务易受攻击，小界面或上下文变化常使成功率翻倍，揭示系统性心理驱动漏洞。

## 摘要（原文）

> Web-based agents powered by large language models are increasingly used for tasks such as email management or professional networking. Their reliance on dynamic web content, however, makes them vulnerable to prompt injection attacks: adversarial instructions hidden in interface elements that persuade the agent to divert from its original task. We introduce the Task-Redirecting Agent Persuasion Benchmark (TRAP), an evaluation for studying how persuasion techniques misguide autonomous web agents on realistic tasks. Across six frontier models, agents are susceptible to prompt injection in 25\% of tasks on average (13\% for GPT-5 to 43\% for DeepSeek-R1), with small interface or contextual changes often doubling success rates and revealing systemic, psychologically driven vulnerabilities in web-based agents. We also provide a modular social-engineering injection framework with controlled experiments on high-fidelity website clones, allowing for further benchmark expansion.

