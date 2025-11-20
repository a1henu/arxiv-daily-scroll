---
layout: default
title: US-X Complete: A Multi-Modal Approach to Anatomical 3D Shape Recovery
---

# US-X Complete: A Multi-Modal Approach to Anatomical 3D Shape Recovery
**arXiv**：[2511.15600v1](https://arxiv.org/abs/2511.15600) · [PDF](https://arxiv.org/pdf/2511.15600.pdf)  
**作者**：Miruna-Alexandra Gafencu, Yordanka Velikova, Nassir Navab, Mohammad Farid Azampour  

**一句话要点**：提出多模态深度学习方法，利用X射线补全超声中遮挡的3D解剖结构。

**关键词**：多模态学习, 3D超声补全, 椎体重建, X射线融合, 深度学习

## 3 点简述
- 超声成像因骨骼声影无法完整显示椎体等解剖结构。
- 方法融合单张X射线图像信息，生成配对数据训练模型。
- 实验显示椎体重建显著改进，无需术前CT配准。

## 摘要（原文）

> Ultrasound offers a radiation-free, cost-effective solution for real-time visualization of spinal landmarks, paraspinal soft tissues and neurovascular structures, making it valuable for intraoperative guidance during spinal procedures. However, ultrasound suffers from inherent limitations in visualizing complete vertebral anatomy, in particular vertebral bodies, due to acoustic shadowing effects caused by bone. In this work, we present a novel multi-modal deep learning method for completing occluded anatomical structures in 3D ultrasound by leveraging complementary information from a single X-ray image. To enable training, we generate paired training data consisting of: (1) 2D lateral vertebral views that simulate X-ray scans, and (2) 3D partial vertebrae representations that mimic the limited visibility and occlusions encountered during ultrasound spine imaging. Our method integrates morphological information from both imaging modalities and demonstrates significant improvements in vertebral reconstruction (p < 0.001) compared to state of art in 3D ultrasound vertebral completion. We perform phantom studies as an initial step to future clinical translation, and achieve a more accurate, complete volumetric lumbar spine visualization overlayed on the ultrasound scan without the need for registration with preoperative modalities such as computed tomography. This demonstrates that integrating a single X-ray projection mitigates ultrasound's key limitation while preserving its strengths as the primary imaging modality. Code and data can be found at https://github.com/miruna20/US-X-Complete

