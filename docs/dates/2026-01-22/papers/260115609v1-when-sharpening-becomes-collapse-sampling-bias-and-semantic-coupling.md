---
layout: default
title: When Sharpening Becomes Collapse: Sampling Bias and Semantic Coupling in RL with Verifiable Rewards
---

# When Sharpening Becomes Collapse: Sampling Bias and Semantic Coupling in RL with Verifiable Rewards
**arXiv**：[2601.15609v1](https://arxiv.org/abs/2601.15609) · [PDF](https://arxiv.org/pdf/2601.15609.pdf)  
**作者**：Mingyuan Fan, Weiguang Han, Daixin Wang, Cen Chen, Zhiqiang Zhang, Jun Zhou  

**一句话要点**：提出逆成功优势校准和分布级校准以缓解RLVR中的过锐化和语义耦合问题

**关键词**：强化学习, 可验证奖励, 过锐化, 语义耦合, 泛化能力, 记忆网络

## 3 点简述
- 核心问题：RLVR可能导致策略过锐化，抑制有效替代方案，源于有限批次更新的采样偏差
- 方法要点：引入逆成功优势校准优先处理困难查询，分布级校准通过记忆网络多样化采样
- 实验或效果：实证评估验证策略能有效提升泛化能力，缓解策略崩溃

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) is a central paradigm for turning large language models (LLMs) into reliable problem solvers, especially in logic-heavy domains. Despite its empirical success, it remains unclear whether RLVR elicits novel capabilities or merely sharpens the distribution over existing knowledge. We study this by formalizing over-sharpening, a phenomenon where the policy collapses onto limited modes, suppressing valid alternatives. At a high level, we discover finite-batch updates intrinsically bias learning toward sampled modes, triggering a collapse that propagates globally via semantic coupling. To mitigate this, we propose inverse-success advantage calibration to prioritize difficult queries and distribution-level calibration to diversify sampling via a memory network. Empirical evaluations validate that our strategies can effectively improve generalization.

