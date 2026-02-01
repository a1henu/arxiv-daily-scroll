---
layout: default
title: Mam-App: A Novel Parameter-Efficient Mamba Model for Apple Leaf Disease Classification
---

# Mam-App: A Novel Parameter-Efficient Mamba Model for Apple Leaf Disease Classification
**arXiv**：[2601.21307v1](https://arxiv.org/abs/2601.21307) · [PDF](https://arxiv.org/pdf/2601.21307.pdf)  
**作者**：Md Nadim Mahamood, Md Imran Hasan, Md Rasheduzzaman, Ausrukona Ray, Md Shafi Ud Doula, Kamrul Hasan  

**一句话要点**：提出Mam-App参数高效Mamba模型，用于苹果叶病分类以平衡效率与性能。

**关键词**：苹果叶病分类, 参数高效模型, Mamba模型, 轻量部署, 植物病害识别

## 3 点简述
- 核心问题：现有深度学习模型参数多，训练推理慢，轻量模型性能下降。
- 方法要点：基于Mamba构建参数高效模型，用于特征提取和疾病分类。
- 实验或效果：在苹果叶病数据集上达99.58%准确率，仅0.051M参数，并在玉米和马铃薯数据集验证泛化性。

## 摘要（原文）

> The rapid growth of the global population, alongside exponential technological advancement, has intensified the demand for food production. Meeting this demand depends not only on increasing agricultural yield but also on minimizing food loss caused by crop diseases. Diseases account for a substantial portion of apple production losses, despite apples being among the most widely produced and nutritionally valuable fruits worldwide. Previous studies have employed machine learning techniques for feature extraction and early diagnosis of apple leaf diseases, and more recently, deep learning-based models have shown remarkable performance in disease recognition. However, most state-of-the-art deep learning models are highly parameter-intensive, resulting in increased training and inference time. Although lightweight models are more suitable for user-friendly and resource-constrained applications, they often suffer from performance degradation. To address the trade-off between efficiency and performance, we propose Mam-App, a parameter-efficient Mamba-based model for feature extraction and leaf disease classification. The proposed approach achieves competitive state-of-the-art performance on the PlantVillage Apple Leaf Disease dataset, attaining 99.58% accuracy, 99.30% precision, 99.14% recall, and a 99.22% F1-score, while using only 0.051M parameters. This extremely low parameter count makes the model suitable for deployment on drones, mobile devices, and other low-resource platforms. To demonstrate the robustness and generalizability of the proposed model, we further evaluate it on the PlantVillage Corn Leaf Disease and Potato Leaf Disease datasets. The model achieves 99.48%, 99.20%, 99.34%, and 99.27% accuracy, precision, recall, and F1-score on the corn dataset and 98.46%, 98.91%, 95.39%, and 97.01% on the potato dataset, respectively.

