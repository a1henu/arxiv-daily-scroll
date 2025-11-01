---
layout: default
title: Which Way Does Time Flow? A Psychophysics-Grounded Evaluation for Vision-Language Models
---

# Which Way Does Time Flow? A Psychophysics-Grounded Evaluation for Vision-Language Models
**arXiv**：[2510.26241v1](https://arxiv.org/abs/2510.26241) · [PDF](https://arxiv.org/pdf/2510.26241.pdf)  
**作者**：Shiho Matta, Lis Kanashiro Pereira, Peitao Han, Fei Cheng, Shigeru Kitazawa  

**一句话要点**：提出AoT-PsyPhyBENCH基准以评估视觉语言模型的时间方向判断能力

**关键词**：视觉语言模型, 时间方向判断, 心理物理学基准, 视频理解, 因果推理, 模型评估

## 3 点简述
- 核心问题：视觉语言模型对视频中时间信息的理解不足，缺乏系统评估。
- 方法要点：基于心理物理学设计基准，测试模型判断视频正向或反向播放的能力。
- 实验或效果：多数模型表现接近随机，远低于人类在物理不可逆和因果动作任务上的准确率。

## 摘要（原文）

> Modern vision-language models (VLMs) excel at many multimodal tasks, yet
> their grasp of temporal information in video remains weak and, crucially,
> under-evaluated. We probe this gap with a deceptively simple but revealing
> challenge: judging the arrow of time (AoT)-whether a short clip is played
> forward or backward. We introduce AoT-PsyPhyBENCH, a psychophysically validated
> benchmark that tests whether VLMs can infer temporal direction in natural
> videos using the same stimuli and behavioral baselines established for humans.
> Our comprehensive evaluation of open-weight and proprietary, reasoning and
> non-reasoning VLMs reveals that most models perform near chance, and even the
> best lag far behind human accuracy on physically irreversible processes (e.g.,
> free fall, diffusion/explosion) and causal manual actions (division/addition)
> that humans recognize almost instantly. These results highlight a fundamental
> gap in current multimodal systems: while they capture rich visual-semantic
> correlations, they lack the inductive biases required for temporal continuity
> and causal understanding. We release the code and data for AoT-PsyPhyBENCH to
> encourage further progress in the physical and temporal reasoning capabilities
> of VLMs.

