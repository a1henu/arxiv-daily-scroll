---
layout: default
title: SOS: Synthetic Object Segments Improve Detection, Segmentation, and Grounding
---

# SOS: Synthetic Object Segments Improve Detection, Segmentation, and Grounding
**arXiv**：[2510.09110v1](https://arxiv.org/abs/2510.09110) · [PDF](https://arxiv.org/pdf/2510.09110.pdf)  
**作者**：Weikai Huang, Jieyu Zhang, Taoyang Jia, Chenhao Zheng, Ziqi Gao, Jae Sung Park, Ranjay Krishna  

**一句话要点**：提出SOS合成数据管道以提升视觉检测、分割和接地任务性能

**关键词**：合成数据生成, 对象检测, 实例分割, 视觉接地, 数据增强, 泛化性能

## 3 点简述
- 视觉分组任务依赖大规模标注数据，但真实数据成本高、覆盖偏差且难以扩展
- SOS通过对象中心合成策略，结合布局先验和生成重光照，生成高质量合成对象片段
- 在检测和接地任务中，SOS训练模型优于大型真实数据集，并增强低数据场景泛化能力

## 摘要（原文）

> Visual grouping -- operationalized via instance segmentation, visual
> grounding, and object detection -- underpins applications from robotic
> perception to photo editing. Large annotated datasets are costly, biased in
> coverage, and hard to scale. Synthetic data are promising but often lack
> flexibility, accuracy, and compositional diversity.
>   We present SOS, a simple and scalable data synthesis pipeline based on an
> object-centric composition strategy. It pastes high-quality synthetic object
> segments into new images using structured layout priors and generative
> relighting, producing accurate and diverse masks, boxes, and referring
> expressions. Models trained on 100000 synthetic images from SOS outperform
> those trained on larger real-image datasets such as GRIT (20M) and V3Det (200K)
> on detection and grounding tasks, achieving +10.9 AP on LVIS detection and +8.4
> $N_{\text{Acc}}$ on gRefCOCO grounding. SOS enables controllable dataset
> construction and improves generalization in both low-data and closed-vocabulary
> settings. Augmenting LVIS and COCO with synthetic object segments yields strong
> performance across real-data scales and even larger gains under extremely
> limited real data (for example, +3.83 $AP_{\text{rare}}$ on LVIS instance
> segmentation and +6.59 AP with a 1 percent COCO setup). This controllability
> also supports targeted data generation for challenging intra-class referring in
> visual grounding.

