---
layout: default
title: SIMSPINE: A Biomechanics-Aware Simulation Framework for 3D Spine Motion Annotation and Benchmarking
---

# SIMSPINE: A Biomechanics-Aware Simulation Framework for 3D Spine Motion Annotation and Benchmarking
**arXiv**：[2602.20792v1](https://arxiv.org/abs/2602.20792) · [PDF](https://arxiv.org/pdf/2602.20792.pdf)  
**作者**：Muhammad Saif Ullah Khan, Didier Stricker  

**一句话要点**：提出SIMSPINE框架与数据集，以解决自然条件下3D脊柱运动标注与基准测试的缺乏问题。

**关键词**：脊柱运动建模, 3D姿态估计, 生物力学模拟, 数据集增强, 多视角重建, 数字人体建模

## 3 点简述
- 核心问题：脊柱运动建模因复杂多关节运动和大规模3D标注缺失而在计算机视觉中未充分探索。
- 方法要点：基于生物力学模拟框架，从现有人体姿态数据生成解剖学一致的3D脊柱关键点，创建SIMSPINE数据集。
- 实验或效果：数据集含214万帧，基准模型在受控环境和野外跟踪中提升性能，促进基于视觉的生物力学研究。

## 摘要（原文）

> Modeling spinal motion is fundamental to understanding human biomechanics, yet remains underexplored in computer vision due to the spine's complex multi-joint kinematics and the lack of large-scale 3D annotations. We present a biomechanics-aware keypoint simulation framework that augments existing human pose datasets with anatomically consistent 3D spinal keypoints derived from musculoskeletal modeling. Using this framework, we create the first open dataset, named SIMSPINE, which provides sparse vertebra-level 3D spinal annotations for natural full-body motions in indoor multi-camera capture without external restraints. With 2.14 million frames, this enables data-driven learning of vertebral kinematics from subtle posture variations and bridges the gap between musculoskeletal simulation and computer vision. In addition, we release pretrained baselines covering fine-tuned 2D detectors, monocular 3D pose lifting models, and multi-view reconstruction pipelines, establishing a unified benchmark for biomechanically valid spine motion estimation. Specifically, our 2D spine baselines improve the state-of-the-art from 0.63 to 0.80 AUC in controlled environments, and from 0.91 to 0.93 AP for in-the-wild spine tracking. Together, the simulation framework and SIMSPINE dataset advance research in vision-based biomechanics, motion analysis, and digital human modeling by enabling reproducible, anatomically grounded 3D spine estimation under natural conditions.

