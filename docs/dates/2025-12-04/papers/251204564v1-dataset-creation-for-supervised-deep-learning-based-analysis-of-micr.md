---
layout: default
title: Dataset creation for supervised deep learning-based analysis of microscopic images - review of important considerations and recommendations
---

# Dataset creation for supervised deep learning-based analysis of microscopic images - review of important considerations and recommendations
**arXiv**：[2512.04564v1](https://arxiv.org/abs/2512.04564) · [PDF](https://arxiv.org/pdf/2512.04564.pdf)  
**作者**：Christof A. Bertram, Viktoria Weiss, Jonas Ammeling, F. Maria Schabel, Taryn A. Donovan, Frauke Wilm, Christian Marzahl, Katharina Breininger, Marc Aubreville  

**一句话要点**：综述显微镜图像监督深度学习数据集创建的关键考虑与推荐，以提升病理学应用模型泛化性

**关键词**：显微镜图像分析, 监督深度学习, 数据集创建, 标注质量, 病理学应用, 领域变异

## 3 点简述
- 核心问题：高质量大规模数据集创建面临资源密集、领域变异和标注偏差等挑战
- 方法要点：涵盖图像采集、标注软件选择和标注创建，强调处理图像变异性和标注质量三C标准
- 实验或效果：提供标准操作程序作为补充材料，促进开放数据集以增强研究可重复性和创新

## 摘要（原文）

> Supervised deep learning (DL) receives great interest for automated analysis of microscopic images with an increasing body of literature supporting its potential. The development and validation of those DL models relies heavily on the availability of high-quality, large-scale datasets. However, creating such datasets is a complex and resource-intensive process, often hindered by challenges such as time constraints, domain variability, and risks of bias in image collection and label creation. This review provides a comprehensive guide to the critical steps in dataset creation, including: 1) image acquisition, 2) selection of annotation software, and 3) annotation creation. In addition to ensuring a sufficiently large number of images, it is crucial to address sources of image variability (domain shifts) - such as those related to slide preparation and digitization - that could lead to algorithmic errors if not adequately represented in the training data. Key quality criteria for annotations are the three "C"s: correctness, completeness, and consistency. This review explores methods to enhance annotation quality through the use of advanced techniques that mitigate the limitations of single annotators. To support dataset creators, a standard operating procedure (SOP) is provided as supplemental material, outlining best practices for dataset development. Furthermore, the article underscores the importance of open datasets in driving innovation and enhancing reproducibility of DL research. By addressing the challenges and offering practical recommendations, this review aims to advance the creation of and availability to high-quality, large-scale datasets, ultimately contributing to the development of generalizable and robust DL models for pathology applications.

