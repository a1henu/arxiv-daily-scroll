---
layout: default
title: BanglaLorica: Design and Evaluation of a Robust Watermarking Algorithm for Large Language Models in Bangla Text Generation
---

# BanglaLorica: Design and Evaluation of a Robust Watermarking Algorithm for Large Language Models in Bangla Text Generation
**arXiv**：[2601.04534v1](https://arxiv.org/abs/2601.04534) · [PDF](https://arxiv.org/pdf/2601.04534.pdf)  
**作者**：Amit Bin Tariqul, A N M Zahid Hossain Milkan, Sahab-Al-Chowdhury, Syed Rifat Raiyan, Hasan Mahmud, Md Kamrul Hasan  

**一句话要点**：提出分层水印策略以提升孟加拉语大语言模型文本生成在跨语言攻击下的鲁棒性

**关键词**：文本水印, 大语言模型, 孟加拉语, 跨语言攻击, 鲁棒性评估, 分层策略

## 3 点简述
- 评估现有水印方法在孟加拉语文本生成中的鲁棒性，发现跨语言回译攻击导致检测准确率崩溃
- 提出结合嵌入时和后生成水印的分层策略，显著提升攻击后检测准确率
- 实验显示分层水印在控制语义退化下实现3-4倍相对改进，量化多语言水印的鲁棒性-质量权衡

## 摘要（原文）

> As large language models (LLMs) are increasingly deployed for text generation, watermarking has become essential for authorship attribution, intellectual property protection, and misuse detection. While existing watermarking methods perform well in high-resource languages, their robustness in low-resource languages remains underexplored. This work presents the first systematic evaluation of state-of-the-art text watermarking methods: KGW, Exponential Sampling (EXP), and Waterfall, for Bangla LLM text generation under cross-lingual round-trip translation (RTT) attacks. Under benign conditions, KGW and EXP achieve high detection accuracy (>88%) with negligible perplexity and ROUGE degradation. However, RTT causes detection accuracy to collapse below RTT causes detection accuracy to collapse to 9-13%, indicating a fundamental failure of token-level watermarking. To address this, we propose a layered watermarking strategy that combines embedding-time and post-generation watermarks. Experimental results show that layered watermarking improves post-RTT detection accuracy by 25-35%, achieving 40-50% accuracy, representing a 3$\times$ to 4$\times$ relative improvement over single-layer methods, at the cost of controlled semantic degradation. Our findings quantify the robustness-quality trade-off in multilingual watermarking and establish layered watermarking as a practical, training-free solution for low-resource languages such as Bangla. Our code and data will be made public.

