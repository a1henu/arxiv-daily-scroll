---
layout: default
title: BayesianVLA: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries
---

# BayesianVLA: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries
**arXiv**：[2601.15197v1](https://arxiv.org/abs/2601.15197) · [PDF](https://arxiv.org/pdf/2601.15197.pdf)  
**作者**：Shijie Lian, Bin Yu, Xiaopeng Lin, Laurence T. Yang, Zhaolong Shen, Changti Wu, Yuzhuo Miao, Cong Huang, Kai Chen  

**一句话要点**：提出BayesianVLA框架，通过贝叶斯分解解决视觉语言动作模型在泛化中的信息崩溃问题。

**关键词**：视觉语言动作模型, 贝叶斯分解, 潜在动作查询, 信息崩溃, 机器人操作, 泛化能力

## 3 点简述
- 核心问题：当前训练范式导致数据集偏差，语言指令与动作间条件互信息消失，模型退化为仅视觉策略。
- 方法要点：引入可学习的潜在动作查询，构建双分支架构估计视觉先验和语言后验，最大化条件点互信息。
- 实验或效果：在SimplerEnv和RoboCasa上显著提升泛化能力，OOD基准上改进11.3%，无需新数据。

## 摘要（原文）

> Vision-Language-Action (VLA) models have shown promise in robot manipulation but often struggle to generalize to new instructions or complex multi-task scenarios. We identify a critical pathology in current training paradigms where goal-driven data collection creates a dataset bias. In such datasets, language instructions are highly predictable from visual observations alone, causing the conditional mutual information between instructions and actions to vanish, a phenomenon we term Information Collapse. Consequently, models degenerate into vision-only policies that ignore language constraints and fail in out-of-distribution (OOD) settings. To address this, we propose BayesianVLA, a novel framework that enforces instruction following via Bayesian decomposition. By introducing learnable Latent Action Queries, we construct a dual-branch architecture to estimate both a vision-only prior $p(a \mid v)$ and a language-conditioned posterior $π(a \mid v, \ell)$. We then optimize the policy to maximize the conditional Pointwise Mutual Information (PMI) between actions and instructions. This objective effectively penalizes the vision shortcut and rewards actions that explicitly explain the language command. Without requiring new data, BayesianVLA significantly improves generalization. Extensive experiments across on SimplerEnv and RoboCasa demonstrate substantial gains, including an 11.3% improvement on the challenging OOD SimplerEnv benchmark, validating the ability of our approach to robustly ground language in action.

