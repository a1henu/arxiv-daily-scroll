---
layout: default
title: AttMetNet: Attention-Enhanced Deep Neural Network for Methane Plume Detection in Sentinel-2 Satellite Imagery
---

# AttMetNet: Attention-Enhanced Deep Neural Network for Methane Plume Detection in Sentinel-2 Satellite Imagery
**arXiv**：[2512.02751v1](https://arxiv.org/abs/2512.02751) · [PDF](https://arxiv.org/pdf/2512.02751.pdf)  
**作者**：Rakib Ahsan, MD Sadik Hossain Shanto, Md Sultanul Arifin, Tanzima Hashem  

**一句话要点**：提出AttMetNet注意力增强深度学习框架，用于Sentinel-2卫星图像中的甲烷羽流检测。

**关键词**：甲烷羽流检测, 注意力机制, Sentinel-2图像, 深度学习, 归一化甲烷指数, 焦点损失

## 3 点简述
- 核心问题：Sentinel-2卫星图像中甲烷羽流检测易受背景变化和多样地表覆盖干扰，导致高误报率。
- 方法要点：结合归一化甲烷指数与注意力增强U-Net，选择性放大甲烷吸收特征并抑制背景噪声。
- 实验或效果：在真实数据集上训练，使用焦点损失处理类别不平衡，实验显示误报率低、精度召回平衡好、IoU高。

## 摘要（原文）

> Methane is a powerful greenhouse gas that contributes significantly to global warming. Accurate detection of methane emissions is the key to taking timely action and minimizing their impact on climate change. We present AttMetNet, a novel attention-enhanced deep learning framework for methane plume detection with Sentinel-2 satellite imagery. The major challenge in developing a methane detection model is to accurately identify methane plumes from Sentinel-2's B11 and B12 bands while suppressing false positives caused by background variability and diverse land cover types. Traditional detection methods typically depend on the differences or ratios between these bands when comparing the scenes with and without plumes. However, these methods often require verification by a domain expert because they generate numerous false positives. Recent deep learning methods make some improvements using CNN-based architectures, but lack mechanisms to prioritize methane-specific features. AttMetNet introduces a methane-aware architecture that fuses the Normalized Difference Methane Index (NDMI) with an attention-enhanced U-Net. By jointly exploiting NDMI's plume-sensitive cues and attention-driven feature selection, AttMetNet selectively amplifies methane absorption features while suppressing background noise. This integration establishes a first-of-its-kind architecture tailored for robust methane plume detection in real satellite imagery. Additionally, we employ focal loss to address the severe class imbalance arising from both limited positive plume samples and sparse plume pixels within imagery. Furthermore, AttMetNet is trained on the real methane plume dataset, making it more robust to practical scenarios. Extensive experiments show that AttMetNet surpasses recent methods in methane plume detection with a lower false positive rate, better precision recall balance, and higher IoU.

