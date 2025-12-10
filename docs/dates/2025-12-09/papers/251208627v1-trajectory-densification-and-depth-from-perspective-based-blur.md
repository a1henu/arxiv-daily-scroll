---
layout: default
title: Trajectory Densification and Depth from Perspective-based Blur
---

# Trajectory Densification and Depth from Perspective-based Blur
**arXiv**：[2512.08627v1](https://arxiv.org/abs/2512.08627) · [PDF](https://arxiv.org/pdf/2512.08627.pdf)  
**作者**：Tianchen Qiu, Qirun Zhang, Jiajian He, Zhengyue Zhuge, Jiahui Xu, Yueting Chen  

**一句话要点**：提出基于透视模糊的深度估计与轨迹稠密化方法，用于手持长曝光视频场景。

**关键词**：深度估计, 透视模糊, 轨迹稠密化, 手持视频, 视觉语言模型, 多窗口聚合

## 3 点简述
- 核心问题：手持相机旋转导致透视模糊，其程度依赖物体深度，影响视频质量与深度估计。
- 方法要点：结合视觉编码器与点跟踪器提取信息，通过窗口嵌入和多窗口聚合估计深度图，并利用视觉语言模型稠密化稀疏轨迹。
- 实验或效果：在多个深度数据集上表现优异，泛化能力强，轨迹重建精度高，优于真实手持拍摄轨迹。

## 摘要（原文）

> In the absence of a mechanical stabilizer, the camera undergoes inevitable rotational dynamics during capturing, which induces perspective-based blur especially under long-exposure scenarios. From an optical standpoint, perspective-based blur is depth-position-dependent: objects residing at distinct spatial locations incur different blur levels even under the same imaging settings. Inspired by this, we propose a novel method that estimate metric depth by examining the blur pattern of a video stream and dense trajectory via joint optical design algorithm. Specifically, we employ off-the-shelf vision encoder and point tracker to extract video information. Then, we estimate depth map via windowed embedding and multi-window aggregation, and densify the sparse trajectory from the optical algorithm using a vision-language model. Evaluations on multiple depth datasets demonstrate that our method attains strong performance over large depth range, while maintaining favorable generalization. Relative to the real trajectory in handheld shooting settings, our optical algorithm achieves superior precision and the dense reconstruction maintains strong accuracy.

