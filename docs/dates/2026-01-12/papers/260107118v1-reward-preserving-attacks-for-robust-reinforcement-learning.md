---
layout: default
title: Reward-Preserving Attacks For Robust Reinforcement Learning
---

# Reward-Preserving Attacks For Robust Reinforcement Learning
**arXiv**：[2601.07118v1](https://arxiv.org/abs/2601.07118) · [PDF](https://arxiv.org/pdf/2601.07118.pdf)  
**作者**：Lucas Schott, Elies Gherbi, Hatem Hajri, Sylvain Lamprier  

**一句话要点**：提出α-奖励保持攻击以解决强化学习中对抗鲁棒性的攻击强度自适应问题。

**关键词**：强化学习, 对抗鲁棒性, 自适应攻击, 奖励保持, 深度强化学习, 梯度攻击

## 3 点简述
- 核心问题：对抗扰动影响整个轨迹，攻击强度难以校准，过强破坏学习，过弱鲁棒性差。
- 方法要点：设计α-奖励保持攻击，自适应调整攻击强度，保持α比例的名义到最坏情况回报差距可达成。
- 实验或效果：在深度强化学习中，通过基于梯度的攻击方向和状态依赖幅度学习，提升跨半径鲁棒性并保持名义性能。

## 摘要（原文）

> Adversarial robustness in RL is difficult because perturbations affect entire trajectories: strong attacks can break learning, while weak attacks yield little robustness, and the appropriate strength varies by state. We propose $α$-reward-preserving attacks, which adapt the strength of the adversary so that an $α$ fraction of the nominal-to-worst-case return gap remains achievable at each state. In deep RL, we use a gradient-based attack direction and learn a state-dependent magnitude $η\le η_{\mathcal B}$ selected via a critic $Q^π_α((s,a),η)$ trained off-policy over diverse radii. This adaptive tuning calibrates attack strength and, with intermediate $α$, improves robustness across radii while preserving nominal performance, outperforming fixed- and random-radius baselines.

