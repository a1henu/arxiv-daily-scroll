---
layout: default
title: Hierarchical Semantic Learning for Multi-Class Aorta Segmentation
---

# Hierarchical Semantic Learning for Multi-Class Aorta Segmentation
**arXiv**：[2511.14187v1](https://arxiv.org/abs/2511.14187) · [PDF](https://arxiv.org/pdf/2511.14187.pdf)  
**作者**：Pengcheng Shi  

**一句话要点**：提出分层语义学习与课程学习策略，以解决主动脉多类分割中的类别不平衡和效率问题

**关键词**：主动脉分割, 课程学习, 分层语义学习, 分形softmax, 多类分割, 医学图像分析

## 3 点简述
- 核心问题：主动脉分割存在类别不平衡和忽略解剖层次关系，影响临床3D分析。
- 方法要点：采用课程学习和分形softmax，从简单到复杂渐进学习解剖结构。
- 实验或效果：在测试集上Dice分数比基线高5.6%，推理速度提升高达五倍。

## 摘要（原文）

> The aorta, the body's largest artery, is prone to pathologies such as dissection, aneurysm, and atherosclerosis, which often require timely intervention. Minimally invasive repairs involving branch vessels necessitate detailed 3D anatomical analysis. Existing methods often overlook hierarchical anatomical relationships while struggling with severe class imbalance inherent in vascular structures. We address these challenges with a curriculum learning strategy that leverages a novel fractal softmax for hierarchical semantic learning. Inspired by human cognition, our approach progressively learns anatomical constraints by decomposing complex structures from simple to complex components. The curriculum learning framework naturally addresses class imbalance by first establishing robust feature representations for dominant classes before tackling rare but anatomically critical structures, significantly accelerating model convergence in multi-class scenarios. Our two-stage inference strategy achieves up to fivefold acceleration, enhancing clinical practicality. On the validation set at epoch 50, our hierarchical semantic loss improves the Dice score of nnU-Net ResEnc M by 11.65%. The proposed model demonstrates a 5.6% higher Dice score than baselines on the test set. Experimental results show significant improvements in segmentation accuracy and efficiency, making the framework suitable for real-time clinical applications. The implementation code for this challenge entry is publicly available at: https://github.com/PengchengShi1220/AortaSeg24. The code for fractal softmax will be available at https://github.com/PengchengShi1220/fractal-softmax.

