---
layout: default
title: V-Thinker: Interactive Thinking with Images
---

# V-Thinker: Interactive Thinking with Images
**arXiv**：[2511.04460v1](https://arxiv.org/abs/2511.04460) · [PDF](https://arxiv.org/pdf/2511.04460.pdf)  
**作者**：Runqi Qiao, Qiuna Tan, Minghan Yang, Guanting Dong, Peiqing Yang, Shiqiang Lang, Enhui Wan, Xiaowan Wang, Yida Xu, Lan Yang, Chong Sun, Chen Li, Honggang Zhang  

**一句话要点**：提出V-Thinker以解决大模型图像交互推理的视觉工具限制问题

**关键词**：大模型图像交互推理, 数据进化飞轮, 视觉渐进训练, 强化学习, VTBench基准

## 3 点简述
- 核心问题：大模型图像交互推理受限于视觉工具空间和任务特定设计
- 方法要点：结合数据进化飞轮和视觉渐进训练课程，通过强化学习实现交互推理
- 实验或效果：在VTBench基准上优于基线模型，提升通用和交互推理能力

## 摘要（原文）

> Empowering Large Multimodal Models (LMMs) to deeply integrate image
> interaction with long-horizon reasoning capabilities remains a long-standing
> challenge in this field. Recent advances in vision-centric reasoning explore a
> promising "Thinking with Images" paradigm for LMMs, marking a shift from
> image-assisted reasoning to image-interactive thinking. While this milestone
> enables models to focus on fine-grained image regions, progress remains
> constrained by limited visual tool spaces and task-specific workflow designs.
> To bridge this gap, we present V-Thinker, a general-purpose multimodal
> reasoning assistant that enables interactive, vision-centric thinking through
> end-to-end reinforcement learning. V-Thinker comprises two key components: (1)
> a Data Evolution Flywheel that automatically synthesizes, evolves, and verifies
> interactive reasoning datasets across three dimensions-diversity, quality, and
> difficulty; and (2) a Visual Progressive Training Curriculum that first aligns
> perception via point-level supervision, then integrates interactive reasoning
> through a two-stage reinforcement learning framework. Furthermore, we introduce
> VTBench, an expert-verified benchmark targeting vision-centric interactive
> reasoning tasks. Extensive experiments demonstrate that V-Thinker consistently
> outperforms strong LMM-based baselines in both general and interactive
> reasoning scenarios, providing valuable insights for advancing
> image-interactive reasoning applications.

