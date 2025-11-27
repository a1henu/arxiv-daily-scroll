---
layout: default
title: CanKD: Cross-Attention-based Non-local operation for Feature-based Knowledge Distillation
---

# CanKD: Cross-Attention-based Non-local operation for Feature-based Knowledge Distillation
**arXiv**：[2511.21503v1](https://arxiv.org/abs/2511.21503) · [PDF](https://arxiv.org/pdf/2511.21503.pdf)  
**作者**：Shizhe Sun, Wataru Ohyama  

**一句话要点**：提出CanKD以改进特征知识蒸馏，通过跨注意力机制增强像素级关系捕获

**关键词**：知识蒸馏, 跨注意力机制, 特征对齐, 目标检测, 图像分割

## 3 点简述
- 传统自注意力蒸馏独立对齐师生特征，难以充分捕捉像素间关系
- CanKD使用跨注意力，使学生特征动态考虑教师特征的所有像素
- 在目标检测和图像分割任务中，CanKD优于现有蒸馏方法，仅需额外损失函数

## 摘要（原文）

> We propose Cross-Attention-based Non-local Knowledge Distillation (CanKD), a novel feature-based knowledge distillation framework that leverages cross-attention mechanisms to enhance the knowledge transfer process. Unlike traditional self-attention-based distillation methods that align teacher and student feature maps independently, CanKD enables each pixel in the student feature map to dynamically consider all pixels in the teacher feature map. This non-local knowledge transfer more thoroughly captures pixel-wise relationships, improving feature representation learning. Our method introduces only an additional loss function to achieve superior performance compared with existing attention-guided distillation methods. Extensive experiments on object detection and image segmentation tasks demonstrate that CanKD outperforms state-of-the-art feature and hybrid distillation methods. These experimental results highlight CanKD's potential as a new paradigm for attention-guided distillation in computer vision tasks. Code is available at https://github.com/tori-hotaru/CanKD

