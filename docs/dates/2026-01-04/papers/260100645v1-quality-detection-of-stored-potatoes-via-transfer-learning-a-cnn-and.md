---
layout: default
title: Quality Detection of Stored Potatoes via Transfer Learning: A CNN and Vision Transformer Approach
---

# Quality Detection of Stored Potatoes via Transfer Learning: A CNN and Vision Transformer Approach
**arXiv**：[2601.00645v1](https://arxiv.org/abs/2601.00645) · [PDF](https://arxiv.org/pdf/2601.00645.pdf)  
**作者**：Shrikant Kapse, Priyankkumar Dhrangdhariya, Priya Kedia, Manasi Patwardhan, Shankar Kausley, Soumyadipta Maiti, Beena Rai, Shirish Karande  

**一句话要点**：提出基于迁移学习的CNN与Vision Transformer方法，用于存储马铃薯的质量检测

**关键词**：马铃薯质量检测, 迁移学习, 卷积神经网络, Vision Transformer, 发芽检测, 保质期预测

## 3 点简述
- 核心问题：存储马铃薯质量监测，包括发芽检测、重量损失估计和保质期预测
- 方法要点：利用ResNet、VGG、DenseNet和Vision Transformer预训练架构，设计二分类和多分类模型
- 实验或效果：DenseNet在发芽检测中准确率达98.03%，保质期预测在粗分类下准确率超过89.83%

## 摘要（原文）

> Image-based deep learning provides a non-invasive, scalable solution for monitoring potato quality during storage, addressing key challenges such as sprout detection, weight loss estimation, and shelf-life prediction. In this study, images and corresponding weight data were collected over a 200-day period under controlled temperature and humidity conditions. Leveraging powerful pre-trained architectures of ResNet, VGG, DenseNet, and Vision Transformer (ViT), we designed two specialized models: (1) a high-precision binary classifier for sprout detection, and (2) an advanced multi-class predictor to estimate weight loss and forecast remaining shelf-life with remarkable accuracy. DenseNet achieved exceptional performance, with 98.03% accuracy in sprout detection. Shelf-life prediction models performed best with coarse class divisions (2-5 classes), achieving over 89.83% accuracy, while accuracy declined for finer divisions (6-8 classes) due to subtle visual differences and limited data per class. These findings demonstrate the feasibility of integrating image-based models into automated sorting and inventory systems, enabling early identification of sprouted potatoes and dynamic categorization based on storage stage. Practical implications include improved inventory management, differential pricing strategies, and reduced food waste across supply chains. While predicting exact shelf-life intervals remains challenging, focusing on broader class divisions ensures robust performance. Future research should aim to develop generalized models trained on diverse potato varieties and storage conditions to enhance adaptability and scalability. Overall, this approach offers a cost-effective, non-destructive method for quality assessment, supporting efficiency and sustainability in potato storage and distribution.

