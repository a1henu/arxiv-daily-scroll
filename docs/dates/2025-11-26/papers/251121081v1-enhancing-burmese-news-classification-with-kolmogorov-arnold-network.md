---
layout: default
title: Enhancing Burmese News Classification with Kolmogorov-Arnold Network Head Fine-tuning
---

# Enhancing Burmese News Classification with Kolmogorov-Arnold Network Head Fine-tuning
**arXiv**：[2511.21081v1](https://arxiv.org/abs/2511.21081) · [PDF](https://arxiv.org/pdf/2511.21081.pdf)  
**作者**：Thura Aung, Eaint Kay Khaing Kyaw, Ye Kyaw Thu, Thazin Myint Oo, Thepchai Supnithi  

**一句话要点**：提出KAN分类头微调方法以提升缅甸语新闻分类性能

**关键词**：低资源语言分类, Kolmogorov-Arnold网络, 分类头微调, 缅甸语新闻, 多语言嵌入, 计算效率

## 3 点简述
- 缅甸语等低资源语言分类常仅微调最终层，固定预训练编码器权重
- 使用Kolmogorov-Arnold网络作为分类头，评估FourierKAN、EfficientKAN和FasterKAN变体
- 实验显示KAN头在F1分数和速度上优于或匹配传统MLP，EfficientKAN达最高0.928 F1

## 摘要（原文）

> In low-resource languages like Burmese, classification tasks often fine-tune only the final classification layer, keeping pre-trained encoder weights frozen. While Multi-Layer Perceptrons (MLPs) are commonly used, their fixed non-linearity can limit expressiveness and increase computational cost. This work explores Kolmogorov-Arnold Networks (KANs) as alternative classification heads, evaluating Fourier-based FourierKAN, Spline-based EfficientKAN, and Grid-based FasterKAN-across diverse embeddings including TF-IDF, fastText, and multilingual transformers (mBERT, Distil-mBERT). Experimental results show that KAN-based heads are competitive with or superior to MLPs. EfficientKAN with fastText achieved the highest F1-score (0.928), while FasterKAN offered the best trade-off between speed and accuracy. On transformer embeddings, EfficientKAN matched or slightly outperformed MLPs with mBERT (0.917 F1). These findings highlight KANs as expressive, efficient alternatives to MLPs for low-resource language classification.

