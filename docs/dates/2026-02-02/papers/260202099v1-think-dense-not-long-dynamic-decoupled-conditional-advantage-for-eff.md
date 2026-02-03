---
layout: default
title: Think Dense, Not Long: Dynamic Decoupled Conditional Advantage for Efficient Reasoning
---

# Think Dense, Not Long: Dynamic Decoupled Conditional Advantage for Efficient Reasoning
**arXiv**：[2602.02099v1](https://arxiv.org/abs/2602.02099) · [PDF](https://arxiv.org/pdf/2602.02099.pdf)  
**作者**：Keqin Peng, Yuanxin Ouyang, Xuebo Liu, Zhiliang Tian, Ruijian Han, Yancheng Yuan, Liang Ding  

**一句话要点**：提出动态解耦条件优势以解决强化学习中效率与准确性的权衡问题

**关键词**：强化学习, 推理效率, 条件优势, 动态惩罚, 数学推理, 基线优化

## 3 点简述
- 核心问题：强化学习中的长度惩罚导致基线稀释和难度惩罚不匹配，影响推理效率与准确性
- 方法要点：动态解耦条件优势通过条件计算长度优势消除基线稀释，并基于通过率动态调整惩罚强度
- 实验或效果：在多个数学推理基准上，DDCA显著减少生成令牌数，同时保持或提高准确性

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) can elicit strong multi-step reasoning, yet it often encourages overly verbose traces. Moreover, naive length penalties in group-relative optimization can severely hurt accuracy. We attribute this failure to two structural issues: (i) Dilution of Length Baseline, where incorrect responses (with zero length reward) depress the group baseline and over-penalize correct solutions; and (ii) Difficulty-Penalty Mismatch, where a static penalty cannot adapt to problem difficulty, suppressing necessary reasoning on hard instances while leaving redundancy on easy ones. We propose Dynamic Decoupled Conditional Advantage (DDCA) to decouple efficiency optimization from correctness. DDCA computes length advantages conditionally within the correct-response cluster to eliminate baseline dilution, and dynamically scales the penalty strength using the group pass rate as a proxy for difficulty. Experiments on GSM8K, MATH500, AMC23, and AIME25 show that DDCA consistently improves the efficiency--accuracy trade-off relative to adaptive baselines, reducing generated tokens by approximately 60% on simpler tasks (e.g., GSM8K) versus over 20% on harder benchmarks (e.g., AIME25), thereby maintaining or improving accuracy. Code is available at https://github.com/alphadl/DDCA.

