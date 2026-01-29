---
layout: default
title: End-to-end example-based sim-to-real RL policy transfer based on neural stylisation with application to robotic cutting
---

# End-to-end example-based sim-to-real RL policy transfer based on neural stylisation with application to robotic cutting
**arXiv**：[2601.20846v1](https://arxiv.org/abs/2601.20846) · [PDF](https://arxiv.org/pdf/2601.20846.pdf)  
**作者**：Jamie Hathaway, Alireza Rastegarpanah, Rustam Stolkin  

**一句话要点**：提出基于神经风格化的端到端示例性模拟到真实强化学习策略转移方法，应用于机器人切割未知材料。

**关键词**：模拟到真实转移, 强化学习策略, 神经风格转移, 变分自编码器, 机器人切割, 弱配对轨迹

## 3 点简述
- 核心问题：模拟到真实策略转移中，数据依赖和领域差距限制真实世界部署。
- 方法要点：利用变分自编码器学习自监督特征表示，通过神经风格转移合成弱配对轨迹以增强物理真实性。
- 实验或效果：在机器人切割任务中，相比基线方法，提升任务完成时间和行为稳定性，对几何和材料变化具有鲁棒性。

## 摘要（原文）

> Whereas reinforcement learning has been applied with success to a range of robotic control problems in complex, uncertain environments, reliance on extensive data - typically sourced from simulation environments - limits real-world deployment due to the domain gap between simulated and physical systems, coupled with limited real-world sample availability. We propose a novel method for sim-to-real transfer of reinforcement learning policies, based on a reinterpretation of neural style transfer from image processing to synthesise novel training data from unpaired unlabelled real world datasets. We employ a variational autoencoder to jointly learn self-supervised feature representations for style transfer and generate weakly paired source-target trajectories to improve physical realism of synthesised trajectories. We demonstrate the application of our approach based on the case study of robot cutting of unknown materials. Compared to baseline methods, including our previous work, CycleGAN, and conditional variational autoencoder-based time series translation, our approach achieves improved task completion time and behavioural stability with minimal real-world data. Our framework demonstrates robustness to geometric and material variation, and highlights the feasibility of policy adaptation in challenging contact-rich tasks where real-world reward information is unavailable.

