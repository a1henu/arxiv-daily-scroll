---
layout: default
title: Facial Expression Recognition with YOLOv11 and YOLOv12: A Comparative Study
---

# Facial Expression Recognition with YOLOv11 and YOLOv12: A Comparative Study
**arXiv**：[2511.10940v1](https://arxiv.org/abs/2511.10940) · [PDF](https://arxiv.org/pdf/2511.10940.pdf)  
**作者**：Umma Aymon, Nur Shazwani Kamarudin, Ahmad Fakhri Ab. Nasir  

**一句话要点**：比较YOLOv11n与YOLOv12n在面部表情识别中的性能，评估轻量模型在真实世界应用中的平衡。

**关键词**：面部表情识别, YOLO轻量模型, 检测分类框架, 性能评估, 实时应用

## 3 点简述
- 核心问题：面部表情识别在无约束真实环境中仍具挑战性。
- 方法要点：使用YOLOv11n和YOLOv12n轻量模型，统一检测与分类框架。
- 实验效果：YOLOv12n在KDEF数据集mAP达95.6，YOLOv11n在FER2013精度更高。

## 摘要（原文）

> Facial Expression Recognition remains a challenging task, especially in unconstrained, real-world environments. This study investigates the performance of two lightweight models, YOLOv11n and YOLOv12n, which are the nano variants of the latest official YOLO series, within a unified detection and classification framework for FER. Two benchmark classification datasets, FER2013 and KDEF, are converted into object detection format and model performance is evaluated using mAP 0.5, precision, recall, and confusion matrices. Results show that YOLOv12n achieves the highest overall performance on the clean KDEF dataset with a mAP 0.5 of 95.6, and also outperforms YOLOv11n on the FER2013 dataset in terms of mAP 63.8, reflecting stronger sensitivity to varied expressions. In contrast, YOLOv11n demonstrates higher precision 65.2 on FER2013, indicating fewer false positives and better reliability in noisy, real-world conditions. On FER2013, both models show more confusion between visually similar expressions, while clearer class separation is observed on the cleaner KDEF dataset. These findings underscore the trade-off between sensitivity and precision, illustrating how lightweight YOLO models can effectively balance performance and efficiency. The results demonstrate adaptability across both controlled and real-world conditions, establishing these models as strong candidates for real-time, resource-constrained emotion-aware AI applications.

