---
layout: default
title: MORE: Multi-Objective Adversarial Attacks on Speech Recognition
---

# MORE: Multi-Objective Adversarial Attacks on Speech Recognition
**arXiv**：[2601.01852v1](https://arxiv.org/abs/2601.01852) · [PDF](https://arxiv.org/pdf/2601.01852.pdf)  
**作者**：Xiaoxue Gao, Zexin Li, Yiming Chen, Nancy F. Chen  

**一句话要点**：提出MORE多目标对抗攻击方法，以同时降低语音识别模型的准确性和效率。

**关键词**：语音识别, 对抗攻击, 多目标优化, 效率鲁棒性, Whisper模型

## 3 点简述
- 核心问题：现有研究主要关注对抗攻击下的准确性下降，忽略了效率鲁棒性，导致对ASR模型漏洞理解不全面。
- 方法要点：MORE采用分层阶段排斥-锚定机制，通过重复鼓励加倍目标（REDO）联合优化准确性和效率下降。
- 实验或效果：实验显示MORE能产生显著更长的转录文本，同时保持高词错误率，验证了多目标攻击的有效性。

## 摘要（原文）

> The emergence of large-scale automatic speech recognition (ASR) models such as Whisper has greatly expanded their adoption across diverse real-world applications. Ensuring robustness against even minor input perturbations is therefore critical for maintaining reliable performance in real-time environments. While prior work has mainly examined accuracy degradation under adversarial attacks, robustness with respect to efficiency remains largely unexplored. This narrow focus provides only a partial understanding of ASR model vulnerabilities. To address this gap, we conduct a comprehensive study of ASR robustness under multiple attack scenarios. We introduce MORE, a multi-objective repetitive doubling encouragement attack, which jointly degrades recognition accuracy and inference efficiency through a hierarchical staged repulsion-anchoring mechanism. Specifically, we reformulate multi-objective adversarial optimization into a hierarchical framework that sequentially achieves the dual objectives. To further amplify effectiveness, we propose a novel repetitive encouragement doubling objective (REDO) that induces duplicative text generation by maintaining accuracy degradation and periodically doubling the predicted sequence length. Overall, MORE compels ASR models to produce incorrect transcriptions at a substantially higher computational cost, triggered by a single adversarial input. Experiments show that MORE consistently yields significantly longer transcriptions while maintaining high word error rates compared to existing baselines, underscoring its effectiveness in multi-objective adversarial attack.

