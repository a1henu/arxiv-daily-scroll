---
layout: default
title: Segmental Advantage Estimation: Enhancing PPO for Long-Context LLM Training
---

# Segmental Advantage Estimation: Enhancing PPO for Long-Context LLM Training
**arXiv**：[2601.07320v1](https://arxiv.org/abs/2601.07320) · [PDF](https://arxiv.org/pdf/2601.07320.pdf)  
**作者**：Xue Gong, Qi Yi, Ziyuan Nan, Guanhua Huang, Kejiao Li, Yuhao Jiang, Ruibin Xiong, Zenan Xu, Jiaming Guo, Shaohui Peng, Bo Zhou  

**一句话要点**：提出Segmental Advantage Estimation以解决PPO在稀疏奖励RLVR中优势估计不可靠的问题

**关键词**：强化学习, 优势估计, 长上下文训练, PPO, 稀疏奖励, 语言模型训练

## 3 点简述
- 核心问题：稀疏奖励导致GAE在每token聚合时引入显著偏差，影响PPO训练稳定性。
- 方法要点：SAE基于低概率token划分序列为子段，仅在信息丰富的段间计算方差降低的优势估计。
- 实验或效果：SAE在最终得分、训练稳定性和样本效率上表现更优，且与近似真实优势相关性更高。

## 摘要（原文）

> Training Large Language Models (LLMs) for reasoning tasks is increasingly driven by Reinforcement Learning with Verifiable Rewards (RLVR), where Proximal Policy Optimization (PPO) provides a principled framework for stable policy updates. However, the practical application of PPO is hindered by unreliable advantage estimation in the sparse-reward RLVR regime. This issue arises because the sparse rewards in RLVR lead to inaccurate intermediate value predictions, which in turn introduce significant bias when aggregated at every token by Generalized Advantage Estimation (GAE). To address this, we introduce Segmental Advantage Estimation (SAE), which mitigates the bias that GAE can incur in RLVR. Our key insight is that aggregating $n$-step advantages at every token(as in GAE) is unnecessary and often introduces excessive bias, since individual tokens carry minimal information. Instead, SAE first partitions the generated sequence into coherent sub-segments using low-probability tokens as heuristic boundaries. It then selectively computes variance-reduced advantage estimates only from these information-rich segment transitions, effectively filtering out noise from intermediate tokens. Our experiments demonstrate that SAE achieves superior performance, with marked improvements in final scores, training stability, and sample efficiency. These gains are shown to be consistent across multiple model sizes, and a correlation analysis confirms that our proposed advantage estimator achieves a higher correlation with an approximate ground-truth advantage, justifying its superior performance.

