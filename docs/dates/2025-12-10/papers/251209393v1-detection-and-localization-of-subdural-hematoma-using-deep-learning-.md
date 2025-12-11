---
layout: default
title: Detection and Localization of Subdural Hematoma Using Deep Learning on Computed Tomography
---

# Detection and Localization of Subdural Hematoma Using Deep Learning on Computed Tomography
**arXiv**：[2512.09393v1](https://arxiv.org/abs/2512.09393) · [PDF](https://arxiv.org/pdf/2512.09393.pdf)  
**作者**：Vasiliki Stoumpou, Rohan Kumar, Bernard Burman, Diego Ojeda, Tapan Mehta, Dimitris Bertsimas  

**一句话要点**：提出多模态深度学习框架，集成临床与影像数据，用于CT中硬膜下血肿的检测与定位。

**关键词**：硬膜下血肿检测, 多模态深度学习, CT影像分析, 3D卷积神经网络, Transformer分割, 临床决策支持

## 3 点简述
- 核心问题：硬膜下血肿是神经外科急症，现有自动化工具检测性能有限且缺乏可解释性。
- 方法要点：结合临床变量、3D卷积网络和Transformer增强的2D分割模型，采用贪婪集成策略。
- 实验或效果：多模态集成在25,315个CT研究中达到AUC 0.9407，提供解剖学定位图。

## 摘要（原文）

> Background. Subdural hematoma (SDH) is a common neurosurgical emergency, with increasing incidence in aging populations. Rapid and accurate identification is essential to guide timely intervention, yet existing automated tools focus primarily on detection and provide limited interpretability or spatial localization. There remains a need for transparent, high-performing systems that integrate multimodal clinical and imaging information to support real-time decision-making.
>   Methods. We developed a multimodal deep-learning framework that integrates structured clinical variables, a 3D convolutional neural network trained on CT volumes, and a transformer-enhanced 2D segmentation model for SDH detection and localization. Using 25,315 head CT studies from Hartford HealthCare (2015--2024), of which 3,774 (14.9\%) contained clinician-confirmed SDH, tabular models were trained on demographics, comorbidities, medications, and laboratory results. Imaging models were trained to detect SDH and generate voxel-level probability maps. A greedy ensemble strategy combined complementary predictors.
>   Findings. Clinical variables alone provided modest discriminatory power (AUC 0.75). Convolutional models trained on CT volumes and segmentation-derived maps achieved substantially higher accuracy (AUCs 0.922 and 0.926). The multimodal ensemble integrating all components achieved the best overall performance (AUC 0.9407; 95\% CI, 0.930--0.951) and produced anatomically meaningful localization maps consistent with known SDH patterns.
>   Interpretation. This multimodal, interpretable framework provides rapid and accurate SDH detection and localization, achieving high detection performance and offering transparent, anatomically grounded outputs. Integration into radiology workflows could streamline triage, reduce time to intervention, and improve consistency in SDH management.

