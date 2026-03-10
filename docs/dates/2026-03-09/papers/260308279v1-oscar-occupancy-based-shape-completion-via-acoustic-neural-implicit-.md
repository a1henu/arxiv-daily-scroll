---
layout: default
title: OSCAR: Occupancy-based Shape Completion via Acoustic Neural Implicit Representations
---

# OSCAR: Occupancy-based Shape Completion via Acoustic Neural Implicit Representations
**arXiv**：[2603.08279v1](https://arxiv.org/abs/2603.08279) · [PDF](https://arxiv.org/pdf/2603.08279.pdf)  
**作者**：Magdalena Wysocki, Kadir Burak Buldu, Miruna-Alexandra Gafencu, Mohammad Farid Azampour, Nassir Navab  

**一句话要点**：提出基于占用和声学神经隐式表示的形状补全方法，以解决超声中椎骨解剖的3D重建挑战。

**关键词**：形状补全, 神经隐式表示, 超声成像, 3D重建, 无标签推理, 声学建模

## 3 点简述
- 核心问题：超声成像中声影和视角依赖信号变化导致椎骨解剖3D重建不完整。
- 方法要点：使用耦合潜在空间联合建模图像外观和解剖形状，通过神经隐式表示直接提取表面，无需推理时标注。
- 实验或效果：在B模式超声上HD95分数优于现有方法80%，在仿真和体模图像中验证了准确重建和鲁棒泛化。

## 摘要（原文）

> Accurate 3D reconstruction of vertebral anatomy from ultrasound is important for guiding minimally invasive spine interventions, but it remains challenging due to acoustic shadowing and view-dependent signal variations. We propose an occupancy-based shape completion method that reconstructs complete 3D anatomical geometry from partial ultrasound observations. Crucially for intra-operative applications, our approach extracts the anatomical surface directly from the image, avoiding the need for anatomical labels during inference. This label-free completion relies on a coupled latent space representing both the image appearance and the underlying anatomical shape. By leveraging a Neural Implicit Representation (NIR) that jointly models both spatial occupancy and acoustic interactions, the method uses acoustic parameters to become implicitly aware of the unseen regions without explicit shadowing labels through tracking acoustic signal transmission. We show that this method outperforms state-of-the-art shape completion for B-mode ultrasound by 80% in HD95 score. We validate our approach both in-silico and on phantom US images with registered mesh models from CT labels, demonstrating accurate reconstruction of occluded anatomy and robust generalization across diverse imaging conditions. Code and data will be released on publication.

