---
layout: default
title: Making Avatars Interact: Towards Text-Driven Human-Object Interaction for Controllable Talking Avatars
---

# Making Avatars Interact: Towards Text-Driven Human-Object Interaction for Controllable Talking Avatars
**arXiv**：[2602.01538v1](https://arxiv.org/abs/2602.01538) · [PDF](https://arxiv.org/pdf/2602.01538.pdf)  
**作者**：Youliang Zhang, Zhengguang Zhou, Zhentao Yu, Ziyao Huang, Teng Hu, Sen Liang, Guozhen Zhang, Ziqiao Peng, Shunkai Li, Yi Chen, Zixiang Zhou, Yuan Zhou, Qinglin Lu, Xiu Li  

**一句话要点**：提出InteractAvatar框架以解决文本驱动的人-物交互说话头像生成中的控制-质量困境

**关键词**：说话头像生成, 人-物交互, 文本驱动控制, 双流框架, 视频合成, 基准评估

## 3 点简述
- 核心问题：现有方法难以生成基于文本的说话头像与周围物体的交互，面临环境感知和控制-质量困境的挑战。
- 方法要点：采用双流框架，通过感知与交互模块生成文本对齐的交互动作，音频交互感知生成模块合成生动的交互视频。
- 实验或效果：建立GroundedInter基准，实验表明方法能有效生成人-物交互的说话头像视频。

## 摘要（原文）

> Generating talking avatars is a fundamental task in video generation. Although existing methods can generate full-body talking avatars with simple human motion, extending this task to grounded human-object interaction (GHOI) remains an open challenge, requiring the avatar to perform text-aligned interactions with surrounding objects. This challenge stems from the need for environmental perception and the control-quality dilemma in GHOI generation. To address this, we propose a novel dual-stream framework, InteractAvatar, which decouples perception and planning from video synthesis for grounded human-object interaction. Leveraging detection to enhance environmental perception, we introduce a Perception and Interaction Module (PIM) to generate text-aligned interaction motions. Additionally, an Audio-Interaction Aware Generation Module (AIM) is proposed to synthesize vivid talking avatars performing object interactions. With a specially designed motion-to-video aligner, PIM and AIM share a similar network structure and enable parallel co-generation of motions and plausible videos, effectively mitigating the control-quality dilemma. Finally, we establish a benchmark, GroundedInter, for evaluating GHOI video generation. Extensive experiments and comparisons demonstrate the effectiveness of our method in generating grounded human-object interactions for talking avatars. Project page: https://interactavatar.github.io

