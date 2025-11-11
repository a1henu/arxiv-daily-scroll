---
layout: default
title: Med-SORA: Symptom to Organ Reasoning in Abdomen CT Images
---

# Med-SORA: Symptom to Organ Reasoning in Abdomen CT Images
**arXiv**：[2511.06752v1](https://arxiv.org/abs/2511.06752) · [PDF](https://arxiv.org/pdf/2511.06752.pdf)  
**作者**：You-Kyoung Na, Yeong-Jun Cho  

**一句话要点**：提出Med-SORA框架以解决腹部CT图像中症状到器官的推理问题

**关键词**：医学多模态学习, 症状器官推理, 腹部CT图像, 软标签, 2D-3D特征融合, 临床推理

## 3 点简述
- 现有医学多模态模型依赖简单一对一硬标签，忽略症状与多器官关联
- 引入RAG数据集构建、可学习器官锚点软标签和2D-3D交叉注意力架构
- 实验显示Med-SORA优于现有模型，实现准确3D临床推理

## 摘要（原文）

> Understanding symptom-image associations is crucial for clinical reasoning.
> However, existing medical multimodal models often rely on simple one-to-one
> hard labeling, oversimplifying clinical reality where symptoms relate to
> multiple organs. In addition, they mainly use single-slice 2D features without
> incorporating 3D information, limiting their ability to capture full anatomical
> context. In this study, we propose Med-SORA, a framework for symptom-to-organ
> reasoning in abdominal CT images. Med-SORA introduces RAG-based dataset
> construction, soft labeling with learnable organ anchors to capture one-to-many
> symptom-organ relationships, and a 2D-3D cross-attention architecture to fuse
> local and global image features. To our knowledge, this is the first work to
> address symptom-to-organ reasoning in medical multimodal learning. Experimental
> results show that Med-SORA outperforms existing medical multimodal models and
> enables accurate 3D clinical reasoning.

