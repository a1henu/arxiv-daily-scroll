---
layout: default
title: Transformer based Multi-task Fusion Network for Food Spoilage Detection and Shelf life Forecasting
---

# Transformer based Multi-task Fusion Network for Food Spoilage Detection and Shelf life Forecasting
**arXiv**：[2601.13665v1](https://arxiv.org/abs/2601.13665) · [PDF](https://arxiv.org/pdf/2601.13665.pdf)  
**作者**：Mounika Kanulla, Rajasree Dadigi, Sailaja Thota, Vivek Yelleti  

**一句话要点**：提出基于Transformer的多任务融合网络，用于食品腐败检测与保质期预测以减少农业供应链浪费。

**关键词**：食品腐败检测, 保质期预测, 多任务学习, Transformer融合, 农业供应链优化, 模型可视化

## 3 点简述
- 核心问题：农业供应链中食品浪费严重，需准确检测腐败并预测保质期以优化管理。
- 方法要点：融合CNN与LSTM或DeiT Transformer，同时处理蔬菜分类、腐败检测和保质期预测多任务。
- 实验或效果：CNN+DeiT Transformer在分类和检测任务中F1分数达0.98和0.61，预测误差较低，并通过噪声验证和LIME可视化增强可靠性。

## 摘要（原文）

> Food wastage is one of the critical challenges in the agricultural supply chain, and accurate and effective spoilage detection can help to reduce it. Further, it is highly important to forecast the spoilage information. This aids the longevity of the supply chain management in the agriculture field. This motivated us to propose fusion based architectures by combining CNN with LSTM and DeiT transformer for the following multi-tasks simultaneously: (i) vegetable classification, (ii) food spoilage detection, and (iii) shelf life forecasting. We developed a dataset by capturing images of vegetables from their fresh state until they were completely spoiled. From the experimental analysis it is concluded that the proposed fusion architectures CNN+CNN-LSTM and CNN+DeiT Transformer outperformed several deep learning models such as CNN, VGG16, ResNet50, Capsule Networks, and DeiT Transformers. Overall, CNN + DeiT Transformer yielded F1-score of 0.98 and 0.61 in vegetable classification and spoilage detection respectively and mean squared error (MSE) and symmetric mean absolute percentage error (SMAPE) of 3.58, and 41.66% respectively in spoilage forecasting. Further, the reliability of the fusion models was validated on noisy images and integrated with LIME to visualize the model decisions.

