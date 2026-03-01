---
layout: default
title: Multilingual Safety Alignment Via Sparse Weight Editing
---

# Multilingual Safety Alignment Via Sparse Weight Editing
**arXiv**：[2602.22554v1](https://arxiv.org/abs/2602.22554) · [PDF](https://arxiv.org/pdf/2602.22554.pdf)  
**作者**：Jiaming Liang, Zhaoxin Wang, Handing Wang  

**一句话要点**：提出基于稀疏权重编辑的无训练对齐框架，以解决多语言大模型安全能力不均衡问题。

**关键词**：多语言安全对齐, 稀疏权重编辑, 无训练框架, 线性变换, 安全神经元, 攻击成功率

## 3 点简述
- 核心问题：大模型在低资源语言中安全能力弱，现有方法计算成本高且依赖稀缺数据。
- 方法要点：通过稀疏神经元识别和线性变换，将低资源语言有害表示映射到高资源语言安全子空间。
- 实验或效果：在8种语言和多个模型上显著降低攻击成功率，对通用推理能力影响可忽略。

## 摘要（原文）

> Large Language Models (LLMs) exhibit significant safety disparities across languages, with low-resource languages (LRLs) often bypassing safety guardrails established for high-resource languages (HRLs) like English. Existing solutions, such as multilingual supervised fine-tuning (SFT) or Reinforcement Learning from Human Feedback (RLHF), are computationally expensive and dependent on scarce multilingual safety data. In this work, we propose a novel, training-free alignment framework based on Sparse Weight Editing. Identifying that safety capabilities are localized within a sparse set of safety neurons, we formulate the cross-lingual alignment problem as a constrained linear transformation. We derive a closed-form solution to optimally map the harmful representations of LRLs to the robust safety subspaces of HRLs, while preserving general utility via a null-space projection constraint. Extensive experiments across 8 languages and multiple model families (Llama-3, Qwen-2.5) demonstrate that our method substantially reduces Attack Success Rate (ASR) in LRLs with negligible impact on general reasoning capabilities, all achieved with a single, data-efficient calculation.

