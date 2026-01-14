---
layout: default
title: 3AM: Segment Anything with Geometric Consistency in Videos
---

# 3AM: Segment Anything with Geometric Consistency in Videos
**arXiv**：[2601.08831v1](https://arxiv.org/abs/2601.08831) · [PDF](https://arxiv.org/pdf/2601.08831.pdf)  
**作者**：Yang-Che Sun, Cheng Sun, Chin-Yang Lin, Fu-En Yang, Min-Hung Chen, Yen-Yu Lin, Yu-Lun Liu  

**一句话要点**：提出3AM方法，通过融合3D感知特征增强SAM2，解决视频中视角变化下的分割一致性问题。

**关键词**：视频对象分割, 3D感知特征, 几何一致性, 轻量级融合, 视场感知采样, RGB输入

## 3 点简述
- 核心问题：视频分割方法如SAM2依赖外观特征，在视角变化大时性能下降；传统3D方法需额外输入如相机位姿。
- 方法要点：集成MUSt3R的3D感知特征到SAM2，使用轻量级特征融合器，结合视场感知采样策略，仅需RGB输入。
- 实验或效果：在ScanNet++等数据集上显著优于SAM2，IoU达90.6%，提升现有方法性能。

## 摘要（原文）

> Video object segmentation methods like SAM2 achieve strong performance through memory-based architectures but struggle under large viewpoint changes due to reliance on appearance features. Traditional 3D instance segmentation methods address viewpoint consistency but require camera poses, depth maps, and expensive preprocessing. We introduce 3AM, a training-time enhancement that integrates 3D-aware features from MUSt3R into SAM2. Our lightweight Feature Merger fuses multi-level MUSt3R features that encode implicit geometric correspondence. Combined with SAM2's appearance features, the model achieves geometry-consistent recognition grounded in both spatial position and visual similarity. We propose a field-of-view aware sampling strategy ensuring frames observe spatially consistent object regions for reliable 3D correspondence learning. Critically, our method requires only RGB input at inference, with no camera poses or preprocessing. On challenging datasets with wide-baseline motion (ScanNet++, Replica), 3AM substantially outperforms SAM2 and extensions, achieving 90.6% IoU and 71.7% Positive IoU on ScanNet++'s Selected Subset, improving over state-of-the-art VOS methods by +15.9 and +30.4 points. Project page: https://jayisaking.github.io/3AM-Page/

