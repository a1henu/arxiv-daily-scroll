---
layout: default
title: Neural Implicit Heart Coordinates: 3D cardiac shape reconstruction from sparse segmentations
---

# Neural Implicit Heart Coordinates: 3D cardiac shape reconstruction from sparse segmentations
**arXiv**：[2512.19316v1](https://arxiv.org/abs/2512.19316) · [PDF](https://arxiv.org/pdf/2512.19316.pdf)  
**作者**：Marica Muffoletto, Uxio Hermida, Charlène Mauger, Avan Suinesiaputra, Yiyang Xu, Richard Burns, Lisa Pankewitz, Andrew D McCulloch, Steffen E Petersen, Daniel Rueckert, Alistair A Young  

**一句话要点**：提出神经隐式心脏坐标以从稀疏分割重建3D心脏形状

**关键词**：神经隐式函数, 心脏形状重建, 稀疏分割, 解剖一致性, 患者特异性建模, 3D网格生成

## 3 点简述
- 核心问题：从稀疏临床图像准确重建心脏解剖结构是患者特异性建模的主要挑战。
- 方法要点：基于通用心室坐标，引入标准化隐式坐标系，从有限2D分割预测坐标并解码为密集3D分割和网格。
- 实验或效果：在5000个心脏网格数据集上训练，重建误差约2.5毫米，推理时间从60秒降至5-15秒。

## 摘要（原文）

> Accurate reconstruction of cardiac anatomy from sparse clinical images remains a major challenge in patient-specific modeling. While neural implicit functions have previously been applied to this task, their application to mapping anatomical consistency across subjects has been limited. In this work, we introduce Neural Implicit Heart Coordinates (NIHCs), a standardized implicit coordinate system, based on universal ventricular coordinates, that provides a common anatomical reference frame for the human heart. Our method predicts NIHCs directly from a limited number of 2D segmentations (sparse acquisition) and subsequently decodes them into dense 3D segmentations and high-resolution meshes at arbitrary output resolution. Trained on a large dataset of 5,000 cardiac meshes, the model achieves high reconstruction accuracy on clinical contours, with mean Euclidean surface errors of 2.51$\pm$0.33 mm in a diseased cohort (n=4549) and 2.3$\pm$0.36 mm in a healthy cohort (n=5576). The NIHC representation enables anatomically coherent reconstruction even under severe slice sparsity and segmentation noise, faithfully recovering complex structures such as the valve planes. Compared with traditional pipelines, inference time is reduced from over 60 s to 5-15 s. These results demonstrate that NIHCs constitute a robust and efficient anatomical representation for patient-specific 3D cardiac reconstruction from minimal input data.

