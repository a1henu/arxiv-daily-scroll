---
layout: default
title: Learning Latent Action World Models In The Wild
---

# Learning Latent Action World Models In The Wild
**arXiv**：[2601.05230v1](https://arxiv.org/abs/2601.05230) · [PDF](https://arxiv.org/pdf/2601.05230.pdf)  
**作者**：Quentin Garrido, Tushar Nagarajan, Basile Terver, Nicolas Ballas, Yann LeCun, Michael Rabbat  

**一句话要点**：提出学习潜在动作世界模型以处理野外视频中的动作预测问题

**关键词**：潜在动作模型, 世界模型, 野外视频学习, 动作预测, 连续潜在空间

## 3 点简述
- 核心问题：野外视频中动作标签获取困难，需从视频中学习潜在动作空间
- 方法要点：采用连续约束的潜在动作表示，避免向量量化，适应视频多样性
- 实验或效果：模型能学习特定于野外视频的动作，控制器映射已知动作，规划任务性能接近基线

## 摘要（原文）

> Agents capable of reasoning and planning in the real world require the ability of predicting the consequences of their actions. While world models possess this capability, they most often require action labels, that can be complex to obtain at scale. This motivates the learning of latent action models, that can learn an action space from videos alone. Our work addresses the problem of learning latent actions world models on in-the-wild videos, expanding the scope of existing works that focus on simple robotics simulations, video games, or manipulation data. While this allows us to capture richer actions, it also introduces challenges stemming from the video diversity, such as environmental noise, or the lack of a common embodiment across videos. To address some of the challenges, we discuss properties that actions should follow as well as relevant architectural choices and evaluations. We find that continuous, but constrained, latent actions are able to capture the complexity of actions from in-the-wild videos, something that the common vector quantization does not. We for example find that changes in the environment coming from agents, such as humans entering the room, can be transferred across videos. This highlights the capability of learning actions that are specific to in-the-wild videos. In the absence of a common embodiment across videos, we are mainly able to learn latent actions that become localized in space, relative to the camera. Nonetheless, we are able to train a controller that maps known actions to latent ones, allowing us to use latent actions as a universal interface and solve planning tasks with our world model with similar performance as action-conditioned baselines. Our analyses and experiments provide a step towards scaling latent action models to the real world.

