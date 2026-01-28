---
layout: default
title: DSTCS: Dual-Student Teacher Framework with Segment Anything Model for Semi-Supervised Pubic Symphysis Fetal Head Segmentation
---

# DSTCS: Dual-Student Teacher Framework with Segment Anything Model for Semi-Supervised Pubic Symphysis Fetal Head Segmentation
**arXiv**：[2601.19446v1](https://arxiv.org/abs/2601.19446) · [PDF](https://arxiv.org/pdf/2601.19446.pdf)  
**作者**：Yalin Luo, Shun Long, Huijin Wang, Jieyun Bai  

**一句话要点**：提出结合CNN与SAM的双学生-教师框架，用于半监督耻骨联合胎儿头部分割。

**关键词**：半监督分割, 耻骨联合胎儿头部分割, Segment Anything Model, 双学生-教师框架, 超声图像处理, 协同学习

## 3 点简述
- 核心问题：超声图像中类不平衡、边界模糊和噪声干扰导致耻骨联合胎儿头部分割困难，且高质量标注数据稀缺。
- 方法要点：集成Segment Anything Model到双学生-教师架构，CNN与SAM分支协同学习，结合边界优化数据增强和新损失函数。
- 实验或效果：在MICCAI 2023和2024基准测试中展现优越鲁棒性，显著超越现有技术，为临床提供可靠分割工具。

## 摘要（原文）

> Segmentation of the pubic symphysis and fetal head (PSFH) is a critical procedure in intrapartum monitoring and is essential for evaluating labor progression and identifying potential delivery complications. However, achieving accurate segmentation remains a significant challenge due to class imbalance, ambiguous boundaries, and noise interference in ultrasound images, compounded by the scarcity of high-quality annotated data. Current research on PSFH segmentation predominantly relies on CNN and Transformer architectures, leaving the potential of more powerful models underexplored. In this work, we propose a Dual-Student and Teacher framework combining CNN and SAM (DSTCS), which integrates the Segment Anything Model (SAM) into a dual student-teacher architecture. A cooperative learning mechanism between the CNN and SAM branches significantly improves segmentation accuracy. The proposed scheme also incorporates a specialized data augmentation strategy optimized for boundary processing and a novel loss function. Extensive experiments on the MICCAI 2023 and 2024 PSFH segmentation benchmarks demonstrate that our method exhibits superior robustness and significantly outperforms existing techniques, providing a reliable segmentation tool for clinical practice.

