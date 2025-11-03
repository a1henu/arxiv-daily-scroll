---
layout: default
title: Gaussian Combined Distance: A Generic Metric for Object Detection
---

# Gaussian Combined Distance: A Generic Metric for Object Detection
**arXiv**：[2510.27649v1](https://arxiv.org/abs/2510.27649) · [PDF](https://arxiv.org/pdf/2510.27649.pdf)  
**作者**：Ziqian Guan, Xieyi Fu, Pengjun Huang, Hengyuan Zhang, Hubin Du, Yongtao Liu, Yinglin Wang, Qang Ma  

**一句话要点**：提出高斯组合距离以解决小物体检测中IoU和Wasserstein距离的不足

**关键词**：物体检测, 相似性度量, 边界框回归, 小物体检测, 高斯分布, 损失函数

## 3 点简述
- IoU对小物体位置偏差敏感，Wasserstein距离缺乏尺度不变性且优化缓慢
- GCD具有尺度不变性，支持联合优化，提升模型定位性能
- 在AI-TOD-v2、MS-COCO-2017和Visdrone-2019数据集上实现SOTA性能

## 摘要（原文）

> In object detection, a well-defined similarity metric can significantly
> enhance model performance. Currently, the IoU-based similarity metric is the
> most commonly preferred choice for detectors. However, detectors using IoU as a
> similarity metric often perform poorly when detecting small objects because of
> their sensitivity to minor positional deviations. To address this issue, recent
> studies have proposed the Wasserstein Distance as an alternative to IoU for
> measuring the similarity of Gaussian-distributed bounding boxes. However, we
> have observed that the Wasserstein Distance lacks scale invariance, which
> negatively impacts the model's generalization capability. Additionally, when
> used as a loss function, its independent optimization of the center attributes
> leads to slow model convergence and unsatisfactory detection precision. To
> address these challenges, we introduce the Gaussian Combined Distance (GCD).
> Through analytical examination of GCD and its gradient, we demonstrate that GCD
> not only possesses scale invariance but also facilitates joint optimization,
> which enhances model localization performance. Extensive experiments on the
> AI-TOD-v2 dataset for tiny object detection show that GCD, as a bounding box
> regression loss function and label assignment metric, achieves state-of-the-art
> performance across various detectors. We further validated the generalizability
> of GCD on the MS-COCO-2017 and Visdrone-2019 datasets, where it outperforms the
> Wasserstein Distance across diverse scales of datasets. Code is available at
> https://github.com/MArKkwanGuan/mmdet-GCD.

