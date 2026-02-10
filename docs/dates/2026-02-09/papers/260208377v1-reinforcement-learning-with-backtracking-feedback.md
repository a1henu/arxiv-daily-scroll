---
layout: default
title: Reinforcement Learning with Backtracking Feedback
---

# Reinforcement Learning with Backtracking Feedback
**arXiv**：[2602.08377v1](https://arxiv.org/abs/2602.08377) · [PDF](https://arxiv.org/pdf/2602.08377.pdf)  
**作者**：Bilgehan Sel, Vaishakh Keshava, Phillip Wallis, Lukas Rutishauser, Ming Jin, Dingcheng Li  

**一句话要点**：提出强化学习回溯反馈框架以增强大语言模型的安全性与对抗鲁棒性

**关键词**：大语言模型安全, 强化学习, 对抗攻击, 回溯机制, 监督微调

## 3 点简述
- 核心问题：大语言模型面临对抗攻击和分布内错误的安全风险，需提升鲁棒性。
- 方法要点：通过强化学习阶段，模型学习动态纠正生成错误，并利用回溯信号恢复安全。
- 实验或效果：在多种基准和模型规模上显著降低攻击成功率，同时保持模型实用性。

## 摘要（原文）

> Addressing the critical need for robust safety in Large Language Models (LLMs), particularly against adversarial attacks and in-distribution errors, we introduce Reinforcement Learning with Backtracking Feedback (RLBF). This framework advances upon prior methods, such as BSAFE, by primarily leveraging a Reinforcement Learning (RL) stage where models learn to dynamically correct their own generation errors. Through RL with critic feedback on the model's live outputs, LLMs are trained to identify and recover from their actual, emergent safety violations by emitting an efficient "backtrack by x tokens" signal, then continuing generation autoregressively. This RL process is crucial for instilling resilience against sophisticated adversarial strategies, including middle filling, Greedy Coordinate Gradient (GCG) attacks, and decoding parameter manipulations. To further support the acquisition of this backtracking capability, we also propose an enhanced Supervised Fine-Tuning (SFT) data generation strategy (BSAFE+). This method improves upon previous data creation techniques by injecting violations into coherent, originally safe text, providing more effective initial training for the backtracking mechanism. Comprehensive empirical evaluations demonstrate that RLBF significantly reduces attack success rates across diverse benchmarks and model scales, achieving superior safety outcomes while critically preserving foundational model utility.

