---
layout: default
title: Long-Term Multi-Session 3D Reconstruction Under Substantial Appearance Change
---

# Long-Term Multi-Session 3D Reconstruction Under Substantial Appearance Change
**arXiv**：[2602.20584v1](https://arxiv.org/abs/2602.20584) · [PDF](https://arxiv.org/pdf/2602.20584.pdf)  
**作者**：Beverley Gorry, Tobias Fischer, Michael Milford, Alejandro Fontan  

**一句话要点**：提出联合SfM重建方法，结合手工与学习特征，解决长期多会话3D重建中的大外观变化问题。

**关键词**：长期3D重建, 多会话对齐, 外观变化处理, 联合SfM, 特征匹配, 视觉地点识别

## 3 点简述
- 核心问题：现有SfM方法假设图像捕获时间相近且外观变化有限，在长期监测（如珊瑚礁调查）中因大外观变化而失效。
- 方法要点：通过跨会话对应关系直接嵌入联合SfM重建，结合手工和学习特征，并利用视觉地点识别减少计算成本。
- 实验或效果：在长期珊瑚礁数据集上评估，能在现有方法失效时实现一致的联合重建，提升对齐鲁棒性。

## 摘要（原文）

> Long-term environmental monitoring requires the ability to reconstruct and align 3D models across repeated site visits separated by months or years. However, existing Structure-from-Motion (SfM) pipelines implicitly assume near-simultaneous image capture and limited appearance change, and therefore fail when applied to long-term monitoring scenarios such as coral reef surveys, where substantial visual and structural change is common. In this paper, we show that the primary limitation of current approaches lies in their reliance on post-hoc alignment of independently reconstructed sessions, which is insufficient under large temporal appearance change. We address this limitation by enforcing cross-session correspondences directly within a joint SfM reconstruction. Our approach combines complementary handcrafted and learned visual features to robustly establish correspondences across large temporal gaps, enabling the reconstruction of a single coherent 3D model from imagery captured years apart, where standard independent and joint SfM pipelines break down. We evaluate our method on long-term coral reef datasets exhibiting significant real-world change, and demonstrate consistent joint reconstruction across sessions in cases where existing methods fail to produce coherent reconstructions. To ensure scalability to large datasets, we further restrict expensive learned feature matching to a small set of likely cross-session image pairs identified via visual place recognition, which reduces computational cost and improves alignment robustness.

