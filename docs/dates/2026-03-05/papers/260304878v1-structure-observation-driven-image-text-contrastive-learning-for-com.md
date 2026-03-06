---
layout: default
title: Structure Observation Driven Image-Text Contrastive Learning for Computed Tomography Report Generation
---

# Structure Observation Driven Image-Text Contrastive Learning for Computed Tomography Report Generation
**arXiv**：[2603.04878v1](https://arxiv.org/abs/2603.04878) · [PDF](https://arxiv.org/pdf/2603.04878.pdf)  
**作者**：Hong Liu, Dong Wei, Qiong Peng, Yawen Huang, Xian Wu, Yefeng Zheng, Liansheng Wang  

**一句话要点**：提出结构观察驱动的图像-文本对比学习框架以解决CT报告生成中的语义对齐问题

**关键词**：CT报告生成, 图像-文本对比学习, 结构观察, 语义对齐, 深度学习

## 3 点简述
- 核心问题：CT图像数据量大、细节复杂，现有方法在CT报告生成中效果受限，需提升图像与报告间的结构级语义对应。
- 方法要点：采用两阶段框架，第一阶段通过可学习结构查询进行图像-文本对比学习，第二阶段冻结查询并解码生成报告。
- 实验或效果：在两个公开数据集上实现最先进性能，验证了框架在临床效率和组件有效性方面的优势。

## 摘要（原文）

> Computed Tomography Report Generation (CTRG) aims to automate the clinical radiology reporting process, thereby reducing the workload of report writing and facilitating patient care. While deep learning approaches have achieved remarkable advances in X-ray report generation, their effectiveness may be limited in CTRG due to larger data volumes of CT images and more intricate details required to describe them. This work introduces a novel two-stage (structure- and report-learning) framework tailored for CTRG featuring effective structure-wise image-text contrasting. In the first stage, a set of learnable structure-specific visual queries observe corresponding structures in a CT image. The resulting observation tokens are contrasted with structure-specific textual features extracted from the accompanying radiology report with a structure-wise image-text contrastive loss. In addition, text-text similarity-based soft pseudo targets are proposed to mitigate the impact of false negatives, i.e., semantically identical image structures and texts from non-paired images and reports. Thus, the model learns structure-level semantic correspondences between CT images and reports. Further, a dynamic, diversity-enhanced negative queue is proposed to guide the network in learning to discriminate various abnormalities. In the second stage, the visual structure queries are frozen and used to select the critical image patch embeddings depicting each anatomical structure, minimizing distractions from irrelevant areas while reducing memory consumption. Also, a text decoder is added and trained for report generation.Our extensive experiments on two public datasets demonstrate that our framework establishes new state-of-the-art performance for CTRG in clinical efficiency, and its components are effective.

