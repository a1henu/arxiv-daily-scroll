---
layout: default
title: CER-HV: A CER-Based Human-in-the-Loop Framework for Cleaning Datasets Applied to Arabic-Script HTR
---

# CER-HV: A CER-Based Human-in-the-Loop Framework for Cleaning Datasets Applied to Arabic-Script HTR
**arXiv**：[2601.16713v1](https://arxiv.org/abs/2601.16713) · [PDF](https://arxiv.org/pdf/2601.16713.pdf)  
**作者**：Sana Al-azzawi, Elisa Barney, Marcus Liwicki  

**一句话要点**：提出CER-HV框架，基于字符错误率检测与人工验证，用于清理阿拉伯文字手写文本识别数据集中的标签错误。

**关键词**：手写文本识别, 数据清理, 人工循环, 字符错误率, 阿拉伯文字, 卷积循环神经网络

## 3 点简述
- 阿拉伯文字手写文本识别因数据质量问题受限，现有数据集存在转录、分割等未充分报告的错误。
- CER-HV结合CRNN噪声检测器与人工验证步骤，以高精度识别错误样本，提升数据质量。
- 实验在多个数据集上验证了框架有效性，CER-HV应用后CER降低0.3-1.8%，CRNN模型在未清理数据上达到先进性能。

## 摘要（原文）

> Handwritten text recognition (HTR) for Arabic-script languages still lags behind Latin-script HTR, despite recent advances in model architectures, datasets, and benchmarks. We show that data quality is a significant limiting factor in many published datasets and propose CER-HV (CER-based Ranking with Human Verification) as a framework to detect and clean label errors. CER-HV combines a CER-based noise detector, built on a carefully configured Convolutional Recurrent Neural Network (CRNN) with early stopping to avoid overfitting noisy samples, and a human-in-the-loop (HITL) step that verifies high-ranking samples. The framework reveals that several existing datasets contain previously underreported problems, including transcription, segmentation, orientation, and non-text content errors. These have been identified with up to 90 percent precision in the Muharaf and 80-86 percent in the PHTI datasets.
>   We also show that our CRNN achieves state-of-the-art performance across five of the six evaluated datasets, reaching 8.45 percent Character Error Rate (CER) on KHATT (Arabic), 8.26 percent on PHTI (Pashto), 10.66 percent on Ajami, and 10.11 percent on Muharaf (Arabic), all without any data cleaning. We establish a new baseline of 11.3 percent CER on the PHTD (Persian) dataset. Applying CER-HV improves the evaluation CER by 0.3-0.6 percent on the cleaner datasets and 1.0-1.8 percent on the noisier ones. Although our experiments focus on documents written in an Arabic-script language, including Arabic, Persian, Urdu, Ajami, and Pashto, the framework is general and can be applied to other text recognition datasets.

