---
layout: default
title: HoneyTrap: Deceiving Large Language Model Attackers to Honeypot Traps with Resilient Multi-Agent Defense
---

# HoneyTrap: Deceiving Large Language Model Attackers to Honeypot Traps with Resilient Multi-Agent Defense
**arXiv**：[2601.04034v1](https://arxiv.org/abs/2601.04034) · [PDF](https://arxiv.org/pdf/2601.04034.pdf)  
**作者**：Siyuan Li, Xi Lin, Jun Wu, Zehao Liu, Haoyu Li, Tianjie Ju, Xiang Chen, Jianhua Li  

**一句话要点**：提出HoneyTrap框架，利用多智能体协同欺骗防御来应对大语言模型的多轮越狱攻击。

**关键词**：大语言模型安全, 越狱攻击防御, 多智能体系统, 欺骗性防御, 多轮攻击数据集, 资源消耗评估

## 3 点简述
- 核心问题：现有防御方法难以应对快速演化的多轮越狱攻击，攻击者持续深化攻击以利用漏洞。
- 方法要点：集成四个防御智能体（威胁拦截器、误导控制器、取证追踪器、系统协调器），通过协同欺骗策略对抗攻击。
- 实验或效果：在GPT-4等模型上，攻击成功率平均降低68.77%，误导成功率和攻击资源消耗分别提升118.11%和149.16%。

## 摘要（原文）

> Jailbreak attacks pose significant threats to large language models (LLMs), enabling attackers to bypass safeguards. However, existing reactive defense approaches struggle to keep up with the rapidly evolving multi-turn jailbreaks, where attackers continuously deepen their attacks to exploit vulnerabilities. To address this critical challenge, we propose HoneyTrap, a novel deceptive LLM defense framework leveraging collaborative defenders to counter jailbreak attacks. It integrates four defensive agents, Threat Interceptor, Misdirection Controller, Forensic Tracker, and System Harmonizer, each performing a specialized security role and collaborating to complete a deceptive defense. To ensure a comprehensive evaluation, we introduce MTJ-Pro, a challenging multi-turn progressive jailbreak dataset that combines seven advanced jailbreak strategies designed to gradually deepen attack strategies across multi-turn attacks. Besides, we present two novel metrics: Mislead Success Rate (MSR) and Attack Resource Consumption (ARC), which provide more nuanced assessments of deceptive defense beyond conventional measures. Experimental results on GPT-4, GPT-3.5-turbo, Gemini-1.5-pro, and LLaMa-3.1 demonstrate that HoneyTrap achieves an average reduction of 68.77% in attack success rates compared to state-of-the-art baselines. Notably, even in a dedicated adaptive attacker setting with intensified conditions, HoneyTrap remains resilient, leveraging deceptive engagement to prolong interactions, significantly increasing the time and computational costs required for successful exploitation. Unlike simple rejection, HoneyTrap strategically wastes attacker resources without impacting benign queries, improving MSR and ARC by 118.11% and 149.16%, respectively.

