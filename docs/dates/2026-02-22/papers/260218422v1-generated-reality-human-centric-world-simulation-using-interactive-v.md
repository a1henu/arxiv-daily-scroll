---
layout: default
title: Generated Reality: Human-centric World Simulation using Interactive Video Generation with Hand and Camera Control
---

# Generated Reality: Human-centric World Simulation using Interactive Video Generation with Hand and Camera Control
**arXiv**：[2602.18422v1](https://arxiv.org/abs/2602.18422) · [PDF](https://arxiv.org/pdf/2602.18422.pdf)  
**作者**：Linxi Xie, Lisong C. Sun, Ashley Neall, Tong Wu, Shengqu Cai, Gordon Wetzstein  

**一句话要点**：提出基于头手姿态控制的人本视频世界模型，以增强扩展现实中的交互体验。

**关键词**：视频生成, 扩散模型, 人本交互, 扩展现实, 姿态控制, 蒸馏训练

## 3 点简述
- 扩展现实需要响应真实世界运动的生成模型，但现有模型仅接受文本等粗粒度控制。
- 评估扩散变换器条件策略，提出3D头手控制机制，支持灵巧的手-物交互。
- 训练双向视频扩散教师模型并蒸馏为因果交互系统，人类实验显示任务性能和感知控制度提升。

## 摘要（原文）

> Extended reality (XR) demands generative models that respond to users' tracked real-world motion, yet current video world models accept only coarse control signals such as text or keyboard input, limiting their utility for embodied interaction. We introduce a human-centric video world model that is conditioned on both tracked head pose and joint-level hand poses. For this purpose, we evaluate existing diffusion transformer conditioning strategies and propose an effective mechanism for 3D head and hand control, enabling dexterous hand--object interactions. We train a bidirectional video diffusion model teacher using this strategy and distill it into a causal, interactive system that generates egocentric virtual environments. We evaluate this generated reality system with human subjects and demonstrate improved task performance as well as a significantly higher level of perceived amount of control over the performed actions compared with relevant baselines.

