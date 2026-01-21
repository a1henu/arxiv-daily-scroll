---
layout: default
title: DroneVLA: VLA based Aerial Manipulation
---

# DroneVLA: VLA based Aerial Manipulation
**arXiv**：[2601.13809v1](https://arxiv.org/abs/2601.13809) · [PDF](https://arxiv.org/pdf/2601.13809.pdf)  
**作者**：Fawad Mehboob, Monijesu James, Amir Habel, Jeffrin Sam, Miguel Altamirano Cabrera, Dzmitry Tsetserukou  

**一句话要点**：提出基于VLA的自主空中操控系统，通过自然语言命令实现物体抓取与交付

**关键词**：空中操控, 视觉语言动作模型, 自然语言交互, 物体抓取, 人体姿态估计, 视觉伺服

## 3 点简述
- 核心问题：设计直观界面使非专家用户能自然命令空中平台进行主动操控
- 方法要点：集成Grounding DINO、VLA模型和MediaPipe，实现语义推理、导航和基于人体姿态的视觉伺服
- 实验或效果：真实世界实验显示定位与导航误差较小，验证了VLA在空中操控中的可行性

## 摘要（原文）

> As aerial platforms evolve from passive observers to active manipulators, the challenge shifts toward designing intuitive interfaces that allow non-expert users to command these systems naturally. This work introduces a novel concept of autonomous aerial manipulation system capable of interpreting high-level natural language commands to retrieve objects and deliver them to a human user. The system is intended to integrate a MediaPipe based on Grounding DINO and a Vision-Language-Action (VLA) model with a custom-built drone equipped with a 1-DOF gripper and an Intel RealSense RGB-D camera. VLA performs semantic reasoning to interpret the intent of a user prompt and generates a prioritized task queue for grasping of relevant objects in the scene. Grounding DINO and dynamic A* planning algorithm are used to navigate and safely relocate the object. To ensure safe and natural interaction during the handover phase, the system employs a human-centric controller driven by MediaPipe. This module provides real-time human pose estimation, allowing the drone to employ visual servoing to maintain a stable, distinct position directly in front of the user, facilitating a comfortable handover. We demonstrate the system's efficacy through real-world experiments for localization and navigation, which resulted in a 0.164m, 0.070m, and 0.084m of max, mean euclidean, and root-mean squared errors, respectively, highlighting the feasibility of VLA for aerial manipulation operations.

