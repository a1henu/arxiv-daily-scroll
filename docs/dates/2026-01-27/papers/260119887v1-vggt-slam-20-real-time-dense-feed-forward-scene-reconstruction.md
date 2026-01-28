---
layout: default
title: VGGT-SLAM 2.0: Real time Dense Feed-forward Scene Reconstruction
---

# VGGT-SLAM 2.0: Real time Dense Feed-forward Scene Reconstruction
**arXiv**：[2601.19887v1](https://arxiv.org/abs/2601.19887) · [PDF](https://arxiv.org/pdf/2601.19887.pdf)  
**作者**：Dominic Maggio, Luca Carlone  

**一句话要点**：提出VGGT-SLAM 2.0以实时重建密集场景，改进因子图设计和利用注意力层增强闭环检测。

**关键词**：实时SLAM, 密集重建, 因子图优化, 注意力机制, 闭环检测, 开放集检测

## 3 点简述
- 核心问题：VGGT-SLAM存在高维漂移和平面退化，且相机内参未知导致重建模糊。
- 方法要点：设计新因子图消除漂移和退化，利用VGGT注意力层辅助图像检索验证，无需额外训练。
- 实验效果：在TUM数据集上姿态误差降低约23%，实现在地面机器人上的在线实时运行，并适应开放集物体检测。

## 摘要（原文）

> We present VGGT-SLAM 2.0, a real time RGB feed-forward SLAM system which substantially improves upon VGGT-SLAM for incrementally aligning submaps created from VGGT. Firstly, we remove high-dimensional 15-degree-of-freedom drift and planar degeneracy from VGGT-SLAM by creating a new factor graph design while still addressing the reconstruction ambiguity of VGGT given unknown camera intrinsics. Secondly, by studying the attention layers of VGGT, we show that one of the layers is well suited to assist in image retrieval verification for free without additional training, which enables both rejecting false positive matches and allows for completing more loop closures. Finally, we conduct a suite of experiments which includes showing VGGT-SLAM 2.0 can easily be adapted for open-set object detection and demonstrating real time performance while running online onboard a ground robot using a Jetson Thor. We also test in environments ranging from cluttered indoor apartments and office scenes to a 4,200 square foot barn, and we also demonstrate VGGT-SLAM 2.0 achieves the highest accuracy on the TUM dataset with about 23 percent less pose error than VGGT-SLAM. Code will be released upon publication.

