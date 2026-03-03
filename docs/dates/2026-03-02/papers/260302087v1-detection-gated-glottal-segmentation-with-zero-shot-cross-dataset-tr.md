---
layout: default
title: Detection-Gated Glottal Segmentation with Zero-Shot Cross-Dataset Transfer and Clinical Feature Extraction
---

# Detection-Gated Glottal Segmentation with Zero-Shot Cross-Dataset Transfer and Clinical Feature Extraction
**arXiv**：[2603.02087v1](https://arxiv.org/abs/2603.02087) · [PDF](https://arxiv.org/pdf/2603.02087.pdf)  
**作者**：Harikrishnan Unnikrishnan  

**一句话要点**：提出检测门控声门分割框架，通过零样本跨数据集迁移实现临床特征提取。

**关键词**：声门分割, 零样本迁移, 临床特征提取, 高速视频喉镜, 深度学习

## 3 点简述
- 现有深度学习模型在高速视频喉镜中易产生伪影且泛化性差。
- 结合YOLOv8检测器和U-Net分割器，加入时序一致性包装器提升鲁棒性。
- 在GIRAFE和BAGLS数据集上实现高性能，临床验证特征提取有效性。

## 摘要（原文）

> Background: Accurate glottal segmentation in high-speed videoendoscopy (HSV) is essential for extracting kinematic biomarkers of laryngeal function. However, existing deep learning models often produce spurious artifacts in non-glottal frames and fail to generalize across different clinical settings.
>   Methods: We propose a detection-gated pipeline that integrates a YOLOv8-based detector with a U-Net segmenter. A temporal consistency wrapper ensures robustness by suppressing false positives during glottal closure and instrument occlusion. The model was trained on a limited subset of the GIRAFE dataset (600 frames) and evaluated via zero-shot transfer on the large-scale BAGLS dataset.
>   Results: The pipeline achieved state-of-the-art performance on the GIRAFE benchmark (DSC 0.81) and demonstrated superior generalizability on BAGLS (DSC 0.85, in-distribution) without institutional fine-tuning. Downstream validation on a 65-subject clinical cohort confirmed that automated kinematic features (Open Quotient, coefficient of variation) remained consistent with established clinical benchmarks. The coefficient of variation (CV) of the glottal area was found to be a significant marker for distinguishing healthy from pathological vocal function (p=0.006).
>   Conclusions: The detection-gated architecture provides a lightweight, computationally efficient solution (~35 frames/s) for real-time clinical use. By enabling robust zero-shot transfer, this framework facilitates the standardized, large-scale extraction of clinical biomarkers across diverse endoscopy platforms. Code, trained weights, and evaluation scripts are released at https://github.com/hari-krishnan/openglottal.

