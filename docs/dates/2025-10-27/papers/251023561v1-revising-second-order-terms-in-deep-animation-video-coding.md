---
layout: default
title: Revising Second Order Terms in Deep Animation Video Coding
---

# Revising Second Order Terms in Deep Animation Video Coding
**arXiv**：[2510.23561v1](https://arxiv.org/abs/2510.23561) · [PDF](https://arxiv.org/pdf/2510.23561.pdf)  
**作者**：Konstantin Schmidt, Thomas Richter  

**一句话要点**：提出全局旋转替换Jacobian变换以改进头部旋转动画视频编码

**关键词**：视频编码, 生成模型, 头部动画, 对抗训练, 比特率优化

## 3 点简述
- 核心问题：一阶运动模型在强头部旋转时生成失败，因依赖图像扭曲
- 方法要点：用全局旋转替换Jacobian变换，并应用归一化技术稳定对抗训练
- 实验或效果：在P帧节省40%-80%比特率，LPIPS和DISTS指标显示优化成功

## 摘要（原文）

> First Order Motion Model is a generative model that animates human heads
> based on very little motion information derived from keypoints. It is a
> promising solution for video communication because first it operates at very
> low bitrate and second its computational complexity is moderate compared to
> other learning based video codecs. However, it has strong limitations by
> design. Since it generates facial animations by warping source-images, it fails
> to recreate videos with strong head movements. This works concentrates on one
> specific kind of head movements, namely head rotations. We show that replacing
> the Jacobian transformations in FOMM by a global rotation helps the system to
> perform better on items with head-rotations while saving 40% to 80% of bitrate
> on P-frames. Moreover, we apply state-of-the-art normalization techniques to
> the discriminator to stabilize the adversarial training which is essential for
> generating visually appealing videos. We evaluate the performance by the
> learned metics LPIPS and DISTS to show the success our optimizations.

