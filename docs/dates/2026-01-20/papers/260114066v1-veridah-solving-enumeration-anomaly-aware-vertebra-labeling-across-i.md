---
layout: default
title: VERIDAH: Solving Enumeration Anomaly Aware Vertebra Labeling across Imaging Sequences
---

# VERIDAH: Solving Enumeration Anomaly Aware Vertebra Labeling across Imaging Sequences
**arXiv**：[2601.14066v1](https://arxiv.org/abs/2601.14066) · [PDF](https://arxiv.org/pdf/2601.14066.pdf)  
**作者**：Hendrik Möller, Hanna Schoen, Robert Graf, Matan Atad, Nathan Molinier, Anjany Sekuboyina, Bettina K. Budai, Fabian Bamberg, Steffen Ringhof, Christopher Schlett, Tobias Pischon, Thoralf Niendorf, Josua A. Decker, Marc-André Weber, Bjoern Menze, Daniel Rueckert, Jan S. Kirschke  

**一句话要点**：提出VERIDAH算法以解决脊柱成像序列中枚举异常感知的椎骨标记问题

**关键词**：椎骨标记, 枚举异常, 深度学习, 医学影像分析, 脊柱成像

## 3 点简述
- 核心问题：脊柱成像中枚举异常（如胸椎11或13节）的自动标记方法缺乏，影响临床评估。
- 方法要点：基于多分类头与加权椎骨序列预测算法，实现异常感知的椎骨标记。
- 实验或效果：在T2w和CT图像上超越现有模型，正确标记所有椎骨的比例显著提高，异常检测准确率高。

## 摘要（原文）

> The human spine commonly consists of seven cervical, twelve thoracic, and five lumbar vertebrae. However, enumeration anomalies may result in individuals having eleven or thirteen thoracic vertebrae and four or six lumbar vertebrae. Although the identification of enumeration anomalies has potential clinical implications for chronic back pain and operation planning, the thoracolumbar junction is often poorly assessed and rarely described in clinical reports. Additionally, even though multiple deep-learning-based vertebra labeling algorithms exist, there is a lack of methods to automatically label enumeration anomalies. Our work closes that gap by introducing "Vertebra Identification with Anomaly Handling" (VERIDAH), a novel vertebra labeling algorithm based on multiple classification heads combined with a weighted vertebra sequence prediction algorithm. We show that our approach surpasses existing models on T2w TSE sagittal (98.30% vs. 94.24% of subjects with all vertebrae correctly labeled, p < 0.001) and CT imaging (99.18% vs. 77.26% of subjects with all vertebrae correctly labeled, p < 0.001) and works in arbitrary field-of-view images. VERIDAH correctly labeled the presence 2 Möller et al. of thoracic enumeration anomalies in 87.80% and 96.30% of T2w and CT images, respectively, and lumbar enumeration anomalies in 94.48% and 97.22% for T2w and CT, respectively. Our code and models are available at: https://github.com/Hendrik-code/spineps.

