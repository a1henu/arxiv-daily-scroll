---
layout: default
title: When "Better" Prompts Hurt: Evaluation-Driven Iteration for LLM Applications
---

# When "Better" Prompts Hurt: Evaluation-Driven Iteration for LLM Applications
**arXiv**：[2601.22025v1](https://arxiv.org/abs/2601.22025) · [PDF](https://arxiv.org/pdf/2601.22025.pdf)  
**作者**：Daniel Commey  

**一句话要点**：提出评估驱动工作流与最小可行评估套件以优化LLM应用迭代

**关键词**：LLM应用评估, 提示工程, 检索增强生成, 代理工作流, 评估套件, 迭代优化

## 3 点简述
- 核心问题：LLM应用评估因输出随机性、高维度和对提示敏感而不同于传统软件测试
- 方法要点：引入Define-Test-Diagnose-Fix工作流和分层评估套件MVES，涵盖通用应用、RAG和代理工具使用
- 实验或效果：实验显示通用提示模板可能降低特定任务性能，如提取通过率从100%降至90%，强调评估驱动迭代的重要性

## 摘要（原文）

> Evaluating Large Language Model (LLM) applications differs from traditional software testing because outputs are stochastic, high-dimensional, and sensitive to prompt and model changes. We present an evaluation-driven workflow - Define, Test, Diagnose, Fix - that turns these challenges into a repeatable engineering loop.
>   We introduce the Minimum Viable Evaluation Suite (MVES), a tiered set of recommended evaluation components for (i) general LLM applications, (ii) retrieval-augmented generation (RAG), and (iii) agentic tool-use workflows. We also synthesize common evaluation methods (automated checks, human rubrics, and LLM-as-judge) and discuss known judge failure modes.
>   In reproducible local experiments (Ollama; Llama 3 8B Instruct and Qwen 2.5 7B Instruct), we observe that a generic "improved" prompt template can trade off behaviors: on our small structured suites, extraction pass rate decreased from 100% to 90% and RAG compliance from 93.3% to 80% for Llama 3 when replacing task-specific prompts with generic rules, while instruction-following improved. These findings motivate evaluation-driven prompt iteration and careful claim calibration rather than universal prompt recipes.
>   All test suites, harnesses, and results are included for reproducibility.

