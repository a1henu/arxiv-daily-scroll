---
layout: default
title: BioAgent Bench: An AI Agent Evaluation Suite for Bioinformatics
---

# BioAgent Bench: An AI Agent Evaluation Suite for Bioinformatics
**arXiv**：[2601.21800v1](https://arxiv.org/abs/2601.21800) · [PDF](https://arxiv.org/pdf/2601.21800.pdf)  
**作者**：Dionizije Fa, Marko Čuljak, Bruno Pandža, Mateo Čupić  

**一句话要点**：提出BioAgent Bench基准套件以评估AI代理在生物信息学任务中的性能与鲁棒性。

**关键词**：AI代理评估, 生物信息学基准, 多步骤管道, 鲁棒性测试, 自动化评分

## 3 点简述
- 核心问题：缺乏标准化基准来评估AI代理在生物信息学多步骤任务中的表现。
- 方法要点：构建包含端到端任务和自动化评估的基准数据集，支持受控扰动下的压力测试。
- 实验或效果：前沿代理能可靠完成管道，但鲁棒性测试揭示在扰动下存在失败模式。

## 摘要（原文）

> This paper introduces BioAgent Bench, a benchmark dataset and an evaluation suite designed for measuring the performance and robustness of AI agents in common bioinformatics tasks. The benchmark contains curated end-to-end tasks (e.g., RNA-seq, variant calling, metagenomics) with prompts that specify concrete output artifacts to support automated assessment, including stress testing under controlled perturbations. We evaluate frontier closed-source and open-weight models across multiple agent harnesses, and use an LLM-based grader to score pipeline progress and outcome validity. We find that frontier agents can complete multi-step bioinformatics pipelines without elaborate custom scaffolding, often producing the requested final artifacts reliably. However, robustness tests reveal failure modes under controlled perturbations (corrupted inputs, decoy files, and prompt bloat), indicating that correct high-level pipeline construction does not guarantee reliable step-level reasoning. Finally, because bioinformatics workflows may involve sensitive patient data, proprietary references, or unpublished IP, closed-source models can be unsuitable under strict privacy constraints; in such settings, open-weight models may be preferable despite lower completion rates. We release the dataset and evaluation suite publicly.

