---
layout: default
title: Radiomics-Integrated Deep Learning with Hierarchical Loss for Osteosarcoma Histology Classification
---

# Radiomics-Integrated Deep Learning with Hierarchical Loss for Osteosarcoma Histology Classification
**arXiv**：[2601.09416v1](https://arxiv.org/abs/2601.09416) · [PDF](https://arxiv.org/pdf/2601.09416.pdf)  
**作者**：Yaxi Chen, Zi Ye, Shaheer U. Saeed, Oliver Yu, Simin Ni, Jie Huang, Yipeng Hu  

**一句话要点**：提出集成放射组学与分层损失的深度学习方法，以提升骨肉瘤组织学分类性能。

**关键词**：骨肉瘤分类, 放射组学, 深度学习, 分层损失, 数字病理学, 多模态学习

## 3 点简述
- 核心问题：骨肉瘤化疗后肿瘤区域评估依赖人工，存在主观性和变异性，且现有深度学习模型在患者级测试中性能下降。
- 方法要点：引入放射组学特征作为多模态输入，并采用分层损失优化肿瘤与非肿瘤、存活与非存活肿瘤的分类任务。
- 实验或效果：在TCIA数据集上验证，新方法显著提升分类性能，达到该应用的最先进水平。

## 摘要（原文）

> Osteosarcoma (OS) is an aggressive primary bone malignancy. Accurate histopathological assessment of viable versus non-viable tumor regions after neoadjuvant chemotherapy is critical for prognosis and treatment planning, yet manual evaluation remains labor-intensive, subjective, and prone to inter-observer variability. Recent advances in digital pathology have enabled automated necrosis quantification. Evaluating on test data, independently sampled on patient-level, revealed that the deep learning model performance dropped significantly from the tile-level generalization ability reported in previous studies. First, this work proposes the use of radiomic features as additional input in model training. We show that, despite that they are derived from the images, such a multimodal input effectively improved the classification performance, in addition to its added benefits in interpretability. Second, this work proposes to optimize two binary classification tasks with hierarchical classes (i.e. tumor-vs-non-tumor and viable-vs-non-viable), as opposed to the alternative ``flat'' three-class classification task (i.e. non-tumor, non-viable tumor, viable tumor), thereby enabling a hierarchical loss. We show that such a hierarchical loss, with trainable weightings between the two tasks, the per-class performance can be improved significantly. Using the TCIA OS Tumor Assessment dataset, we experimentally demonstrate the benefits from each of the proposed new approaches and their combination, setting a what we consider new state-of-the-art performance on this open dataset for this application. Code and trained models: https://github.com/YaxiiC/RadiomicsOS.git.

