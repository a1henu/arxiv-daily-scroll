---
layout: default
title: Learning Latent Action World Models In The Wild
---

# Learning Latent Action World Models In The Wild
**arXiv**：[2601.05230v1](https://arxiv.org/abs/2601.05230) · [PDF](https://arxiv.org/pdf/2601.05230.pdf)  
**作者**：Quentin Garrido, Tushar Nagarajan, Basile Terver, Nicolas Ballas, Yann LeCun, Michael Rabbat  

**一句话要点**：提出学习野外视频中的潜在动作世界模型，以扩展动作预测至真实世界场景。

**关键词**：潜在动作模型, 世界模型, 野外视频学习, 动作预测, 连续潜在表示, 规划任务

## 3 点简述
- 核心问题：在野外视频中学习潜在动作世界模型，面临视频多样性、环境噪声和缺乏共同体现的挑战。
- 方法要点：采用连续但受限的潜在动作表示，替代向量量化，以捕获复杂动作并讨论相关架构选择。
- 实验或效果：训练控制器映射已知动作到潜在动作，实现规划任务性能与动作条件基线相当，验证模型泛化能力。

## 摘要（原文）

> Agents capable of reasoning and planning in the real world require the ability of predicting the consequences of their actions. While world models possess this capability, they most often require action labels, that can be complex to obtain at scale. This motivates the learning of latent action models, that can learn an action space from videos alone. Our work addresses the problem of learning latent actions world models on in-the-wild videos, expanding the scope of existing works that focus on simple robotics simulations, video games, or manipulation data. While this allows us to capture richer actions, it also introduces challenges stemming from the video diversity, such as environmental noise, or the lack of a common embodiment across videos. To address some of the challenges, we discuss properties that actions should follow as well as relevant architectural choices and evaluations. We find that continuous, but constrained, latent actions are able to capture the complexity of actions from in-the-wild videos, something that the common vector quantization does not. We for example find that changes in the environment coming from agents, such as humans entering the room, can be transferred across videos. This highlights the capability of learning actions that are specific to in-the-wild videos. In the absence of a common embodiment across videos, we are mainly able to learn latent actions that become localized in space, relative to the camera. Nonetheless, we are able to train a controller that maps known actions to latent ones, allowing us to use latent actions as a universal interface and solve planning tasks with our world model with similar performance as action-conditioned baselines. Our analyses and experiments provide a step towards scaling latent action models to the real world.

