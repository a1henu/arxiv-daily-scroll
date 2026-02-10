---
layout: default
title: Robust Policy Optimization to Prevent Catastrophic Forgetting
---

# Robust Policy Optimization to Prevent Catastrophic Forgetting
**arXiv**：[2602.08813v1](https://arxiv.org/abs/2602.08813) · [PDF](https://arxiv.org/pdf/2602.08813.pdf)  
**作者**：Mahdi Sabbaghi, George Pappas, Adel Javanmard, Hamed Hassani  

**一句话要点**：提出Fine-tuning Robust Policy Optimization以解决大语言模型下游微调中的灾难性遗忘问题

**关键词**：灾难性遗忘, 策略优化, 鲁棒性训练, 大语言模型, 下游微调, 奖励稳定性

## 3 点简述
- 核心问题：标准RLHF训练的大语言模型在下游微调时易发生灾难性遗忘，导致先前学习的行为（如安全性）退化。
- 方法要点：基于GRPO设计FRPO框架，通过最大-最小优化在KL有界策略邻域内确保奖励稳定性，无需额外计算。
- 实验或效果：在多种基础模型和下游微调场景中，FRPO显著减少安全性退化，同时保持下游任务性能。

## 摘要（原文）

> Large language models are commonly trained through multi-stage post-training: first via RLHF, then fine-tuned for other downstream objectives. Yet even small downstream updates can compromise earlier learned behaviors (e.g., safety), exposing a brittleness known as catastrophic forgetting. This suggests standard RLHF objectives do not guarantee robustness to future adaptation. To address it, most prior work designs downstream-time methods to preserve previously learned behaviors. We argue that preventing this requires pre-finetuning robustness: the base policy should avoid brittle high-reward solutions whose reward drops sharply under standard fine-tuning.
>   We propose Fine-tuning Robust Policy Optimization (FRPO), a robust RLHF framework that optimizes reward not only at the current policy, but across a KL-bounded neighborhood of policies reachable by downstream adaptation. The key idea is to ensure reward stability under policy shifts via a max-min formulation. By modifying GRPO, we develop an algorithm with no extra computation, and empirically show it substantially reduces safety degradation across multiple base models and downstream fine-tuning regimes (SFT and RL) while preserving downstream task performance. We further study a math-focused RL setting, demonstrating that FRPO preserves accuracy under subsequent fine-tuning.

