---
layout: default
title: Synergy vs. Noise: Performance-Guided Multimodal Fusion For Biochemical Recurrence-Free Survival in Prostate Cancer
---

# Synergy vs. Noise: Performance-Guided Multimodal Fusion For Biochemical Recurrence-Free Survival in Prostate Cancer
**arXiv**：[2511.11452v1](https://arxiv.org/abs/2511.11452) · [PDF](https://arxiv.org/pdf/2511.11452.pdf)  
**作者**：Seth Alain Chang, Muhammad Mueez Amjad, Noorul Wahab, Ethar Alzaid, Nasir Rajpoot, Adam Shephard  

**一句话要点**：提出性能引导多模态融合方法以优化前列腺癌生化复发预测

**关键词**：多模态深度学习, 计算病理学, 前列腺癌预测, 模态融合策略, 性能引导选择

## 3 点简述
- 核心问题：多模态融合是否必然提升性能，或可能引入噪声
- 方法要点：基于模态预测性能选择性整合，避免弱模态干扰
- 实验或效果：在病理、放射和临床数据上验证，高绩效模态组合优于单模态

## 摘要（原文）

> Multimodal deep learning (MDL) has emerged as a transformative approach in computational pathology. By integrating complementary information from multiple data sources, MDL models have demonstrated superior predictive performance across diverse clinical tasks compared to unimodal models. However, the assumption that combining modalities inherently improves performance remains largely unexamined. We hypothesise that multimodal gains depend critically on the predictive quality of individual modalities, and that integrating weak modalities may introduce noise rather than complementary information. We test this hypothesis on a prostate cancer dataset with histopathology, radiology, and clinical data to predict time-to-biochemical recurrence. Our results confirm that combining high-performing modalities yield superior performance compared to unimodal approaches. However, integrating a poor-performing modality with other higher-performing modalities degrades predictive accuracy. These findings demonstrate that multimodal benefit requires selective, performance-guided integration rather than indiscriminate modality combination, with implications for MDL design across computational pathology and medical imaging.

