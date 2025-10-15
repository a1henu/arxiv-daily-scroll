---
layout: default
title: BEEP3D: Box-Supervised End-to-End Pseudo-Mask Generation for 3D Instance Segmentation
---

# BEEP3D: Box-Supervised End-to-End Pseudo-Mask Generation for 3D Instance Segmentation
**arXiv**：[2510.12182v1](https://arxiv.org/abs/2510.12182) · [PDF](https://arxiv.org/pdf/2510.12182.pdf)  
**作者**：Youngju Yoo, Seho Kim, Changick Kim  

**一句话要点**：提出BEEP3D以解决3D实例分割中框监督的模糊性问题

**关键词**：3D实例分割, 框监督学习, 师生框架, 伪掩码生成, 弱监督方法

## 3 点简述
- 核心问题：框级监督在重叠区域引入模糊性，阻碍点对实例的准确分配
- 方法要点：采用师生框架，通过查询精炼和一致性损失生成精确伪掩码
- 实验或效果：在ScanNetV2和S3DIS数据集上性能竞争或优于先进弱监督方法

## 摘要（原文）

> 3D instance segmentation is crucial for understanding complex 3D
> environments, yet fully supervised methods require dense point-level
> annotations, resulting in substantial annotation costs and labor overhead. To
> mitigate this, box-level annotations have been explored as a weaker but more
> scalable form of supervision. However, box annotations inherently introduce
> ambiguity in overlapping regions, making accurate point-to-instance assignment
> challenging. Recent methods address this ambiguity by generating pseudo-masks
> through training a dedicated pseudo-labeler in an additional training stage.
> However, such two-stage pipelines often increase overall training time and
> complexity, hinder end-to-end optimization. To overcome these challenges, we
> propose BEEP3D-Box-supervised End-to-End Pseudo-mask generation for 3D instance
> segmentation. BEEP3D adopts a student-teacher framework, where the teacher
> model serves as a pseudo-labeler and is updated by the student model via an
> Exponential Moving Average. To better guide the teacher model to generate
> precise pseudo-masks, we introduce an instance center-based query refinement
> that enhances position query localization and leverages features near instance
> centers. Additionally, we design two novel losses-query consistency loss and
> masked feature consistency loss-to align semantic and geometric signals between
> predictions and pseudo-masks. Extensive experiments on ScanNetV2 and S3DIS
> datasets demonstrate that BEEP3D achieves competitive or superior performance
> compared to state-of-the-art weakly supervised methods while remaining
> computationally efficient.

