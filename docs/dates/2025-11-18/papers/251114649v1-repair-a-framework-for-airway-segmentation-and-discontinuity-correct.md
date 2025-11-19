---
layout: default
title: RepAir: A Framework for Airway Segmentation and Discontinuity Correction in CT
---

# RepAir: A Framework for Airway Segmentation and Discontinuity Correction in CT
**arXiv**：[2511.14649v1](https://arxiv.org/abs/2511.14649) · [PDF](https://arxiv.org/pdf/2511.14649.pdf)  
**作者**：John M. Oyer, Ali Namvar, Benjamin A. Hoff, Wassim W. Labaki, Ella A. Kazerooni, Charles R. Hatt, Fernando J. Martinez, MeiLan K. Han, Craig J. Galbán, Sundaresh Ram  

**一句话要点**：提出RepAir框架以解决CT气道分割中的不连续性问题

**关键词**：气道分割, CT图像处理, 拓扑校正, nnU-Net, 骨架算法, 1D卷积分类器

## 3 点简述
- 核心问题：自动U-Net方法在CT气道分割中产生不连续组件，影响生物标志物提取。
- 方法要点：结合nnU-Net分割、骨架算法识别不连续，并使用1D卷积分类器校正拓扑。
- 实验或效果：在健康和病理数据集上优于现有方法，提升分割完整性和拓扑准确性。

## 摘要（原文）

> Accurate airway segmentation from chest computed tomography (CT) scans is essential for quantitative lung analysis, yet manual annotation is impractical and many automated U-Net-based methods yield disconnected components that hinder reliable biomarker extraction. We present RepAir, a three-stage framework for robust 3D airway segmentation that combines an nnU-Net-based network with anatomically informed topology correction. The segmentation network produces an initial airway mask, after which a skeleton-based algorithm identifies potential discontinuities and proposes reconnections. A 1D convolutional classifier then determines which candidate links correspond to true anatomical branches versus false or obstructed paths. We evaluate RepAir on two distinct datasets: ATM'22, comprising annotated CT scans from predominantly healthy subjects and AeroPath, encompassing annotated scans with severe airway pathology. Across both datasets, RepAir outperforms existing 3D U-Net-based approaches such as Bronchinet and NaviAirway on both voxel-level and topological metrics, and produces more complete and anatomically consistent airway trees while maintaining high segmentation accuracy.

