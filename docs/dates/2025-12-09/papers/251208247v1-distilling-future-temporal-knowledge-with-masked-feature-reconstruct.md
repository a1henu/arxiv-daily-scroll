---
layout: default
title: Distilling Future Temporal Knowledge with Masked Feature Reconstruction for 3D Object Detection
---

# Distilling Future Temporal Knowledge with Masked Feature Reconstruction for 3D Object Detection
**arXiv**：[2512.08247v1](https://arxiv.org/abs/2512.08247) · [PDF](https://arxiv.org/pdf/2512.08247.pdf)  
**作者**：Haowen Zheng, Hu Zhu, Lu Deng, Weihao Gu, Yang Yang, Yanyan Liang  

**一句话要点**：提出未来时序知识蒸馏方法，通过掩码特征重建解决在线3D目标检测中未来帧知识迁移问题。

**关键词**：3D目标检测, 知识蒸馏, 时序建模, 自动驾驶, 特征重建

## 3 点简述
- 核心问题：现有知识蒸馏方法忽视未来帧，难以让在线模型有效学习未来知识。
- 方法要点：采用稀疏查询和未来感知特征重建策略，无需严格帧对齐即可迁移未来特征。
- 实验或效果：在nuScenes数据集上提升mAP和NDS达1.3，实现最准确速度估计，推理成本不变。

## 摘要（原文）

> Camera-based temporal 3D object detection has shown impressive results in autonomous driving, with offline models improving accuracy by using future frames. Knowledge distillation (KD) can be an appealing framework for transferring rich information from offline models to online models. However, existing KD methods overlook future frames, as they mainly focus on spatial feature distillation under strict frame alignment or on temporal relational distillation, thereby making it challenging for online models to effectively learn future knowledge. To this end, we propose a sparse query-based approach, Future Temporal Knowledge Distillation (FTKD), which effectively transfers future frame knowledge from an offline teacher model to an online student model. Specifically, we present a future-aware feature reconstruction strategy to encourage the student model to capture future features without strict frame alignment. In addition, we further introduce future-guided logit distillation to leverage the teacher's stable foreground and background context. FTKD is applied to two high-performing 3D object detection baselines, achieving up to 1.3 mAP and 1.3 NDS gains on the nuScenes dataset, as well as the most accurate velocity estimation, without increasing inference cost.

