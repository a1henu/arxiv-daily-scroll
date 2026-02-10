---
layout: default
title: Beyond Correctness: Learning Robust Reasoning via Transfer
---

# Beyond Correctness: Learning Robust Reasoning via Transfer
**arXiv**：[2602.08489v1](https://arxiv.org/abs/2602.08489) · [PDF](https://arxiv.org/pdf/2602.08489.pdf)  
**作者**：Hyunseok Lee, Soheil Abbasloo, Jihoon Tack, Jinwoo Shin  

**一句话要点**：提出RLTR方法，通过可转移奖励增强大语言模型推理的鲁棒性。

**关键词**：大语言模型推理, 强化学习, 可转移奖励, 鲁棒性, 样本效率

## 3 点简述
- 核心问题：现有RLVR方法仅关注答案正确性，忽略推理过程的鲁棒性。
- 方法要点：引入可转移奖励，测试部分推理前缀能否指导其他模型得出正确答案。
- 实验或效果：在MATH500上，RLTR提升Maj@64 3.6%，训练步骤减少约2.5倍。

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) has recently strengthened LLM reasoning, but its focus on final answer correctness leaves a critical gap: it does not ensure the robustness of the reasoning process itself. We adopt a simple philosophical view, robust reasoning should remain useful beyond the mind that produced it, and treat reasoning as a form of meaning transfer that must survive truncation, reinterpretation, and continuation. Building on this principle, we introduce Reinforcement Learning with Transferable Reward (RLTR), which operationalizes robustness via transfer reward that tests whether a partial reasoning prefix from one model can guide a separate model to the correct answer. This encourages LLMs to produce reasoning that is stable, interpretable, and genuinely generalizable. Our approach improves sampling consistency while improving final answer accuracy, and it reaches comparable performance in substantially fewer training steps. For example, on MATH500, RLTR achieves a +3.6%p gain in Maj@64 compared to RLVR and matches RLVR's average accuracy with roughly 2.5x fewer training steps, providing both more reliable reasoning and significantly more sample efficient.

