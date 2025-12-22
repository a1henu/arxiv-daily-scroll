---
layout: default
title: Dexterous World Models
---

# Dexterous World Models
**arXiv**：[2512.17907v1](https://arxiv.org/abs/2512.17907) · [PDF](https://arxiv.org/pdf/2512.17907.pdf)  
**作者**：Byungjun Kim, Taeksoo Kim, Junyoung Lee, Hanbyul Joo  

**一句话要点**：提出Dexterous World Model，通过场景-动作条件视频扩散框架实现静态3D场景与灵巧人手的动态交互生成。

**关键词**：视频扩散模型, 数字孪生, 3D场景交互, 以自我为中心视觉, 动态场景生成, 具身人工智能

## 3 点简述
- 核心问题：现有数字孪生静态且缺乏具身交互，难以模拟人手动作引发的场景动态变化。
- 方法要点：结合静态场景渲染和以自我为中心的手部运动序列，训练视频扩散模型生成时空一致的交互视频。
- 实验或效果：DWM能生成抓取、打开和移动物体等真实物理交互，保持相机和场景一致性，支持具身模拟。

## 摘要（原文）

> Recent progress in 3D reconstruction has made it easy to create realistic digital twins from everyday environments. However, current digital twins remain largely static and are limited to navigation and view synthesis without embodied interactivity. To bridge this gap, we introduce Dexterous World Model (DWM), a scene-action-conditioned video diffusion framework that models how dexterous human actions induce dynamic changes in static 3D scenes.
>   Given a static 3D scene rendering and an egocentric hand motion sequence, DWM generates temporally coherent videos depicting plausible human-scene interactions. Our approach conditions video generation on (1) static scene renderings following a specified camera trajectory to ensure spatial consistency, and (2) egocentric hand mesh renderings that encode both geometry and motion cues to model action-conditioned dynamics directly. To train DWM, we construct a hybrid interaction video dataset. Synthetic egocentric interactions provide fully aligned supervision for joint locomotion and manipulation learning, while fixed-camera real-world videos contribute diverse and realistic object dynamics.
>   Experiments demonstrate that DWM enables realistic and physically plausible interactions, such as grasping, opening, and moving objects, while maintaining camera and scene consistency. This framework represents a first step toward video diffusion-based interactive digital twins and enables embodied simulation from egocentric actions.

