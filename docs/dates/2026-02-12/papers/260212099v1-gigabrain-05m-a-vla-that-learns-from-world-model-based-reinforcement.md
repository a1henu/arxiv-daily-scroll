---
layout: default
title: GigaBrain-0.5M*: a VLA That Learns From World Model-Based Reinforcement Learning
---

# GigaBrain-0.5M*: a VLA That Learns From World Model-Based Reinforcement Learning
**arXiv**：[2602.12099v1](https://arxiv.org/abs/2602.12099) · [PDF](https://arxiv.org/pdf/2602.12099.pdf)  
**作者**：GigaBrain Team, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Hao Li, Jie Li, Jindi Lv, Jingyu Liu, Lv Feng, Mingming Yu, Peng Li, Qiuping Deng, Tianze Liu, Xinyu Zhou, Xinze Chen, Xiaofeng Wang, Yang Wang, Yifan Li, Yifei Nie, Yilong Li, Yukun Zhou, Yun Ye, Zhichao Liu, Zheng Zhu  

**一句话要点**：提出GigaBrain-0.5M*，通过世界模型强化学习增强视觉-语言-动作模型的跨任务适应能力。

**关键词**：视觉-语言-动作模型, 世界模型强化学习, 跨任务适应, 机器人操作, 长时程执行, 时空推理

## 3 点简述
- 核心问题：传统视觉-语言-动作模型因场景理解和未来预测能力受限，影响多步动作预测。
- 方法要点：基于视频世界模型，采用RAMP强化学习框架，提升模型的时空推理和未来预测能力。
- 实验或效果：在Laundry Folding等挑战性任务上，性能比RECAP基线提升约30%，实现可靠的长时程执行。

## 摘要（原文）

> Vision-language-action (VLA) models that directly predict multi-step action chunks from current observations face inherent limitations due to constrained scene understanding and weak future anticipation capabilities. In contrast, video world models pre-trained on web-scale video corpora exhibit robust spatiotemporal reasoning and accurate future prediction, making them a natural foundation for enhancing VLA learning. Therefore, we propose \textit{GigaBrain-0.5M*}, a VLA model trained via world model-based reinforcement learning. Built upon \textit{GigaBrain-0.5}, which is pre-trained on over 10,000 hours of robotic manipulation data, whose intermediate version currently ranks first on the international RoboChallenge benchmark. \textit{GigaBrain-0.5M*} further integrates world model-based reinforcement learning via \textit{RAMP} (Reinforcement leArning via world Model-conditioned Policy) to enable robust cross-task adaptation. Empirical results demonstrate that \textit{RAMP} achieves substantial performance gains over the RECAP baseline, yielding improvements of approximately 30\% on challenging tasks including \texttt{Laundry Folding}, \texttt{Box Packing}, and \texttt{Espresso Preparation}. Critically, \textit{GigaBrain-0.5M$^*$} exhibits reliable long-horizon execution, consistently accomplishing complex manipulation tasks without failure as validated by real-world deployment videos on our \href{https://gigabrain05m.github.io}{project page}.

