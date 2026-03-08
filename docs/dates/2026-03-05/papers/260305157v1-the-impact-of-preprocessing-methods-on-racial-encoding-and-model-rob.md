---
layout: default
title: The Impact of Preprocessing Methods on Racial Encoding and Model Robustness in CXR Diagnosis
---

# The Impact of Preprocessing Methods on Racial Encoding and Model Robustness in CXR Diagnosis
**arXiv**：[2603.05157v1](https://arxiv.org/abs/2603.05157) · [PDF](https://arxiv.org/pdf/2603.05157.pdf)  
**作者**：Dishantkumar Sutariya, Eike Petersen  

**一句话要点**：提出基于肺裁剪的预处理方法以减少胸片诊断中的种族捷径学习

**关键词**：胸片诊断, 种族捷径学习, 图像预处理, 肺裁剪, 模型鲁棒性, 医疗公平

## 3 点简述
- 核心问题：深度学习模型能从胸片中高精度识别种族，导致种族捷径学习，威胁医疗公平和模型鲁棒性。
- 方法要点：研究肺掩膜、肺裁剪和CLAHE等预处理方法，旨在抑制种族编码的虚假线索，同时保持诊断准确性。
- 实验或效果：实验表明，简单的基于边界框的肺裁剪能有效减少种族捷径学习，且不牺牲诊断性能，避免了公平性与准确性的权衡。

## 摘要（原文）

> Deep learning models can identify racial identity with high accuracy from chest X-ray (CXR) recordings. Thus, there is widespread concern about the potential for racial shortcut learning, where a model inadvertently learns to systematically bias its diagnostic predictions as a function of racial identity. Such racial biases threaten healthcare equity and model reliability, as models may systematically misdiagnose certain demographic groups. Since racial shortcuts are diffuse - non-localized and distributed throughout the whole CXR recording - image preprocessing methods may influence racial shortcut learning, yet the potential of such methods for reducing biases remains underexplored. Here, we investigate the effects of image preprocessing methods including lung masking, lung cropping, and Contrast Limited Adaptive Histogram Equalization (CLAHE). These approaches aim to suppress spurious cues encoding racial information while preserving diagnostic accuracy. Our experiments reveal that simple bounding box-based lung cropping can be an effective strategy for reducing racial shortcut learning while maintaining diagnostic model performance, bypassing frequently postulated fairness-accuracy trade-offs.

