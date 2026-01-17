---
layout: default
title: Defending Large Language Models Against Jailbreak Attacks via In-Decoding Safety-Awareness Probing
---

# Defending Large Language Models Against Jailbreak Attacks via In-Decoding Safety-Awareness Probing
**arXiv**：[2601.10543v1](https://arxiv.org/abs/2601.10543) · [PDF](https://arxiv.org/pdf/2601.10543.pdf)  
**作者**：Yinzhi Zhao, Ming Wang, Shi Feng, Xiaocui Yang, Daling Wang, Yifei Zhang  

**一句话要点**：提出解码中安全感知探测方法以防御大语言模型的越狱攻击

**关键词**：大语言模型, 越狱攻击防御, 解码过程, 安全感知, 早期检测, 潜在信号

## 3 点简述
- 问题：大语言模型安全对齐浅层，易受越狱攻击，现有防御机制效果有限。
- 方法：基于解码过程观察，显式利用模型内部潜在安全信号进行早期不安全内容检测。
- 效果：实验表明显著提升安全性，同时保持低误拒率和响应质量。

## 摘要（原文）

> Large language models (LLMs) have achieved impressive performance across natural language tasks and are increasingly deployed in real-world applications. Despite extensive safety alignment efforts, recent studies show that such alignment is often shallow and remains vulnerable to jailbreak attacks. Existing defense mechanisms, including decoding-based constraints and post-hoc content detectors, struggle against sophisticated jailbreaks, often intervening robust detection or excessively degrading model utility. In this work, we examine the decoding process of LLMs and make a key observation: even when successfully jailbroken, models internally exhibit latent safety-related signals during generation. However, these signals are overridden by the model's drive for fluent continuation, preventing timely self-correction or refusal. Building on this observation, we propose a simple yet effective approach that explicitly surfaces and leverages these latent safety signals for early detection of unsafe content during decoding. Experiments across diverse jailbreak attacks demonstrate that our approach significantly enhances safety, while maintaining low over-refusal rates on benign inputs and preserving response quality. Our results suggest that activating intrinsic safety-awareness during decoding offers a promising and complementary direction for defending against jailbreak attacks. Code is available at: https://github.com/zyz13590/SafeProbing.

