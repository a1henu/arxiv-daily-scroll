---
layout: default
title: Zero-Shot Segmentation through Prototype-Guidance for Multi-Label Plant Species Identification
---

# Zero-Shot Segmentation through Prototype-Guidance for Multi-Label Plant Species Identification
**arXiv**：[2512.19957v1](https://arxiv.org/abs/2512.19957) · [PDF](https://arxiv.org/pdf/2512.19957.pdf)  
**作者**：Luciano Araujo Dourado Filho, Almir Moreira da Silva Neto, Rodrigo Pereira David, Rodrigo Tripodi Calumby  

**一句话要点**：提出原型引导的零样本分割方法，用于高分辨率图像中的多标签植物物种识别。

**关键词**：零样本分割, 多标签分类, 原型引导, 视觉Transformer, 植物物种识别, 高分辨率图像

## 3 点简述
- 核心问题：解决PlantCLEF 2025挑战中的细粒度多标签物种识别，需从高分辨率植被图像中定位和分类多个物种。
- 方法要点：使用训练数据集提取特征并聚类生成类原型，指导定制ViT分割模型在测试集上训练，通过注意力分数定位兴趣区域辅助分类。
- 实验或效果：在PlantCLEF 2025挑战中排名第五，F1分数为0.33331，与最佳提交相差0.03，显示竞争性能。

## 摘要（原文）

> This paper presents an approach developed to address the PlantClef 2025 challenge, which consists of a fine-grained multi-label species identification, over high-resolution images. Our solution focused on employing class prototypes obtained from the training dataset as a proxy guidance for training a segmentation Vision Transformer (ViT) on the test set images. To obtain these representations, the proposed method extracts features from training dataset images and create clusters, by applying K-Means, with $K$ equals to the number of classes in the dataset. The segmentation model is a customized narrow ViT, built by replacing the patch embedding layer with a frozen DinoV2, pre-trained on the training dataset for individual species classification. This model is trained to reconstruct the class prototypes of the training dataset from the test dataset images. We then use this model to obtain attention scores that enable to identify and localize areas of interest and consequently guide the classification process. The proposed approach enabled a domain-adaptation from multi-class identification with individual species, into multi-label classification from high-resolution vegetation plots. Our method achieved fifth place in the PlantCLEF 2025 challenge on the private leaderboard, with an F1 score of 0.33331. Besides that, in absolute terms our method scored 0.03 lower than the top-performing submission, suggesting that it may achieved competitive performance in the benchmark task. Our code is available at \href{https://github.com/ADAM-UEFS/PlantCLEF2025}{https://github.com/ADAM-UEFS/PlantCLEF2025}.

