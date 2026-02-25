---
layout: default
title: TrajGPT-R: Generating Urban Mobility Trajectory with Reinforcement Learning-Enhanced Generative Pre-trained Transformer
---

# TrajGPT-R: Generating Urban Mobility Trajectory with Reinforcement Learning-Enhanced Generative Pre-trained Transformer
**arXiv**：[2602.20643v1](https://arxiv.org/abs/2602.20643) · [PDF](https://arxiv.org/pdf/2602.20643.pdf)  
**作者**：Jiawei Wang, Chuang Yang, Jiawei Yong, Xiaohang Xu, Hongjun Wang, Noboru Koshizuka, Shintaro Fukushima, Ryosuke Shibasaki, Renhe Jiang  

**一句话要点**：提出TrajGPT-R框架，通过强化学习增强的生成预训练Transformer生成城市移动轨迹以解决隐私数据获取难题。

**关键词**：城市移动轨迹生成, 生成预训练Transformer, 离线强化学习, 逆强化学习, 隐私保护数据模拟

## 3 点简述
- 核心问题：城市移动轨迹数据因隐私限制难以获取，影响城市动态理解和规划。
- 方法要点：采用两阶段Transformer模型，结合离线强化学习和逆强化学习捕获轨迹奖励信号。
- 实验或效果：在多个数据集上评估，显示模型在可靠性和多样性上显著优于现有方法。

## 摘要（原文）

> Mobility trajectories are essential for understanding urban dynamics and enhancing urban planning, yet access to such data is frequently hindered by privacy concerns. This research introduces a transformative framework for generating large-scale urban mobility trajectories, employing a novel application of a transformer-based model pre-trained and fine-tuned through a two-phase process. Initially, trajectory generation is conceptualized as an offline reinforcement learning (RL) problem, with a significant reduction in vocabulary space achieved during tokenization. The integration of Inverse Reinforcement Learning (IRL) allows for the capture of trajectory-wise reward signals, leveraging historical data to infer individual mobility preferences. Subsequently, the pre-trained model is fine-tuned using the constructed reward model, effectively addressing the challenges inherent in traditional RL-based autoregressive methods, such as long-term credit assignment and handling of sparse reward environments. Comprehensive evaluations on multiple datasets illustrate that our framework markedly surpasses existing models in terms of reliability and diversity. Our findings not only advance the field of urban mobility modeling but also provide a robust methodology for simulating urban data, with significant implications for traffic management and urban development planning. The implementation is publicly available at https://github.com/Wangjw6/TrajGPT_R.

