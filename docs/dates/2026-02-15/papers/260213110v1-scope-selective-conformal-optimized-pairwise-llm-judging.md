---
layout: default
title: SCOPE: Selective Conformal Optimized Pairwise LLM Judging
---

# SCOPE: Selective Conformal Optimized Pairwise LLM Judging
**arXiv**：[2602.13110v1](https://arxiv.org/abs/2602.13110) · [PDF](https://arxiv.org/pdf/2602.13110.pdf)  
**作者**：Sher Badshah, Ali Emami, Hassan Sajjad  

**一句话要点**：提出SCOPE框架，通过选择性校准优化LLM成对评估，确保有限样本下的统计保证。

**关键词**：大语言模型评估, 成对判断, 选择性校准, 统计保证, 不确定性量化, 偏好熵

## 3 点简述
- 核心问题：LLM作为成对评估的法官存在校准不足和系统偏差，影响可靠性。
- 方法要点：引入Bidirectional Preference Entropy（BPE）作为偏差中立的信号，结合SCOPE框架校准接受阈值，控制非弃权判断的错误率。
- 实验或效果：在MT-Bench、RewardBench和Chatbot Arena上，SCOPE在目标风险水平下保持高覆盖率，提升判断接受量。

## 摘要（原文）

> Large language models (LLMs) are increasingly used as judges to replace costly human preference labels in pairwise evaluation. Despite their practicality, LLM judges remain prone to miscalibration and systematic biases. This paper proposes SCOPE (Selective Conformal Optimized Pairwise Evaluation), a framework for selective pairwise judging with finite-sample statistical guarantees. Under exchangeability, SCOPE calibrates an acceptance threshold such that the error rate among non-abstained judgments is at most a user-specified level $α$. To provide SCOPE with a bias-neutral uncertainty signal, we introduce Bidirectional Preference Entropy (BPE), which queries the judge under both response positions, aggregates the implied preference probabilities to enforce invariance to response order, and converts the aggregated probability into an entropy-based uncertainty score. Across MT-Bench, RewardBench, and Chatbot Arena, BPE improves uncertainty quality over standard confidence proxies, providing a stronger selection signal that enables SCOPE to consistently meet the target risk level while retaining good coverage across judge scales. In particular, at $α= 0.10$, \textsc{Scope} consistently satisfies the risk bound across all benchmarks and judge scales (empirical risk $\approx 0.097$ to $0.099$), while retaining substantial coverage, reaching $0.89$ on RewardBench with Qwen-14B and $0.98$ on RewardBench with Qwen-32B. Compared to naïve baselines, \textsc{Scope} accepts up to $2.4\times$ more judgments on MT-Bench with Qwen-7B under the same target risk constraint, demonstrating that BPE enables reliable and high-coverage LLM-based evaluation.

