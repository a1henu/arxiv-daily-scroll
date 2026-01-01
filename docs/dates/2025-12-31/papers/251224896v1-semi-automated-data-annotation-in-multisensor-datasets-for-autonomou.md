---
layout: default
title: Semi-Automated Data Annotation in Multisensor Datasets for Autonomous Vehicle Testing
---

# Semi-Automated Data Annotation in Multisensor Datasets for Autonomous Vehicle Testing
**arXiv**：[2512.24896v1](https://arxiv.org/abs/2512.24896) · [PDF](https://arxiv.org/pdf/2512.24896.pdf)  
**作者**：Andrii Gamalii, Daniel Górniak, Robert Nowak, Bartłomiej Olber, Krystian Radlak, Jakub Winter  

**一句话要点**：提出半自动化数据标注流水线以加速自动驾驶测试中多传感器数据集标注

**关键词**：半自动化标注, 多传感器数据集, 3D目标检测, 自动驾驶测试, 数据匿名化, 域适应

## 3 点简述
- 核心问题：多传感器驾驶场景数据手动标注成本高、耗时久。
- 方法要点：结合AI与人工，采用3D目标检测生成初始标注，支持迭代模型重训练。
- 实验或效果：显著节省时间，确保跨传感器模态的高质量一致标注。

## 摘要（原文）

> This report presents the design and implementation of a semi-automated data annotation pipeline developed within the DARTS project, whose goal is to create a large-scale, multimodal dataset of driving scenarios recorded in Polish conditions. Manual annotation of such heterogeneous data is both costly and time-consuming. To address this challenge, the proposed solution adopts a human-in-the-loop approach that combines artificial intelligence with human expertise to reduce annotation cost and duration. The system automatically generates initial annotations, enables iterative model retraining, and incorporates data anonymization and domain adaptation techniques. At its core, the tool relies on 3D object detection algorithms to produce preliminary annotations. Overall, the developed tools and methodology result in substantial time savings while ensuring consistent, high-quality annotations across different sensor modalities. The solution directly supports the DARTS project by accelerating the preparation of large annotated dataset in the project's standardized format, strengthening the technological base for autonomous vehicle research in Poland.

