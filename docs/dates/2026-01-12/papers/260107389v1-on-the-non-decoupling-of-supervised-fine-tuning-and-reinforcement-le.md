---
layout: default
title: On the Non-decoupling of Supervised Fine-tuning and Reinforcement Learning in Post-training
---

# On the Non-decoupling of Supervised Fine-tuning and Reinforcement Learning in Post-training
**arXiv**：[2601.07389v1](https://arxiv.org/abs/2601.07389) · [PDF](https://arxiv.org/pdf/2601.07389.pdf)  
**作者**：Xueyan Niu, Bo Bai, Wei Han, Weixi Zhang  

**一句话要点**：证明大语言模型后训练中监督微调与强化学习不可解耦，实验验证性能退化

**关键词**：大语言模型后训练, 监督微调, 强化学习, 理论分析, 性能退化

## 3 点简述
- 核心问题：后训练中交替SFT与RL能否解耦，缺乏理论分析
- 方法要点：理论证明SFT-then-RL和RL-then-SFT耦合均导致性能损失
- 实验或效果：在Qwen3-0.6B上实验确认预测的性能退化

## 摘要（原文）

> Post-training of large language models routinely interleaves supervised fine-tuning (SFT) with reinforcement learning (RL). These two methods have different objectives: SFT minimizes the cross-entropy loss between model outputs and expert responses, while RL maximizes reward signals derived from human preferences or rule-based verifiers. Modern reasoning models have widely adopted the practice of alternating SFT and RL training. However, there is no theoretical account of whether they can be decoupled. We prove that decoupling is impossible in either order: (1) SFT-then-RL coupling: RL increases SFT loss under SFT optimality and (2) RL-then-SFT coupling: SFT lowers the reward achieved by RL. Experiments on Qwen3-0.6B confirm the predicted degradation, verifying that SFT and RL cannot be separated without loss of prior performance in the post-training

