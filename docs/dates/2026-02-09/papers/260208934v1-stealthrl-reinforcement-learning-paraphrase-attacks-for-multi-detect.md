---
layout: default
title: StealthRL: Reinforcement Learning Paraphrase Attacks for Multi-Detector Evasion of AI-Text Detectors
---

# StealthRL: Reinforcement Learning Paraphrase Attacks for Multi-Detector Evasion of AI-Text Detectors
**arXiv**：[2602.08934v1](https://arxiv.org/abs/2602.08934) · [PDF](https://arxiv.org/pdf/2602.08934.pdf)  
**作者**：Suraj Ranganath, Atharv Ramesh  

**一句话要点**：提出StealthRL强化学习框架，通过对抗性改写攻击评估AI文本检测器的鲁棒性。

**关键词**：对抗性攻击, 强化学习, 文本检测, 鲁棒性评估, 语义保留

## 3 点简述
- 核心问题：AI文本检测器面临对抗性改写攻击，需在保持语义的同时规避检测。
- 方法要点：使用GRPO与LoRA适配器训练改写策略，针对多检测器集成优化复合奖励。
- 实验或效果：在1%误报率下实现近零检测，攻击成功率99.9%，揭示共享架构漏洞。

## 摘要（原文）

> AI-text detectors face a critical robustness challenge: adversarial paraphrasing attacks that preserve semantics while evading detection. We introduce StealthRL, a reinforcement learning framework that stress-tests detector robustness under realistic adversarial conditions. StealthRL trains a paraphrase policy against a multi-detector ensemble using Group Relative Policy Optimization (GRPO) with LoRA adapters on Qwen3-4B, optimizing a composite reward that balances detector evasion with semantic preservation. We evaluate six attack settings (M0-M5) against three detector families (RoBERTa, FastDetectGPT, and Binoculars) at the security-relevant 1% false positive rate operating point. StealthRL achieves near-zero detection (0.001 mean TPR@1%FPR), reduces mean AUROC from 0.74 to 0.27, and attains a 99.9% attack success rate. Critically, attacks transfer to a held-out detector family not seen during training, revealing shared architectural vulnerabilities rather than detector-specific brittleness. We additionally conduct LLM-based quality evaluation via Likert scoring, analyze detector score distributions to explain why evasion succeeds, and provide per-detector AUROC with bootstrap confidence intervals. Our results expose significant robustness gaps in current AI-text detection and establish StealthRL as a principled adversarial evaluation protocol. Code and evaluation pipeline are publicly available at https://github.com/suraj-ranganath/StealthRL.

