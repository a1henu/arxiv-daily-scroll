---
layout: default
title: PlanarTrack: A high-quality and challenging benchmark for large-scale planar object tracking
---

# PlanarTrack: A high-quality and challenging benchmark for large-scale planar object tracking
**arXiv**：[2510.23368v1](https://arxiv.org/abs/2510.23368) · [PDF](https://arxiv.org/pdf/2510.23368.pdf)  
**作者**：Yifan Jiao, Xinran Liu, Xiaoqiong Liu, Xiaohui Yuan, Heng Fan, Libo Zhang  

**一句话要点**：提出PlanarTrack基准以解决平面跟踪缺乏大规模平台的问题

**关键词**：平面目标跟踪, 大规模基准数据集, 长短期跟踪评估, 真实世界应用, 手动标注质量

## 3 点简述
- 平面跟踪在机器人和增强现实中应用广泛，但缺乏大规模数据集限制发展
- 构建包含1150个序列、733K帧的大规模高质量基准，支持短长期跟踪评估
- 评估10种现有方法，显示性能显著下降，表明需进一步改进平面跟踪技术

## 摘要（原文）

> Planar tracking has drawn increasing interest owing to its key roles in
> robotics and augmented reality. Despite recent great advancement, further
> development of planar tracking, particularly in the deep learning era, is
> largely limited compared to generic tracking due to the lack of large-scale
> platforms. To mitigate this, we propose PlanarTrack, a large-scale high-quality
> and challenging benchmark for planar tracking. Specifically, PlanarTrack
> consists of 1,150 sequences with over 733K frames, including 1,000 short-term
> and 150 new long-term videos, which enables comprehensive evaluation of short-
> and long-term tracking performance. All videos in PlanarTrack are recorded in
> unconstrained conditions from the wild, which makes PlanarTrack challenging but
> more realistic for real-world applications. To ensure high-quality annotations,
> each video frame is manually annotated by four corner points with multi-round
> meticulous inspection and refinement. To enhance target diversity of
> PlanarTrack, we only capture a unique target in one sequence, which is
> different from existing benchmarks. To our best knowledge, PlanarTrack is by
> far the largest and most diverse and challenging dataset dedicated to planar
> tracking. To understand performance of existing methods on PlanarTrack and to
> provide a comparison for future research, we evaluate 10 representative planar
> trackers with extensive comparison and in-depth analysis. Our evaluation
> reveals that, unsurprisingly, the top planar trackers heavily degrade on the
> challenging PlanarTrack, which indicates more efforts are required for
> improving planar tracking. Our data and results will be released at
> https://github.com/HengLan/PlanarTrack

