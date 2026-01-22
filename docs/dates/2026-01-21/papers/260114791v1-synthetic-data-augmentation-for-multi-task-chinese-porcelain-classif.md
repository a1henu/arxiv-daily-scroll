---
layout: default
title: Synthetic Data Augmentation for Multi-Task Chinese Porcelain Classification: A Stable Diffusion Approach
---

# Synthetic Data Augmentation for Multi-Task Chinese Porcelain Classification: A Stable Diffusion Approach
**arXiv**：[2601.14791v1](https://arxiv.org/abs/2601.14791) · [PDF](https://arxiv.org/pdf/2601.14791.pdf)  
**作者**：Ziyao Ling, Silvia Mirri, Paola Salomoni, Giovanni Delnevo  

**一句话要点**：提出基于Stable Diffusion的合成数据增强方法，以解决中国瓷器多任务分类中训练数据稀缺问题

**关键词**：合成数据增强, Stable Diffusion, 中国瓷器分类, 多任务学习, 考古人工智能

## 3 点简述
- 核心问题：考古文物分类中真实训练数据稀缺，特别是稀有类型中国瓷器
- 方法要点：使用Stable Diffusion与LoRA生成合成图像，以95:5和90:10比例混合真实数据增强训练集
- 实验效果：在多任务分类中，类型识别提升最显著（F1-macro增加5.5%），朝代和窑口任务有适度改善

## 摘要（原文）

> The scarcity of training data presents a fundamental challenge in applying deep learning to archaeological artifact classification, particularly for the rare types of Chinese porcelain. This study investigates whether synthetic images generated through Stable Diffusion with Low-Rank Adaptation (LoRA) can effectively augment limited real datasets for multi-task CNN-based porcelain classification. Using MobileNetV3 with transfer learning, we conducted controlled experiments comparing models trained on pure real data against those trained on mixed real-synthetic datasets (95:5 and 90:10 ratios) across four classification tasks: dynasty, glaze, kiln and type identification. Results demonstrate task-specific benefits: type classification showed the most substantial improvement (5.5\% F1-macro increase with 90:10 ratio), while dynasty and kiln tasks exhibited modest gains (3-4\%), suggesting that synthetic augmentation effectiveness depends on the alignment between generated features and task-relevant visual signatures. Our work contributes practical guidelines for deploying generative AI in archaeological research, demonstrating both the potential and limitations of synthetic data when archaeological authenticity must be balanced with data diversity.

