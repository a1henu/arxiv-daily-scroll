---
layout: default
title: Automated Risk-of-Bias Assessment of Randomized Controlled Trials: A First Look at a GEPA-trained Programmatic Prompting Framework
---

# Automated Risk-of-Bias Assessment of Randomized Controlled Trials: A First Look at a GEPA-trained Programmatic Prompting Framework
**arXiv**：[2512.01452v1](https://arxiv.org/abs/2512.01452) · [PDF](https://arxiv.org/pdf/2512.01452.pdf)  
**作者**：Lingbo Li, Anuradha Mathrani, Teo Susnjak  

**一句话要点**：提出基于GEPA的程序化提示框架以自动化随机对照试验偏倚风险评估

**关键词**：偏倚风险评估, 程序化提示, GEPA模块, 随机对照试验, 证据合成, 大型语言模型

## 3 点简述
- 核心问题：手动偏倚风险评估资源密集且存在变异性，现有LLM方法依赖难以复现的手工提示
- 方法要点：使用DSPy和GEPA模块，通过帕累托引导搜索优化代码化提示，生成可检查的执行轨迹
- 实验或效果：在100个RCT上评估，GEPA提示在清晰报告领域表现最佳，整体准确率最高，相比手动提示提升30%-40%

## 摘要（原文）

> Assessing risk of bias (RoB) in randomized controlled trials is essential for trustworthy evidence synthesis, but the process is resource-intensive and prone to variability across reviewers. Large language models (LLMs) offer a route to automation, but existing methods rely on manually engineered prompts that are difficult to reproduce, generalize, or evaluate. This study introduces a programmable RoB assessment pipeline that replaces ad-hoc prompt design with structured, code-based optimization using DSPy and its GEPA module. GEPA refines LLM reasoning through Pareto-guided search and produces inspectable execution traces, enabling transparent replication of every step in the optimization process. We evaluated the method on 100 RCTs from published meta-analyses across seven RoB domains. GEPA-generated prompts were applied to both open-weight models (Mistral Small 3.1 with GPT-oss-20b) and commercial models (GPT-5 Nano and GPT-5 Mini). In domains with clearer methodological reporting, such as Random Sequence Generation, GEPA-generated prompts performed best, with similar results for Allocation Concealment and Blinding of Participants, while the commercial model performed slightly better overall. We also compared GEPA with three manually designed prompts using Claude 3.5 Sonnet. GEPA achieved the highest overall accuracy and improved performance by 30%-40% in Random Sequence Generation and Selective Reporting, and showed generally comparable, competitively aligned performance in the other domains relative to manual prompts. These findings suggest that GEPA can produce consistent and reproducible prompts for RoB assessment, supporting the structured and principled use of LLMs in evidence synthesis.

