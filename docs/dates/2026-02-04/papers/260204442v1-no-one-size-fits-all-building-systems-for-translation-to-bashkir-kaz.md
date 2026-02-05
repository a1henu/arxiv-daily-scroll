---
layout: default
title: No One-Size-Fits-All: Building Systems For Translation to Bashkir, Kazakh, Kyrgyz, Tatar and Chuvash Using Synthetic And Original Data
---

# No One-Size-Fits-All: Building Systems For Translation to Bashkir, Kazakh, Kyrgyz, Tatar and Chuvash Using Synthetic And Original Data
**arXiv**：[2602.04442v1](https://arxiv.org/abs/2602.04442) · [PDF](https://arxiv.org/pdf/2602.04442.pdf)  
**作者**：Dmitry Karpov  

**一句话要点**：提出基于合成与原始数据的系统，以提升俄语-巴什基尔语等五种突厥语对的机器翻译性能。

**关键词**：机器翻译, 突厥语对, 合成数据, LoRA微调, 检索增强, 开源资源

## 3 点简述
- 研究俄语-巴什基尔语等五种突厥语对的机器翻译，资源稀缺是核心挑战。
- 采用LoRA微调NLLB模型和基于检索的提示方法，结合合成与原始数据。
- 实验显示，哈萨克语chrF++达49.71，楚瓦什语达39.47，并开源数据集与模型权重。

## 摘要（原文）

> We explore machine translation for five Turkic language pairs: Russian-Bashkir, Russian-Kazakh, Russian-Kyrgyz, English-Tatar, English-Chuvash. Fine-tuning nllb-200-distilled-600M with LoRA on synthetic data achieved chrF++ 49.71 for Kazakh and 46.94 for Bashkir. Prompting DeepSeek-V3.2 with retrieved similar examples achieved chrF++ 39.47 for Chuvash. For Tatar, zero-shot or retrieval-based approaches achieved chrF++ 41.6, while for Kyrgyz the zero-shot approach reached 45.6. We release the dataset and the obtained weights.

