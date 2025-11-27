---
layout: default
title: SocialNav: Training Human-Inspired Foundation Model for Socially-Aware Embodied Navigation
---

# SocialNav: Training Human-Inspired Foundation Model for Socially-Aware Embodied Navigation
**arXiv**：[2511.21135v1](https://arxiv.org/abs/2511.21135) · [PDF](https://arxiv.org/pdf/2511.21135.pdf)  
**作者**：Ziyi Chen, Yingnan Guo, Zedong Chu, Minghua Luo, Yanfen Shen, Mingchao Sun, Junjun Hu, Shichao Xie, Kuan Yang, Pei Shi, Zhining Gu, Lu Liu, Honglin Han, Xiaolong Wu, Mu Xu, Yu Zhang  

**一句话要点**：提出SocialNav基础模型，通过分层架构解决具身导航中的社会规范遵从问题

**关键词**：具身导航, 社会规范遵从, 分层架构, 模仿学习, 强化学习, 数据集构建

## 3 点简述
- 核心问题：具身导航需遵守社会规范，但现有方法难以实现高社会合规性。
- 方法要点：采用分层'大脑-行动'架构，结合模仿学习和基于流的强化学习SAFE-GRPO。
- 实验效果：相比SOTA方法，成功率提升38%，社会合规率提升46%。

## 摘要（原文）

> Embodied navigation that adheres to social norms remains an open research challenge. Our \textbf{SocialNav} is a foundational model for socially-aware navigation with a hierarchical "brain-action" architecture, capable of understanding high-level social norms and generating low-level, socially compliant trajectories. To enable such dual capabilities, we construct the SocNav Dataset, a large-scale collection of 7 million samples, comprising (1) a Cognitive Activation Dataset providing social reasoning signals such as chain-of-thought explanations and social traversability prediction, and (2) an Expert Trajectories Pyramid aggregating diverse navigation demonstrations from internet videos, simulated environments, and real-world robots. A multi-stage training pipeline is proposed to gradually inject and refine navigation intelligence: we first inject general navigation skills and social norms understanding into the model via imitation learning, and then refine such skills through a deliberately designed Socially-Aware Flow Exploration GRPO (SAFE-GRPO), the first flow-based reinforcement learning framework for embodied navigation that explicitly rewards socially compliant behaviors. SocialNav achieves +38% success rate and +46% social compliance rate compared to the state-of-the-art method, demonstrating strong gains in both navigation performance and social compliance. Our project page: https://amap-eai.github.io/SocialNav/

