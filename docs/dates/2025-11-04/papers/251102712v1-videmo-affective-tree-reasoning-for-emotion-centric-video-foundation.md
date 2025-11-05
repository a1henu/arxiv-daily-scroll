---
layout: default
title: VidEmo: Affective-Tree Reasoning for Emotion-Centric Video Foundation Models
---

# VidEmo: Affective-Tree Reasoning for Emotion-Centric Video Foundation Models
**arXiv**：[2511.02712v1](https://arxiv.org/abs/2511.02712) · [PDF](https://arxiv.org/pdf/2511.02712.pdf)  
**作者**：Zhicheng Zhang, Weicheng Wang, Yongjie Zhu, Wenyu Qin, Pengfei Wan, Di Zhang, Jufeng Yang  

**一句话要点**：提出VidEmo框架以解决视频中动态情感理解难题

**关键词**：视频情感理解, 情感树推理, 指令微调, 情感数据集, 强化学习, 基础模型

## 3 点简述
- 核心问题：视频情感动态且依赖线索，难以理解复杂情感状态。
- 方法要点：采用情感线索引导推理，结合属性感知和情感树强化学习。
- 实验或效果：在15项人脸感知任务中表现优异，设立新里程碑。

## 摘要（原文）

> Understanding and predicting emotion from videos has gathered significant
> attention in recent studies, driven by advancements in video large language
> models (VideoLLMs). While advanced methods have made progress in video emotion
> analysis, the intrinsic nature of emotions poses significant challenges.
> Emotions are characterized by dynamic and cues-dependent properties, making it
> difficult to understand complex and evolving emotional states with reasonable
> rationale. To tackle these challenges, we propose a novel affective cues-guided
> reasoning framework that unifies fundamental attribute perception, expression
> analysis, and high-level emotional understanding in a stage-wise manner. At the
> core of our approach is a family of video emotion foundation models (VidEmo),
> specifically designed for emotion reasoning and instruction-following. These
> models undergo a two-stage tuning process: first, curriculum emotion learning
> for injecting emotion knowledge, followed by affective-tree reinforcement
> learning for emotion reasoning. Moreover, we establish a foundational data
> infrastructure and introduce a emotion-centric fine-grained dataset (Emo-CFG)
> consisting of 2.1M diverse instruction-based samples. Emo-CFG includes
> explainable emotional question-answering, fine-grained captions, and associated
> rationales, providing essential resources for advancing emotion understanding
> tasks. Experimental results demonstrate that our approach achieves competitive
> performance, setting a new milestone across 15 face perception tasks.

