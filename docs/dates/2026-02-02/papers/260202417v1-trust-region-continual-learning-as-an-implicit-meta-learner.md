---
layout: default
title: Trust Region Continual Learning as an Implicit Meta-Learner
---

# Trust Region Continual Learning as an Implicit Meta-Learner
**arXiv**：[2602.02417v1](https://arxiv.org/abs/2602.02417) · [PDF](https://arxiv.org/pdf/2602.02417.pdf)  
**作者**：Zekun Wang, Anant Gupta, Christopher J. MacLellan  

**一句话要点**：提出信任区域持续学习，结合生成回放与Fisher度量约束，实现隐式元学习以缓解灾难性遗忘。

**关键词**：持续学习, 信任区域优化, 生成回放, Fisher信息矩阵, 隐式元学习, 灾难性遗忘

## 3 点简述
- 持续学习中正则化与回放方法存在权衡：前者可能过度约束更新，后者可能因不完美回放导致性能漂移。
- 方法结合生成回放提供旧任务梯度信号，Fisher加权惩罚提供离线曲率整形，形成单步隐式元学习更新。
- 在任务增量扩散图像生成和持续扩散策略控制实验中，该方法在最终性能和保留率上表现最佳，并更快恢复早期任务性能。

## 摘要（原文）

> Continual learning aims to acquire tasks sequentially without catastrophic forgetting, yet standard strategies face a core tradeoff: regularization-based methods (e.g., EWC) can overconstrain updates when task optima are weakly overlapping, while replay-based methods can retain performance but drift due to imperfect replay. We study a hybrid perspective: \emph{trust region continual learning} that combines generative replay with a Fisher-metric trust region constraint. We show that, under local approximations, the resulting update admits a MAML-style interpretation with a single implicit inner step: replay supplies an old-task gradient signal (query-like), while the Fisher-weighted penalty provides an efficient offline curvature shaping (support-like). This yields an emergent meta-learning property in continual learning: the model becomes an initialization that rapidly \emph{re-converges} to prior task optima after each task transition, without explicitly optimizing a bilevel objective. Empirically, on task-incremental diffusion image generation and continual diffusion-policy control, trust region continual learning achieves the best final performance and retention, and consistently recovers early-task performance faster than EWC, replay, and continual meta-learning baselines.

