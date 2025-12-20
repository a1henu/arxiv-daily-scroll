---
layout: default
title: Avatar4D: Synthesizing Domain-Specific 4D Humans for Real-World Pose Estimation
---

# Avatar4D: Synthesizing Domain-Specific 4D Humans for Real-World Pose Estimation
**arXiv**：[2512.16199v1](https://arxiv.org/abs/2512.16199) · [PDF](https://arxiv.org/pdf/2512.16199.pdf)  
**作者**：Jerrin Bright, Zhibo Wang, Dmytro Klepachevskyi, Yuhao Chen, Sirisha Rambhatla, David Clausi, John Zelek  

**一句话要点**：提出Avatar4D以生成领域特定4D人体运动数据集，用于真实世界姿态估计

**关键词**：4D人体合成, 姿态估计, 合成数据集, 领域自适应, 体育动作分析, 零样本迁移

## 3 点简述
- 核心问题：现有合成数据集缺乏对领域特定动作的精细控制和灵活性，难以适应如体育等复杂场景。
- 方法要点：Avatar4D提供对姿态、外观、视角和环境的可控生成，无需人工标注，支持高保真4D序列。
- 实验或效果：在Syn2Sport数据集上验证了模型在监督学习、零样本迁移和跨体育泛化中的有效性，并评估了合成与真实数据的特征对齐。

## 摘要（原文）

> We present Avatar4D, a real-world transferable pipeline for generating customizable synthetic human motion datasets tailored to domain-specific applications. Unlike prior works, which focus on general, everyday motions and offer limited flexibility, our approach provides fine-grained control over body pose, appearance, camera viewpoint, and environmental context, without requiring any manual annotations. To validate the impact of Avatar4D, we focus on sports, where domain-specific human actions and movement patterns pose unique challenges for motion understanding. In this setting, we introduce Syn2Sport, a large-scale synthetic dataset spanning sports, including baseball and ice hockey. Avatar4D features high-fidelity 4D (3D geometry over time) human motion sequences with varying player appearances rendered in diverse environments. We benchmark several state-of-the-art pose estimation models on Syn2Sport and demonstrate their effectiveness for supervised learning, zero-shot transfer to real-world data, and generalization across sports. Furthermore, we evaluate how closely the generated synthetic data aligns with real-world datasets in feature space. Our results highlight the potential of such systems to generate scalable, controllable, and transferable human datasets for diverse domain-specific tasks without relying on domain-specific real data.

