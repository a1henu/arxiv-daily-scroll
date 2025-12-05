---
layout: default
title: Contract-Driven QoE Auditing for Speech and Singing Services: From MOS Regression to Service Graphs
---

# Contract-Driven QoE Auditing for Speech and Singing Services: From MOS Regression to Service Graphs
**arXiv**：[2512.04827v1](https://arxiv.org/abs/2512.04827) · [PDF](https://arxiv.org/pdf/2512.04827.pdf)  
**作者**：Wenzhang Du  

**一句话要点**：提出基于契约的QoE审计框架，用于语音和歌唱服务的质量评估，以解决MOS标量局限性问题。

**关键词**：语音质量评估, 歌唱质量评估, QoE审计, 服务图, 契约驱动, MOS回归

## 3 点简述
- 核心问题：MOS标量无法捕捉用户期望异质性，忽略服务级目标，且难以跨部署图比较。
- 方法要点：通过人类可解释的经验契约集评估服务图，生成契约级满意度向量，将经典MOS回归视为退化特例。
- 实验或效果：在URGENT2024和SingMOS数据集上验证，契约驱动质量在视图变换下更稳定，学习复杂度受语义而非维度控制。

## 摘要（原文）

> Subjective mean opinion scores (MOS) remain the de-facto target for non-intrusive speech and singing quality assessment. However, MOS is a scalar that collapses heterogeneous user expectations, ignores service-level objectives, and is difficult to compare across deployment graphs. We propose a contract-driven QoE auditing framework: each service graph G is evaluated under a set of human-interpretable experience contracts C, yielding a contract-level satisfaction vector Q(G, C). We show that (i) classical MOS regression is a special case with a degenerate contract set, (ii) contract-driven quality is more stable than MOS under graph view transformations (e.g., pooling by system vs. by system type), and (iii) the effective sample complexity of learning contracts is governed by contract semantics rather than merely the dimensionality of C. We instantiate the framework on URGENT2024 MOS (6.9k speech utterances with raw rating vectors) and SingMOS v1 (7,981 singing clips; 80 systems). On URGENT, we train a contract-aware neural auditor on self-supervised WavLM embeddings; on SingMOS, we perform contract-driven graph auditing using released rating vectors and metadata without decoding audio. Empirically, our auditor matches strong MOS predictors in MOS accuracy while providing calibrated contract probabilities; on SingMOS, Q(G, C) exhibits substantially smaller cross-view drift than raw MOS and graph-only baselines; on URGENT, difficulty curves reveal that mis-specified "simple" contracts can be harder to learn than richer but better aligned contract sets.

