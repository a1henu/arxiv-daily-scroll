---
layout: default
title: Coded-E2LF: Coded Aperture Light Field Imaging from Events
---

# Coded-E2LF: Coded Aperture Light Field Imaging from Events
**arXiv**：[2602.22620v1](https://arxiv.org/abs/2602.22620) · [PDF](https://arxiv.org/pdf/2602.22620.pdf)  
**作者**：Tomoya Tsuchida, Keita Takahashi, Chihiro Tsutake, Toshiaki Fujii, Hajime Nagahara  

**一句话要点**：提出Coded-E2LF方法，利用编码孔径和事件相机重建4D光场

**关键词**：事件相机, 光场成像, 编码孔径, 计算成像, 4D重建

## 3 点简述
- 核心问题：如何仅用事件相机获取高精度4D光场，简化硬件限制
- 方法要点：采用编码孔径，理论分析黑色图案作用，纯事件驱动重建
- 实验或效果：硬件实现验证，首次展示像素级精度光场重建

## 摘要（原文）

> We propose Coded-E2LF (coded event to light field), a computational imaging method for acquiring a 4-D light field using a coded aperture and a stationary event-only camera. In a previous work, an imaging system similar to ours was adopted, but both events and intensity images were captured and used for light field reconstruction. In contrast, our method is purely event-based, which relaxes restrictions for hardware implementation. We also introduce several advancements from the previous work that enable us to theoretically support and practically improve light field reconstruction from events alone. In particular, we clarify the key role of a black pattern in aperture coding patterns. We finally implemented our method on real imaging hardware to demonstrate its effectiveness in capturing real 3-D scenes. To the best of our knowledge, we are the first to demonstrate that a 4-D light field with pixel-level accuracy can be reconstructed from events alone. Our software and supplementary video are available from our project website.

