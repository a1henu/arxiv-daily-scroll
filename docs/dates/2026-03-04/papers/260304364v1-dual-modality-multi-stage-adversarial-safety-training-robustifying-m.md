---
layout: default
title: Dual-Modality Multi-Stage Adversarial Safety Training: Robustifying Multimodal Web Agents Against Cross-Modal Attacks
---

# Dual-Modality Multi-Stage Adversarial Safety Training: Robustifying Multimodal Web Agents Against Cross-Modal Attacks
**arXiv**：[2603.04364v1](https://arxiv.org/abs/2603.04364) · [PDF](https://arxiv.org/pdf/2603.04364.pdf)  
**作者**：Haoyu Liu, Dingcheng Li, Lukas Rutishauser, Zeyu Zheng  

**一句话要点**：提出双模态多阶段对抗安全训练框架，以增强多模态网页代理对跨模态攻击的鲁棒性。

**关键词**：多模态网页代理, 对抗安全训练, 跨模态攻击, 零和马尔可夫博弈, 强化学习, 鲁棒性增强

## 3 点简述
- 核心问题：多模态网页代理的双流架构易受跨模态攻击，视觉组件攻击效果远超纯文本注入。
- 方法要点：将代理-攻击者交互建模为零和马尔可夫博弈，通过模仿学习、监督微调和对抗强化学习三阶段训练。
- 实验或效果：在分布外任务中显著降低对抗风险，同时任务完成效率翻倍，优于现有防御方法。

## 摘要（原文）

> Multimodal web agents that process both screenshots and accessibility trees are increasingly deployed to interact with web interfaces, yet their dual-stream architecture opens an underexplored attack surface: an adversary who injects content into the webpage DOM simultaneously corrupts both observation channels with a consistent deceptive narrative. Our vulnerability analysis on MiniWob++ reveals that attacks including a visual component far outperform text-only injections, exposing critical gaps in text-centric VLM safety training. Motivated by this finding, we propose Dual-Modality Multi-Stage Adversarial Safety Training (DMAST), a framework that formalizes the agent-attacker interaction as a two-player zero-sum Markov game and co-trains both players through a three-stage pipeline: (1) imitation learning from a strong teacher model, (2) oracle-guided supervised fine-tuning that uses a novel zero-acknowledgment strategy to instill task-focused reasoning under adversarial noise, and (3) adversarial reinforcement learning via Group Relative Policy Optimization (GRPO) self-play. On out-of-distribution tasks, DMAST substantially mitigates adversarial risks while simultaneously doubling task completion efficiency. Our approach significantly outperforms established training-based and prompt-based defenses, demonstrating genuine co-evolutionary progress and robust generalization to complex, unseen environments.

