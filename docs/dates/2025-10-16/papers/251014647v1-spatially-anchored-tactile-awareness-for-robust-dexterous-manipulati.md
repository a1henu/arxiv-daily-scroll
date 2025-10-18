---
layout: default
title: Spatially anchored Tactile Awareness for Robust Dexterous Manipulation
---

# Spatially anchored Tactile Awareness for Robust Dexterous Manipulation
**arXiv**：[2510.14647v1](https://arxiv.org/abs/2510.14647) · [PDF](https://arxiv.org/pdf/2510.14647.pdf)  
**作者**：Jialei Huang, Yang Ye, Yuanqing Gong, Xuezhou Zhu, Yang Gao, Kaifeng Zhang  

**一句话要点**：提出SaTA框架，通过空间锚定触觉特征提升灵巧操作精度

**关键词**：灵巧操作, 触觉感知, 空间锚定, 几何推理, 强化学习

## 3 点简述
- 现有视觉触觉学习方法在亚毫米精度任务中表现不佳，缺乏触觉信号与手部运动的空间关联利用
- SaTA通过前向运动学将触觉特征锚定于手部坐标系，实现无模型几何推理
- 在USB-C插接等任务中，成功率提升30%，完成时间减少27%

## 摘要（原文）

> Dexterous manipulation requires precise geometric reasoning, yet existing
> visuo-tactile learning methods struggle with sub-millimeter precision tasks
> that are routine for traditional model-based approaches. We identify a key
> limitation: while tactile sensors provide rich contact information, current
> learning frameworks fail to effectively leverage both the perceptual richness
> of tactile signals and their spatial relationship with hand kinematics. We
> believe an ideal tactile representation should explicitly ground contact
> measurements in a stable reference frame while preserving detailed sensory
> information, enabling policies to not only detect contact occurrence but also
> precisely infer object geometry in the hand's coordinate system. We introduce
> SaTA (Spatially-anchored Tactile Awareness for dexterous manipulation), an
> end-to-end policy framework that explicitly anchors tactile features to the
> hand's kinematic frame through forward kinematics, enabling accurate geometric
> reasoning without requiring object models or explicit pose estimation. Our key
> insight is that spatially grounded tactile representations allow policies to
> not only detect contact occurrence but also precisely infer object geometry in
> the hand's coordinate system. We validate SaTA on challenging dexterous
> manipulation tasks, including bimanual USB-C mating in free space, a task
> demanding sub-millimeter alignment precision, as well as light bulb
> installation requiring precise thread engagement and rotational control, and
> card sliding that demands delicate force modulation and angular precision.
> These tasks represent significant challenges for learning-based methods due to
> their stringent precision requirements. Across multiple benchmarks, SaTA
> significantly outperforms strong visuo-tactile baselines, improving success
> rates by up to 30 percentage while reducing task completion times by 27
> percentage.

