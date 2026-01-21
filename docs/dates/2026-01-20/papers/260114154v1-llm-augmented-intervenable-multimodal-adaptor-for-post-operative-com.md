---
layout: default
title: LLM Augmented Intervenable Multimodal Adaptor for Post-operative Complication Prediction in Lung Cancer Surgery
---

# LLM Augmented Intervenable Multimodal Adaptor for Post-operative Complication Prediction in Lung Cancer Surgery
**arXiv**：[2601.14154v1](https://arxiv.org/abs/2601.14154) · [PDF](https://arxiv.org/pdf/2601.14154.pdf)  
**作者**：Shubham Pandey, Bhavin Jawade, Srirangaraj Setlur, Venu Govindaraju, Kenneth Seastedt  

**一句话要点**：提出MIRACLE架构，通过融合术前临床与影像数据预测肺癌术后并发症风险，并增强可解释性。

**关键词**：术后并发症预测, 多模态融合, 可解释深度学习, 肺癌手术, 临床决策支持

## 3 点简述
- 核心问题：术后并发症影响患者预后和医疗成本，需精准预测以改善临床管理。
- 方法要点：采用超球嵌入空间融合异构数据，结合干预模块提供可解释和可操作的见解。
- 实验或效果：在POC-L数据集上验证，MIRACLE优于传统机器学习模型和大型语言模型变体。

## 摘要（原文）

> Postoperative complications remain a critical concern in clinical practice, adversely affecting patient outcomes and contributing to rising healthcare costs. We present MIRACLE, a deep learning architecture for prediction of risk of postoperative complications in lung cancer surgery by integrating preoperative clinical and radiological data. MIRACLE employs a hyperspherical embedding space fusion of heterogeneous inputs, enabling the extraction of robust, discriminative features from both structured clinical records and high-dimensional radiological images. To enhance transparency of prediction and clinical utility, we incorporate an interventional deep learning module in MIRACLE, that not only refines predictions but also provides interpretable and actionable insights, allowing domain experts to interactively adjust recommendations based on clinical expertise. We validate our approach on POC-L, a real-world dataset comprising 3,094 lung cancer patients who underwent surgery at Roswell Park Comprehensive Cancer Center. Our results demonstrate that MIRACLE outperforms various traditional machine learning models and contemporary large language models (LLM) variants alone, for personalized and explainable postoperative risk management.

