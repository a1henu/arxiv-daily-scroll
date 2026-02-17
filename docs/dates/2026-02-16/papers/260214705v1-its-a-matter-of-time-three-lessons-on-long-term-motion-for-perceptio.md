---
layout: default
title: It's a Matter of Time: Three Lessons on Long-Term Motion for Perception
---

# It's a Matter of Time: Three Lessons on Long-Term Motion for Perception
**arXiv**：[2602.14705v1](https://arxiv.org/abs/2602.14705) · [PDF](https://arxiv.org/pdf/2602.14705.pdf)  
**作者**：Willem Davison, Xinyue Hao, Laura Sevilla-Lara  

**一句话要点**：利用长时运动信息提升感知任务性能，揭示其在动作、物体和材料理解中的优势。

**关键词**：长时运动表示, 点轨迹估计, 感知任务, 零样本学习, 计算效率

## 3 点简述
- 核心问题：长时运动信息在感知任务中的作用和特性尚不明确，需探索其学习潜力。
- 方法要点：基于点轨迹估计技术，构建长时运动表示，应用于多种感知任务进行实验验证。
- 实验或效果：长时运动表示在低数据设置和零样本任务中泛化能力更强，且计算效率优于标准视频表示。

## 摘要（原文）

> Temporal information has long been considered to be essential for perception. While there is extensive research on the role of image information for perceptual tasks, the role of the temporal dimension remains less well understood: What can we learn about the world from long-term motion information? What properties does long-term motion information have for visual learning? We leverage recent success in point-track estimation, which offers an excellent opportunity to learn temporal representations and experiment on a variety of perceptual tasks. We draw 3 clear lessons: 1) Long-term motion representations contain information to understand actions, but also objects, materials, and spatial information, often even better than images. 2) Long-term motion representations generalize far better than image representations in low-data settings and in zero-shot tasks. 3) The very low dimensionality of motion information makes motion representations a better trade-off between GFLOPs and accuracy than standard video representations, and used together they achieve higher performance than video representations alone. We hope these insights will pave the way for the design of future models that leverage the power of long-term motion information for perception.

