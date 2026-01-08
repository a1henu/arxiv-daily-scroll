---
layout: default
title: TRec: Egocentric Action Recognition using 2D Point Tracks
---

# TRec: Egocentric Action Recognition using 2D Point Tracks
**arXiv**：[2601.03667v1](https://arxiv.org/abs/2601.03667) · [PDF](https://arxiv.org/pdf/2601.03667.pdf)  
**作者**：Dennis Holzmann, Sven Wachsmuth  

**一句话要点**：提出TRec方法，利用2D点轨迹增强第一人称动作识别性能

**关键词**：第一人称动作识别, 2D点轨迹, Transformer模型, 运动线索, 轻量级表示

## 3 点简述
- 核心问题：现有第一人称动作识别方法依赖RGB外观或姿态估计，缺乏有效运动线索
- 方法要点：使用CoTracker随机采样并跟踪图像点，结合Transformer模型处理轨迹和帧
- 实验或效果：仅用初始帧和点轨迹即可提升识别准确率，验证了运动信息的有效性

## 摘要（原文）

> We present a novel approach for egocentric action recognition that leverages 2D point tracks as an additional motion cue. While most existing methods rely on RGB appearance, human pose estimation, or their combination, our work demonstrates that tracking randomly sampled image points across video frames can substantially improve recognition accuracy. Unlike prior approaches, we do not detect hands, objects, or interaction regions. Instead, we employ CoTracker to follow a set of randomly initialized points through each video and use the resulting trajectories, together with the corresponding image frames, as input to a Transformer-based recognition model. Surprisingly, our method achieves notable gains even when only the initial frame and its associated point tracks are provided, without incorporating the full video sequence. Experimental results confirm that integrating 2D point tracks consistently enhances performance compared to the same model trained without motion information, highlighting their potential as a lightweight yet effective representation for egocentric action understanding.

