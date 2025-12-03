---
layout: default
title: Boosting Medical Vision-Language Pretraining via Momentum Self-Distillation under Limited Computing Resources
---

# Boosting Medical Vision-Language Pretraining via Momentum Self-Distillation under Limited Computing Resources
**arXiv**：[2512.02438v1](https://arxiv.org/abs/2512.02438) · [PDF](https://arxiv.org/pdf/2512.02438.pdf)  
**作者**：Phuc Pham, Nhu Pham, Ngoc Quoc Ly  

**一句话要点**：提出动量自蒸馏方法，在有限计算资源下提升医学视觉-语言预训练性能

**关键词**：医学视觉-语言模型, 动量自蒸馏, 对比学习, 计算效率, 少样本学习, 多模态预训练

## 3 点简述
- 医学视觉-语言模型训练面临标注数据少和计算资源受限问题
- 结合动量机制与自蒸馏，增强多模态学习并扩大有效批次大小
- 在零样本分类和少样本适应任务中达到SOTA性能，训练效率高

## 摘要（原文）

> In medical healthcare, obtaining detailed annotations is challenging, highlighting the need for robust Vision-Language Models (VLMs). Pretrained VLMs enable fine-tuning on small datasets or zero-shot inference, achieving performance comparable to task-specific models. Contrastive learning (CL) is a key paradigm for training VLMs but inherently requires large batch sizes for effective learning, making it computationally demanding and often limited to well-resourced institutions. Moreover, with limited data in healthcare, it is important to prioritize knowledge extraction from both data and models during training to improve performance. Therefore, we focus on leveraging the momentum method combined with distillation to simultaneously address computational efficiency and knowledge exploitation. Our contributions can be summarized as follows: (1) leveraging momentum self-distillation to enhance multimodal learning, and (2) integrating momentum mechanisms with gradient accumulation to enlarge the effective batch size without increasing resource consumption. Our method attains competitive performance with state-of-the-art (SOTA) approaches in zero-shot classification, while providing a substantial boost in the few-shot adaption, achieving over 90% AUC-ROC and improving retrieval tasks by 2-3%. Importantly, our method achieves high training efficiency with a single GPU while maintaining reasonable training time. Our approach aims to advance efficient multimodal learning by reducing resource requirements while improving performance over SOTA methods. The implementation of our method is available at https://github.com/phphuc612/MSD .

