---
layout: default
title: Instruction-Guided Lesion Segmentation for Chest X-rays with Automatically Generated Large-Scale Dataset
---

# Instruction-Guided Lesion Segmentation for Chest X-rays with Automatically Generated Large-Scale Dataset
**arXiv**：[2511.15186v1](https://arxiv.org/abs/2511.15186) · [PDF](https://arxiv.org/pdf/2511.15186.pdf)  
**作者**：Geon Choi, Hangyul Yoon, Hyunju Shin, Hyunki Park, Sang Hoon Seo, Eunho Yang, Edward Choi  

**一句话要点**：提出指令引导病变分割范式以解决胸片分割模型标签少和输入复杂的问题

**关键词**：指令引导分割, 胸片病变分割, 多模态数据集, 自动化标注, 视觉语言模型, 像素级定位

## 3 点简述
- 当前胸片病变分割模型标签数量少且依赖专家级文本输入，实用性受限
- 构建首个大规模指令-答案数据集MIMIC-ILS，使用自动化多模态管道生成标注
- 微调模型ROSALIA在分割和文本解释任务中表现高准确度，验证方法有效性

## 摘要（原文）

> The applicability of current lesion segmentation models for chest X-rays (CXRs) has been limited both by a small number of target labels and the reliance on long, detailed expert-level text inputs, creating a barrier to practical use. To address these limitations, we introduce a new paradigm: instruction-guided lesion segmentation (ILS), which is designed to segment diverse lesion types based on simple, user-friendly instructions. Under this paradigm, we construct MIMIC-ILS, the first large-scale instruction-answer dataset for CXR lesion segmentation, using our fully automated multimodal pipeline that generates annotations from chest X-ray images and their corresponding reports. MIMIC-ILS contains 1.1M instruction-answer pairs derived from 192K images and 91K unique segmentation masks, covering seven major lesion types. To empirically demonstrate its utility, we introduce ROSALIA, a vision-language model fine-tuned on MIMIC-ILS. ROSALIA can segment diverse lesions and provide textual explanations in response to user instructions. The model achieves high segmentation and textual accuracy in our newly proposed task, highlighting the effectiveness of our pipeline and the value of MIMIC-ILS as a foundational resource for pixel-level CXR lesion grounding.

