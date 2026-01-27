---
layout: default
title: Trust, Don't Trust, or Flip: Robust Preference-Based Reinforcement Learning with Multi-Expert Feedback
---

# Trust, Don't Trust, or Flip: Robust Preference-Based Reinforcement Learning with Multi-Expert Feedback
**arXiv**：[2601.18751v1](https://arxiv.org/abs/2601.18751) · [PDF](https://arxiv.org/pdf/2601.18751.pdf)  
**作者**：Seyed Amir Hosseini, Maryam Abdolali, Amirhosein Tavakkoli, Fardin Ayar, Ehsan Javanmardi, Manabu Tsukada, Mahdi Javanmardi  

**一句话要点**：提出TriTrust-PBRL框架，通过多专家反馈学习共享奖励模型和专家信任参数，以解决对抗性标注者下的偏好强化学习鲁棒性问题。

**关键词**：偏好强化学习, 多专家反馈, 鲁棒性学习, 对抗性标注, 奖励建模, 梯度分析

## 3 点简述
- 核心问题：真实世界偏好数据来自异质标注者，包括对抗性标注者，现有方法难以处理。
- 方法要点：联合学习共享奖励模型和专家信任参数，信任参数可自动演化为信任、忽略或翻转。
- 实验或效果：在多个领域评估，TTP在对抗性污染下保持接近最优性能，优于现有基线。

## 摘要（原文）

> Preference-based reinforcement learning (PBRL) offers a promising alternative to explicit reward engineering by learning from pairwise trajectory comparisons. However, real-world preference data often comes from heterogeneous annotators with varying reliability; some accurate, some noisy, and some systematically adversarial. Existing PBRL methods either treat all feedback equally or attempt to filter out unreliable sources, but both approaches fail when faced with adversarial annotators who systematically provide incorrect preferences. We introduce TriTrust-PBRL (TTP), a unified framework that jointly learns a shared reward model and expert-specific trust parameters from multi-expert preference feedback. The key insight is that trust parameters naturally evolve during gradient-based optimization to be positive (trust), near zero (ignore), or negative (flip), enabling the model to automatically invert adversarial preferences and recover useful signal rather than merely discarding corrupted feedback. We provide theoretical analysis establishing identifiability guarantees and detailed gradient analysis that explains how expert separation emerges naturally during training without explicit supervision. Empirically, we evaluate TTP on four diverse domains spanning manipulation tasks (MetaWorld) and locomotion (DM Control) under various corruption scenarios. TTP achieves state-of-the-art robustness, maintaining near-oracle performance under adversarial corruption while standard PBRL methods fail catastrophically. Notably, TTP outperforms existing baselines by successfully learning from mixed expert pools containing both reliable and adversarial annotators, all while requiring no expert features beyond identification indices and integrating seamlessly with existing PBRL pipelines.

