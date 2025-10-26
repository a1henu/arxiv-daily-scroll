---
layout: default
title: PPMStereo: Pick-and-Play Memory Construction for Consistent Dynamic Stereo Matching
---

# PPMStereo: Pick-and-Play Memory Construction for Consistent Dynamic Stereo Matching
**arXiv**：[2510.20178v1](https://arxiv.org/abs/2510.20178) · [PDF](https://arxiv.org/pdf/2510.20178.pdf)  
**作者**：Yun Wang, Junjie Hu, Qiaole Dong, Yongjian Zhang, Yanwei Fu, Tin Lun Lam, Dapeng Wu  

**一句话要点**：提出PPMStereo方法以解决立体视频中长时深度估计一致性问题

**关键词**：立体匹配, 时间一致性, 动态视频, 内存缓冲, 时空聚合, 深度估计

## 3 点简述
- 立体视频深度估计中，长时时间一致性建模困难且计算成本高
- 采用Pick-and-Play内存模块，选择相关帧并自适应加权聚合时空信息
- 实验显示在Sintel数据集上精度和一致性领先，计算成本较低

## 摘要（原文）

> Temporally consistent depth estimation from stereo video is critical for
> real-world applications such as augmented reality, where inconsistent depth
> estimation disrupts the immersion of users. Despite its importance, this task
> remains challenging due to the difficulty in modeling long-term temporal
> consistency in a computationally efficient manner. Previous methods attempt to
> address this by aggregating spatio-temporal information but face a fundamental
> trade-off: limited temporal modeling provides only modest gains, whereas
> capturing long-range dependencies significantly increases computational cost.
> To address this limitation, we introduce a memory buffer for modeling
> long-range spatio-temporal consistency while achieving efficient dynamic stereo
> matching. Inspired by the two-stage decision-making process in humans, we
> propose a \textbf{P}ick-and-\textbf{P}lay \textbf{M}emory (PPM) construction
> module for dynamic \textbf{Stereo} matching, dubbed as \textbf{PPMStereo}. PPM
> consists of a `pick' process that identifies the most relevant frames and a
> `play' process that weights the selected frames adaptively for spatio-temporal
> aggregation. This two-stage collaborative process maintains a compact yet
> highly informative memory buffer while achieving temporally consistent
> information aggregation. Extensive experiments validate the effectiveness of
> PPMStereo, demonstrating state-of-the-art performance in both accuracy and
> temporal consistency. % Notably, PPMStereo achieves 0.62/1.11 TEPE on the
> Sintel clean/final (17.3\% \& 9.02\% improvements over BiDAStereo) with fewer
> computational costs. Codes are available at
> \textcolor{blue}{https://github.com/cocowy1/PPMStereo}.

