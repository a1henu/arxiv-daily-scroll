---
layout: default
title: Vision-Language Models for Ergonomic Assessment of Manual Lifting Tasks: Estimating Horizontal and Vertical Hand Distances from RGB Video
---

# Vision-Language Models for Ergonomic Assessment of Manual Lifting Tasks: Estimating Horizontal and Vertical Hand Distances from RGB Video
**arXiv**：[2602.20658v1](https://arxiv.org/abs/2602.20658) · [PDF](https://arxiv.org/pdf/2602.20658.pdf)  
**作者**：Mohammad Sadra Rajabi, Aanuoluwapo Ojelade, Sunwook Kim, Maury A. Nussbaum  

**一句话要点**：提出基于视觉语言模型的RGB视频流水线，用于非侵入式估计手动举升任务中的水平和垂直手部距离。

**关键词**：视觉语言模型, 人体工程学评估, 手动举升任务, RGB视频分析, 距离估计, 分割增强

## 3 点简述
- 核心问题：手动举升任务易致工作相关肌肉骨骼疾病，但传统RNLE距离参数测量依赖手动或专用传感，难以实时应用。
- 方法要点：开发两种多阶段VLM流水线，包括文本引导检测和检测加分割，结合视觉特征提取与基于Transformer的时间回归。
- 实验或效果：通过留一受试者验证，分割多视图流水线误差最小，水平和垂直距离平均绝对误差约6-8厘米和5-8厘米，分割相比检测减少误差20-40%。

## 摘要（原文）

> Manual lifting tasks are a major contributor to work-related musculoskeletal disorders, and effective ergonomic risk assessment is essential for quantifying physical exposure and informing ergonomic interventions. The Revised NIOSH Lifting Equation (RNLE) is a widely used ergonomic risk assessment tool for lifting tasks that relies on six task variables, including horizontal (H) and vertical (V) hand distances; such distances are typically obtained through manual measurement or specialized sensing systems and are difficult to use in real-world environments. We evaluated the feasibility of using innovative vision-language models (VLMs) to non-invasively estimate H and V from RGB video streams. Two multi-stage VLM-based pipelines were developed: a text-guided detection-only pipeline and a detection-plus-segmentation pipeline. Both pipelines used text-guided localization of task-relevant regions of interest, visual feature extraction from those regions, and transformer-based temporal regression to estimate H and V at the start and end of a lift. For a range of lifting tasks, estimation performance was evaluated using leave-one-subject-out validation across the two pipelines and seven camera view conditions. Results varied significantly across pipelines and camera view conditions, with the segmentation-based, multi-view pipeline consistently yielding the smallest errors, achieving mean absolute errors of approximately 6-8 cm when estimating H and 5-8 cm when estimating V. Across pipelines and camera view configurations, pixel-level segmentation reduced estimation error by approximately 20-30% for H and 35-40% for V relative to the detection-only pipeline. These findings support the feasibility of VLM-based pipelines for video-based estimation of RNLE distance parameters.

