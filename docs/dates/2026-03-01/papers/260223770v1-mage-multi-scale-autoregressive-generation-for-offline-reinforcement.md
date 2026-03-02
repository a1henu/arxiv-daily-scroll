---
layout: default
title: MAGE: Multi-scale Autoregressive Generation for Offline Reinforcement Learning
---

# MAGE: Multi-scale Autoregressive Generation for Offline Reinforcement Learning
**arXiv**：[2602.23770v1](https://arxiv.org/abs/2602.23770) · [PDF](https://arxiv.org/pdf/2602.23770.pdf)  
**作者**：Chenxing Lin, Xinhui Gao, Haipeng Zhang, Xinran Li, Haitao Wang, Songzhu Mei, Chenglu Wen, Weiquan Liu, Siqi Shen, Cheng Wang  

**一句话要点**：提出MAGE方法，通过多尺度自回归生成解决离线强化学习中长时程稀疏奖励任务的问题。

**关键词**：离线强化学习, 多尺度生成, 自回归模型, 稀疏奖励, 轨迹建模, 条件引导

## 3 点简述
- 核心问题：现有生成方法在长时程稀疏奖励任务中表现不佳，忽视轨迹的多尺度时间结构。
- 方法要点：使用条件引导多尺度自编码器学习层次轨迹表示，结合多尺度Transformer从粗到细自回归生成。
- 实验或效果：在五个离线RL基准测试中优于十五个基线算法，生成连贯可控的轨迹。

## 摘要（原文）

> Generative models have gained significant traction in offline reinforcement learning (RL) due to their ability to model complex trajectory distributions. However, existing generation-based approaches still struggle with long-horizon tasks characterized by sparse rewards. Some hierarchical generation methods have been developed to mitigate this issue by decomposing the original problem into shorter-horizon subproblems using one policy and generating detailed actions with another. While effective, these methods often overlook the multi-scale temporal structure inherent in trajectories, resulting in suboptimal performance. To overcome these limitations, we propose MAGE, a Multi-scale Autoregressive GEneration-based offline RL method. MAGE incorporates a condition-guided multi-scale autoencoder to learn hierarchical trajectory representations, along with a multi-scale transformer that autoregressively generates trajectory representations from coarse to fine temporal scales. MAGE effectively captures temporal dependencies of trajectories at multiple resolutions. Additionally, a condition-guided decoder is employed to exert precise control over short-term behaviors. Extensive experiments on five offline RL benchmarks against fifteen baseline algorithms show that MAGE successfully integrates multi-scale trajectory modeling with conditional guidance, generating coherent and controllable trajectories in long-horizon sparse-reward settings.

