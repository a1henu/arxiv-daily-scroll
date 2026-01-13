---
layout: default
title: OSCAR: Open-Set CAD Retrieval from a Language Prompt and a Single Image
---

# OSCAR: Open-Set CAD Retrieval from a Language Prompt and a Single Image
**arXiv**：[2601.07333v1](https://arxiv.org/abs/2601.07333) · [PDF](https://arxiv.org/pdf/2601.07333.pdf)  
**作者**：Tessa Pulli, Jean-Baptiste Weibel, Peter Hönig, Matthias Hirschmanner, Markus Vincze, Andreas Holzinger  

**一句话要点**：提出OSCAR方法，通过语言提示和单张图像从无标签3D数据库中检索CAD模型，以支持零样本6D物体姿态估计。

**关键词**：零样本物体姿态估计, CAD模型检索, 多模态检索, 开放集识别, 6D姿态估计, 机器人视觉

## 3 点简述
- 核心问题：在机器人等应用中，零样本姿态估计依赖CAD模型，但模型获取困难且物体集动态变化，导致实例模型识别不可靠。
- 方法要点：OSCAR无需训练，使用GroundedSAM检测物体，结合CLIP和DINOv2进行两阶段检索，从数据库渲染图像并生成描述性标注。
- 实验或效果：在MI3DOR基准上超越现有方法，在YCB-V数据集上检索精度达90.48%，并可用于姿态估计提升性能。

## 摘要（原文）

> 6D object pose estimation plays a crucial role in scene understanding for applications such as robotics and augmented reality. To support the needs of ever-changing object sets in such context, modern zero-shot object pose estimators were developed to not require object-specific training but only rely on CAD models. Such models are hard to obtain once deployed, and a continuously changing and growing set of objects makes it harder to reliably identify the instance model of interest. To address this challenge, we introduce an Open-Set CAD Retrieval from a Language Prompt and a Single Image (OSCAR), a novel training-free method that retrieves a matching object model from an unlabeled 3D object database. During onboarding, OSCAR generates multi-view renderings of database models and annotates them with descriptive captions using an image captioning model. At inference, GroundedSAM detects the queried object in the input image, and multi-modal embeddings are computed for both the Region-of-Interest and the database captions. OSCAR employs a two-stage retrieval: text-based filtering using CLIP identifies candidate models, followed by image-based refinement using DINOv2 to select the most visually similar object. In our experiments we demonstrate that OSCAR outperforms all state-of-the-art methods on the cross-domain 3D model retrieval benchmark MI3DOR. Furthermore, we demonstrate OSCAR's direct applicability in automating object model sourcing for 6D object pose estimation. We propose using the most similar object model for pose estimation if the exact instance is not available and show that OSCAR achieves an average precision of 90.48\% during object retrieval on the YCB-V object dataset. Moreover, we demonstrate that the most similar object model can be utilized for pose estimation using Megapose achieving better results than a reconstruction-based approach.

