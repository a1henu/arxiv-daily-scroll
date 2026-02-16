---
layout: default
title: Lung nodule classification on CT scan patches using 3D convolutional neural networks
---

# Lung nodule classification on CT scan patches using 3D convolutional neural networks
**arXiv**：[2602.12750v1](https://arxiv.org/abs/2602.12750) · [PDF](https://arxiv.org/pdf/2602.12750.pdf)  
**作者**：Volodymyr Sydorskyi  

**一句话要点**：提出CT扫描裁剪、标签过滤与数据增强方法以提升肺结节分类性能

**关键词**：肺结节分类, 3D卷积神经网络, CT扫描处理, 数据增强, 临床决策支持系统

## 3 点简述
- 核心问题：肺结节分类对早期肺癌检测至关重要，但面临数据量大、结节小、视觉评估困难等挑战。
- 方法要点：采用CT扫描裁剪策略聚焦目标结节，结合标签过滤去除噪声，并引入新数据增强提升模型鲁棒性。
- 实验或效果：在LIDC-IDRI数据集上，多类模型Macro ROC AUC达0.9176，优于先前方法，实现先进性能。

## 摘要（原文）

> Lung cancer remains one of the most common and deadliest forms of cancer worldwide. The likelihood of successful treatment depends strongly on the stage at which the disease is diagnosed. Therefore, early detection of lung cancer represents a critical medical challenge. However, this task poses significant difficulties for thoracic radiologists due to the large number of studies to review, the presence of multiple nodules within the lungs, and the small size of many nodules, which complicates visual assessment. Consequently, the development of automated systems that incorporate highly accurate and computationally efficient lung nodule detection and classification modules is essential. This study introduces three methodological improvements for lung nodule classification: (1) an advanced CT scan cropping strategy that focuses the model on the target nodule while reducing computational cost; (2) target filtering techniques for removing noisy labels; (3) novel augmentation methods to improve model robustness. The integration of these techniques enables the development of a robust classification subsystem within a comprehensive Clinical Decision Support System for lung cancer detection, capable of operating across diverse acquisition protocols, scanner types, and upstream models (segmentation or detection). The multiclass model achieved a Macro ROC AUC of 0.9176 and a Macro F1-score of 0.7658, while the binary model reached a Binary ROC AUC of 0.9383 and a Binary F1-score of 0.8668 on the LIDC-IDRI dataset. These results outperform several previously reported approaches and demonstrate state-of-the-art performance for this task.

