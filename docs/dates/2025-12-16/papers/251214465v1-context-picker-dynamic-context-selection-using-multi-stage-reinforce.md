---
layout: default
title: Context-Picker: Dynamic context selection using multi-stage reinforcement learning
---

# Context-Picker: Dynamic context selection using multi-stage reinforcement learning
**arXiv**：[2512.14465v1](https://arxiv.org/abs/2512.14465) · [PDF](https://arxiv.org/pdf/2512.14465.pdf)  
**作者**：Siyuan Zhu, Chengdong Xu, Kaiqiang Ke, Chao Yu  

**一句话要点**：提出Context-Picker框架，通过多阶段强化学习解决长上下文问答中的动态上下文选择问题。

**关键词**：长上下文问答, 强化学习, 证据蒸馏, 动态选择, 多阶段优化, 最小充分集

## 3 点简述
- 核心问题：长上下文问答中，固定检索或单阶段重排难以平衡信息覆盖与噪声引入，影响答案质量。
- 方法要点：采用两阶段强化学习，先召回导向覆盖推理链，后精度导向剪枝冗余，蒸馏最小充分证据集。
- 实验或效果：在五个基准测试中显著优于RAG基线，以更少或相当上下文长度实现更高答案准确率。

## 摘要（原文）

> In long-context question answering (LCQA), determining the optimal amount of context for a given query is a significant challenge. Including too few passages may omit critical information, while including too many can introduce noise and reduce the quality of the answer. Traditional approaches, such as fixed Top-$K$ retrieval and single-stage reranking, face the dilemma of selecting the right number of passages. This problem is particularly pronounced for factoid questions, which often require only a few specific pieces of evidence. To address this issue, we introduce \emph{Context-Picker}, a reasoning-aware framework that shifts the paradigm from similarity-based ranking to minimal sufficient subset selection. Context-Picker treats context selection as a decision-making process optimized via a human-inspired, two-stage reinforcement learning schedule: a \emph{recall-oriented} stage that prioritizes the coverage of reasoning chains, followed by a \emph{precision-oriented} stage that aggressively prunes redundancy to distill a compact evidence set. To resolve reward sparsity, we propose an offline evidence distillation pipeline that mines "minimal sufficient sets" via a Leave-One-Out (LOO) procedure, providing dense, task-aligned supervision. Experiments on five long-context and multi-hop QA benchmarks demonstrate that Context-Picker significantly outperforms strong RAG baselines, achieving superior answer accuracy with comparable or reduced context lengths. Ablation studies indicate that the coarse-to-fine optimization schedule, the redundancy-aware reward shaping, and the rationale-guided format all contribute substantially to these gains.

