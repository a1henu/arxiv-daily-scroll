---
layout: default
title: MTQE.en-he: Machine Translation Quality Estimation for English-Hebrew
---

# MTQE.en-he: Machine Translation Quality Estimation for English-Hebrew
**arXiv**：[2602.06546v1](https://arxiv.org/abs/2602.06546) · [PDF](https://arxiv.org/pdf/2602.06546.pdf)  
**作者**：Andy Rosenbaum, Assaf Siani, Ilan Kernerman  

**一句话要点**：发布首个公开英希机器翻译质量估计基准MTQE.en-he，并评估模型性能与微调方法。

**关键词**：机器翻译质量估计, 英希语言对, 基准数据集, 模型集成, 参数高效微调, 人工评估

## 3 点简述
- 核心问题：英希语言对缺乏公开机器翻译质量估计基准，限制相关研究发展。
- 方法要点：构建包含959个英希翻译对及人工评分的基准，测试ChatGPT、TransQuest和CometKiwi模型。
- 实验或效果：集成模型优于最佳单模型，参数高效微调方法稳定提升性能2-3个百分点。

## 摘要（原文）

> We release MTQE.en-he: to our knowledge, the first publicly available English-Hebrew benchmark for Machine Translation Quality Estimation. MTQE.en-he contains 959 English segments from WMT24++, each paired with a machine translation into Hebrew, and Direct Assessment scores of the translation quality annotated by three human experts. We benchmark ChatGPT prompting, TransQuest, and CometKiwi and show that ensembling the three models outperforms the best single model (CometKiwi) by 6.4 percentage points Pearson and 5.6 percentage points Spearman. Fine-tuning experiments with TransQuest and CometKiwi reveal that full-model updates are sensitive to overfitting and distribution collapse, yet parameter-efficient methods (LoRA, BitFit, and FTHead, i.e., fine-tuning only the classification head) train stably and yield improvements of 2-3 percentage points. MTQE.en-he and our experimental results enable future research on this under-resourced language pair.

