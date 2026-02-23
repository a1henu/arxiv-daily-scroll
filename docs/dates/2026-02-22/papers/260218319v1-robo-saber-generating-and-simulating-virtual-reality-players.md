---
layout: default
title: Robo-Saber: Generating and Simulating Virtual Reality Players
---

# Robo-Saber: Generating and Simulating Virtual Reality Players
**arXiv**：[2602.18319v1](https://arxiv.org/abs/2602.18319) · [PDF](https://arxiv.org/pdf/2602.18319.pdf)  
**作者**：Nam Hee Kim, Jingjing May Liu, Jaakko Lehtinen, Perttu Hämäläinen, James F. O'Brien, Xue Bin Peng  

**一句话要点**：提出首个虚拟现实游戏玩家运动生成系统，用于基于物理的全身VR游戏测试。

**关键词**：虚拟现实游戏测试, 运动生成, 玩家建模, 物理模拟, 风格引导

## 3 点简述
- 核心问题：缺乏从游戏对象布局生成VR头显和手持控制器运动的系统，以支持游戏测试。
- 方法要点：利用风格示例引导，训练模型从BOXRR-23数据集学习，优化模拟游戏得分。
- 实验或效果：在Beat Saber游戏中验证，模型能生成熟练游戏玩法并捕捉多样玩家行为。

## 摘要（原文）

> We present the first motion generation system for playtesting virtual reality (VR) games. Our player model generates VR headset and handheld controller movements from in-game object arrangements, guided by style exemplars and aligned to maximize simulated gameplay score. We train on the large BOXRR-23 dataset and apply our framework on the popular VR game Beat Saber. The resulting model Robo-Saber produces skilled gameplay and captures diverse player behaviors, mirroring the skill levels and movement patterns specified by input style exemplars. Robo-Saber demonstrates promise in synthesizing rich gameplay data for predictive applications and enabling a physics-based whole-body VR playtesting agent.

