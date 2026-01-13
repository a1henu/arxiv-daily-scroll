---
layout: default
title: Vision-Language Model for Accurate Crater Detection
---

# Vision-Language Model for Accurate Crater Detection
**arXiv**：[2601.07795v1](https://arxiv.org/abs/2601.07795) · [PDF](https://arxiv.org/pdf/2601.07795.pdf)  
**作者**：Patrick Bauer, Marius Schwinning, Florian Renk, Andreas Weinmann, Hichem Snoussi  

**一句话要点**：提出基于OWLv2的视觉语言模型，用于在月球图像中实现可靠的陨石坑检测。

**关键词**：陨石坑检测, 视觉语言模型, 参数高效微调, 月球图像分析, 目标检测

## 3 点简述
- 核心问题：月球陨石坑检测因尺寸形状多样、光照变化和崎岖地形而具有挑战性。
- 方法要点：采用OWLv2模型，结合LoRA参数高效微调和CIoU与对比损失优化。
- 实验或效果：在IMPACT测试集上达到94.0%召回率和73.1%精确率，视觉结果满意。

## 摘要（原文）

> The European Space Agency (ESA), driven by its ambitions on planned lunar missions with the Argonaut lander, has a profound interest in reliable crater detection, since craters pose a risk to safe lunar landings. This task is usually addressed with automated crater detection algorithms (CDA) based on deep learning techniques. It is non-trivial due to the vast amount of craters of various sizes and shapes, as well as challenging conditions such as varying illumination and rugged terrain. Therefore, we propose a deep-learning CDA based on the OWLv2 model, which is built on a Vision Transformer, that has proven highly effective in various computer vision tasks. For fine-tuning, we utilize a manually labeled dataset fom the IMPACT project, that provides crater annotations on high-resolution Lunar Reconnaissance Orbiter Camera Calibrated Data Record images. We insert trainable parameters using a parameter-efficient fine-tuning strategy with Low-Rank Adaptation, and optimize a combined loss function consisting of Complete Intersection over Union (CIoU) for localization and a contrastive loss for classification. We achieve satisfactory visual results, along with a maximum recall of 94.0% and a maximum precision of 73.1% on a test dataset from IMPACT. Our method achieves reliable crater detection across challenging lunar imaging conditions, paving the way for robust crater analysis in future lunar exploration.

