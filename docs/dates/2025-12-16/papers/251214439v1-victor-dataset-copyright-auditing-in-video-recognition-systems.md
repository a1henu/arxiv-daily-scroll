---
layout: default
title: VICTOR: Dataset Copyright Auditing in Video Recognition Systems
---

# VICTOR: Dataset Copyright Auditing in Video Recognition Systems
**arXiv**：[2512.14439v1](https://arxiv.org/abs/2512.14439) · [PDF](https://arxiv.org/pdf/2512.14439.pdf)  
**作者**：Quan Yuan, Zhikun Zhang, Linkang Du, Min Chen, Mingyang Sun, Yunjun Gao, Shibo He, Jiming Chen  

**一句话要点**：提出VICTOR以解决视频识别系统中的数据集版权审计问题

**关键词**：视频识别, 数据集版权, 样本修改, 模型行为分析, 版权审计

## 3 点简述
- 视频数据因时间维度复杂，现有图像域版权审计方法难以适用
- 通过修改少量样本增强模型输出差异，实现隐蔽且有效的审计
- 在多个模型和数据集上验证了方法的优越性和鲁棒性

## 摘要（原文）

> Video recognition systems are increasingly being deployed in daily life, such as content recommendation and security monitoring. To enhance video recognition development, many institutions have released high-quality public datasets with open-source licenses for training advanced models. At the same time, these datasets are also susceptible to misuse and infringement. Dataset copyright auditing is an effective solution to identify such unauthorized use. However, existing dataset copyright solutions primarily focus on the image domain; the complex nature of video data leaves dataset copyright auditing in the video domain unexplored. Specifically, video data introduces an additional temporal dimension, which poses significant challenges to the effectiveness and stealthiness of existing methods.
>   In this paper, we propose VICTOR, the first dataset copyright auditing approach for video recognition systems. We develop a general and stealthy sample modification strategy that enhances the output discrepancy of the target model. By modifying only a small proportion of samples (e.g., 1%), VICTOR amplifies the impact of published modified samples on the prediction behavior of the target models. Then, the difference in the model's behavior for published modified and unpublished original samples can serve as a key basis for dataset auditing. Extensive experiments on multiple models and datasets highlight the superiority of VICTOR. Finally, we show that VICTOR is robust in the presence of several perturbation mechanisms to the training videos or the target models.

