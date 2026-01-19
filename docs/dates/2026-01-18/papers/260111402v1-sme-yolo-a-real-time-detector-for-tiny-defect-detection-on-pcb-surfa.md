---
layout: default
title: SME-YOLO: A Real-Time Detector for Tiny Defect Detection on PCB Surfaces
---

# SME-YOLO: A Real-Time Detector for Tiny Defect Detection on PCB Surfaces
**arXiv**：[2601.11402v1](https://arxiv.org/abs/2601.11402) · [PDF](https://arxiv.org/pdf/2601.11402.pdf)  
**作者**：Meng Han  

**一句话要点**：提出SME-YOLO以解决PCB表面微小缺陷实时检测的挑战

**关键词**：微小目标检测, PCB缺陷检测, YOLO改进, 多尺度增强, 实时检测

## 3 点简述
- 核心问题：PCB缺陷微小、纹理相似且尺度分布不均，导致高精度检测困难。
- 方法要点：采用NWDLoss缓解IoU对微小目标位置偏差的敏感，EUCB增强细节恢复，MSFA模块自适应强化关键尺度感知。
- 实验或效果：在PKU-PCB数据集上，相比基线YOLOv11n，mAP提升2.2%，精确率提升4%。

## 摘要（原文）

> Surface defects on Printed Circuit Boards (PCBs) directly compromise product reliability and safety. However, achieving high-precision detection is challenging because PCB defects are typically characterized by tiny sizes, high texture similarity, and uneven scale distributions. To address these challenges, this paper proposes a novel framework based on YOLOv11n, named SME-YOLO (Small-target Multi-scale Enhanced YOLO). First, we employ the Normalized Wasserstein Distance Loss (NWDLoss). This metric effectively mitigates the sensitivity of Intersection over Union (IoU) to positional deviations in tiny objects. Second, the original upsampling module is replaced by the Efficient Upsampling Convolution Block (EUCB). By utilizing multi-scale convolutions, the EUCB gradually recovers spatial resolution and enhances the preservation of edge and texture details for tiny defects. Finally, this paper proposes the Multi-Scale Focused Attention (MSFA) module. Tailored to the specific spatial distribution of PCB defects, this module adaptively strengthens perception within key scale intervals, achieving efficient fusion of local fine-grained features and global context information. Experimental results on the PKU-PCB dataset demonstrate that SME-YOLO achieves state-of-the-art performance. Specifically, compared to the baseline YOLOv11n, SME-YOLO improves mAP by 2.2% and Precision by 4%, validating the effectiveness of the proposed method.

