---
layout: default
title: WebArbiter: A Principle-Guided Reasoning Process Reward Model for Web Agents
---

# WebArbiter: A Principle-Guided Reasoning Process Reward Model for Web Agents
**arXiv**：[2601.21872v1](https://arxiv.org/abs/2601.21872) · [PDF](https://arxiv.org/pdf/2601.21872.pdf)  
**作者**：Yao Zhang, Shijie Tang, Zeyu Li, Zhen Han, Volker Tresp  

**一句话要点**：提出WebArbiter，一种基于原则推理的过程奖励模型，以解决网页代理在长序列决策中的稀疏监督问题。

**关键词**：网页代理, 过程奖励模型, 推理蒸馏, 强化学习, 文本生成, 长序列决策

## 3 点简述
- 核心问题：网页代理任务中，基于结果的监督稀疏且延迟，现有过程奖励模型信号粗糙或依赖脆弱模板匹配。
- 方法要点：将奖励建模转化为文本生成，通过推理蒸馏和强化学习两阶段训练，生成结构化理由和偏好裁决。
- 实验或效果：在WebPRMBench上超越GPT-5基准9.1分，在WebArena-Lite中提升轨迹搜索性能达7.2分。

## 摘要（原文）

> Web agents hold great potential for automating complex computer tasks, yet their interactions involve long-horizon, sequential decision-making with irreversible actions. In such settings, outcome-based supervision is sparse and delayed, often rewarding incorrect trajectories and failing to support inference-time scaling. This motivates the use of Process Reward Models (WebPRMs) for web navigation, but existing approaches remain limited: scalar WebPRMs collapse progress into coarse, weakly grounded signals, while checklist-based WebPRMs rely on brittle template matching that fails under layout or semantic changes and often mislabels superficially correct actions as successful, providing little insight or interpretability. To address these challenges, we introduce WebArbiter, a reasoning-first, principle-inducing WebPRM that formulates reward modeling as text generation, producing structured justifications that conclude with a preference verdict and identify the action most conducive to task completion under the current context. Training follows a two-stage pipeline: reasoning distillation equips the model with coherent principle-guided reasoning, and reinforcement learning corrects teacher biases by directly aligning verdicts with correctness, enabling stronger generalization. To support systematic evaluation, we release WebPRMBench, a comprehensive benchmark spanning four diverse web environments with rich tasks and high-quality preference annotations. On WebPRMBench, WebArbiter-7B outperforms the strongest baseline, GPT-5, by 9.1 points. In reward-guided trajectory search on WebArena-Lite, it surpasses the best prior WebPRM by up to 7.2 points, underscoring its robustness and practical value in real-world complex web tasks.

