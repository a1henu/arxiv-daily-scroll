---
layout: default
title: Do You Have Freestyle? Expressive Humanoid Locomotion via Audio Control
---

# Do You Have Freestyle? Expressive Humanoid Locomotion via Audio Control
**arXiv**：[2512.23650v1](https://arxiv.org/abs/2512.23650) · [PDF](https://arxiv.org/pdf/2512.23650.pdf)  
**作者**：Zhe Li, Cheng Chi, Yangyang Wei, Boan Zhu, Tao Huang, Zhenguo Sun, Yibo Peng, Pengwei Wang, Zhongyuan Wang, Fangzhou Liu, Chang Xu, Shanghang Zhang  

**一句话要点**：提出RoboPerform框架，通过音频直接生成人形机器人舞蹈与手势，无需显式运动重建。

**关键词**：音频驱动运动, 人形机器人控制, 扩散模型, 运动风格迁移, 实时生成

## 3 点简述
- 核心问题：人形机器人缺乏即兴表达能力，现有方法依赖运动重建导致延迟高、误差累积。
- 方法要点：基于“运动=内容+风格”原则，用音频作为隐式风格信号，结合ResMoE教师策略和扩散学生策略。
- 实验或效果：验证显示RoboPerform在物理合理性和音频对齐方面表现良好，实现低延迟高保真。

## 摘要（原文）

> Humans intuitively move to sound, but current humanoid robots lack expressive improvisational capabilities, confined to predefined motions or sparse commands. Generating motion from audio and then retargeting it to robots relies on explicit motion reconstruction, leading to cascaded errors, high latency, and disjointed acoustic-actuation mapping. We propose RoboPerform, the first unified audio-to-locomotion framework that can directly generate music-driven dance and speech-driven co-speech gestures from audio. Guided by the core principle of "motion = content + style", the framework treats audio as implicit style signals and eliminates the need for explicit motion reconstruction. RoboPerform integrates a ResMoE teacher policy for adapting to diverse motion patterns and a diffusion-based student policy for audio style injection. This retargeting-free design ensures low latency and high fidelity. Experimental validation shows that RoboPerform achieves promising results in physical plausibility and audio alignment, successfully transforming robots into responsive performers capable of reacting to audio.

