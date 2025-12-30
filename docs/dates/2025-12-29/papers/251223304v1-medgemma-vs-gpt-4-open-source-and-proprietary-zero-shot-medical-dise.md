---
layout: default
title: MedGemma vs GPT-4: Open-Source and Proprietary Zero-shot Medical Disease Classification from Images
---

# MedGemma vs GPT-4: Open-Source and Proprietary Zero-shot Medical Disease Classification from Images
**arXiv**：[2512.23304v1](https://arxiv.org/abs/2512.23304) · [PDF](https://arxiv.org/pdf/2512.23304.pdf)  
**作者**：Md. Sazzadul Islam Prottasha, Nabil Walid Rafi  

**一句话要点**：比较MedGemma与GPT-4在零样本医学图像疾病分类中的性能，强调领域微调的重要性。

**关键词**：医学图像分类, 多模态大语言模型, 零样本学习, 低秩适应, 疾病诊断, 开源模型

## 3 点简述
- 核心问题：评估开源与专有多模态大模型在医学图像疾病分类中的零样本诊断能力。
- 方法要点：使用LoRA微调MedGemma-4b-it模型，并与未调优的GPT-4进行对比分析。
- 实验或效果：MedGemma在六种疾病分类中平均准确率达80.37%，高于GPT-4的69.58%，尤其在癌症和肺炎检测中敏感性更高。

## 摘要（原文）

> Multimodal Large Language Models (LLMs) introduce an emerging paradigm for medical imaging by interpreting scans through the lens of extensive clinical knowledge, offering a transformative approach to disease classification. This study presents a critical comparison between two fundamentally different AI architectures: the specialized open-source agent MedGemma and the proprietary large multimodal model GPT-4 for diagnosing six different diseases. The MedGemma-4b-it model, fine-tuned using Low-Rank Adaptation (LoRA), demonstrated superior diagnostic capability by achieving a mean test accuracy of 80.37% compared to 69.58% for the untuned GPT-4. Furthermore, MedGemma exhibited notably higher sensitivity in high-stakes clinical tasks, such as cancer and pneumonia detection. Quantitative analysis via confusion matrices and classification reports provides comprehensive insights into model performance across all categories. These results emphasize that domain-specific fine-tuning is essential for minimizing hallucinations in clinical implementation, positioning MedGemma as a sophisticated tool for complex, evidence-based medical reasoning.

