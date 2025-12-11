---
layout: default
title: H2R-Grounder: A Paired-Data-Free Paradigm for Translating Human Interaction Videos into Physically Grounded Robot Videos
---

# H2R-Grounder: A Paired-Data-Free Paradigm for Translating Human Interaction Videos into Physically Grounded Robot Videos
**arXiv**：[2512.09406v1](https://arxiv.org/abs/2512.09406) · [PDF](https://arxiv.org/pdf/2512.09406.pdf)  
**作者**：Hai Ci, Xiaokang Liu, Pei Yang, Yiren Song, Mike Zheng Shou  

**一句话要点**：提出H2R-Grounder框架，将人类交互视频转换为物理真实的机器人视频，无需配对数据训练。

**关键词**：视频到视频翻译, 机器人学习, 物理基础交互, 无配对数据训练, 视频扩散模型, 人类-机器人交互

## 3 点简述
- 核心问题：从人类视频学习机器人操作技能，但缺乏配对数据导致训练困难。
- 方法要点：通过可转移表示（如修复背景和叠加视觉提示），利用视频扩散模型生成运动一致的机器人视频。
- 实验或效果：相比基线，生成更真实和物理基础的机器人动作，验证了从无标签人类视频扩展机器人学习的潜力。

## 摘要（原文）

> Robots that learn manipulation skills from everyday human videos could acquire broad capabilities without tedious robot data collection. We propose a video-to-video translation framework that converts ordinary human-object interaction videos into motion-consistent robot manipulation videos with realistic, physically grounded interactions. Our approach does not require any paired human-robot videos for training only a set of unpaired robot videos, making the system easy to scale. We introduce a transferable representation that bridges the embodiment gap: by inpainting the robot arm in training videos to obtain a clean background and overlaying a simple visual cue (a marker and arrow indicating the gripper's position and orientation), we can condition a generative model to insert the robot arm back into the scene. At test time, we apply the same process to human videos (inpainting the person and overlaying human pose cues) and generate high-quality robot videos that mimic the human's actions. We fine-tune a SOTA video diffusion model (Wan 2.2) in an in-context learning manner to ensure temporal coherence and leveraging of its rich prior knowledge. Empirical results demonstrate that our approach achieves significantly more realistic and grounded robot motions compared to baselines, pointing to a promising direction for scaling up robot learning from unlabeled human videos. Project page: https://showlab.github.io/H2R-Grounder/

