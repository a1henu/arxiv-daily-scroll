---
layout: default
title: DrugR: Optimizing Molecular Drugs through LLM-based Explicit Reasoning
---

# DrugR: Optimizing Molecular Drugs through LLM-based Explicit Reasoning
**arXiv**：[2602.08213v1](https://arxiv.org/abs/2602.08213) · [PDF](https://arxiv.org/pdf/2602.08213.pdf)  
**作者**：Haoran Liu, Zheni Zeng, Yukun Yan, Yuxuan Chen, Yunduo Xiao  

**一句话要点**：提出DrugR方法，通过LLM显式推理优化分子药物，以解决分子结构与药理性质间复杂关系问题。

**关键词**：分子优化, 大语言模型, 显式推理, 药理性质, 强化学习, 可解释性

## 3 点简述
- 核心问题：LLM在分子优化中面临分子结构与药理性质间复杂隐式关系及标注数据不足的挑战。
- 方法要点：结合领域持续预训练、反向数据工程监督微调和自平衡多粒度强化学习，引入显式逐步药理推理。
- 实验或效果：实验显示DrugR能全面增强ADMET性质，保持结构相似性和靶点结合亲和力，并提供可解释的推理过程。

## 摘要（原文）

> Molecule generation and optimization is a fundamental task in chemical domain. The rapid development of intelligent tools, especially large language models (LLMs) with powerful knowledge reserves and interactive capabilities, has provided new paradigms for it. Nevertheless, the intrinsic challenge for LLMs lies in the complex implicit relationship between molecular structure and pharmacological properties and the lack of corresponding labeled data. To bridge this gap, we propose DrugR, an LLM-based method that introduces explicit, step-by-step pharmacological reasoning into the optimization process. Our approach integrates domain-specific continual pretraining, supervised fine-tuning via reverse data engineering, and self-balanced multi-granular reinforcement learning. This framework enables DrugR to effectively improve key ADMET properties while preserving the original molecule's core efficacy. Experimental results demonstrate that DrugR achieves comprehensive enhancement across multiple properties without compromising structural similarity or target binding affinity. Importantly, its explicit reasoning process provides clear, interpretable rationales for each optimization step, yielding actionable design insights and advancing toward automated, knowledge-driven scientific discovery. Our code and model checkpoints are open-sourced to foster future research.

