---
layout: default
title: PointMapPolicy: Structured Point Cloud Processing for Multi-Modal Imitation Learning
---

# PointMapPolicy: Structured Point Cloud Processing for Multi-Modal Imitation Learning
**arXiv**：[2510.20406v1](https://arxiv.org/abs/2510.20406) · [PDF](https://arxiv.org/pdf/2510.20406.pdf)  
**作者**：Xiaogang Jia, Qian Wang, Anrui Wang, Han A. Wang, Balázs Gyenes, Emiliyan Gospodinov, Xinkai Jiang, Ge Li, Hongyi Zhou, Weiran Liao, Xi Huang, Maximilian Beck, Moritz Reuss, Rudolf Lioutikov, Gerhard Neumann  

**一句话要点**：提出PointMapPolicy，通过结构化点云处理增强多模态模仿学习性能

**关键词**：点云处理, 多模态模仿学习, 扩散策略, 机器人操作, xLSTM, 3D计算机视觉

## 3 点简述
- 当前点云方法难以捕捉细粒度细节，RGB方法缺乏几何感知，影响机器人操作精度
- 基于xLSTM融合结构化点云与RGB数据，无需下采样，支持3D计算机视觉技术
- 在RoboCasa和CALVIN基准测试及真实机器人评估中，实现先进性能

## 摘要（原文）

> Robotic manipulation systems benefit from complementary sensing modalities,
> where each provides unique environmental information. Point clouds capture
> detailed geometric structure, while RGB images provide rich semantic context.
> Current point cloud methods struggle to capture fine-grained detail, especially
> for complex tasks, which RGB methods lack geometric awareness, which hinders
> their precision and generalization. We introduce PointMapPolicy, a novel
> approach that conditions diffusion policies on structured grids of points
> without downsampling. The resulting data type makes it easier to extract shape
> and spatial relationships from observations, and can be transformed between
> reference frames. Yet due to their structure in a regular grid, we enable the
> use of established computer vision techniques directly to 3D data. Using xLSTM
> as a backbone, our model efficiently fuses the point maps with RGB data for
> enhanced multi-modal perception. Through extensive experiments on the RoboCasa
> and CALVIN benchmarks and real robot evaluations, we demonstrate that our
> method achieves state-of-the-art performance across diverse manipulation tasks.
> The overview and demos are available on our project page:
> https://point-map.github.io/Point-Map/

