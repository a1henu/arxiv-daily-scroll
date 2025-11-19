---
layout: default
title: Online Data Curation for Object Detection via Marginal Contributions to Dataset-level Average Precision
---

# Online Data Curation for Object Detection via Marginal Contributions to Dataset-level Average Precision
**arXiv**：[2511.14197v1](https://arxiv.org/abs/2511.14197) · [PDF](https://arxiv.org/pdf/2511.14197.pdf)  
**作者**：Zitang Sun, Masakazu Yoshimura, Junji Otsuka, Atsushi Irie, Takeshi Ohashi  

**一句话要点**：提出DetGain在线数据筛选方法以提升目标检测的数据效率

**关键词**：目标检测, 在线数据筛选, 平均精度, 知识蒸馏, 数据效率

## 3 点简述
- 核心问题：目标检测因结构复杂和领域差距，现有在线采样策略难以适用
- 方法要点：基于预测质量估计图像对数据集AP的边际贡献，选择信息样本
- 实验或效果：在COCO数据集上提高多种检测器精度，并增强鲁棒性

## 摘要（原文）

> High-quality data has become a primary driver of progress under scale laws, with curated datasets often outperforming much larger unfiltered ones at lower cost. Online data curation extends this idea by dynamically selecting training samples based on the model's evolving state. While effective in classification and multimodal learning, existing online sampling strategies rarely extend to object detection because of its structural complexity and domain gaps. We introduce DetGain, an online data curation method specifically for object detection that estimates the marginal perturbation of each image to dataset-level Average Precision (AP) based on its prediction quality. By modeling global score distributions, DetGain efficiently estimates the global AP change and computes teacher-student contribution gaps to select informative samples at each iteration. The method is architecture-agnostic and minimally intrusive, enabling straightforward integration into diverse object detection architectures. Experiments on the COCO dataset with multiple representative detectors show consistent improvements in accuracy. DetGain also demonstrates strong robustness under low-quality data and can be effectively combined with knowledge distillation techniques to further enhance performance, highlighting its potential as a general and complementary strategy for data-efficient object detection.

