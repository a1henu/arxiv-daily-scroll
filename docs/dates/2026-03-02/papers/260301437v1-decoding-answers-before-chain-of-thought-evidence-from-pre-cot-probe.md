---
layout: default
title: Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering
---

# Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering
**arXiv**：[2603.01437v1](https://arxiv.org/abs/2603.01437) · [PDF](https://arxiv.org/pdf/2603.01437.pdf)  
**作者**：Kyle Cox, Darius Kianersi, Adrià Garriga-Alonso  

**一句话要点**：揭示指令微调模型在思维链前已确定答案，通过激活探针和转向提供机制证据。

**关键词**：思维链忠实性, 激活探针, 指令微调模型, 机制解释, 残差流分析, 因果干预

## 3 点简述
- 核心问题：思维链的忠实性，即模型陈述的推理是否反映底层决策过程。
- 方法要点：在思维链前最后一个令牌的残差流激活上训练线性探针，预测最终答案。
- 实验或效果：探针方向具有预测性和因果性，转向可翻转答案，并观察到两种失败模式。

## 摘要（原文）

> As chain-of-thought (CoT) has become central to scaling reasoning capabilities in large language models (LLMs), it has also emerged as a promising tool for interpretability, suggesting the opportunity to understand model decisions through verbalized reasoning. However, the utility of CoT toward interpretability depends upon its faithfulness -- whether the model's stated reasoning reflects the underlying decision process. We provide mechanistic evidence that instruction-tuned models often determine their answer before generating CoT. Training linear probes on residual stream activations at the last token before CoT, we can predict the model's final answer with 0.9 AUC on most tasks. We find that these directions are not only predictive, but also causal: steering activations along the probe direction flips model answers in over 50% of cases, significantly exceeding orthogonal baselines. When steering induces incorrect answers, we observe two distinct failure modes: non-entailment (stating correct premises but drawing unsupported conclusions) and confabulation (fabricating false premises). While post-hoc reasoning may be instrumentally useful when the model has a correct pre-CoT belief, these failure modes suggest it can result in undesirable behaviors when reasoning from a false belief.

