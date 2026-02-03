---
layout: default
title: Combined Flicker-banding and Moire Removal for Screen-Captured Images
---

# Combined Flicker-banding and Moire Removal for Screen-Captured Images
**arXiv**：[2602.01559v1](https://arxiv.org/abs/2602.01559) · [PDF](https://arxiv.org/pdf/2602.01559.pdf)  
**作者**：Libo Zhu, Zihan Zhou, Zhiyi Zhou, Yiyang Qu, Weihang Zhang, Keyu Shi, Yifan Fu, Yulun Zhang  

**一句话要点**：提出CLEAR框架以联合去除屏幕捕获图像中的摩尔纹和闪烁带

**关键词**：图像恢复, 摩尔纹去除, 闪烁带去除, 复合伪影, 频率域处理, 数据集构建

## 3 点简述
- 核心问题：屏幕捕获图像中摩尔纹和闪烁带共存导致严重视觉退化，现有单退化方法失效。
- 方法要点：设计频率域分解重组模块和轨迹对齐损失，增强复合伪影建模。
- 实验或效果：构建大规模数据集，引入ISP模拟管道，实验显示方法在多项指标上优于现有方法。

## 摘要（原文）

> Capturing display screens with mobile devices has become increasingly common, yet the resulting images often suffer from severe degradations caused by the coexistence of moiré patterns and flicker-banding, leading to significant visual quality degradation. Due to the strong coupling of these two artifacts in real imaging processes, existing methods designed for single degradations fail to generalize to such compound scenarios. In this paper, we present the first systematic study on joint removal of moiré patterns and flicker-banding in screen-captured images, and propose a unified restoration framework, named CLEAR. To support this task, we construct a large-scale dataset containing both moiré patterns and flicker-banding, and introduce an ISP-based flicker simulation pipeline to stabilize model training and expand the degradation distribution. Furthermore, we design a frequency-domain decomposition and re-composition module together with a trajectory alignment loss to enhance the modeling of compound artifacts. Extensive experiments demonstrate that the proposed method consistently. outperforms existing image restoration approaches across multiple evaluation metrics, validating its effectiveness in complex real-world scenarios.

