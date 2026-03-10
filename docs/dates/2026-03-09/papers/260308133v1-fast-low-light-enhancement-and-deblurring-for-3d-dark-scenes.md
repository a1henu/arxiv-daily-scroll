---
layout: default
title: Fast Low-light Enhancement and Deblurring for 3D Dark Scenes
---

# Fast Low-light Enhancement and Deblurring for 3D Dark Scenes
**arXiv**：[2603.08133v1](https://arxiv.org/abs/2603.08133) · [PDF](https://arxiv.org/pdf/2603.08133.pdf)  
**作者**：Feng Zhang, Jinglong Wang, Ze Li, Yanghong Zhou, Yang Chen, Lei Chen, Xiatian Zhu  

**一句话要点**：提出FLED-GS框架，通过交替增强与重建快速恢复低光模糊3D场景

**关键词**：低光增强, 3D场景重建, 去模糊, 高斯溅射, 新视角合成, 噪声抑制

## 3 点简述
- 核心问题：现有方法难以处理低光、噪声和运动模糊的复合退化，影响新视角合成质量
- 方法要点：采用渐进恢复策略，插入亮度锚点，结合2D去模糊和噪声感知3D高斯重建交替优化
- 实验或效果：相比LuSh-NeRF，训练速度提升21倍，渲染速度提升11倍，性能更优

## 摘要（原文）

> Novel view synthesis from low-light, noisy, and motion-blurred imagery remains a valuable and challenging task. Current volumetric rendering methods struggle with compound degradation, and sequential 2D preprocessing introduces artifacts due to interdependencies. In this work, we introduce FLED-GS, a fast low-light enhancement and deblurring framework that reformulates 3D scene restoration as an alternating cycle of enhancement and reconstruction. Specifically, FLED-GS inserts several intermediate brightness anchors to enable progressive recovery, preventing noise blow-up from harming deblurring or geometry. Each iteration sharpens inputs with an off-the-shelf 2D deblurrer and then performs noise-aware 3DGS reconstruction that estimates and suppresses noise while producing clean priors for the next level. Experiments show FLED-GS outperforms state-of-the-art LuSh-NeRF, achieving 21$\times$ faster training and 11$\times$ faster rendering.

