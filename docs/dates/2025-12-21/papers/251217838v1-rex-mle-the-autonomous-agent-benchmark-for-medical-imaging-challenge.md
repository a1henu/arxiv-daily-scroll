---
layout: default
title: ReX-MLE: The Autonomous Agent Benchmark for Medical Imaging Challenges
---

# ReX-MLE: The Autonomous Agent Benchmark for Medical Imaging Challenges
**arXiv**：[2512.17838v1](https://arxiv.org/abs/2512.17838) · [PDF](https://arxiv.org/pdf/2512.17838.pdf)  
**作者**：Roshan Kenia, Xiaoman Zhang, Pranav Rajpurkar  

**一句话要点**：提出ReX-MLE基准以评估自主代理在医学影像挑战中的端到端工作流能力

**关键词**：自主代理基准, 医学影像挑战, 端到端工作流, 领域特定AI, 大语言模型评估, 数据预处理

## 3 点简述
- 核心问题：现有自主代理基准无法有效衡量复杂医学影像任务中的领域特定能力
- 方法要点：基于20个高影响力医学影像竞赛构建基准，要求代理独立管理数据预处理、模型训练和提交
- 实验或效果：评估显示当前代理性能远低于人类专家，暴露领域知识和工程限制

## 摘要（原文）

> Autonomous coding agents built on large language models (LLMs) can now solve many general software and machine learning tasks, but they remain ineffective on complex, domain-specific scientific problems. Medical imaging is a particularly demanding domain, requiring long training cycles, high-dimensional data handling, and specialized preprocessing and validation pipelines, capabilities not fully measured in existing agent benchmarks. To address this gap, we introduce ReX-MLE, a benchmark of 20 challenges derived from high-impact medical imaging competitions spanning diverse modalities and task types. Unlike prior ML-agent benchmarks, ReX-MLE evaluates full end-to-end workflows, requiring agents to independently manage data preprocessing, model training, and submission under realistic compute and time constraints. Evaluating state-of-the-art agents (AIDE, ML-Master, R&D-Agent) with different LLM backends (GPT-5, Gemini, Claude), we observe a severe performance gap: most submissions rank in the 0th percentile compared to human experts. Failures stem from domain-knowledge and engineering limitations. ReX-MLE exposes these bottlenecks and provides a foundation for developing domain-aware autonomous AI systems.

