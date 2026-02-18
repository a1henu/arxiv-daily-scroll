---
layout: default
title: Emergent Morphing Attack Detection in Open Multi-modal Large Language Models
---

# Emergent Morphing Attack Detection in Open Multi-modal Large Language Models
**arXiv**：[2602.15461v1](https://arxiv.org/abs/2602.15461) · [PDF](https://arxiv.org/pdf/2602.15461.pdf)  
**作者**：Marija Ivanovska, Vitomir Štruc  

**一句话要点**：评估开源多模态大语言模型在零样本单图像人脸变形攻击检测中的涌现能力

**关键词**：人脸变形攻击检测, 多模态大语言模型, 零样本学习, 生物特征安全, 图像法医分析, 视觉语言推理

## 3 点简述
- 人脸变形攻击威胁生物特征验证，现有检测系统泛化性差且需任务特定训练
- 首次系统评估开源多模态大语言模型在零样本单图像变形攻击检测中的性能，无需微调
- LLaVA1.6-Mistral-7B在等错误率上超越任务特定基线至少23%，显示多模态预训练隐含编码面部不一致性

## 摘要（原文）

> Face morphing attacks threaten biometric verification, yet most morphing attack detection (MAD) systems require task-specific training and generalize poorly to unseen attack types. Meanwhile, open-source multimodal large language models (MLLMs) have demonstrated strong visual-linguistic reasoning, but their potential in biometric forensics remains underexplored. In this paper, we present the first systematic zero-shot evaluation of open-source MLLMs for single-image MAD, using publicly available weights and a standardized, reproducible protocol. Across diverse morphing techniques, many MLLMs show non-trivial discriminative ability without any fine-tuning or domain adaptation, and LLaVA1.6-Mistral-7B achieves state-of-the-art performance, surpassing highly competitive task-specific MAD baselines by at least 23% in terms of equal error rate (EER). The results indicate that multimodal pretraining can implicitly encode fine-grained facial inconsistencies indicative of morphing artifacts, enabling zero-shot forensic sensitivity. Our findings position open-source MLLMs as reproducible, interpretable, and competitive foundations for biometric security and forensic image analysis. This emergent capability also highlights new opportunities to develop state-of-the-art MAD systems through targeted fine-tuning or lightweight adaptation, further improving accuracy and efficiency while preserving interpretability. To support future research, all code and evaluation protocols will be released upon publication.

