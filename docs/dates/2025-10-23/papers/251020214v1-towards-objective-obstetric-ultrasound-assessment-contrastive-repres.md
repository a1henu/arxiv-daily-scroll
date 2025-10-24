---
layout: default
title: Towards Objective Obstetric Ultrasound Assessment: Contrastive Representation Learning for Fetal Movement Detection
---

# Towards Objective Obstetric Ultrasound Assessment: Contrastive Representation Learning for Fetal Movement Detection
**arXiv**：[2510.20214v1](https://arxiv.org/abs/2510.20214) · [PDF](https://arxiv.org/pdf/2510.20214.pdf)  
**作者**：Talha Ilyas, Duong Nhu, Allison Thomas, Arie Levin, Lim Wei Yap, Shu Gong, David Vera Anaya, Yiwen Jiang, Deval Mehta, Ritesh Warty, Vinayak Smith, Maya Reddy, Euan Wallace, Wenlong Cheng, Zongyuan Ge, Faezeh Marzbanrad  

**一句话要点**：提出对比超声视频表示学习框架以客观检测胎儿运动

**关键词**：胎儿运动检测, 自监督学习, 对比学习, 超声视频分析, 时空表示学习

## 3 点简述
- 胎儿运动检测主观性强，传统方法如母体感知和CTG准确性有限。
- 采用双对比损失结合时空对比学习，学习鲁棒运动表示。
- 在92名受试者数据集上，敏感度78.01%，AUROC 81.60%。

## 摘要（原文）

> Accurate fetal movement (FM) detection is essential for assessing prenatal
> health, as abnormal movement patterns can indicate underlying complications
> such as placental dysfunction or fetal distress. Traditional methods, including
> maternal perception and cardiotocography (CTG), suffer from subjectivity and
> limited accuracy. To address these challenges, we propose Contrastive
> Ultrasound Video Representation Learning (CURL), a novel self-supervised
> learning framework for FM detection from extended fetal ultrasound video
> recordings. Our approach leverages a dual-contrastive loss, incorporating both
> spatial and temporal contrastive learning, to learn robust motion
> representations. Additionally, we introduce a task-specific sampling strategy,
> ensuring the effective separation of movement and non-movement segments during
> self-supervised training, while enabling flexible inference on arbitrarily long
> ultrasound recordings through a probabilistic fine-tuning approach. Evaluated
> on an in-house dataset of 92 subjects, each with 30-minute ultrasound sessions,
> CURL achieves a sensitivity of 78.01% and an AUROC of 81.60%, demonstrating its
> potential for reliable and objective FM analysis. These results highlight the
> potential of self-supervised contrastive learning for fetal movement analysis,
> paving the way for improved prenatal monitoring and clinical decision-making.

