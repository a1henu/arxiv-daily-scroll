---
layout: default
title: SafeMed-R1: Adversarial Reinforcement Learning for Generalizable and Robust Medical Reasoning in Vision-Language Models
---

# SafeMed-R1: Adversarial Reinforcement Learning for Generalizable and Robust Medical Reasoning in Vision-Language Models
**arXiv**：[2512.19317v1](https://arxiv.org/abs/2512.19317) · [PDF](https://arxiv.org/pdf/2512.19317.pdf)  
**作者**：A. A. Gde Yogi Pramana, Jason Ray, Anthony Jaya, Michael Wijaya  

**一句话要点**：提出SafeMed-R1框架，通过对抗强化学习增强医疗视觉问答模型的鲁棒性与泛化性。

**关键词**：医疗视觉问答, 对抗鲁棒性, 强化学习, 随机平滑, 链式推理

## 3 点简述
- 医疗视觉语言模型易受对抗攻击，标准对抗训练损害泛化与推理质量。
- 采用两阶段方法：训练时结合对抗训练与策略优化，推理时添加随机平滑保证。
- 在OmniMedVQA基准上，模型在对抗条件下准确率从25%提升至84.45%。

## 摘要（原文）

> Vision--Language Models (VLMs) show significant promise for Medical Visual Question Answering (VQA), yet their deployment in clinical settings is hindered by severe vulnerability to adversarial attacks. Standard adversarial training, while effective for simpler tasks, often degrades both generalization performance and the quality of generated clinical reasoning. We introduce SafeMed-R1, a hybrid defense framework that ensures robust performance while preserving high-quality, interpretable medical reasoning. SafeMed-R1 employs a two-stage approach: at training time, we integrate Adversarial Training with Group Relative Policy Optimization (AT-GRPO) to explicitly robustify the reasoning process against worst-case perturbations; at inference time, we augment the model with Randomized Smoothing to provide certified $L_2$-norm robustness guarantees. We evaluate SafeMed-R1 on the OmniMedVQA benchmark across eight medical imaging modalities comprising over 88,000 samples. Our experiments reveal that standard fine-tuned VLMs, despite achieving 95\% accuracy on clean inputs, collapse to approximately 25\% under PGD attacks. In contrast, SafeMed-R1 maintains 84.45\% accuracy under the same adversarial conditions, representing a 59 percentage point improvement in robustness. Furthermore, we demonstrate that models trained with explicit chain-of-thought reasoning exhibit superior adversarial robustness compared to instruction-only variants, suggesting a synergy between interpretability and security in medical AI systems.

