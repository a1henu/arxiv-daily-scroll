---
layout: default
title: DARE-bench: Evaluating Modeling and Instruction Fidelity of LLMs in Data Science
---

# DARE-bench: Evaluating Modeling and Instruction Fidelity of LLMs in Data Science
**arXiv**：[2602.24288v1](https://arxiv.org/abs/2602.24288) · [PDF](https://arxiv.org/pdf/2602.24288.pdf)  
**作者**：Fan Shu, Yite Wang, Ruofan Wu, Boyi Liu, Zhewei Yao, Yuxiong He, Feng Yan  

**一句话要点**：提出DARE-bench基准以评估LLM在数据科学任务中的建模与指令遵循能力

**关键词**：数据科学基准, 指令遵循评估, 机器学习建模, 可验证真值, 微调训练

## 3 点简述
- 现有基准缺乏标准化、过程感知的评估，且缺少准确标注的训练数据
- DARE-bench基于Kaggle任务，提供可验证真值，覆盖广泛任务并支持工具使用
- 实验显示模型性能不足，但微调可显著提升，如Qwen3-4B准确率提升超8倍

## 摘要（原文）

> The fast-growing demands in using Large Language Models (LLMs) to tackle complex multi-step data science tasks create an emergent need for accurate benchmarking. There are two major gaps in existing benchmarks: (i) the lack of standardized, process-aware evaluation that captures instruction adherence and process fidelity, and (ii) the scarcity of accurately labeled training data. To bridge these gaps, we introduce DARE-bench, a benchmark designed for machine learning modeling and data science instruction following. Unlike many existing benchmarks that rely on human- or model-based judges, all tasks in DARE-bench have verifiable ground truth, ensuring objective and reproducible evaluation. To cover a broad range of tasks and support agentic tools, DARE-bench consists of 6,300 Kaggle-derived tasks and provides both large-scale training data and evaluation sets. Extensive evaluations show that even highly capable models such as gpt-o4-mini struggle to achieve good performance, especially in machine learning modeling tasks. Using DARE-bench training tasks for fine-tuning can substantially improve model performance. For example, supervised fine-tuning boosts Qwen3-32B's accuracy by 1.83x and reinforcement learning boosts Qwen3-4B's accuracy by more than 8x. These significant improvements verify the importance of DARE-bench both as an accurate evaluation benchmark and critical training data.

