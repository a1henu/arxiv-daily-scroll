---
layout: default
title: NeRFscopy: Neural Radiance Fields for in-vivo Time-Varying Tissues from Endoscopy
---

# NeRFscopy: Neural Radiance Fields for in-vivo Time-Varying Tissues from Endoscopy
**arXiv**：[2602.15775v1](https://arxiv.org/abs/2602.15775) · [PDF](https://arxiv.org/pdf/2602.15775.pdf)  
**作者**：Laura Salort-Benejam, Antonio Agudo  

**一句话要点**：提出NeRFscopy以解决内窥镜视频中可变形组织的动态3D重建问题

**关键词**：神经辐射场, 内窥镜成像, 可变形组织重建, 单目视频, 新视角合成, 自监督学习

## 3 点简述
- 核心问题：内窥镜视频中组织变形、单目相机、光照变化等挑战阻碍动态3D重建
- 方法要点：基于神经辐射场，引入可变形模型，结合规范辐射场和SE(3)参数化的时变变形场
- 实验或效果：在多种挑战性内窥镜场景中，新视角合成准确，优于竞争方法

## 摘要（原文）

> Endoscopy is essential in medical imaging, used for diagnosis, prognosis and treatment. Developing a robust dynamic 3D reconstruction pipeline for endoscopic videos could enhance visualization, improve diagnostic accuracy, aid in treatment planning, and guide surgery procedures. However, challenges arise due to the deformable nature of the tissues, the use of monocular cameras, illumination changes, occlusions and unknown camera trajectories. Inspired by neural rendering, we introduce NeRFscopy, a self-supervised pipeline for novel view synthesis and 3D reconstruction of deformable endoscopic tissues from a monocular video. NeRFscopy includes a deformable model with a canonical radiance field and a time-dependent deformation field parameterized by SE(3) transformations. In addition, the color images are efficiently exploited by introducing sophisticated terms to learn a 3D implicit model without assuming any template or pre-trained model, solely from data. NeRFscopy achieves accurate results in terms of novel view synthesis, outperforming competing methods across various challenging endoscopy scenes.

