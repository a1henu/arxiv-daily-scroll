---
layout: default
title: LAOF: Robust Latent Action Learning with Optical Flow Constraints
---

# LAOF: Robust Latent Action Learning with Optical Flow Constraints
**arXiv**：[2511.16407v1](https://arxiv.org/abs/2511.16407) · [PDF](https://arxiv.org/pdf/2511.16407.pdf)  
**作者**：Xizhou Bu, Jiexi Lyu, Fulei Sun, Ruichen Yang, Zhiqiang Ma, Wei Li  

**一句话要点**：提出LAOF框架，利用光流约束学习鲁棒潜在动作表示以应对动作无关干扰

**关键词**：潜在动作学习, 光流约束, 伪监督框架, 鲁棒表示学习, 模仿学习, 强化学习

## 3 点简述
- 核心问题：大规模视频中学习潜在动作易受动作无关干扰，且动作标签稀缺。
- 方法要点：使用光流作为动作驱动信号，构建伪监督框架学习鲁棒潜在表示。
- 实验或效果：在模仿学习和强化学习任务中表现优异，训练稳定且标签效率高。

## 摘要（原文）

> Learning latent actions from large-scale videos is crucial for the pre-training of scalable embodied foundation models, yet existing methods often struggle with action-irrelevant distractors. Although incorporating action supervision can alleviate these distractions, its effectiveness is restricted by the scarcity of available action labels. Optical flow represents pixel-level motion between consecutive frames, naturally suppressing background elements and emphasizing moving objects. Motivated by this, we propose robust Latent Action learning with Optical Flow constraints, called LAOF, a pseudo-supervised framework that leverages the agent's optical flow as an action-driven signal to learn latent action representations robust to distractors. Experimental results show that the latent representations learned by LAOF outperform existing methods on downstream imitation learning and reinforcement learning tasks. This superior performance arises from optical flow constraints, which substantially stabilize training and improve the quality of latent representations under extremely label-scarce conditions, while remaining effective as the proportion of action labels increases to 10 percent. Importantly, even without action supervision, LAOF matches or surpasses action-supervised methods trained with 1 percent of action labels.

