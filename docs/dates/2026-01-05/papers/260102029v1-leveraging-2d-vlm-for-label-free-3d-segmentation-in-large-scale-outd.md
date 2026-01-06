---
layout: default
title: Leveraging 2D-VLM for Label-Free 3D Segmentation in Large-Scale Outdoor Scene Understanding
---

# Leveraging 2D-VLM for Label-Free 3D Segmentation in Large-Scale Outdoor Scene Understanding
**arXiv**：[2601.02029v1](https://arxiv.org/abs/2601.02029) · [PDF](https://arxiv.org/pdf/2601.02029.pdf)  
**作者**：Toshihiko Nishimura, Hirofumi Abe, Kazuhiko Murasaki, Taiga Yoshida, Ryuichi Tanida  

**一句话要点**：提出基于2D视觉语言模型的免标注3D分割方法，用于大规模户外场景理解。

**关键词**：3D语义分割, 点云处理, 视觉语言模型, 免标注学习, 开放词汇识别, 多视角融合

## 3 点简述
- 核心问题：无需标注3D数据或配对RGB图像，实现大规模点云语义分割。
- 方法要点：通过虚拟相机投影点云至2D，利用自然语言提示的2D基础模型进行分割，多视角加权投票聚合预测。
- 实验或效果：超越现有免训练方法，分割精度接近监督方法，支持开放词汇识别。

## 摘要（原文）

> This paper presents a novel 3D semantic segmentation method for large-scale point cloud data that does not require annotated 3D training data or paired RGB images. The proposed approach projects 3D point clouds onto 2D images using virtual cameras and performs semantic segmentation via a foundation 2D model guided by natural language prompts. 3D segmentation is achieved by aggregating predictions from multiple viewpoints through weighted voting. Our method outperforms existing training-free approaches and achieves segmentation accuracy comparable to supervised methods. Moreover, it supports open-vocabulary recognition, enabling users to detect objects using arbitrary text queries, thus overcoming the limitations of traditional supervised approaches.

