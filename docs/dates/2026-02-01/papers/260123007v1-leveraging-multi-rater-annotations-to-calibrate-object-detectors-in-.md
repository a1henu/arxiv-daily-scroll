---
layout: default
title: Leveraging Multi-Rater Annotations to Calibrate Object Detectors in Microscopy Imaging
---

# Leveraging Multi-Rater Annotations to Calibrate Object Detectors in Microscopy Imaging
**arXiv**：[2601.23007v1](https://arxiv.org/abs/2601.23007) · [PDF](https://arxiv.org/pdf/2601.23007.pdf)  
**作者**：Francesco Campi, Lucrezia Tondo, Ekin Karabati, Johannes Betge, Marie Piraud  

**一句话要点**：提出基于多标注者注释的集成策略以校准显微镜成像中的目标检测器

**关键词**：目标检测, 模型校准, 多标注者注释, 显微镜成像, 生物医学应用, 集成学习

## 3 点简述
- 问题：深度学习目标检测器在显微镜成像中置信度估计缺乏校准，影响生物医学应用可靠性。
- 方法：利用多标注者注释，训练独立模型并集成预测以模拟共识，优于混合标注训练。
- 实验：在结直肠类器官数据集上验证，集成策略提升校准性能，保持检测精度。

## 摘要（原文）

> Deep learning-based object detectors have achieved impressive performance in microscopy imaging, yet their confidence estimates often lack calibration, limiting their reliability for biomedical applications. In this work, we introduce a new approach to improve model calibration by leveraging multi-rater annotations. We propose to train separate models on the annotations from single experts and aggregate their predictions to emulate consensus. This improves upon label sampling strategies, where models are trained on mixed annotations, and offers a more principled way to capture inter-rater variability. Experiments on a colorectal organoid dataset annotated by two experts demonstrate that our rater-specific ensemble strategy improves calibration performance while maintaining comparable detection accuracy. These findings suggest that explicitly modelling rater disagreement can lead to more trustworthy object detectors in biomedical imaging.

