---
layout: default
title: Detection Fire in Camera RGB-NIR
---

# Detection Fire in Camera RGB-NIR
**arXiv**：[2512.23594v1](https://arxiv.org/abs/2512.23594) · [PDF](https://arxiv.org/pdf/2512.23594.pdf)  
**作者**：Nguyen Truong Khai, Luong Duc Vinh  

**一句话要点**：提出两阶段检测模型与Patched-YOLO以提升红外夜视相机火灾检测精度并减少误报

**关键词**：火灾检测, 红外夜视相机, 两阶段检测模型, 数据增强, Patched-YOLO, 误报减少

## 3 点简述
- 核心问题：红外夜视相机火灾检测中，数据集不足和人工亮光误分类影响准确性。
- 方法要点：引入额外NIR数据集，结合YOLOv11和EfficientNetV2-B0的两阶段检测模型，以及基于补丁处理的Patched-YOLO。
- 实验或效果：相比YOLOv7、RT-DETR和YOLOv9，新方法在夜间火灾检测中实现更高精度，减少误报。

## 摘要（原文）

> Improving the accuracy of fire detection using infrared night vision cameras remains a challenging task. Previous studies have reported strong performance with popular detection models. For example, YOLOv7 achieved an mAP50-95 of 0.51 using an input image size of 640 x 1280, RT-DETR reached an mAP50-95 of 0.65 with an image size of 640 x 640, and YOLOv9 obtained an mAP50-95 of 0.598 at the same resolution. Despite these results, limitations in dataset construction continue to cause issues, particularly the frequent misclassification of bright artificial lights as fire.
>   This report presents three main contributions: an additional NIR dataset, a two-stage detection model, and Patched-YOLO. First, to address data scarcity, we explore and apply various data augmentation strategies for both the NIR dataset and the classification dataset. Second, to improve night-time fire detection accuracy while reducing false positives caused by artificial lights, we propose a two-stage pipeline combining YOLOv11 and EfficientNetV2-B0. The proposed approach achieves higher detection accuracy compared to previous methods, particularly for night-time fire detection. Third, to improve fire detection in RGB images, especially for small and distant objects, we introduce Patched-YOLO, which enhances the model's detection capability through patch-based processing. Further details of these contributions are discussed in the following sections.

