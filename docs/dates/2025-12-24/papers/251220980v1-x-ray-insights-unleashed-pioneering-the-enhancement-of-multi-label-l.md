---
layout: default
title: X-ray Insights Unleashed: Pioneering the Enhancement of Multi-Label Long-Tail Data
---

# X-ray Insights Unleashed: Pioneering the Enhancement of Multi-Label Long-Tail Data
**arXiv**：[2512.20980v1](https://arxiv.org/abs/2512.20980) · [PDF](https://arxiv.org/pdf/2512.20980.pdf)  
**作者**：Xinquan Yang, Jinheng Xie, Yawen Huang, Yuexiang Li, Huimin Huang, Hao Zheng, Xian Wu, Yefeng Zheng, Linlin Shen  

**一句话要点**：提出基于扩散模型的数据合成管道，以增强胸部X光中长尾肺异常的诊断性能。

**关键词**：长尾数据增强, 扩散模型, 胸部X光分析, 数据合成, 多标签分类, 渐进学习

## 3 点简述
- 核心问题：胸部X光中长尾肺异常数据稀缺，导致基于扩散的方法生成能力受限，诊断精度不足。
- 方法要点：利用大量正常X光训练扩散模型，通过修复头部病变图像来增强尾部类数据，并引入大语言模型知识指导和渐进增量学习策略。
- 实验或效果：在MIMIC和CheXpert数据集上评估，该方法在性能上设定了新基准。

## 摘要（原文）

> Long-tailed pulmonary anomalies in chest radiography present formidable diagnostic challenges. Despite the recent strides in diffusion-based methods for enhancing the representation of tailed lesions, the paucity of rare lesion exemplars curtails the generative capabilities of these approaches, thereby leaving the diagnostic precision less than optimal. In this paper, we propose a novel data synthesis pipeline designed to augment tail lesions utilizing a copious supply of conventional normal X-rays. Specifically, a sufficient quantity of normal samples is amassed to train a diffusion model capable of generating normal X-ray images. This pre-trained diffusion model is subsequently utilized to inpaint the head lesions present in the diseased X-rays, thereby preserving the tail classes as augmented training data. Additionally, we propose the integration of a Large Language Model Knowledge Guidance (LKG) module alongside a Progressive Incremental Learning (PIL) strategy to stabilize the inpainting fine-tuning process. Comprehensive evaluations conducted on the public lung datasets MIMIC and CheXpert demonstrate that the proposed method sets a new benchmark in performance.

