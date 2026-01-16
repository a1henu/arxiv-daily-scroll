---
layout: default
title: Handling Missing Modalities in Multimodal Survival Prediction for Non-Small Cell Lung Cancer
---

# Handling Missing Modalities in Multimodal Survival Prediction for Non-Small Cell Lung Cancer
**arXiv**：[2601.10386v1](https://arxiv.org/abs/2601.10386) · [PDF](https://arxiv.org/pdf/2601.10386.pdf)  
**作者**：Filippo Ruffini, Camillo Maria Caruso, Claudia Tacconi, Lorenzo Nibid, Francesca Miccolis, Marta Lovino, Carlo Greco, Edy Ippolito, Michele Fiore, Alessio Cortellini, Bruno Beomonte Zobel, Giuseppe Perrone, Bruno Vincenzi, Claudio Marrocco, Alessandro Bria, Elisa Ficarra, Sara Ramella, Valerio Guarrasi, Paolo Soda  

**一句话要点**：提出缺失感知多模态生存框架以解决非小细胞肺癌生存预测中模态缺失问题

**关键词**：多模态生存预测, 模态缺失处理, 非小细胞肺癌, 中间融合, 基础模型, 自适应权重

## 3 点简述
- 核心问题：多模态深度学习在非小细胞肺癌生存预测中受限于小样本和模态缺失，影响临床适用性。
- 方法要点：利用基础模型提取模态特征，采用缺失感知编码策略，实现中间融合以处理不完整模态数据。
- 实验或效果：中间融合优于单模态及早期/晚期融合，WSI与临床模态融合性能最佳（C-index 73.30），模型自适应调整模态权重。

## 摘要（原文）

> Accurate survival prediction in Non-Small Cell Lung Cancer (NSCLC) requires the integration of heterogeneous clinical, radiological, and histopathological information. While Multimodal Deep Learning (MDL) offers a promises for precision prognosis and survival prediction, its clinical applicability is severely limited by small cohort sizes and the presence of missing modalities, often forcing complete-case filtering or aggressive imputation. In this work, we present a missing-aware multimodal survival framework that integrates Computed Tomography (CT), Whole-Slide Histopathology (WSI) Images, and structured clinical variables for overall survival modeling in unresectable stage II-III NSCLC. By leveraging Foundation Models (FM) for modality-specific feature extraction and a missing-aware encoding strategy, the proposed approach enables intermediate multimodal fusion under naturally incomplete modality profiles. The proposed architecture is resilient to missing modalities by design, allowing the model to utilize all available data without being forced to drop patients during training or inference. Experimental results demonstrate that intermediate fusion consistently outperforms unimodal baselines as well as early and late fusion strategies, with the strongest performance achieved by the fusion of WSI and clinical modalities (73.30 C-index). Further analyses of modality importance reveal an adaptive behavior in which less informative modalities, i.e., CT modality, are automatically down-weighted and contribute less to the final survival prediction.

