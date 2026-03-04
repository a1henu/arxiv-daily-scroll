---
layout: default
title: Robotic Grasping and Placement Controlled by EEG-Based Hybrid Visual and Motor Imagery
---

# Robotic Grasping and Placement Controlled by EEG-Based Hybrid Visual and Motor Imagery
**arXiv**：[2603.03181v1](https://arxiv.org/abs/2603.03181) · [PDF](https://arxiv.org/pdf/2603.03181.pdf)  
**作者**：Yichang Liu, Tianyu Wang, Ziyi Ye, Yawei Li, Yu-Gang Jiang, Shouyan Wang, Yanwei Fu  

**一句话要点**：提出基于EEG视觉与运动想象的混合脑机接口框架，实现机器人实时意图驱动的抓取与放置控制。

**关键词**：脑机接口, 机器人控制, 视觉想象, 运动想象, 实时解码, 人机协作

## 3 点简述
- 核心问题：如何利用脑电信号实现直观的人机交互，以控制机器人完成抓取和放置任务。
- 方法要点：采用零样本在线流式处理，结合视觉想象识别抓取对象和运动想象确定放置姿态。
- 实验或效果：在线解码准确率视觉想象40.23%、运动想象62.59%，端到端任务成功率20.88%。

## 摘要（原文）

> We present a framework that integrates EEG-based visual and motor imagery (VI/MI) with robotic control to enable real-time, intention-driven grasping and placement. Motivated by the promise of BCI-driven robotics to enhance human-robot interaction, this system bridges neural signals with physical control by deploying offline-pretrained decoders in a zero-shot manner within an online streaming pipeline. This establishes a dual-channel intent interface that translates visual intent into robotic actions, with VI identifying objects for grasping and MI determining placement poses, enabling intuitive control over both what to grasp and where to place. The system operates solely on EEG via a cue-free imagery protocol, achieving integration and online validation. Implemented on a Base robotic platform and evaluated across diverse scenarios, including occluded targets or varying participant postures, the system achieves online decoding accuracies of 40.23% (VI) and 62.59% (MI), with an end-to-end task success rate of 20.88%. These results demonstrate that high-level visual cognition can be decoded in real time and translated into executable robot commands, bridging the gap between neural signals and physical interaction, and validating the flexibility of a purely imagery-based BCI paradigm for practical human-robot collaboration.

