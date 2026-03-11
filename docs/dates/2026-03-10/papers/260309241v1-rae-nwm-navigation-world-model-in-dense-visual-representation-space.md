---
layout: default
title: RAE-NWM: Navigation World Model in Dense Visual Representation Space
---

# RAE-NWM: Navigation World Model in Dense Visual Representation Space
**arXiv**：[2603.09241v1](https://arxiv.org/abs/2603.09241) · [PDF](https://arxiv.org/pdf/2603.09241.pdf)  
**作者**：Mingkun Zhang, Wangtian Shen, Fan Zhang, Haijian Qin, Zihao Pei, Ziyang Meng  

**一句话要点**：提出RAE-NWM，在密集视觉表示空间建模导航世界模型以提升结构稳定性和动作精度。

**关键词**：视觉导航, 世界模型, 密集表示, 扩散变换器, 动作预测, 线性动力学

## 3 点简述
- 当前导航世界模型在压缩潜在空间中学习状态演化，常丢失细粒度结构信息，影响精确控制。
- 通过线性动力学探测发现DINOv2特征具有更强线性可预测性，提出在密集视觉表示空间建模导航动态。
- 采用CDiT-DH建模连续转移，引入时间驱动门控模块调节动作注入强度，实验显示改善下游规划和导航性能。

## 摘要（原文）

> Visual navigation requires agents to reach goals in complex environments through perception and planning. World models address this task by simulating action-conditioned state transitions to predict future observations. Current navigation world models typically learn state evolution under actions within the compressed latent space of a Variational Autoencoder, where spatial compression often discards fine-grained structural information and hinders precise control. To better understand the propagation characteristics of different representations, we conduct a linear dynamics probe and observe that dense DINOv2 features exhibit stronger linear predictability for action-conditioned transitions. Motivated by this observation, we propose the Representation Autoencoder-based Navigation World Model (RAE-NWM), which models navigation dynamics in a dense visual representation space. We employ a Conditional Diffusion Transformer with Decoupled Diffusion Transformer head (CDiT-DH) to model continuous transitions, and introduce a separate time-driven gating module for dynamics conditioning to regulate action injection strength during generation. Extensive evaluations show that modeling sequential rollouts in this space improves structural stability and action accuracy, benefiting downstream planning and navigation.

