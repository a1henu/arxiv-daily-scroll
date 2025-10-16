---
layout: default
title: DEF-YOLO: Leveraging YOLO for Concealed Weapon Detection in Thermal Imagin
---

# DEF-YOLO: Leveraging YOLO for Concealed Weapon Detection in Thermal Imagin
**arXiv**：[2510.13326v1](https://arxiv.org/abs/2510.13326) · [PDF](https://arxiv.org/pdf/2510.13326.pdf)  
**作者**：Divya Bhardwaj, Arnav Ramamoorthy, Poonam Goyal  

**一句话要点**：提出DEF-YOLO与TICW数据集以解决热成像隐蔽武器检测问题

**关键词**：隐蔽武器检测, 热成像, YOLO架构, 可变形卷积, 焦点损失, 数据集贡献

## 3 点简述
- 核心问题：热成像隐蔽武器检测缺乏基准数据集，且存在类不平衡和热均匀区域定位挑战。
- 方法要点：基于YOLOv8引入可变形卷积和焦点损失，增强多尺度特征提取和类不平衡处理。
- 实验或效果：通过广泛实验建立新基准，实现实时检测而不显著牺牲速度和吞吐量。

## 摘要（原文）

> Concealed weapon detection aims at detecting weapons hidden beneath a
> person's clothing or luggage. Various imaging modalities like Millimeter Wave,
> Microwave, Terahertz, Infrared, etc., are exploited for the concealed weapon
> detection task. These imaging modalities have their own limitations, such as
> poor resolution in microwave imaging, privacy concerns in millimeter wave
> imaging, etc. To provide a real-time, 24 x 7 surveillance, low-cost, and
> privacy-preserved solution, we opted for thermal imaging in spite of the lack
> of availability of a benchmark dataset. We propose a novel approach and a
> dataset for concealed weapon detection in thermal imagery. Our YOLO-based
> architecture, DEF-YOLO, is built with key enhancements in YOLOv8 tailored to
> the unique challenges of concealed weapon detection in thermal vision. We adopt
> deformable convolutions at the SPPF layer to exploit multi-scale features;
> backbone and neck layers to extract low, mid, and high-level features, enabling
> DEF-YOLO to adaptively focus on localization around the objects in thermal
> homogeneous regions, without sacrificing much of the speed and throughput. In
> addition to these simple yet effective key architectural changes, we introduce
> a new, large-scale Thermal Imaging Concealed Weapon dataset, TICW, featuring a
> diverse set of concealed weapons and capturing a wide range of scenarios. To
> the best of our knowledge, this is the first large-scale contributed dataset
> for this task. We also incorporate focal loss to address the significant class
> imbalance inherent in the concealed weapon detection task. The efficacy of the
> proposed work establishes a new benchmark through extensive experimentation for
> concealed weapon detection in thermal imagery.

