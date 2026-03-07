---
layout: default
title: Location-Aware Pretraining for Medical Difference Visual Question Answering
---

# Location-Aware Pretraining for Medical Difference Visual Question Answering
**arXiv**：[2603.04950v1](https://arxiv.org/abs/2603.04950) · [PDF](https://arxiv.org/pdf/2603.04950.pdf)  
**作者**：Denis Musinguzi, Caren Han, Prasenjit Mitra  

**一句话要点**：提出位置感知预训练框架以提升医学差异视觉问答性能

**关键词**：医学视觉问答, 位置感知预训练, 差异检测, 胸部X光分析, 视觉表示学习

## 3 点简述
- 核心问题：传统视觉编码器在医学差异VQA中难以捕捉细微视觉变化，如区分疾病进展与采集差异。
- 方法要点：引入AREF、GCAP和CAREF等位置感知任务，学习细粒度空间视觉表示。
- 实验或效果：在胸部X光图像上实现最先进性能，有效检测和推理临床相关变化。

## 摘要（原文）

> Unlike conventional single-image models, differential medical VQA frameworks process multiple images to identify differences, mirroring the comparative diagnostic workflow of radiologists. However, standard vision encoders trained on contrastive or classification objectives often fail to capture the subtle visual variations necessary for distinguishing disease progression from acquisition differences. To address this limitation, we introduce a pretraining framework that incorporates location-aware tasks, including automatic referring expressions (AREF), grounded captioning (GCAP), and conditional automatic referring expressions (CAREF). These specific tasks enable the vision encoder to learn fine-grained, spatially grounded visual representations that are often overlooked by traditional pre-training methods. We subsequently integrate this enhanced vision encoder with a language model to perform medical difference VQA. Experimental results demonstrate that our approach achieves state-of-the-art performance in detecting and reasoning about clinically relevant changes in chest X-ray images.

