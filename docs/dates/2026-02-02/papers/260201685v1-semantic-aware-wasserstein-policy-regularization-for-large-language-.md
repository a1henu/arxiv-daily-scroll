---
layout: default
title: Semantic-aware Wasserstein Policy Regularization for Large Language Model Alignment
---

# Semantic-aware Wasserstein Policy Regularization for Large Language Model Alignment
**arXiv**：[2602.01685v1](https://arxiv.org/abs/2602.01685) · [PDF](https://arxiv.org/pdf/2602.01685.pdf)  
**作者**：Byeonghu Na, Hyungho Na, Yeongmin Kim, Suhyeon Jo, HeeSun Bae, Mina Kang, Il-Chul Moon  

**一句话要点**：提出基于Wasserstein距离的语义感知策略正则化，以增强大语言模型对齐中的语义相似性捕获。

**关键词**：大语言模型对齐, 强化学习从人类反馈, Wasserstein距离, 策略正则化, 语义相似性

## 3 点简述
- 核心问题：传统KL和f-散度正则化仅比较相同索引的token概率，忽略语义相似性。
- 方法要点：引入熵正则化Wasserstein距离，通过最优对偶变量将正则化转化为奖励惩罚项，兼容标准强化学习算法。
- 实验或效果：在RLHF框架中优于KL和f-散度基线，验证语义感知策略距离的对齐优势。

## 摘要（原文）

> Large language models (LLMs) are commonly aligned with human preferences using reinforcement learning from human feedback (RLHF). In this method, LLM policies are generally optimized through reward maximization with Kullback-Leibler (KL) divergence regularization of the reference policy. However, KL and its $f$-divergence variants only compare token probabilities at identical indices, failing to capture semantic similarity. We propose Wasserstein Policy Regularization (WPR), a semantic-aware regularization for the RLHF framework based on the entropy-regularized Wasserstein distance, which incorporates the geometry of the token space. The dual formulation of the distance expresses the regularization as penalty terms applied to the reward via optimal dual variables, which yield a tractable objective compatible with standard RL algorithms. Empirically, our method outperforms KL- and $f$-divergence-based baselines, demonstrating the benefits of semantic-aware policy distances for alignment. Our code is available at https://github.com/aailab-kaist/WPR.

