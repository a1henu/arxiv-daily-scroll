---
layout: default
title: Satellite-Based Detection of Looted Archaeological Sites Using Machine Learning
---

# Satellite-Based Detection of Looted Archaeological Sites Using Machine Learning
**arXiv**：[2602.19608v1](https://arxiv.org/abs/2602.19608) · [PDF](https://arxiv.org/pdf/2602.19608.pdf)  
**作者**：Girmaw Abebe Tadesse, Titien Bartette, Andrew Hassanali, Allen Kim, Jonathan Chemla, Andrew Zolli, Yves Ubelmann, Caleb Robinson, Inbal Becker-Reshef, Juan Lavista Ferres  

**一句话要点**：提出基于卫星图像和机器学习的可扩展管道，以检测阿富汗被掠夺的考古遗址。

**关键词**：卫星图像分析, 考古遗址监测, 卷积神经网络, 机器学习, 文化遗产保护, 遥感基础模型

## 3 点简述
- 核心问题：考古遗址掠夺威胁文化遗产，但远程监测数千地点操作困难。
- 方法要点：使用PlanetScope月度镶嵌图像和CNN分类器，结合空间掩码提升性能。
- 实验或效果：ImageNet预训练CNN达到F1分数0.926，优于传统机器学习方法。

## 摘要（原文）

> Looting at archaeological sites poses a severe risk to cultural heritage, yet monitoring thousands of remote locations remains operationally difficult. We present a scalable and satellite-based pipeline to detect looted archaeological sites, using PlanetScope monthly mosaics (4.7m/pixel) and a curated dataset of 1,943 archaeological sites in Afghanistan (898 looted, 1,045 preserved) with multi-year imagery (2016--2023) and site-footprint masks. We compare (i) end-to-end CNN classifiers trained on raw RGB patches and (ii) traditional machine learning (ML) trained on handcrafted spectral/texture features and embeddings from recent remote-sensing foundation models. Results indicate that ImageNet-pretrained CNNs combined with spatial masking reach an F1 score of 0.926, clearly surpassing the strongest traditional ML setup, which attains an F1 score of 0.710 using SatCLIP-V+RF+Mean, i.e., location and vision embeddings fed into a Random Forest with mean-based temporal aggregation. Ablation studies demonstrate that ImageNet pretraining (even in the presence of domain shift) and spatial masking enhance performance. In contrast, geospatial foundation model embeddings perform competitively with handcrafted features, suggesting that looting signatures are extremely localized. The repository is available at https://github.com/microsoft/looted_site_detection.

