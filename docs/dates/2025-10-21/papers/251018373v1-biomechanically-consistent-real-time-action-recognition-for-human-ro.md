---
layout: default
title: Biomechanically consistent real-time action recognition for human-robot interaction
---

# Biomechanically consistent real-time action recognition for human-robot interaction
**arXiv**：[2510.18373v1](https://arxiv.org/abs/2510.18373) · [PDF](https://arxiv.org/pdf/2510.18373.pdf)  
**作者**：Wanchen Li, Kahina Chalabi, Sabbah Maxime, Thomas Bousquet, Robin Passama, Sofiane Ramdani, Andrea Cherubini, Vincent Bonnet  

**一句话要点**：提出基于生物力学先验的实时动作识别框架，用于工业人机交互。

**关键词**：实时动作识别, 生物力学先验, Transformer网络, 人机交互, 关节角度估计

## 3 点简述
- 核心问题：现有方法依赖关节中心位置，多为离线，难以实时鲁棒识别。
- 方法要点：使用关节角度作为输入，结合Transformer网络，实现实时动作识别。
- 实验或效果：在11人数据集上达88%准确率，泛化能力强，支持机器人实时交互。

## 摘要（原文）

> This paper presents a novel framework for real-time human action recognition
> in industrial contexts, using standard 2D cameras. We introduce a complete
> pipeline for robust and real-time estimation of human joint kinematics, input
> to a temporally smoothed Transformer-based network, for action recognition. We
> rely on a new dataset including 11 subjects performing various actions, to
> evaluate our approach. Unlike most of the literature that relies on joint
> center positions (JCP) and is offline, ours uses biomechanical prior, eg. joint
> angles, for fast and robust real-time recognition. Besides, joint angles make
> the proposed method agnostic to sensor and subject poses as well as to
> anthropometric differences, and ensure robustness across environments and
> subjects. Our proposed learning model outperforms the best baseline model,
> running also in real-time, along various metrics. It achieves 88% accuracy and
> shows great generalization ability, for subjects not facing the cameras.
> Finally, we demonstrate the robustness and usefulness of our technique, through
> an online interaction experiment, with a simulated robot controlled in
> real-time via the recognized actions.

