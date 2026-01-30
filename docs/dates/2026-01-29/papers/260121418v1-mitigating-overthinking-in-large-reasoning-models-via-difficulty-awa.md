---
layout: default
title: Mitigating Overthinking in Large Reasoning Models via Difficulty-aware Reinforcement Learning
---

# Mitigating Overthinking in Large Reasoning Models via Difficulty-aware Reinforcement Learning
**arXiv**：[2601.21418v1](https://arxiv.org/abs/2601.21418) · [PDF](https://arxiv.org/pdf/2601.21418.pdf)  
**作者**：Qian Wan, Ziao Xu, Luona Wei, Xiaoxuan Shen, Jianwen Sun  

**一句话要点**：提出难度感知策略优化以解决大型推理模型在处理简单任务时的过度思考问题

**关键词**：大型推理模型, 过度思考缓解, 难度感知强化学习, 推理资源分配, 任务复杂度建模

## 3 点简述
- 核心问题：大型推理模型在简单任务上因深度思考模式导致推理冗长和资源低效
- 方法要点：基于强化学习的难度感知策略优化框架，鼓励模型自发建模任务复杂度并调整生成偏好
- 实验或效果：显著减少冗余推理标记，在保持性能的同时降低推理开销

## 摘要（原文）

> Large Reasoning Models (LRMs) achieve explicit chain-of-thought expansion by imitating deep thinking behaviors of humans, demonstrating excellent performance in complex task scenarios. However, the deep-thinking mode often leads to unnecessarily lengthy reasoning and resource inefficiency when handling simple tasks. This overthinking phenomenon may arise from the generation preference triggered by the reward function during post-training. Existing research attempts to mitigate overthinking from the perspective of prompt design or model training, but generally underestimates the importance of task difficulty awareness, which makes it difficult for LRMs to effectively allocate reasoning resources. In this paper, we propose Difficulty-aware Policy Optimization (DiPO), a reinforcement learning-based LRM training framework. DiPO encourages LRM to spontaneously model task complexity, and integrates them into reinforcement learning framework to adjust the generation preferences introduced by post-training. A difficulty modeling method based on model self-reasoning is proposed, which significantly reduces the dependence on manual annotation and formalize task complexity. We further develop a difficulty-signal-enhanced reward function that incorporates a penalty for lengthy reasoning while considering reasoning performance and output format. Experimental results indicate that DiPO enables the model to spontaneously adjust inference overhead, significantly reducing redundant tokens without losing performance due to thought compression.

