---
layout: default
title: X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale
---

# X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale
**arXiv**：[2512.04537v1](https://arxiv.org/abs/2512.04537) · [PDF](https://arxiv.org/pdf/2512.04537.pdf)  
**作者**：Pei Yang, Hai Ci, Yiren Song, Mike Zheng Shou  

**一句话要点**：提出X-Humanoid方法，通过视频编辑将人类视频转换为大规模人形机器人视频以解决数据稀缺问题。

**关键词**：视频生成, 人形机器人, 数据增强, 视频编辑, 具身AI

## 3 点简述
- 核心问题：具身AI发展中，大规模多样化训练数据稀缺，现有方法难以处理复杂全身运动和遮挡。
- 方法要点：基于Wan 2.2模型构建视频到视频结构，微调用于人类到人形机器人转换，并设计可扩展数据创建管道。
- 实验或效果：生成超过360万帧机器人化视频，用户研究显示在运动一致性和体现正确性上优于基线。

## 摘要（原文）

> The advancement of embodied AI has unlocked significant potential for intelligent humanoid robots. However, progress in both Vision-Language-Action (VLA) models and world models is severely hampered by the scarcity of large-scale, diverse training data. A promising solution is to "robotize" web-scale human videos, which has been proven effective for policy training. However, these solutions mainly "overlay" robot arms to egocentric videos, which cannot handle complex full-body motions and scene occlusions in third-person videos, making them unsuitable for robotizing humans. To bridge this gap, we introduce X-Humanoid, a generative video editing approach that adapts the powerful Wan 2.2 model into a video-to-video structure and finetunes it for the human-to-humanoid translation task. This finetuning requires paired human-humanoid videos, so we designed a scalable data creation pipeline, turning community assets into 17+ hours of paired synthetic videos using Unreal Engine. We then apply our trained model to 60 hours of the Ego-Exo4D videos, generating and releasing a new large-scale dataset of over 3.6 million "robotized" humanoid video frames. Quantitative analysis and user studies confirm our method's superiority over existing baselines: 69% of users rated it best for motion consistency, and 62.1% for embodiment correctness.

