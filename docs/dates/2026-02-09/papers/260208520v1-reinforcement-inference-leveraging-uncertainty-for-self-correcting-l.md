---
layout: default
title: Reinforcement Inference: Leveraging Uncertainty for Self-Correcting Language Model Reasoning
---

# Reinforcement Inference: Leveraging Uncertainty for Self-Correcting Language Model Reasoning
**arXiv**：[2602.08520v1](https://arxiv.org/abs/2602.08520) · [PDF](https://arxiv.org/pdf/2602.08520.pdf)  
**作者**：Xinhai Sun  

**一句话要点**：提出强化推理方法，利用不确定性在推理时自我纠正语言模型，无需重新训练。

**关键词**：推理时优化, 不确定性感知, 自我纠正, 熵控制, 语言模型推理

## 3 点简述
- 核心问题：单次贪婪推理在内部模糊时导致错误，低估模型能力。
- 方法要点：基于熵感知选择性触发二次推理，利用不确定性作为控制信号。
- 实验或效果：在MMLU-Pro上提升准确率至84.03%，额外推理调用仅61.06%。

## 摘要（原文）

> Modern large language models (LLMs) are often evaluated and deployed under a \emph{one-shot, greedy} inference protocol, especially in professional settings that require deterministic behavior. This regime can systematically under-estimate a fixed model's true capability: many errors arise not from missing knowledge, but from premature commitment under internal ambiguity. We introduce \emph{Reinforcement Inference}, an entropy-aware inference-time control strategy that uses the model's own uncertainty to selectively invoke a second, more deliberate reasoning attempt, enabling stronger performance \emph{without any retraining}.
>   On 12,032 MMLU-Pro questions across 14 subjects, using DeepSeek-v3.2 with deterministic decoding in a zero-shot setting, Reinforcement Inference improves accuracy from 60.72\% to 84.03\%, while only incurring 61.06\% additional inference calls. A 100\% re-asking ablation reaches 84.35\%, indicating that uncertainty-aware selection captures most of the attainable improvement with substantially less compute. Moreover, a \emph{prompt-only} ablation underperforms the baseline, suggesting that the gains are not explained by generic `` your output had high entropy, think step-by-step'' prompting alone.
>   Beyond providing a practical inference-time upgrade, our results suggest a broader \emph{entropy-aware} paradigm for measuring and expanding model capability: because modern decoder-based models generate outputs autoregressively, entropy and related confidence measures arise naturally as first-class control signals during generation. The resulting gap between one-pass greedy inference and uncertainty-conditioned deliberation offers a diagnostic lens on an LLM's latent reasoning horizon and motivates future training objectives that explicitly constrain correctness--confidence alignment.

