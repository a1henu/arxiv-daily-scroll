---
layout: default
title: ZeroWBC: Learning Natural Visuomotor Humanoid Control Directly from Human Egocentric Video
---

# ZeroWBC: Learning Natural Visuomotor Humanoid Control Directly from Human Egocentric Video
**arXiv**：[2603.09170v1](https://arxiv.org/abs/2603.09170) · [PDF](https://arxiv.org/pdf/2603.09170.pdf)  
**作者**：Haoran Yang, Jiacheng Bao, Yucheng Xin, Haoming Song, Yuyang Tian, Bin Zhao, Dong Wang, Xuelong Li  

**一句话要点**：提出ZeroWBC框架，直接从人类第一人称视频学习自然全身人形机器人控制

**关键词**：人形机器人控制, 第一人称视频学习, 视觉语言模型, 运动重定向, 全身控制

## 3 点简述
- 核心问题：现有方法依赖昂贵遥操作数据，难以实现自然全身交互控制
- 方法要点：基于视觉语言模型预测人体运动，再重定向至机器人执行
- 实验效果：在Unitree G1机器人上验证，运动自然性和多样性优于基线

## 摘要（原文）

> Achieving versatile and naturalistic whole-body control for humanoid robot scene-interaction remains a significant challenge. While some recent works have demonstrated autonomous humanoid interactive control, they are constrained to rigid locomotion patterns and expensive teleoperation data collection, lacking the versatility to execute more human-like natural behaviors such as sitting or kicking. Furthermore, acquiring the necessary real robot teleoperation data is prohibitively expensive and time-consuming. To address these limitations, we introduce ZeroWBC, a novel framework that learns a natural humanoid visuomotor control policy directly from human egocentric videos, eliminating the need for large-scale robot teleoperation data and enabling natural humanoid robot scene-interaction control. Specifically, our approach first fine-tunes a Vision-Language Model (VLM) to predict future whole-body human motions based on text instructions and egocentric visual context, then these generated motions are retargeted to real robot joints and executed via our robust general motion tracking policy for humanoid whole-body control. Extensive experiments on the Unitree G1 humanoid robot demonstrate that our method outperforms baseline approaches in motion naturalness and versatility, successfully establishing a pipeline that eliminates teleoperation data collection overhead for whole-body humanoid control, offering a scalable and efficient paradigm for general humanoid whole-body control.

