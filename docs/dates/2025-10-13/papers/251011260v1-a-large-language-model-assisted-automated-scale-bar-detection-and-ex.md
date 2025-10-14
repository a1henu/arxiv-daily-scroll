---
layout: default
title: A Large-Language-Model Assisted Automated Scale Bar Detection and Extraction Framework for Scanning Electron Microscopic Images
---

# A Large-Language-Model Assisted Automated Scale Bar Detection and Extraction Framework for Scanning Electron Microscopic Images
**arXiv**：[2510.11260v1](https://arxiv.org/abs/2510.11260) · [PDF](https://arxiv.org/pdf/2510.11260.pdf)  
**作者**：Yuxuan Chen, Ruotong Yang, Zhengyang Zhang, Mehreen Ahmed, Yanming Wang  

**一句话要点**：提出多模态自动化标尺检测提取框架，结合LLM提升SEM图像分析效率与准确性

**关键词**：标尺检测, 多模态框架, 大型语言模型, 光学字符识别, 扫描电子显微镜图像, 自动化分析

## 3 点简述
- 核心问题：SEM图像标尺检测依赖人工，耗时且易错。
- 方法要点：四阶段框架，包括自动数据集生成、对象检测、混合OCR和LLM验证。
- 实验或效果：对象检测mAP达99.2%，OCR F1分数75%，显著优于主流引擎。

## 摘要（原文）

> Microscopic characterizations, such as Scanning Electron Microscopy (SEM),
> are widely used in scientific research for visualizing and analyzing
> microstructures. Determining the scale bars is an important first step of
> accurate SEM analysis; however, currently, it mainly relies on manual
> operations, which is both time-consuming and prone to errors. To address this
> issue, we propose a multi-modal and automated scale bar detection and
> extraction framework that provides concurrent object detection, text detection
> and text recognition with a Large Language Model (LLM) agent. The proposed
> framework operates in four phases; i) Automatic Dataset Generation (Auto-DG)
> model to synthesize a diverse dataset of SEM images ensuring robust training
> and high generalizability of the model, ii) scale bar object detection, iii)
> information extraction using a hybrid Optical Character Recognition (OCR)
> system with DenseNet and Convolutional Recurrent Neural Network (CRNN) based
> algorithms, iv) an LLM agent to analyze and verify accuracy of the results. The
> proposed model demonstrates a strong performance in object detection and
> accurate localization with a precision of 100%, recall of 95.8%, and a mean
> Average Precision (mAP) of 99.2% at IoU=0.5 and 69.1% at IoU=0.5:0.95. The
> hybrid OCR system achieved 89% precision, 65% recall, and a 75% F1 score on the
> Auto-DG dataset, significantly outperforming several mainstream standalone
> engines, highlighting its reliability for scientific image analysis. The LLM is
> introduced as a reasoning engine as well as an intelligent assistant that
> suggests follow-up steps and verifies the results. This automated method
> powered by an LLM agent significantly enhances the efficiency and accuracy of
> scale bar detection and extraction in SEM images, providing a valuable tool for
> microscopic analysis and advancing the field of scientific imaging.

