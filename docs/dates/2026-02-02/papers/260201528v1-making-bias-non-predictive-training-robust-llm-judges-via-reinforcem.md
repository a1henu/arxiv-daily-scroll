---
layout: default
title: Making Bias Non-Predictive: Training Robust LLM Judges via Reinforcement Learning
---

# Making Bias Non-Predictive: Training Robust LLM Judges via Reinforcement Learning
**arXiv**：[2602.01528v1](https://arxiv.org/abs/2602.01528) · [PDF](https://arxiv.org/pdf/2602.01528.pdf)  
**作者**：Qian Wang, Xuandong Zhao, Zirui Zhang, Zhanzhi Lou, Nuo Chen, Dawn Song, Bingsheng He  

**一句话要点**：提出Epistemic Independence Training，通过强化学习训练LLM法官以消除认知偏差预测性

**关键词**：大语言模型, 认知偏差, 强化学习, 自动评估, 鲁棒性训练, 泛化能力

## 3 点简述
- 核心问题：LLM作为自动法官易受共识或权威等提示级偏差影响，现有方法泛化性差
- 方法要点：基于偏差信号非预测性奖励原则，采用平衡冲突策略和惩罚偏差跟随的奖励设计
- 实验或效果：在Qwen3-4B上提升准确性和鲁棒性，并泛化至未见偏差类型如权威和分心

## 摘要（原文）

> Large language models (LLMs) increasingly serve as automated judges, yet they remain susceptible to cognitive biases -- often altering their reasoning when faced with spurious prompt-level cues such as consensus claims or authority appeals. Existing mitigations via prompting or supervised fine-tuning fail to generalize, as they modify surface behavior without changing the optimization objective that makes bias cues predictive. To address this gap, we propose Epistemic Independence Training (EIT), a reinforcement learning framework grounded in a key principle: to learn independence, bias cues must be made non-predictive of reward. EIT operationalizes this through a balanced conflict strategy where bias signals are equally likely to support correct and incorrect answers, combined with a reward design that penalizes bias-following without rewarding bias agreement. Experiments on Qwen3-4B demonstrate that EIT improves both accuracy and robustness under adversarial biases, while preserving performance when bias aligns with truth. Notably, models trained only on bandwagon bias generalize to unseen bias types such as authority and distraction, indicating that EIT induces transferable epistemic independence rather than bias-specific heuristics. Code and data are available at https://anonymous.4open.science/r/bias-mitigation-with-rl-BC47.

