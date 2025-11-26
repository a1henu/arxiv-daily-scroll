---
layout: default
title: MotionV2V: Editing Motion in a Video
---

# MotionV2V: Editing Motion in a Video
**arXiv**：[2511.20640v1](https://arxiv.org/abs/2511.20640) · [PDF](https://arxiv.org/pdf/2511.20640.pdf)  
**作者**：Ryan Burgert, Charles Herrmann, Forrester Cole, Michael S Ryoo, Neal Wadhwa, Andrey Voynov, Nataniel Ruiz  

**一句话要点**：提出MotionV2V方法，通过编辑稀疏轨迹实现视频运动编辑

**关键词**：视频运动编辑, 稀疏轨迹编辑, 运动反事实生成, 视频扩散模型, 用户偏好研究

## 3 点简述
- 核心问题：现有视频编辑方法难以实现精确运动控制
- 方法要点：提取并编辑输入视频的稀疏轨迹，结合生成模型生成运动反事实视频对
- 实验或效果：用户研究中偏好率超65%，支持任意时间戳编辑和自然传播

## 摘要（原文）

> While generative video models have achieved remarkable fidelity and consistency, applying these capabilities to video editing remains a complex challenge. Recent research has explored motion controllability as a means to enhance text-to-video generation or image animation; however, we identify precise motion control as a promising yet under-explored paradigm for editing existing videos. In this work, we propose modifying video motion by directly editing sparse trajectories extracted from the input. We term the deviation between input and output trajectories a "motion edit" and demonstrate that this representation, when coupled with a generative backbone, enables powerful video editing capabilities. To achieve this, we introduce a pipeline for generating "motion counterfactuals", video pairs that share identical content but distinct motion, and we fine-tune a motion-conditioned video diffusion architecture on this dataset. Our approach allows for edits that start at any timestamp and propagate naturally. In a four-way head-to-head user study, our model achieves over 65 percent preference against prior work. Please see our project page: https://ryanndagreat.github.io/MotionV2V

