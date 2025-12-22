---
layout: default
title: Vidarc: Embodied Video Diffusion Model for Closed-loop Control
---

# Vidarc: Embodied Video Diffusion Model for Closed-loop Control
**arXiv**：[2512.17661v1](https://arxiv.org/abs/2512.17661) · [PDF](https://arxiv.org/pdf/2512.17661.pdf)  
**作者**：Yao Feng, Chendong Xiang, Xinyi Mao, Hengkai Tan, Zuyue Zhang, Shuhe Huang, Kaiwen Zheng, Haitian Liu, Hang Su, Jun Zhu  

**一句话要点**：提出Vidarc，一种基于掩码逆动力学模型的视频扩散方法，用于数据稀缺场景下的机器人闭环控制。

**关键词**：视频扩散模型, 机器人闭环控制, 掩码逆动力学, 自回归生成, 跨体现泛化

## 3 点简述
- 核心问题：数据稀缺环境下机器人操作因复杂动力学和多样上下文而困难，现有视频方法在闭环控制中延迟高、接地不足。
- 方法要点：结合掩码逆动力学模型，通过动作相关掩码接地视频预测，并利用缓存自回归生成实现实时反馈。
- 实验或效果：在百万跨体现片段上预训练，实际部署成功率提升至少15%，延迟降低91%，展现强泛化和纠错能力。

## 摘要（原文）

> Robotic arm manipulation in data-scarce settings is a highly challenging task due to the complex embodiment dynamics and diverse contexts. Recent video-based approaches have shown great promise in capturing and transferring the temporal and physical interactions by pre-training on Internet-scale video data. However, such methods are often not optimized for the embodiment-specific closed-loop control, typically suffering from high latency and insufficient grounding. In this paper, we present Vidarc (Video Diffusion for Action Reasoning and Closed-loop Control), a novel autoregressive embodied video diffusion approach augmented by a masked inverse dynamics model. By grounding video predictions with action-relevant masks and incorporating real-time feedback through cached autoregressive generation, Vidarc achieves fast, accurate closed-loop control. Pre-trained on one million cross-embodiment episodes, Vidarc surpasses state-of-the-art baselines, achieving at least a 15% higher success rate in real-world deployment and a 91% reduction in latency. We also highlight its robust generalization and error correction capabilities across previously unseen robotic platforms.

