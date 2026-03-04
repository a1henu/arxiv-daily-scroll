---
layout: default
title: Post Hoc Extraction of Pareto Fronts for Continuous Control
---

# Post Hoc Extraction of Pareto Fronts for Continuous Control
**arXiv**：[2603.02628v1](https://arxiv.org/abs/2603.02628) · [PDF](https://arxiv.org/pdf/2603.02628.pdf)  
**作者**：Raghav Thakar, Gaurav Dixit, Kagan Tumer  

**一句话要点**：提出MAPEX方法，利用预训练专家策略离线提取帕累托前沿以降低样本成本。

**关键词**：多目标强化学习, 帕累托前沿提取, 离线学习, 专家策略重用, 样本效率, 连续控制

## 3 点简述
- 核心问题：多目标偏好常出现在单目标训练后，现有MORL方法无法重用专家策略，导致样本成本高。
- 方法要点：MAPEX结合专家评论家评估为混合优势信号，加权行为克隆损失训练新策略，实现离线帕累托前沿提取。
- 实验或效果：在五个MuJoCo环境中，MAPEX以0.001%样本成本产生可比帕累托前沿，验证其高效性。

## 摘要（原文）

> Agents in the real world must often balance multiple objectives, such as speed, stability, and energy efficiency in continuous control. To account for changing conditions and preferences, an agent must ideally learn a Pareto frontier of policies representing multiple optimal trade-offs. Recent advances in multi-policy multi-objective reinforcement learning (MORL) enable learning a Pareto front directly, but require full multi-objective consideration from the start of training. In practice, multi-objective preferences often arise after a policy has already been trained on a single specialised objective. Existing MORL methods cannot leverage these pre-trained `specialists' to learn Pareto fronts and avoid incurring the sample costs of retraining. We introduce Mixed Advantage Pareto Extraction (MAPEX), an offline MORL method that constructs a frontier of policies by reusing pre-trained specialist policies, critics, and replay buffers. MAPEX combines evaluations from specialist critics into a mixed advantage signal, and weights a behaviour cloning loss with it to train new policies that balance multiple objectives. MAPEX's post hoc Pareto front extraction preserves the simplicity of single-objective off-policy RL, and avoids retrofitting these algorithms into complex MORL frameworks. We formally describe the MAPEX procedure and evaluate MAPEX on five multi-objective MuJoCo environments. Given the same starting policies, MAPEX produces comparable fronts at $0.001\%$ the sample cost of established baselines.

