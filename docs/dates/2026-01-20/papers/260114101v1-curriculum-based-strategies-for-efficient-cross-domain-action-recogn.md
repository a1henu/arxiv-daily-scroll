---
layout: default
title: Curriculum-Based Strategies for Efficient Cross-Domain Action Recognition
---

# Curriculum-Based Strategies for Efficient Cross-Domain Action Recognition
**arXiv**：[2601.14101v1](https://arxiv.org/abs/2601.14101) · [PDF](https://arxiv.org/pdf/2601.14101.pdf)  
**作者**：Emily Kim, Allen Wu, Jessica Hodgins  

**一句话要点**：提出课程学习策略以提升跨视角动作识别的训练效率与泛化能力

**关键词**：跨域动作识别, 课程学习, 合成数据, 训练效率, 视角泛化

## 3 点简述
- 核心问题：动作识别模型从地面视角泛化到空中视角时性能下降，缺乏真实空中数据训练。
- 方法要点：利用合成空中数据和真实地面数据，通过两阶段或渐进式课程学习策略优化训练过程。
- 实验或效果：在REMAG数据集上，课程策略在保持准确率的同时，显著减少训练迭代次数，提升效率。

## 摘要（原文）

> Despite significant progress in human action recognition, generalizing to diverse viewpoints remains a challenge. Most existing datasets are captured from ground-level perspectives, and models trained on them often struggle to transfer to drastically different domains such as aerial views. This paper examines how curriculum-based training strategies can improve generalization to unseen real aerial-view data without using any real aerial data during training.
>   We explore curriculum learning for cross-view action recognition using two out-of-domain sources: synthetic aerial-view data and real ground-view data. Our results on the evaluation on order of training (fine-tuning on synthetic aerial data vs. real ground data) shows that fine-tuning on real ground data but differ in how they transition from synthetic to real. The first uses a two-stage curriculum with direct fine-tuning, while the second applies a progressive curriculum that expands the dataset in multiple stages before fine-tuning. We evaluate both methods on the REMAG dataset using SlowFast (CNN-based) and MViTv2 (Transformer-based) architectures.
>   Results show that combining the two out-of-domain datasets clearly outperforms training on a single domain, whether real ground-view or synthetic aerial-view. Both curriculum strategies match the top-1 accuracy of simple dataset combination while offering efficiency gains. With the two-step fine-tuning method, SlowFast achieves up to a 37% reduction in iterations and MViTv2 up to a 30% reduction compared to simple combination. The multi-step progressive approach further reduces iterations, by up to 9% for SlowFast and 30% for MViTv2, relative to the two-step method. These findings demonstrate that curriculum-based training can maintain comparable performance (top-1 accuracy within 3% range) while improving training efficiency in cross-view action recognition.

