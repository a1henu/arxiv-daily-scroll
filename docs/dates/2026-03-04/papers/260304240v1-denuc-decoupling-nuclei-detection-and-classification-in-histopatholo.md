---
layout: default
title: DeNuC: Decoupling Nuclei Detection and Classification in Histopathology
---

# DeNuC: Decoupling Nuclei Detection and Classification in Histopathology
**arXiv**：[2603.04240v1](https://arxiv.org/abs/2603.04240) · [PDF](https://arxiv.org/pdf/2603.04240.pdf)  
**作者**：Zijiang Yang, Chen Kuang, Dongmei Fu  

**一句话要点**：提出DeNuC方法，通过解耦检测与分类解决病理图像中细胞核识别性能瓶颈问题。

**关键词**：病理图像分析, 细胞核检测, 任务解耦, 基础模型应用, 轻量模型

## 3 点简述
- 核心问题：病理基础模型在细胞核检测与分类联合优化中表现不佳，存在表示退化和计算负担。
- 方法要点：采用轻量模型定位细胞核，再基于坐标用病理基础模型查询特征进行分类，实现任务解耦。
- 实验或效果：在多个基准测试中显著提升性能，如BRCAM2C和PUMA数据集F1分数提高超3.6%，参数仅需16%。

## 摘要（原文）

> Pathology Foundation Models (FMs) have shown strong performance across a wide range of pathology image representation and diagnostic tasks. However, FMs do not exhibit the expected performance advantage over traditional specialized models in Nuclei Detection and Classification (NDC). In this work, we reveal that jointly optimizing nuclei detection and classification leads to severe representation degradation in FMs. Moreover, we identify that the substantial intrinsic disparity in task difficulty between nuclei detection and nuclei classification renders joint NDC optimization unnecessarily computationally burdensome for the detection stage. To address these challenges, we propose DeNuC, a simple yet effective method designed to break through existing bottlenecks by Decoupling Nuclei detection and Classification. DeNuC employs a lightweight model for accurate nuclei localization, subsequently leveraging a pathology FM to encode input images and query nucleus-specific features based on the detected coordinates for classification. Extensive experiments on three widely used benchmarks demonstrate that DeNuC effectively unlocks the representational potential of FMs for NDC and significantly outperforms state-of-the-art methods. Notably, DeNuC improves F1 scores by 4.2% and 3.6% (or higher) on the BRCAM2C and PUMA datasets, respectively, while using only 16% (or fewer) trainable parameters compared to other methods. Code is available at https://github.com/ZijiangY1116/DeNuC.

