---
layout: default
title: DA-SSL: self-supervised domain adaptor to leverage foundational models in turbt histopathology slides
---

# DA-SSL: self-supervised domain adaptor to leverage foundational models in turbt histopathology slides
**arXiv**：[2512.13600v1](https://arxiv.org/abs/2512.13600) · [PDF](https://arxiv.org/pdf/2512.13600.pdf)  
**作者**：Haoyue Zhang, Meera Chappidi, Erolcan Sayar, Helen Richards, Zhijun Chen, Lucas Liu, Roxanne Wadia, Peter A Humphrey, Fady Ghali, Alberto Contreras-Sanz, Peter Black, Jonathan Wright, Stephanie Harmon, Michael Haffner  

**一句话要点**：提出DA-SSL自监督域适配器，以提升病理基础模型在TURBT切片中的性能。

**关键词**：自监督学习, 域适应, 病理学基础模型, 多实例学习, 膀胱癌诊断

## 3 点简述
- 核心问题：病理基础模型在TURBT切片上因域偏移和伪影导致性能受限。
- 方法要点：通过自监督域适配对齐特征，无需微调基础模型。
- 实验或效果：在多中心研究中，DA-SSL在预测治疗响应任务中取得高AUC和准确率。

## 摘要（原文）

> Recent deep learning frameworks in histopathology, particularly multiple instance learning (MIL) combined with pathology foundational models (PFMs), have shown strong performance. However, PFMs exhibit limitations on certain cancer or specimen types due to domain shifts - these cancer types were rarely used for pretraining or specimens contain tissue-based artifacts rarely seen within the pretraining population. Such is the case for transurethral resection of bladder tumor (TURBT), which are essential for diagnosing muscle-invasive bladder cancer (MIBC), but contain fragmented tissue chips and electrocautery artifacts and were not widely used in publicly available PFMs. To address this, we propose a simple yet effective domain-adaptive self-supervised adaptor (DA-SSL) that realigns pretrained PFM features to the TURBT domain without fine-tuning the foundational model itself. We pilot this framework for predicting treatment response in TURBT, where histomorphological features are currently underutilized and identifying patients who will benefit from neoadjuvant chemotherapy (NAC) is challenging. In our multi-center study, DA-SSL achieved an AUC of 0.77+/-0.04 in five-fold cross-validation and an external test accuracy of 0.84, sensitivity of 0.71, and specificity of 0.91 using majority voting. Our results demonstrate that lightweight domain adaptation with self-supervision can effectively enhance PFM-based MIL pipelines for clinically challenging histopathology tasks. Code is Available at https://github.com/zhanghaoyue/DA_SSL_TURBT.

