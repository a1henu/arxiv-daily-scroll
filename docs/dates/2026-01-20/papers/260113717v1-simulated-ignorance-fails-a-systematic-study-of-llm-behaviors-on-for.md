---
layout: default
title: Simulated Ignorance Fails: A Systematic Study of LLM Behaviors on Forecasting Problems Before Model Knowledge Cutoff
---

# Simulated Ignorance Fails: A Systematic Study of LLM Behaviors on Forecasting Problems Before Model Knowledge Cutoff
**arXiv**：[2601.13717v1](https://arxiv.org/abs/2601.13717) · [PDF](https://arxiv.org/pdf/2601.13717.pdf)  
**作者**：Zehan Li, Yuxuan Wang, Ali El Lahib, Ying-Jieh Xia, Xinyu Pi  

**一句话要点**：系统评估模拟无知在LLM预测问题中的失败，揭示其无法近似真实无知

**关键词**：大语言模型预测, 模拟无知, 知识截止, 回顾预测, 推理抑制, 评估方法

## 3 点简述
- 核心问题：评估LLM预测能力时，前瞻评估延迟高，回顾预测面临知识截止后数据减少的挑战
- 方法要点：测试模拟无知（通过提示抑制知识）是否能近似真实无知，使用477个竞争级问题和9个模型
- 实验或效果：模拟无知系统性失败，性能差距达52%，推理无法有效抑制知识，推理优化模型表现更差

## 摘要（原文）

> Evaluating LLM forecasting capabilities is constrained by a fundamental tension: prospective evaluation offers methodological rigor but prohibitive latency, while retrospective forecasting (RF) -- evaluating on already-resolved events -- faces rapidly shrinking clean evaluation data as SOTA models possess increasingly recent knowledge cutoffs. Simulated Ignorance (SI), prompting models to suppress pre-cutoff knowledge, has emerged as a potential solution. We provide the first systematic test of whether SI can approximate True Ignorance (TI). Across 477 competition-level questions and 9 models, we find that SI fails systematically: (1) cutoff instructions leave a 52% performance gap between SI and TI; (2) chain-of-thought reasoning fails to suppress prior knowledge, even when reasoning traces contain no explicit post-cutoff references; (3) reasoning-optimized models exhibit worse SI fidelity despite superior reasoning trace quality. These findings demonstrate that prompts cannot reliably "rewind" model knowledge. We conclude that RF on pre-cutoff events is methodologically flawed; we recommend against using SI-based retrospective setups to benchmark forecasting capabilities.

