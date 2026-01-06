---
layout: default
title: Refinement Provenance Inference: Detecting LLM-Refined Training Prompts from Model Behavior
---

# Refinement Provenance Inference: Detecting LLM-Refined Training Prompts from Model Behavior
**arXiv**：[2601.01966v1](https://arxiv.org/abs/2601.01966) · [PDF](https://arxiv.org/pdf/2601.01966.pdf)  
**作者**：Bo Yin, Qi Li, Runpeng Yu, Xinchao Wang  

**一句话要点**：提出RePro框架以检测指令调优中LLM精炼训练提示的来源

**关键词**：指令调优, 提示精炼, 来源推断, 模型审计, 分布偏移

## 3 点简述
- 核心问题：在混合训练语料中推断模型是否基于原始提示或其LLM精炼版本训练
- 方法要点：基于教师强制标记分布和logit排序信号，通过影子微调学习可迁移表示
- 实验或效果：RePro在跨精炼器上表现稳定，利用与精炼器无关的分布偏移

## 摘要（原文）

> Instruction tuning increasingly relies on LLM-based prompt refinement, where prompts in the training corpus are selectively rewritten by an external refiner to improve clarity and instruction alignment. This motivates an instance-level audit problem: for a fine-tuned model and a training prompt-response pair, can we infer whether the model was trained on the original prompt or its LLM-refined version within a mixed corpus? This matters for dataset governance and dispute resolution when training data are contested. However, it is non-trivial in practice: refined and raw instances are interleaved in the training corpus with unknown, source-dependent mixture ratios, making it harder to develop provenance methods that generalize across models and training setups. In this paper, we formalize this audit task as Refinement Provenance Inference (RPI) and show that prompt refinement yields stable, detectable shifts in teacher-forced token distributions, even when semantic differences are not obvious. Building on this phenomenon, we propose RePro, a logit-based provenance framework that fuses teacher-forced likelihood features with logit-ranking signals. During training, RePro learns a transferable representation via shadow fine-tuning, and uses a lightweight linear head to infer provenance on unseen victims without training-data access. Empirically, RePro consistently attains strong performance and transfers well across refiners, suggesting that it exploits refiner-agnostic distribution shifts rather than rewrite-style artifacts.

