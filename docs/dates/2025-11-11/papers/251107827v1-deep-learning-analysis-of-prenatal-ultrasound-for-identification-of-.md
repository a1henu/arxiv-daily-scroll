---
layout: default
title: Deep Learning Analysis of Prenatal Ultrasound for Identification of Ventriculomegaly
---

# Deep Learning Analysis of Prenatal Ultrasound for Identification of Ventriculomegaly
**arXiv**：[2511.07827v1](https://arxiv.org/abs/2511.07827) · [PDF](https://arxiv.org/pdf/2511.07827.pdf)  
**作者**：Youssef Megahed, Inok Lee, Robin Ducharme, Aylin Erman, Olivier X. Miguel, Kevin Dick, Adrian D. C. Chan, Steven Hawken, Mark Walker, Felipe Moretti  

**一句话要点**：提出基于自监督预训练模型的深度学习方法来检测产前超声中的脑室扩大

**关键词**：产前超声分析, 脑室扩大检测, 自监督学习, Vision Transformer, 医学图像分类, 模型可解释性

## 3 点简述
- 核心问题：产前脑室扩大（脑室扩大）的早期诊断，与胎儿非整倍体和遗传综合征风险相关。
- 方法要点：使用USF-MAE模型，基于Vision Transformer编码器，在胎儿脑超声图像上进行微调。
- 实验或效果：模型在独立测试集上F1-score达91.78%，优于基线模型，并具有临床可解释性。

## 摘要（原文）

> The proposed study aimed to develop a deep learning model capable of detecting ventriculomegaly on prenatal ultrasound images. Ventriculomegaly is a prenatal condition characterized by dilated cerebral ventricles of the fetal brain and is important to diagnose early, as it can be associated with an increased risk for fetal aneuploidies and/or underlying genetic syndromes. An Ultrasound Self-Supervised Foundation Model with Masked Autoencoding (USF-MAE), recently developed by our group, was fine-tuned for a binary classification task to distinguish fetal brain ultrasound images as either normal or showing ventriculomegaly. The USF-MAE incorporates a Vision Transformer encoder pretrained on more than 370,000 ultrasound images from the OpenUS-46 corpus. For this study, the pretrained encoder was adapted and fine-tuned on a curated dataset of fetal brain ultrasound images to optimize its performance for ventriculomegaly detection. Model evaluation was conducted using 5-fold cross-validation and an independent test cohort, and performance was quantified using accuracy, precision, recall, specificity, F1-score, and area under the receiver operating characteristic curve (AUC). The proposed USF-MAE model reached an F1-score of 91.76% on the 5-fold cross-validation and 91.78% on the independent test set, with much higher scores than those obtained by the baseline models by 19.37% and 16.15% compared to VGG-19, 2.31% and 2.56% compared to ResNet-50, and 5.03% and 11.93% compared to ViT-B/16, respectively. The model also showed a high mean test precision of 94.47% and an accuracy of 97.24%. The Eigen-CAM (Eigen Class Activation Map) heatmaps showed that the model was focusing on the ventricle area for the diagnosis of ventriculomegaly, which has explainability and clinical plausibility.

