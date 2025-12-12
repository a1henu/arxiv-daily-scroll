---
layout: default
title: Solving Semi-Supervised Few-Shot Learning from an Auto-Annotation Perspective
---

# Solving Semi-Supervised Few-Shot Learning from an Auto-Annotation Perspective
**arXiv**：[2512.10244v1](https://arxiv.org/abs/2512.10244) · [PDF](https://arxiv.org/pdf/2512.10244.pdf)  
**作者**：Tian Liu, Anwesha Basu, James Caverlee, Shu Kong  

**一句话要点**：提出SWIFT方法，通过初始化分类器和温度调优解决半监督少样本学习中的VLM微调问题

**关键词**：半监督少样本学习, 视觉语言模型, 自动标注, 温度调优, 伪标签, 微调策略

## 3 点简述
- 核心问题：现有SSL方法微调VLM时，因softmax概率分布平坦导致未标记数据利用率和监督信号弱
- 方法要点：引入分类器初始化和温度调优，提升伪标签置信度，并设计SWIFT进行分阶段微调
- 实验或效果：在五个SSFSL基准上，SWIFT超越近期FSL和SSL方法约5个准确率点，媲美监督学习

## 摘要（原文）

> Semi-supervised few-shot learning (SSFSL) formulates real-world applications like ''auto-annotation'', as it aims to learn a model over a few labeled and abundant unlabeled examples to annotate the unlabeled ones. Despite the availability of powerful open-source Vision-Language Models (VLMs) and their pretraining data, the SSFSL literature largely neglects these open-source resources. In contrast, the related area few-shot learning (FSL) has already exploited them to boost performance. Arguably, to achieve auto-annotation in the real world, SSFSL should leverage such open-source resources. To this end, we start by applying established SSL methods to finetune a VLM. Counterintuitively, they significantly underperform FSL baselines. Our in-depth analysis reveals the root cause: VLMs produce rather ''flat'' distributions of softmax probabilities. This results in zero utilization of unlabeled data and weak supervision signals. We address this issue with embarrassingly simple techniques: classifier initialization and temperature tuning. They jointly increase the confidence scores of pseudo-labels, improving the utilization rate of unlabeled data, and strengthening supervision signals. Building on this, we propose: Stage-Wise Finetuning with Temperature Tuning (SWIFT), which enables existing SSL methods to effectively finetune a VLM on limited labeled data, abundant unlabeled data, and task-relevant but noisy data retrieved from the VLM's pretraining set. Extensive experiments on five SSFSL benchmarks show that SWIFT outperforms recent FSL and SSL methods by $\sim$5 accuracy points. SWIFT even rivals supervised learning, which finetunes VLMs with the unlabeled data being labeled with ground truth!

