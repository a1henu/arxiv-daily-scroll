---
layout: default
title: NAU-QMUL: Utilizing BERT and CLIP for Multi-modal AI-Generated Image Detection
---

# NAU-QMUL: Utilizing BERT and CLIP for Multi-modal AI-Generated Image Detection
**arXiv**：[2602.23863v1](https://arxiv.org/abs/2602.23863) · [PDF](https://arxiv.org/pdf/2602.23863.pdf)  
**作者**：Xiaoyu Guo, Arkaitz Zubiaga  

**一句话要点**：提出多模态多任务模型，利用BERT和CLIP检测AI生成图像并识别生成模型

**关键词**：AI生成图像检测, 多模态融合, BERT, CLIP, 多任务学习, 伪标签数据增强

## 3 点简述
- 核心问题：检测AI生成图像并识别其生成模型，以应对虚假内容挑战
- 方法要点：结合BERT和CLIP提取文本与图像特征，通过跨模态融合和多任务损失优化
- 实验或效果：在CT2竞赛中获第五名，F1分数分别为83.16%和48.88%，验证了架构有效性

## 摘要（原文）

> With the aim of detecting AI-generated images and identifying the specific models responsible for their generation, we propose a multi-modal multi-task model. The model leverages pre-trained BERT and CLIP Vision encoders for text and image feature extraction, respectively, and employs cross-modal feature fusion with a tailored multi-task loss function. Additionally, a pseudo-labeling-based data augmentation strategy was utilized to expand the training dataset with high-confidence samples. The model achieved fifth place in both Tasks A and B of the `CT2: AI-Generated Image Detection' competition, with F1 scores of 83.16\% and 48.88\%, respectively. These findings highlight the effectiveness of the proposed architecture and its potential for advancing AI-generated content detection in real-world scenarios. The source code for our method is published on https://github.com/xxxxxxxxy/AIGeneratedImageDetection.

