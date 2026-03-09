---
layout: default
title: Text-Driven Emotionally Continuous Talking Face Generation
---

# Text-Driven Emotionally Continuous Talking Face Generation
**arXiv**：[2603.06071v1](https://arxiv.org/abs/2603.06071) · [PDF](https://arxiv.org/pdf/2603.06071.pdf)  
**作者**：Hao Yang, Yanyan Zhao, Tian Zheng, Hongbo Zhang, Bichen Wang, Di Wu, Xing Fu, Xuda Zhi, Yongbo Huang, Hao He  

**一句话要点**：提出TIE-TFG模型以解决文本驱动下情感连续变化的人脸生成问题

**关键词**：情感连续人脸生成, 时序密集情感建模, 文本驱动合成, 动态表情变化, 视频生成质量

## 3 点简述
- 核心问题：现有TFG方法生成视频情感固定，缺乏人类表达时的连续自然变化
- 方法要点：采用时序密集情感波动建模，根据输入文本生成情感变化序列驱动面部表情
- 实验或效果：评估显示能产生平滑情感过渡，并在多样情感状态下保持高质量视觉和运动真实性

## 摘要（原文）

> Talking Face Generation (TFG) strives to create realistic and emotionally expressive digital faces. While previous TFG works have mastered the creation of naturalistic facial movements, they typically express a fixed target emotion in synthetic videos and lack the ability to exhibit continuously changing and natural expressions like humans do when conveying information. To synthesize realistic videos, we propose a novel task called Emotionally Continuous Talking Face Generation (EC-TFG), which takes a text segment and an emotion description with varying emotions as driving data, aiming to generate a video where the person speaks the text while reflecting the emotional changes within the description. Alongside this, we introduce a customized model, i.e., Temporal-Intensive Emotion Modulated Talking Face Generation (TIE-TFG), which innovatively manages dynamic emotional variations by employing Temporal-Intensive Emotion Fluctuation Modeling, allowing it to provide emotion variation sequences corresponding to the input text to drive continuous facial expression changes in synthesized videos. Extensive evaluations demonstrate our method's exceptional ability to produce smooth emotion transitions and uphold high-quality visuals and motion authenticity across diverse emotional states.

