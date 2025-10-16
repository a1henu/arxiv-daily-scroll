---
layout: default
title: Fusion Meets Diverse Conditions: A High-diversity Benchmark and Baseline for UAV-based Multimodal Object Detection with Condition Cues
---

# Fusion Meets Diverse Conditions: A High-diversity Benchmark and Baseline for UAV-based Multimodal Object Detection with Condition Cues
**arXiv**：[2510.13620v1](https://arxiv.org/abs/2510.13620) · [PDF](https://arxiv.org/pdf/2510.13620.pdf)  
**作者**：Chen Chen, Kangcheng Bin, Ting Hu, Jiahao Qi, Xingyue Liu, Tianpeng Liu, Zhen Liu, Yongxiang Liu, Ping Zhong  

**一句话要点**：提出PCDF方法以解决无人机多模态目标检测在多样条件下的自适应融合问题

**关键词**：无人机目标检测, 多模态融合, 条件感知, RGB-IR图像, 动态融合, 数据集构建

## 3 点简述
- 现有数据集难以覆盖真实世界复杂成像条件，限制了无人机RGB-IR目标检测的鲁棒性。
- PCDF利用条件提示自适应调整多模态贡献，通过软门控变换建模条件与模态关系。
- 在ATR-UMOD数据集上实验验证PCDF有效性，提升检测性能。

## 摘要（原文）

> Unmanned aerial vehicles (UAV)-based object detection with visible (RGB) and
> infrared (IR) images facilitates robust around-the-clock detection, driven by
> advancements in deep learning techniques and the availability of high-quality
> dataset. However, the existing dataset struggles to fully capture real-world
> complexity for limited imaging conditions. To this end, we introduce a
> high-diversity dataset ATR-UMOD covering varying scenarios, spanning altitudes
> from 80m to 300m, angles from 0{\deg} to 75{\deg}, and all-day, all-year time
> variations in rich weather and illumination conditions. Moreover, each RGB-IR
> image pair is annotated with 6 condition attributes, offering valuable
> high-level contextual information. To meet the challenge raised by such diverse
> conditions, we propose a novel prompt-guided condition-aware dynamic fusion
> (PCDF) to adaptively reassign multimodal contributions by leveraging annotated
> condition cues. By encoding imaging conditions as text prompts, PCDF
> effectively models the relationship between conditions and multimodal
> contributions through a task-specific soft-gating transformation. A
> prompt-guided condition-decoupling module further ensures the availability in
> practice without condition annotations. Experiments on ATR-UMOD dataset reveal
> the effectiveness of PCDF.

