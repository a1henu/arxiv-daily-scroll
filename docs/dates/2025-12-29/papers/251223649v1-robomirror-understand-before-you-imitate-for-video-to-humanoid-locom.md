---
layout: default
title: RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion
---

# RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion
**arXiv**：[2512.23649v1](https://arxiv.org/abs/2512.23649) · [PDF](https://arxiv.org/pdf/2512.23649.pdf)  
**作者**：Zhe Li, Cheng Chi, Yangyang Wei, Boan Zhu, Tao Huang, Zhenguo Sun, Yibo Peng, Pengwei Wang, Zhongyuan Wang, Fangzhou Liu, Chang Xu, Shanghang Zhang  

**一句话要点**：提出RoboMirror框架，通过视觉理解实现视频到人形机器人运动控制，无需重定向。

**关键词**：视频到运动控制, 视觉语言模型, 扩散策略, 人形机器人, 运动意图提取

## 3 点简述
- 问题：现有方法依赖运动捕捉或文本命令，缺乏视觉理解与控制的直接桥梁。
- 方法：利用视觉语言模型从视频提取运动意图，基于扩散策略生成物理合理运动。
- 效果：实验显示降低控制延迟80%，任务成功率提升3.7%，支持第一人称视频远程控制。

## 摘要（原文）

> Humans learn locomotion through visual observation, interpreting visual content first before imitating actions. However, state-of-the-art humanoid locomotion systems rely on either curated motion capture trajectories or sparse text commands, leaving a critical gap between visual understanding and control. Text-to-motion methods suffer from semantic sparsity and staged pipeline errors, while video-based approaches only perform mechanical pose mimicry without genuine visual understanding. We propose RoboMirror, the first retargeting-free video-to-locomotion framework embodying "understand before you imitate". Leveraging VLMs, it distills raw egocentric/third-person videos into visual motion intents, which directly condition a diffusion-based policy to generate physically plausible, semantically aligned locomotion without explicit pose reconstruction or retargeting. Extensive experiments validate the effectiveness of RoboMirror, it enables telepresence via egocentric videos, drastically reduces third-person control latency by 80%, and achieves a 3.7% higher task success rate than baselines. By reframing humanoid control around video understanding, we bridge the visual understanding and action gap.

