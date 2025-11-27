---
layout: default
title: Seeing without Pixels: Perception from Camera Trajectories
---

# Seeing without Pixels: Perception from Camera Trajectories
**arXiv**：[2511.21681v1](https://arxiv.org/abs/2511.21681) · [PDF](https://arxiv.org/pdf/2511.21681.pdf)  
**作者**：Zihui Xue, Kristen Grauman, Dima Damen, Andrew Zisserman, Tengda Han  

**一句话要点**：提出CamFormer框架，利用相机轨迹感知视频内容，无需像素信息。

**关键词**：相机轨迹感知, 对比学习, 视频内容理解, 跨模态对齐, 鲁棒表示学习

## 3 点简述
- 核心问题：仅从相机轨迹能否感知视频内容，挑战传统像素依赖。
- 方法要点：采用对比学习，将相机轨迹与自然语言对齐于嵌入空间。
- 实验或效果：在跨模态对齐、分类等任务中验证轨迹信息的鲁棒性和通用性。

## 摘要（原文）

> Can one perceive a video's content without seeing its pixels, just from the camera trajectory-the path it carves through space? This paper is the first to systematically investigate this seemingly implausible question. Towards this end, we propose a contrastive learning framework to train CamFormer, a dedicated encoder that projects camera pose trajectories into a joint embedding space, aligning them with natural language. We find that, contrary to its apparent simplicity, the camera trajectory is a remarkably informative signal to uncover video content. In other words, "how you move" can indeed reveal "what you are doing" (egocentric) or "observing" (exocentric). We demonstrate the versatility of our learned CamFormer embeddings on a diverse suite of downstream tasks, ranging from cross-modal alignment to classification and temporal analysis. Importantly, our representations are robust across diverse camera pose estimation methods, including both high-fidelity multi-sensored and standard RGB-only estimators. Our findings establish camera trajectory as a lightweight, robust, and versatile modality for perceiving video content.

