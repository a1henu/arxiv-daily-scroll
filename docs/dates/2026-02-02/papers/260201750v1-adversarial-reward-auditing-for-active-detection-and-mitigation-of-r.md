---
layout: default
title: Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking
---

# Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking
**arXiv**：[2602.01750v1](https://arxiv.org/abs/2602.01750) · [PDF](https://arxiv.org/pdf/2602.01750.pdf)  
**作者**：Mohammad Beigi, Ming Jin, Junshan Zhang, Qifan Wang, Lifu Huang  

**一句话要点**：提出对抗性奖励审计框架，以动态检测和缓解强化学习中的奖励黑客问题

**关键词**：奖励黑客, 对抗性审计, 强化学习对齐, 跨领域泛化, 动态检测

## 3 点简述
- 核心问题：RLHF易受奖励黑客攻击，模型利用奖励模型中的虚假相关性，违背人类意图
- 方法要点：将奖励黑客重构为动态竞争游戏，通过黑客策略发现漏洞，审计器检测并引导RLHF惩罚黑客行为
- 实验或效果：在三种黑客场景中实现最佳对齐-效用权衡，检测和缓解能力可跨领域泛化

## 摘要（原文）

> Reinforcement Learning from Human Feedback (RLHF) remains vulnerable to reward hacking, where models exploit spurious correlations in learned reward models to achieve high scores while violating human intent. Existing mitigations rely on static defenses that cannot adapt to novel exploitation strategies. We propose Adversarial Reward Auditing (ARA), a framework that reconceptualizes reward hacking as a dynamic, competitive game. ARA operates in two stages: first, a Hacker policy discovers reward model vulnerabilities while an Auditor learns to detect exploitation from latent representations; second, Auditor-Guided RLHF (AG-RLHF) gates reward signals to penalize detected hacking, transforming reward hacking from an unobservable failure into a measurable, controllable signal. Experiments across three hacking scenarios demonstrate that ARA achieves the best alignment-utility tradeoff among all baselines: reducing sycophancy to near-SFT levels while improving helpfulness, decreasing verbosity while achieving the highest ROUGE-L, and suppressing code gaming while improving Pass@1. Beyond single-domain evaluation, we show that reward hacking, detection, and mitigation all generalize across domains -- a Hacker trained on code gaming exhibits increased sycophancy despite no reward for this behavior, and an Auditor trained on one domain effectively suppresses exploitation in others, enabling efficient multi-domain defense with a single model.

