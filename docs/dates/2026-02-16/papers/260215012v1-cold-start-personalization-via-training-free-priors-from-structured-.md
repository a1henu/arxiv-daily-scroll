---
layout: default
title: Cold-Start Personalization via Training-Free Priors from Structured World Models
---

# Cold-Start Personalization via Training-Free Priors from Structured World Models
**arXiv**：[2602.15012v1](https://arxiv.org/abs/2602.15012) · [PDF](https://arxiv.org/pdf/2602.15012.pdf)  
**作者**：Avinandan Bose, Shuyue Stella Li, Faeze Brahman, Pang Wei Koh, Simon Shaolei Du, Yulia Tsvetkov, Maryam Fazel, Lin Xiao, Asli Celikyilmaz  

**一句话要点**：提出Pep框架，通过离线结构化世界模型与在线贝叶斯推理解决冷启动个性化中的偏好维度路由问题。

**关键词**：冷启动个性化, 偏好启发, 结构化世界模型, 贝叶斯推理, 强化学习对比, 参数效率

## 3 点简述
- 核心问题：冷启动个性化中，如何在有限交互内有效推断用户偏好维度，避免静态提问序列忽略用户响应。
- 方法要点：离线学习偏好关联的结构化世界模型，在线进行无训练贝叶斯推理以选择信息性问题并预测完整偏好。
- 实验或效果：在多个领域实现80.8%偏好对齐，比RL减少3-5倍交互，参数规模小且能动态调整后续问题。

## 摘要（原文）

> Cold-start personalization requires inferring user preferences through interaction when no user-specific historical data is available. The core challenge is a routing problem: each task admits dozens of preference dimensions, yet individual users care about only a few, and which ones matter depends on who is asking. With a limited question budget, asking without structure will miss the dimensions that matter. Reinforcement learning is the natural formulation, but in multi-turn settings its terminal reward fails to exploit the factored, per-criterion structure of preference data, and in practice learned policies collapse to static question sequences that ignore user responses. We propose decomposing cold-start elicitation into offline structure learning and online Bayesian inference. Pep (Preference Elicitation with Priors) learns a structured world model of preference correlations offline from complete profiles, then performs training-free Bayesian inference online to select informative questions and predict complete preference profiles, including dimensions never asked about. The framework is modular across downstream solvers and requires only simple belief models. Across medical, mathematical, social, and commonsense reasoning, Pep achieves 80.8% alignment between generated responses and users' stated preferences versus 68.5% for RL, with 3-5x fewer interactions. When two users give different answers to the same question, Pep changes its follow-up 39-62% of the time versus 0-28% for RL. It does so with ~10K parameters versus 8B for RL, showing that the bottleneck in cold-start elicitation is the capability to exploit the factored structure of preference data.

