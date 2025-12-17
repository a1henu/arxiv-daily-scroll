---
layout: default
title: VASA-3D: Lifelike Audio-Driven Gaussian Head Avatars from a Single Image
---

# VASA-3D: Lifelike Audio-Driven Gaussian Head Avatars from a Single Image
**arXiv**：[2512.14677v1](https://arxiv.org/abs/2512.14677) · [PDF](https://arxiv.org/pdf/2512.14677.pdf)  
**作者**：Sicheng Xu, Guojun Chen, Jiaolong Yang, Yizhong Zhang, Yu Deng, Steve Lin, Baining Guo  

**一句话要点**：提出VASA-3D，从单张图像生成音频驱动的逼真3D头部化身，解决表情细节建模和单图重建挑战。

**关键词**：音频驱动生成, 3D头部化身, 单图像重建, 表情建模, 优化框架, 自由视角视频

## 3 点简述
- 核心问题：从单张肖像图像重建复杂3D头部化身，并捕捉真实人脸中的细微表情细节。
- 方法要点：利用VASA-1的运动潜变量，设计基于该潜变量的3D头部模型，通过优化框架实现单图像定制。
- 实验或效果：生成逼真3D说话头部，支持在线生成512x512自由视角视频，最高75 FPS，提升沉浸感。

## 摘要（原文）

> We propose VASA-3D, an audio-driven, single-shot 3D head avatar generator. This research tackles two major challenges: capturing the subtle expression details present in real human faces, and reconstructing an intricate 3D head avatar from a single portrait image. To accurately model expression details, VASA-3D leverages the motion latent of VASA-1, a method that yields exceptional realism and vividness in 2D talking heads. A critical element of our work is translating this motion latent to 3D, which is accomplished by devising a 3D head model that is conditioned on the motion latent. Customization of this model to a single image is achieved through an optimization framework that employs numerous video frames of the reference head synthesized from the input image. The optimization takes various training losses robust to artifacts and limited pose coverage in the generated training data. Our experiment shows that VASA-3D produces realistic 3D talking heads that cannot be achieved by prior art, and it supports the online generation of 512x512 free-viewpoint videos at up to 75 FPS, facilitating more immersive engagements with lifelike 3D avatars.

