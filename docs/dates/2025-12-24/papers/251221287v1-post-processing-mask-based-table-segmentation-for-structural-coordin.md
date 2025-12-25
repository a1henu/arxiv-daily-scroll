---
layout: default
title: Post-Processing Mask-Based Table Segmentation for Structural Coordinate Extraction
---

# Post-Processing Mask-Based Table Segmentation for Structural Coordinate Extraction
**arXiv**：[2512.21287v1](https://arxiv.org/abs/2512.21287) · [PDF](https://arxiv.org/pdf/2512.21287.pdf)  
**作者**：Suren Bandara  

**一句话要点**：提出基于掩码的多尺度信号处理方法，以提升低质量图像中表格结构分割的准确性。

**关键词**：表格分割, 掩码处理, 信号处理, 边缘检测, 文档图像分析

## 3 点简述
- 核心问题：现有方法在低分辨率或噪声图像中难以准确提取表格行列边界。
- 方法要点：将行列过渡建模为一维信号，通过高斯卷积和统计阈值抑制噪声并保留边缘。
- 实验或效果：在PubLayNet-1M基准上，将CASA指标从67%提升至76%。

## 摘要（原文）

> Structured data extraction from tables plays a crucial role in document image analysis for scanned documents and digital archives. Although many methods have been proposed to detect table structures and extract cell contents, accurately identifying table segment boundaries (rows and columns) remains challenging, particularly in low-resolution or noisy images. In many real-world scenarios, table data are incomplete or degraded, limiting the adaptability of transformer-based methods to noisy inputs. Mask-based edge detection techniques have shown greater robustness under such conditions, as their sensitivity can be adjusted through threshold tuning; however, existing approaches typically apply masks directly to images, leading to noise sensitivity, resolution loss, or high computational cost. This paper proposes a novel multi-scale signal-processing method for detecting table edges from table masks. Row and column transitions are modeled as one-dimensional signals and processed using Gaussian convolution with progressively increasing variances, followed by statistical thresholding to suppress noise while preserving stable structural edges. Detected signal peaks are mapped back to image coordinates to obtain accurate segment boundaries. Experimental results show that applying the proposed approach to column edge detection improves Cell-Aware Segmentation Accuracy (CASA) a layout-aware metric evaluating both textual correctness and correct cell placement from 67% to 76% on the PubLayNet-1M benchmark when using TableNet with PyTesseract OCR. The method is robust to resolution variations through zero-padding and scaling strategies and produces optimized structured tabular outputs suitable for downstream analysis.

