---
layout: default
title: Efficient Brain Extraction of MRI Scans with Mild to Moderate Neuropathology
---

# Efficient Brain Extraction of MRI Scans with Mild to Moderate Neuropathology
**arXiv**：[2602.08764v1](https://arxiv.org/abs/2602.08764) · [PDF](https://arxiv.org/pdf/2602.08764.pdf)  
**作者**：Hjalti Thrastarson, Lotta M. Ellingsen  

**一句话要点**：提出基于U-net和符号距离变换的稳健方法，用于轻度至中度神经病理学MRI的颅骨剥离。

**关键词**：颅骨剥离, MRI处理, U-net, 符号距离变换, 神经病理学, 脑分割

## 3 点简述
- 核心问题：现有颅骨剥离方法在神经病理学存在时易失败，且脑掩膜边界定义不一致。
- 方法要点：使用改进U-net和符号距离变换损失函数，训练于银标准数据，以稳健分割脑外表面。
- 实验或效果：在内部和外部数据集上验证，DSC达0.964±0.006和0.958±0.006，性能优于或媲美现有方法。

## 摘要（原文）

> Skull stripping magnetic resonance images (MRI) of the human brain is an important process in many image processing techniques, such as automatic segmentation of brain structures. Numerous methods have been developed to perform this task, however, they often fail in the presence of neuropathology and can be inconsistent in defining the boundary of the brain mask. Here, we propose a novel approach to skull strip T1-weighted images in a robust and efficient manner, aiming to consistently segment the outer surface of the brain, including the sulcal cerebrospinal fluid (CSF), while excluding the full extent of the subarachnoid space and meninges. We train a modified version of the U-net on silver-standard ground truth data using a novel loss function based on the signed-distance transform (SDT). We validate our model both qualitatively and quantitatively using held-out data from the training dataset, as well as an independent external dataset. The brain masks used for evaluation partially or fully include the subarachnoid space, which may introduce bias into the comparison; nonetheless, our model demonstrates strong performance on the held-out test data, achieving a consistent mean Dice similarity coefficient (DSC) of 0.964$\pm$0.006 and an average symmetric surface distance (ASSD) of 1.4mm$\pm$0.2mm. Performance on the external dataset is comparable, with a DSC of 0.958$\pm$0.006 and an ASSD of 1.7$\pm$0.2mm. Our method achieves performance comparable to or better than existing state-of-the-art methods for brain extraction, particularly in its highly consistent preservation of the brain's outer surface. The method is publicly available on GitHub.

