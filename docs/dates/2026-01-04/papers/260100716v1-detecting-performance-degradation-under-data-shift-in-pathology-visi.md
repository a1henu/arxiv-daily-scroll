---
layout: default
title: Detecting Performance Degradation under Data Shift in Pathology Vision-Language Model
---

# Detecting Performance Degradation under Data Shift in Pathology Vision-Language Model
**arXiv**：[2601.00716v1](https://arxiv.org/abs/2601.00716) · [PDF](https://arxiv.org/pdf/2601.00716.pdf)  
**作者**：Hao Guan, Li Zhou  

**一句话要点**：提出结合输入数据偏移检测与输出置信度指标的方法，以监测病理视觉语言模型在数据偏移下的性能退化。

**关键词**：视觉语言模型, 数据偏移检测, 性能退化监测, 病理图像分析, 无标签监控, 模型可靠性

## 3 点简述
- 研究病理视觉语言模型在部署后因数据偏移导致的性能退化检测问题。
- 开发DomainSAT工具箱分析输入数据偏移，并引入基于置信度的无标签退化指标。
- 在大规模病理数据集上实验，验证结合方法能更可靠地检测和解释性能退化。

## 摘要（原文）

> Vision-Language Models have demonstrated strong potential in medical image analysis and disease diagnosis. However, after deployment, their performance may deteriorate when the input data distribution shifts from that observed during development. Detecting such performance degradation is essential for clinical reliability, yet remains challenging for large pre-trained VLMs operating without labeled data. In this study, we investigate performance degradation detection under data shift in a state-of-the-art pathology VLM. We examine both input-level data shift and output-level prediction behavior to understand their respective roles in monitoring model reliability. To facilitate systematic analysis of input data shift, we develop DomainSAT, a lightweight toolbox with a graphical interface that integrates representative shift detection algorithms and enables intuitive exploration of data shift. Our analysis shows that while input data shift detection is effective at identifying distributional changes and providing early diagnostic signals, it does not always correspond to actual performance degradation. Motivated by this observation, we further study output-based monitoring and introduce a label-free, confidence-based degradation indicator that directly captures changes in model prediction confidence. We find that this indicator exhibits a close relationship with performance degradation and serves as an effective complement to input shift detection. Experiments on a large-scale pathology dataset for tumor classification demonstrate that combining input data shift detection and output confidence-based indicators enables more reliable detection and interpretation of performance degradation in VLMs under data shift. These findings provide a practical and complementary framework for monitoring the reliability of foundation models in digital pathology.

