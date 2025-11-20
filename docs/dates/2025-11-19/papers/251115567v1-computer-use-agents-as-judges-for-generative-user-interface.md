---
layout: default
title: Computer-Use Agents as Judges for Generative User Interface
---

# Computer-Use Agents as Judges for Generative User Interface
**arXiv**：[2511.15567v1](https://arxiv.org/abs/2511.15567) · [PDF](https://arxiv.org/pdf/2511.15567.pdf)  
**作者**：Kevin Qinghong Lin, Siyuan Hu, Linjie Li, Zhengyuan Yang, Lijuan Wang, Philip Torr, Mike Zheng Shou  

**一句话要点**：提出Coder-CUA协作框架，利用计算机使用代理作为评判者辅助自动GUI设计

**关键词**：计算机使用代理, 自动GUI设计, 语言模型协作, 任务可解性评估, 导航成功率, AUI-Gym基准

## 3 点简述
- 核心问题：GUI设计以人类为中心，代理需采用不必要行为，影响任务执行效率
- 方法要点：Coder生成和修订网站，CUA评估功能性和导航成功率，提供反馈
- 实验或效果：构建AUI-Gym基准，涵盖52应用和1560任务，验证任务可解性和导航成功率

## 摘要（原文）

> Computer-Use Agents (CUA) are becoming increasingly capable of autonomously operating digital environments through Graphical User Interfaces (GUI). Yet, most GUI remain designed primarily for humans--prioritizing aesthetics and usability--forcing agents to adopt human-oriented behaviors that are unnecessary for efficient task execution. At the same time, rapid advances in coding-oriented language models (Coder) have transformed automatic GUI design. This raises a fundamental question: Can CUA as judges to assist Coder for automatic GUI design? To investigate, we introduce AUI-Gym, a benchmark for Automatic GUI development spanning 52 applications across diverse domains. Using language models, we synthesize 1560 tasks that simulate real-world scenarios. To ensure task reliability, we further develop a verifier that programmatically checks whether each task is executable within its environment. Building on this, we propose a Coder-CUA in Collaboration framework: the Coder acts as Designer, generating and revising websites, while the CUA serves as Judge, evaluating functionality and refining designs. Success is measured not by visual appearance, but by task solvability and CUA navigation success rate. To turn CUA feedback into usable guidance, we design a CUA Dashboard that compresses multi-step navigation histories into concise visual summaries, offering interpretable guidance for iterative redesign. By positioning agents as both designers and judges, our framework shifts interface design toward agent-native efficiency and reliability. Our work takes a step toward shifting agents from passive use toward active participation in digital environments. Our code and dataset are available at https://github.com/showlab/AUI.

