---
layout: default
title: PROTEA: Securing Robot Task Planning and Execution
---

# PROTEA: Securing Robot Task Planning and Execution
**arXiv**：[2601.07186v1](https://arxiv.org/abs/2601.07186) · [PDF](https://arxiv.org/pdf/2601.07186.pdf)  
**作者**：Zainab Altaweel, Mohaiminul Al Nahian, Jake Juettner, Adnan Siraj Rakin, Shiqi Zhang  

**一句话要点**：提出PROTEA防御机制，利用LLM评估机器人任务计划安全性

**关键词**：机器人任务规划, 对抗攻击防御, LLM安全评估, 计划安全性, 基础模型安全

## 3 点简述
- 核心问题：现有机器人任务规划器存在对抗攻击漏洞，尤其基于基础模型的系统
- 方法要点：采用LLM-as-a-Judge机制，解决计划安全评估中的维度和历史挑战
- 实验或效果：构建包含良性/恶意计划的数据集，评估不同隐蔽程度的攻击

## 摘要（原文）

> Robots need task planning methods to generate action sequences for complex tasks. Recent work on adversarial attacks has revealed significant vulnerabilities in existing robot task planners, especially those built on foundation models. In this paper, we aim to address these security challenges by introducing PROTEA, an LLM-as-a-Judge defense mechanism, to evaluate the security of task plans. PROTEA is developed to address the dimensionality and history challenges in plan safety assessment. We used different LLMs to implement multiple versions of PROTEA for comparison purposes. For systemic evaluations, we created a dataset containing both benign and malicious task plans, where the harmful behaviors were injected at varying levels of stealthiness. Our results provide actionable insights for robotic system practitioners seeking to enhance robustness and security of their task planning systems. Details, dataset and demos are provided: https://protea-secure.github.io/PROTEA/

