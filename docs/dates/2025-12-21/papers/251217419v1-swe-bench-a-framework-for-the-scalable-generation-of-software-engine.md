---
layout: default
title: SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories
---

# SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories
**arXiv**：[2512.17419v1](https://arxiv.org/abs/2512.17419) · [PDF](https://arxiv.org/pdf/2512.17419.pdf)  
**作者**：Lilin Wang, Lucas Ramalho, Alan Celestino, Phuc Anthony Pham, Yu Liu, Umang Kumar Sinha, Andres Portillo, Onassis Osunwa, Gabriel Maduekwe  

**一句话要点**：提出SWE-Bench++框架，从开源仓库自动生成多语言软件工程基准测试任务

**关键词**：软件工程基准测试, 多语言代码生成, 自动化任务生成, GitHub拉取请求, 执行式评估, 模型微调

## 3 点简述
- 现有基准测试依赖人工构建，局限于Python错误修复，缺乏多语言覆盖
- 通过自动化管道从GitHub拉取请求生成任务，覆盖11种语言的错误修复和功能请求
- 在1,782个实例上评估，最强模型通过率最高达36.20%，微调可提升多语言基准性能

## 摘要（原文）

> Benchmarks like SWE-bench have standardized the evaluation of Large Language Models (LLMs) on repository-level software engineering tasks. However, these efforts remain limited by manual curation, static datasets, and a focus on Python-based bug fixes. We introduce SWE-Bench++, an automated framework that generates repository-level coding tasks from open-source GitHub projects. Unlike synthetic approaches, our pipeline harvests live pull requests to cover both bug fixes and feature requests across 11 languages. SWE-Bench++ turns GitHub pull requests (PRs) into reproducible, execution-based tasks via four stages: programmatic sourcing, environment synthesis, test oracle extraction, and quality assurance. A final hint-guided trajectory synthesis step converts instances that strong models fail on into training trajectories. Our initial benchmark consists of 11,133 instances from 3,971 repositories across 11 languages. On a subset of 1,782 instances of this benchmark, today's strongest models perform as follows: claude-sonnet-4.5 achieves 36.20% pass@10, gpt-5-2025-08-07 34.57%, gemini/gemini-2.5-pro 24.92%, and gpt-4o 16.89%. We further demonstrate the utility of our dataset by showing that fine-tuning on SWE-Bench++ instances yields measurable improvements on the SWE-bench Multilingual benchmark. SWE-Bench++ provides a scalable, multilingual benchmark for evaluating and improving repository-level code generation.

