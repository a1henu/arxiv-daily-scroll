---
layout: default
title: Hi-Light: A Path to high-fidelity, high-resolution video relighting with a Novel Evaluation Paradigm
---

# Hi-Light: A Path to high-fidelity, high-resolution video relighting with a Novel Evaluation Paradigm
**arXiv**：[2601.23167v1](https://arxiv.org/abs/2601.23167) · [PDF](https://arxiv.org/pdf/2601.23167.pdf)  
**作者**：Xiangrui Liu, Haoxiang Li, Yezhou Yang  

**一句话要点**：提出Hi-Light框架以解决视频重照明中的稳定性与细节保留问题

**关键词**：视频重照明, 时间稳定性, 细节保留, 评估指标, 无训练框架, 高分辨率视频

## 3 点简述
- 核心问题：视频重照明缺乏评估指标、存在光闪烁和细节退化
- 方法要点：基于轻量先验引导扩散、混合运动自适应平滑滤波和LAB细节融合
- 实验或效果：在定性和定量比较中显著优于现有方法，产生稳定高细节视频

## 摘要（原文）

> Video relighting offers immense creative potential and commercial value but is hindered by challenges, including the absence of an adequate evaluation metric, severe light flickering, and the degradation of fine-grained details during editing. To overcome these challenges, we introduce Hi-Light, a novel, training-free framework for high-fidelity, high-resolution, robust video relighting. Our approach introduces three technical innovations: lightness prior anchored guided relighting diffusion that stabilises intermediate relit video, a Hybrid Motion-Adaptive Lighting Smoothing Filter that leverages optical flow to ensure temporal stability without introducing motion blur, and a LAB-based Detail Fusion module that preserves high-frequency detail information from the original video. Furthermore, to address the critical gap in evaluation, we propose the Light Stability Score, the first quantitative metric designed to specifically measure lighting consistency. Extensive experiments demonstrate that Hi-Light significantly outperforms state-of-the-art methods in both qualitative and quantitative comparisons, producing stable, highly detailed relit videos.

