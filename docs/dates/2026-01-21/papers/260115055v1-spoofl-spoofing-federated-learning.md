---
layout: default
title: SpooFL: Spoofing Federated Learning
---

# SpooFL: Spoofing Federated Learning
**arXiv**：[2601.15055v1](https://arxiv.org/abs/2601.15055) · [PDF](https://arxiv.org/pdf/2601.15055.pdf)  
**作者**：Isaac Baglin, Xiatian Zhu, Simon Hadfield  

**一句话要点**：提出SpooFL防御方法，通过欺骗攻击者解决联邦学习中的深度泄漏问题。

**关键词**：联邦学习, 深度泄漏防御, 欺骗攻击, 合成数据生成, 隐私保护

## 3 点简述
- 核心问题：传统防御方法仍泄露高级信息，易被去噪攻击破解。
- 方法要点：采用欺骗策略，生成无关任务的合成样本误导攻击者。
- 实验或效果：评估显示能有效误导攻击者，且模型性能影响较小。

## 摘要（原文）

> Traditional defenses against Deep Leakage (DL) attacks in Federated Learning (FL) primarily focus on obfuscation, introducing noise, transformations or encryption to degrade an attacker's ability to reconstruct private data. While effective to some extent, these methods often still leak high-level information such as class distributions or feature representations, and are frequently broken by increasingly powerful denoising attacks. We propose a fundamentally different perspective on FL defense: framing it as a spoofing problem.We introduce SpooFL (Figure 1), a spoofing-based defense that deceives attackers into believing they have recovered the true training data, while actually providing convincing but entirely synthetic samples from an unrelated task. Unlike prior synthetic-data defenses that share classes or distributions with the private data and thus still leak semantic information, SpooFL uses a state-of-the-art generative model trained on an external dataset with no class overlap. As a result, attackers are misled into recovering plausible yet completely irrelevant samples, preventing meaningful data leakage while preserving FL training integrity. We implement the first example of such a spoofing defense, and evaluate our method against state-of-the-art DL defenses and demonstrate that it successfully misdirects attackers without compromising model performance significantly.

