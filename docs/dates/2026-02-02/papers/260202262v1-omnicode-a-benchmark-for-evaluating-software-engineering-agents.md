---
layout: default
title: OmniCode: A Benchmark for Evaluating Software Engineering Agents
---

# OmniCode: A Benchmark for Evaluating Software Engineering Agents
**arXiv**：[2602.02262v1](https://arxiv.org/abs/2602.02262) · [PDF](https://arxiv.org/pdf/2602.02262.pdf)  
**作者**：Atharv Sonwane, Eng-Shen Tu, Wei-Chung Lu, Claas Beger, Carter Larsen, Debjit Dhar, Rachel Chen, Ronit Pattanayak, Tuan Anh Dang, Guohao Chen, Gloria Geng, Kevin Ellis, Saikat Dutta  

**一句话要点**：提出OmniCode基准以评估软件工程代理在多样化任务中的能力

**关键词**：软件工程基准, 代码生成评估, 多样化任务, 人工验证, 合成数据生成, 代理性能分析

## 3 点简述
- 现有编码基准如HumanEval和SWE-Bench任务范围狭窄，难以评估真实软件开发中的多样化任务。
- OmniCode包含1794个任务，覆盖Python、Java和C++三种语言，涵盖bug修复、测试生成、代码审查修复和风格修复四类。
- 实验显示，现有代理如SWE-Agent在Python bug修复表现良好，但在测试生成和Java/C++任务上表现不佳，如Java测试生成最高仅20.9%。

## 摘要（原文）

> LLM-powered coding agents are redefining how real-world software is developed. To drive the research towards better coding agents, we require challenging benchmarks that can rigorously evaluate the ability of such agents to perform various software engineering tasks. However, popular coding benchmarks such as HumanEval and SWE-Bench focus on narrowly scoped tasks such as competition programming and patch generation. In reality, software engineers have to handle a broader set of tasks for real-world software development. To address this gap, we propose OmniCode, a novel software engineering benchmark that contains a broader and more diverse set of task categories beyond code or patch generation. Overall, OmniCode contains 1794 tasks spanning three programming languages (Python, Java, and C++) and four key categories: bug fixing, test generation, code review fixing, and style fixing. In contrast to prior software engineering benchmarks, the tasks in OmniCode are (1) manually validated to eliminate ill-defined problems, and (2) synthetically crafted or recently curated to avoid data leakage issues, presenting a new framework for synthetically generating diverse software tasks from limited real-world data. We evaluate OmniCode with popular agent frameworks such as SWE-Agent and show that while they may perform well on bug fixing for Python, they fall short on tasks such as Test Generation and in languages such as C++ and Java. For instance, SWE-Agent achieves a maximum of 20.9% with DeepSeek-V3.1 on Java Test Generation tasks. OmniCode aims to serve as a robust benchmark and spur the development of agents that can perform well across different aspects of software development. Code and data are available at https://github.com/seal-research/OmniCode.

