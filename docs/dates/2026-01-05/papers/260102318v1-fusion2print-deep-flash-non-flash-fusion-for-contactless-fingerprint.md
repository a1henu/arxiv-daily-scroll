---
layout: default
title: Fusion2Print: Deep Flash-Non-Flash Fusion for Contactless Fingerprint Matching
---

# Fusion2Print: Deep Flash-Non-Flash Fusion for Contactless Fingerprint Matching
**arXiv**：[2601.02318v1](https://arxiv.org/abs/2601.02318) · [PDF](https://arxiv.org/pdf/2601.02318.pdf)  
**作者**：Roja Sahoo, Anoop Namboodiri  

**一句话要点**：提出Fusion2Print框架，通过融合闪光-非闪光图像以提升非接触式指纹匹配性能。

**关键词**：非接触式指纹识别, 多模态融合, 图像增强, 深度学习嵌入, 注意力机制, U-Net

## 3 点简述
- 核心问题：非接触式指纹图像因光照变化和反射导致脊线清晰度下降。
- 方法要点：构建配对数据集，使用注意力融合网络和U-Net增强模块优化图像质量。
- 实验或效果：在验证任务中实现AUC=0.999和EER=1.12%，优于单模态基线。

## 摘要（原文）

> Contactless fingerprint recognition offers a hygienic and convenient alternative to contact-based systems, enabling rapid acquisition without latent prints, pressure artifacts, or hygiene risks. However, contactless images often show degraded ridge clarity due to illumination variation, subcutaneous skin discoloration, and specular reflections. Flash captures preserve ridge detail but introduce noise, whereas non-flash captures reduce noise but lower ridge contrast. We propose Fusion2Print (F2P), the first framework to systematically capture and fuse paired flash-non-flash contactless fingerprints. We construct a custom paired dataset, FNF Database, and perform manual flash-non-flash subtraction to isolate ridge-preserving signals. A lightweight attention-based fusion network also integrates both modalities, emphasizing informative channels and suppressing noise, and then a U-Net enhancement module produces an optimally weighted grayscale image. Finally, a deep embedding model with cross-domain compatibility, generates discriminative and robust representations in a unified embedding space compatible with both contactless and contact-based fingerprints for verification. F2P enhances ridge clarity and achieves superior recognition performance (AUC=0.999, EER=1.12%) over single-capture baselines (Verifinger, DeepPrint).

