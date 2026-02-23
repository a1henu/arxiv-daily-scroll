---
layout: default
title: Flow Matching with Injected Noise for Offline-to-Online Reinforcement Learning
---

# Flow Matching with Injected Noise for Offline-to-Online Reinforcement Learning
**arXiv**：[2602.18117v1](https://arxiv.org/abs/2602.18117) · [PDF](https://arxiv.org/pdf/2602.18117.pdf)  
**作者**：Yongjae Shin, Jongseong Chae, Jongeui Park, Youngchul Sung  

**一句话要点**：提出FINO方法，通过注入噪声增强离线到在线强化学习的样本效率。

**关键词**：离线到在线强化学习, 流匹配策略, 噪声注入, 熵引导采样, 样本效率

## 3 点简述
- 核心问题：生成模型在离线强化学习中表现良好，但在在线微调时面临探索不足的挑战。
- 方法要点：利用流匹配策略，注入噪声以鼓励超出离线数据集的行动，并引入熵引导采样平衡探索与利用。
- 实验或效果：在多样挑战性任务中，FINO在有限在线预算下持续实现优越性能。

## 摘要（原文）

> Generative models have recently demonstrated remarkable success across diverse domains, motivating their adoption as expressive policies in reinforcement learning (RL). While they have shown strong performance in offline RL, particularly where the target distribution is well defined, their extension to online fine-tuning has largely been treated as a direct continuation of offline pre-training, leaving key challenges unaddressed. In this paper, we propose Flow Matching with Injected Noise for Offline-to-Online RL (FINO), a novel method that leverages flow matching-based policies to enhance sample efficiency for offline-to-online RL. FINO facilitates effective exploration by injecting noise into policy training, thereby encouraging a broader range of actions beyond those observed in the offline dataset. In addition to exploration-enhanced flow policy training, we combine an entropy-guided sampling mechanism to balance exploration and exploitation, allowing the policy to adapt its behavior throughout online fine-tuning. Experiments across diverse, challenging tasks demonstrate that FINO consistently achieves superior performance under limited online budgets.

