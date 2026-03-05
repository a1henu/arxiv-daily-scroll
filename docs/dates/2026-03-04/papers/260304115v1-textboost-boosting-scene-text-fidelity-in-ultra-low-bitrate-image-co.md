---
layout: default
title: TextBoost: Boosting Scene Text Fidelity in Ultra-low Bitrate Image Compression
---

# TextBoost: Boosting Scene Text Fidelity in Ultra-low Bitrate Image Compression
**arXiv**：[2603.04115v1](https://arxiv.org/abs/2603.04115) · [PDF](https://arxiv.org/pdf/2603.04115.pdf)  
**作者**：Bingxin Wang, Yuan Lan, Zhaoyi Sun, Yang Xiang, Jie Sun  

**一句话要点**：提出TextBoost方法，通过OCR辅助信息提升超低码率图像压缩中的场景文本保真度

**关键词**：超低码率图像压缩, 场景文本保真, OCR辅助引导, 注意力融合, 正则化损失

## 3 点简述
- 超低码率压缩中，小字体场景文本保真与全局视觉质量存在权衡问题
- 利用OCR提取文本信息作为语义引导，通过注意力融合和正则化损失增强文本区域重建
- 在TextOCR和ICDAR 2015数据集上，文本识别F1分数提升高达60.6%，同时保持PSNR和bpp

## 摘要（原文）

> Ultra-low bitrate image compression faces a critical challenge: preserving small-font scene text while maintaining overall visual quality. Region-of-interest (ROI) bit allocation can prioritize text but often degrades global fidelity, leading to a trade-off between local accuracy and overall image quality. Instead of relying on ROI coding, we incorporate auxiliary textual information extracted by OCR and transmitted with negligible overhead, enabling the decoder to leverage this semantic guidance. Our method, TextBoost, operationalizes this idea through three strategic designs: (i) adaptively filtering OCR outputs and rendering them into a guidance map; (ii) integrating this guidance with decoder features in a calibrated manner via an attention-guided fusion block; and (iii) enforcing guidance-consistent reconstruction in text regions with a regularizing loss that promotes natural blending with the scene. Extensive experiments on TextOCR and ICDAR 2015 demonstrate that TextBoost yields up to 60.6% higher text-recognition F1 at comparable Peak Signal-to-Noise Ratio (PSNR) and bits per pixel (bpp), producing sharper small-font text while preserving global image quality and effectively decoupling text enhancement from global rate-distortion optimization.

