---
layout: default
title: Adaptive Prototype-based Interpretable Grading of Prostate Cancer
---

# Adaptive Prototype-based Interpretable Grading of Prostate Cancer
**arXiv**：[2603.04947v1](https://arxiv.org/abs/2603.04947) · [PDF](https://arxiv.org/pdf/2603.04947.pdf)  
**作者**：Riddhasree Bhattacharyya, Pallabi Dutta, Sushmita Mitra  

**一句话要点**：提出基于自适应原型的弱监督框架，用于前列腺癌组织病理学图像的可解释分级。

**关键词**：前列腺癌分级, 原型学习, 弱监督学习, 可解释人工智能, 组织病理学图像, 注意力机制

## 3 点简述
- 核心问题：前列腺癌分级自动化需求高，但现有深度学习模型可解释性不足，难以在医疗高风险应用中推广。
- 方法要点：采用原型学习，通过补丁级预训练和原型感知损失微调，结合注意力动态剪枝处理样本异质性。
- 实验或效果：在PANDA和SICAP数据集上验证，框架可作为病理学家可靠辅助工具，提升分级可解释性。

## 摘要（原文）

> Prostate cancer being one of the frequently diagnosed malignancy in men, the rising demand for biopsies places a severe workload on pathologists. The grading procedure is tedious and subjective, motivating the development of automated systems. Although deep learning has made inroads in terms of performance, its limited interpretability poses challenges for widespread adoption in high-stake applications like medicine. Existing interpretability techniques for prostate cancer classifiers provide a coarse explanation but do not reveal why the highlighted regions matter. In this scenario, we propose a novel prototype-based weakly-supervised framework for an interpretable grading of prostate cancer from histopathology images. These networks can prove to be more trustworthy since their explicit reasoning procedure mirrors the workflow of a pathologist in comparing suspicious regions with clinically validated examples. The network is initially pre-trained at patch-level to learn robust prototypical features associated with each grade. In order to adapt it to a weakly-supervised setup for prostate cancer grading, the network is fine-tuned with a new prototype-aware loss function. Finally, a new attention-based dynamic pruning mechanism is introduced to handle inter-sample heterogeneity, while selectively emphasizing relevant prototypes for optimal performance. Extensive validation on the benchmark PANDA and SICAP datasets confirms that the framework can serve as a reliable assistive tool for pathologists in their routine diagnostic workflows.

