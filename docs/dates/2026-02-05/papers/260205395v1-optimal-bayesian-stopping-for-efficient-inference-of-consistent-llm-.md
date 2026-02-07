---
layout: default
title: Optimal Bayesian Stopping for Efficient Inference of Consistent LLM Answers
---

# Optimal Bayesian Stopping for Efficient Inference of Consistent LLM Answers
**arXiv**：[2602.05395v1](https://arxiv.org/abs/2602.05395) · [PDF](https://arxiv.org/pdf/2602.05395.pdf)  
**作者**：Jingkai Huang, Will Ma, Zhengyuan Zhou  

**一句话要点**：提出基于贝叶斯先验的L-聚合停止策略，以高效推断LLM一致答案并降低采样成本。

**关键词**：贝叶斯停止策略, LLM推理优化, 采样效率, 一致答案推断, 后验近似计算

## 3 点简述
- 核心问题：通过采样多个LLM响应提升准确性，但采样成本高，需优化停止时机。
- 方法要点：利用贝叶斯先验信息，设计L-聚合策略跟踪最频繁答案计数，实现高效后验计算。
- 实验或效果：理论证明L=3可达渐近最优，实证减少采样达50%，保持相似准确率。

## 摘要（原文）

> A simple strategy for improving LLM accuracy, especially in math and reasoning problems, is to sample multiple responses and submit the answer most consistently reached. In this paper we leverage Bayesian prior information to save on sampling costs, stopping once sufficient consistency is reached. Although the exact posterior is computationally intractable, we further introduce an efficient "L-aggregated" stopping policy that tracks only the L-1 most frequent answer counts. Theoretically, we prove that L=3 is all you need: this coarse approximation is sufficient to achieve asymptotic optimality, and strictly dominates prior-free baselines, while having a fast posterior computation. Empirically, this identifies the most consistent (i.e., mode) LLM answer using fewer samples, and can achieve similar answer accuracy while cutting the number of LLM calls (i.e., saving on LLM inference costs) by up to 50%.

