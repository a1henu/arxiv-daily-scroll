---
layout: default
title: On the Effectiveness of Instruction-Tuning Local LLMs for Identifying Software Vulnerabilities
---

# On the Effectiveness of Instruction-Tuning Local LLMs for Identifying Software Vulnerabilities
**arXiv**：[2512.20062v1](https://arxiv.org/abs/2512.20062) · [PDF](https://arxiv.org/pdf/2512.20062.pdf)  
**作者**：Sangryu Park, Gihyuk Ko, Homook Cho  

**一句话要点**：提出指令微调本地LLMs以识别软件漏洞类型，解决依赖在线API和二元分类的局限。

**关键词**：软件漏洞识别, 指令微调, 本地大语言模型, CWE分类, 安全分析

## 3 点简述
- 核心问题：现有LLMs漏洞分析依赖在线API，需披露源码，且多为二元分类，实用性受限。
- 方法要点：将任务重构为软件漏洞识别，输出CWE ID类型，指令微调本地LLMs提升性能。
- 实验或效果：指令微调本地LLMs在整体性能和成本权衡上优于在线API模型，更安全实用。

## 摘要（原文）

> Large Language Models (LLMs) show significant promise in automating software vulnerability analysis, a critical task given the impact of security failure of modern software systems. However, current approaches in using LLMs to automate vulnerability analysis mostly rely on using online API-based LLM services, requiring the user to disclose the source code in development. Moreover, they predominantly frame the task as a binary classification(vulnerable or not vulnerable), limiting potential practical utility. This paper addresses these limitations by reformulating the problem as Software Vulnerability Identification (SVI), where LLMs are asked to output the type of weakness in Common Weakness Enumeration (CWE) IDs rather than simply indicating the presence or absence of a vulnerability. We also tackle the reliance on large, API-based LLMs by demonstrating that instruction-tuning smaller, locally deployable LLMs can achieve superior identification performance. In our analysis, instruct-tuning a local LLM showed better overall performance and cost trade-off than online API-based LLMs. Our findings indicate that instruct-tuned local models represent a more effective, secure, and practical approach for leveraging LLMs in real-world vulnerability management workflows.

