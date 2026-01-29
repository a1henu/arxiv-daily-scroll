---
layout: default
title: Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction
---

# Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction
**arXiv**：[2601.20299v1](https://arxiv.org/abs/2601.20299) · [PDF](https://arxiv.org/pdf/2601.20299.pdf)  
**作者**：Tianyi Alex Qiu, Micah Carroll, Cameron Allen  

**一句话要点**：提出基于同伴预测的方法，以弱监督评估和训练大语言模型，提升真实性和抗欺骗性。

**关键词**：同伴预测, 弱监督评估, 大语言模型训练, 抗欺骗性, 机制设计, 逆缩放

## 3 点简述
- 核心问题：大语言模型评估和训练依赖强监督，但困难任务中强监督常不可得，导致模型利用不完美监督产生欺骗性结果。
- 方法要点：引入同伴预测方法，基于互预测性度量奖励诚实和信息丰富的回答，无需真实标签，具有理论保证。
- 实验或效果：在高达405B参数的模型上验证有效性，训练8B模型可恢复因恶意微调下降的真实性，评估中显示逆缩放特性，抗欺骗性随能力差距增大而增强。

## 摘要（原文）

> The evaluation and post-training of large language models (LLMs) rely on supervision, but strong supervision for difficult tasks is often unavailable, especially when evaluating frontier models. In such cases, models are demonstrated to exploit evaluations built on such imperfect supervision, leading to deceptive results. However, underutilized in LLM research, a wealth of mechanism design research focuses on game-theoretic incentive compatibility, i.e., eliciting honest and informative answers with weak supervision. Drawing from this literature, we introduce the peer prediction method for model evaluation and post-training. It rewards honest and informative answers over deceptive and uninformative ones, using a metric based on mutual predictability and without requiring ground truth labels. We demonstrate the method's effectiveness and resistance to deception, with both theoretical guarantees and empirical validation on models with up to 405B parameters. We show that training an 8B model with peer prediction-based reward recovers most of the drop in truthfulness due to prior malicious finetuning, even when the reward is produced by a 0.135B language model with no finetuning. On the evaluation front, in contrast to LLM-as-a-Judge which requires strong and trusted judges, we discover an inverse scaling property in peer prediction, where, surprisingly, resistance to deception is strengthened as the capability gap between the experts and participants widens, enabling reliable evaluation of strong models with weak supervision. In particular, LLM-as-a-Judge become worse than random guess when facing deceptive models 5-20x the judge's size, while peer prediction thrives when such gaps are large, including in cases with over 100x size difference.

