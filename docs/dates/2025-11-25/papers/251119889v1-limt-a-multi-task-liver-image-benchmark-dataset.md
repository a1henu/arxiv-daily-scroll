---
layout: default
title: LiMT: A Multi-task Liver Image Benchmark Dataset
---

# LiMT: A Multi-task Liver Image Benchmark Dataset
**arXiv**：[2511.19889v1](https://arxiv.org/abs/2511.19889) · [PDF](https://arxiv.org/pdf/2511.19889.pdf)  
**作者**：Zhe Liu, Kai Han, Siqi Ma, Yan Zhu, Jun Chen, Chongwen Lyu, Xinyi Qiu, Chengxuan Qian, Yuqing Song, Yi Liu, Liyuan Tian, Yang Ji, Yuefeng Li  

**一句话要点**：提出LiMT多任务肝脏图像数据集以解决现有数据集仅支持单任务的问题

**关键词**：肝脏图像数据集, 多任务学习, 计算机辅助诊断, CT图像分割, 病变检测, 医学影像基准

## 3 点简述
- 现有肝脏CAD数据集多限于单任务，限制了技术发展
- 构建基于动脉期增强CT的多任务数据集，支持分割、分类和检测
- 提供150例CT数据、基线实验和数据集回顾，促进医学影像研究

## 摘要（原文）

> Computer-aided diagnosis (CAD) technology can assist clinicians in evaluating liver lesions and intervening with treatment in time. Although CAD technology has advanced in recent years, the application scope of existing datasets remains relatively limited, typically supporting only single tasks, which has somewhat constrained the development of CAD technology. To address the above limitation, in this paper, we construct a multi-task liver dataset (LiMT) used for liver and tumor segmentation, multi-label lesion classification, and lesion detection based on arterial phase-enhanced computed tomography (CT), potentially providing an exploratory solution that is able to explore the correlation between tasks and does not need to worry about the heterogeneity between task-specific datasets during training. The dataset includes CT volumes from 150 different cases, comprising four types of liver diseases as well as normal cases. Each volume has been carefully annotated and calibrated by experienced clinicians. This public multi-task dataset may become a valuable resource for the medical imaging research community in the future. In addition, this paper not only provides relevant baseline experimental results but also reviews existing datasets and methods related to liver-related tasks. Our dataset is available at https://drive.google.com/drive/folders/1l9HRK13uaOQTNShf5pwgSz3OTanWjkag?usp=sharing.

