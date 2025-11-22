---
layout: default
title: Towards a Safer and Sustainable Manufacturing Process: Material classification in Laser Cutting Using Deep Learning
---

# Towards a Safer and Sustainable Manufacturing Process: Material classification in Laser Cutting Using Deep Learning
**arXiv**：[2511.16026v1](https://arxiv.org/abs/2511.16026) · [PDF](https://arxiv.org/pdf/2511.16026.pdf)  
**作者**：Mohamed Abdallah Salem, Hamdy Ahmed Ashur, Ahmed Elshinnawy  

**一句话要点**：提出基于深度学习的散斑模式材料分类方法，以提升激光切割的安全性和可持续性。

**关键词**：材料分类, 激光散斑传感, 卷积神经网络, 激光切割监控, 工业安全

## 3 点简述
- 激光切割产生粉尘烟雾，危害环境和工人健康，需实时材料识别。
- 使用卷积神经网络训练散斑模式，实现材料分类，适应激光颜色变化。
- 实验显示高准确率，验证集达96.88%，F1分数0.9643，覆盖30种材料。

## 摘要（原文）

> Laser cutting is a widely adopted technology in material processing across various industries, but it generates a significant amount of dust, smoke, and aerosols during operation, posing a risk to both the environment and workers' health. Speckle sensing has emerged as a promising method to monitor the cutting process and identify material types in real-time. This paper proposes a material classification technique using a speckle pattern of the material's surface based on deep learning to monitor and control the laser cutting process. The proposed method involves training a convolutional neural network (CNN) on a dataset of laser speckle patterns to recognize distinct material types for safe and efficient cutting. Previous methods for material classification using speckle sensing may face issues when the color of the laser used to produce the speckle pattern is changed. Experiments conducted in this study demonstrate that the proposed method achieves high accuracy in material classification, even when the laser color is changed. The model achieved an accuracy of 98.30 % on the training set and 96.88% on the validation set. Furthermore, the model was evaluated on a set of 3000 new images for 30 different materials, achieving an F1-score of 0.9643. The proposed method provides a robust and accurate solution for material-aware laser cutting using speckle sensing.

