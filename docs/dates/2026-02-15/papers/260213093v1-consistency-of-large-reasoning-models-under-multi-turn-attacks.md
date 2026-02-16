---
layout: default
title: Consistency of Large Reasoning Models Under Multi-Turn Attacks
---

# Consistency of Large Reasoning Models Under Multi-Turn Attacks
**arXiv**：[2602.13093v1](https://arxiv.org/abs/2602.13093) · [PDF](https://arxiv.org/pdf/2602.13093.pdf)  
**作者**：Yubo Li, Ramayya Krishnan, Rema Padman  

**一句话要点**：评估大型推理模型在多轮对抗攻击下的鲁棒性，揭示推理能力不自动保证对抗鲁棒性

**关键词**：大型推理模型, 多轮对抗攻击, 鲁棒性评估, 失败模式分析, 置信度防御

## 3 点简述
- 核心问题：大型推理模型在多轮对抗攻击下的鲁棒性未知，需评估其脆弱性。
- 方法要点：对九种前沿推理模型进行对抗攻击测试，分析失败模式如自我怀疑和社会从众。
- 实验或效果：发现推理模型优于指令调优基线，但存在特定脆弱性，基于置信度的防御需重新设计。

## 摘要（原文）

> Large reasoning models with reasoning capabilities achieve state-of-the-art performance on complex tasks, but their robustness under multi-turn adversarial pressure remains underexplored. We evaluate nine frontier reasoning models under adversarial attacks. Our findings reveal that reasoning confers meaningful but incomplete robustness: most reasoning models studied significantly outperform instruction-tuned baselines, yet all exhibit distinct vulnerability profiles, with misleading suggestions universally effective and social pressure showing model-specific efficacy. Through trajectory analysis, we identify five failure modes (Self-Doubt, Social Conformity, Suggestion Hijacking, Emotional Susceptibility, and Reasoning Fatigue) with the first two accounting for 50% of failures. We further demonstrate that Confidence-Aware Response Generation (CARG), effective for standard LLMs, fails for reasoning models due to overconfidence induced by extended reasoning traces; counterintuitively, random confidence embedding outperforms targeted extraction. Our results highlight that reasoning capabilities do not automatically confer adversarial robustness and that confidence-based defenses require fundamental redesign for reasoning models.

