---
layout: default
title: Hydra-Nav: Object Navigation via Adaptive Dual-Process Reasoning
---

# Hydra-Nav: Object Navigation via Adaptive Dual-Process Reasoning
**arXiv**：[2602.09972v1](https://arxiv.org/abs/2602.09972) · [PDF](https://arxiv.org/pdf/2602.09972.pdf)  
**作者**：Zixuan Wang, Huang Fang, Shaoan Wang, Yuanfei Luo, Heng Dong, Wei Li, Yiming Gan  

**一句话要点**：提出Hydra-Nav架构，通过自适应双过程推理提升目标导航的效率和成功率。

**关键词**：目标导航, 视觉语言模型, 自适应推理, 时空推理, 课程学习, 搜索效率

## 3 点简述
- 核心问题：现有VLM导航方法时空推理弱，导致成功率低且计算开销大。
- 方法要点：采用自适应慢快系统切换，结合三阶段课程训练增强推理与执行。
- 实验或效果：在多个基准上实现SOTA性能，并引入SOT指标验证搜索效率提升。

## 摘要（原文）

> While large vision-language models (VLMs) show promise for object goal navigation, current methods still struggle with low success rates and inefficient localization of unseen objects--failures primarily attributed to weak temporal-spatial reasoning. Meanwhile, recent attempts to inject reasoning into VLM-based agents improve success rates but incur substantial computational overhead. To address both the ineffectiveness and inefficiency of existing approaches, we introduce Hydra-Nav, a unified VLM architecture that adaptively switches between a deliberative slow system for analyzing exploration history and formulating high-level plans, and a reactive fast system for efficient execution. We train Hydra-Nav through a three-stage curriculum: (i) spatial-action alignment to strengthen trajectory planning, (ii) memory-reasoning integration to enhance temporal-spatial reasoning over long-horizon exploration, and (iii) iterative rejection fine-tuning to enable selective reasoning at critical decision points. Extensive experiments demonstrate that Hydra-Nav achieves state-of-the-art performance on the HM3D, MP3D, and OVON benchmarks, outperforming the second-best methods by 11.1%, 17.4%, and 21.2%, respectively. Furthermore, we introduce SOT (Success weighted by Operation Time), a new metric to measure search efficiency across VLMs with varying reasoning intensity. Results show that adaptive reasoning significantly enhances search efficiency over fixed-frequency baselines.

