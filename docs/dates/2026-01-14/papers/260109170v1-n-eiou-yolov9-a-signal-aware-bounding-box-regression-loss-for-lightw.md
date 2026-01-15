---
layout: default
title: N-EIoU-YOLOv9: A Signal-Aware Bounding Box Regression Loss for Lightweight Mobile Detection of Rice Leaf Diseases
---

# N-EIoU-YOLOv9: A Signal-Aware Bounding Box Regression Loss for Lightweight Mobile Detection of Rice Leaf Diseases
**arXiv**：[2601.09170v1](https://arxiv.org/abs/2601.09170) · [PDF](https://arxiv.org/pdf/2601.09170.pdf)  
**作者**：Dung Ta Nguyen Duc, Thanh Bui Dang, Hoang Le Minh, Tung Nguyen Viet, Huong Nguyen Thanh, Dong Trinh Cong  

**一句话要点**：提出N-EIoU-YOLOv9，一种基于信号感知边界框回归损失的轻量级水稻叶病移动检测方法。

**关键词**：边界框回归损失, 轻量级目标检测, 农业病害监测, 移动部署, 梯度优化

## 3 点简述
- 针对农业病害图像中小目标和低对比度目标检测困难的问题。
- 设计N-EIoU损失，结合非单调梯度聚焦和几何解耦原理，增强弱回归信号并减少梯度干扰。
- 在自收集数据集上验证，平均精度达90.3%，移动部署平均推理时间156毫秒/帧。

## 摘要（原文）

> In this work, we propose N EIoU YOLOv9, a lightweight detection framework based on a signal aware bounding box regression loss derived from non monotonic gradient focusing and geometric decoupling principles, referred to as N EIoU (Non monotonic Efficient Intersection over Union). The proposed loss reshapes localization gradients by combining non monotonic focusing with decoupled width and height optimization, thereby enhancing weak regression signals for hard samples with low overlap while reducing gradient interference. This design is particularly effective for small and low contrast targets commonly observed in agricultural disease imagery. The proposed N EIoU loss is integrated into a lightweight YOLOv9t architecture and evaluated on a self collected field dataset comprising 5908 rice leaf images across four disease categories and healthy leaves. Experimental results demonstrate consistent performance gains over the standard CIoU loss, achieving a mean Average Precision of 90.3 percent, corresponding to a 4.3 percent improvement over the baseline, with improved localization accuracy under stricter evaluation criteria. For practical validation, the optimized model is deployed on an Android device using TensorFlow Lite with Float16 quantization, achieving an average inference time of 156 milliseconds per frame while maintaining accuracy. These results confirm that the proposed approach effectively balances accuracy, optimization stability, and computational efficiency for edge based agricultural monitoring systems.

