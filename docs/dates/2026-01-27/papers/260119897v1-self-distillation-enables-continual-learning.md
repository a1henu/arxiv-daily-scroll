---
layout: default
title: Self-Distillation Enables Continual Learning
---

# Self-Distillation Enables Continual Learning
**arXiv**：[2601.19897v1](https://arxiv.org/abs/2601.19897) · [PDF](https://arxiv.org/pdf/2601.19897.pdf)  
**作者**：Idan Shenfeld, Mehul Damani, Jonas Hübotter, Pulkit Agrawal  

**一句话要点**：提出自蒸馏微调方法，以演示数据实现持续学习中的策略内学习。

**关键词**：持续学习, 自蒸馏, 策略内学习, 演示学习, 灾难性遗忘

## 3 点简述
- 持续学习面临遗忘问题，现有方法依赖奖励函数或策略外监督微调。
- SDFT利用演示条件模型作为自身教师，生成策略内训练信号，减少遗忘。
- 实验显示SDFT在新任务准确率和多技能累积上优于监督微调，降低灾难性遗忘。

## 摘要（原文）

> Continual learning, enabling models to acquire new skills and knowledge without degrading existing capabilities, remains a fundamental challenge for foundation models. While on-policy reinforcement learning can reduce forgetting, it requires explicit reward functions that are often unavailable. Learning from expert demonstrations, the primary alternative, is dominated by supervised fine-tuning (SFT), which is inherently off-policy. We introduce Self-Distillation Fine-Tuning (SDFT), a simple method that enables on-policy learning directly from demonstrations. SDFT leverages in-context learning by using a demonstration-conditioned model as its own teacher, generating on-policy training signals that preserve prior capabilities while acquiring new skills. Across skill learning and knowledge acquisition tasks, SDFT consistently outperforms SFT, achieving higher new-task accuracy while substantially reducing catastrophic forgetting. In sequential learning experiments, SDFT enables a single model to accumulate multiple skills over time without performance regression, establishing on-policy distillation as a practical path to continual learning from demonstrations.

