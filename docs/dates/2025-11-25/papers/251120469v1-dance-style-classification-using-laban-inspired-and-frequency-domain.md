---
layout: default
title: Dance Style Classification using Laban-Inspired and Frequency-Domain Motion Features
---

# Dance Style Classification using Laban-Inspired and Frequency-Domain Motion Features
**arXiv**：[2511.20469v1](https://arxiv.org/abs/2511.20469) · [PDF](https://arxiv.org/pdf/2511.20469.pdf)  
**作者**：Ben Hamscher, Arnold Brosch, Nicolas Binninger, Maksymilian Jan Dejna, Kira Maag  

**一句话要点**：提出基于Laban分析和频域特征的轻量框架以解决舞蹈风格分类问题

**关键词**：舞蹈风格分类, Laban运动分析, 频域特征, 轻量框架, 姿态估计

## 3 点简述
- 核心问题：舞蹈风格分类因相似姿态和运动模式而复杂，需从视频中识别运动特征。
- 方法要点：结合Laban启发的时空描述符和FFT频域特征，捕捉关节动态和节奏模式。
- 实验或效果：实现鲁棒分类，计算量低，无需复杂模型，可解释性强。

## 摘要（原文）

> Dance is an essential component of human culture and serves as a tool for conveying emotions and telling stories. Identifying and distinguishing dance genres based on motion data is a complex problem in human activity recognition, as many styles share similar poses, gestures, and temporal motion patterns. This work presents a lightweight framework for classifying dance styles that determines motion characteristics based on pose estimates extracted from videos. We propose temporal-spatial descriptors inspired by Laban Movement Analysis. These features capture local joint dynamics such as velocity, acceleration, and angular movement of the upper body, enabling a structured representation of spatial coordination. To further encode rhythmic and periodic aspects of movement, we integrate Fast Fourier Transform features that characterize movement patterns in the frequency domain. The proposed approach achieves robust classification of different dance styles with low computational effort, as complex model architectures are not required, and shows that interpretable motion representations can effectively capture stylistic nuances.

