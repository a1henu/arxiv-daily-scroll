---
layout: default
title: FactCorrector: A Graph-Inspired Approach to Long-Form Factuality Correction of Large Language Models
---

# FactCorrector: A Graph-Inspired Approach to Long-Form Factuality Correction of Large Language Models
**arXiv**：[2601.11232v1](https://arxiv.org/abs/2601.11232) · [PDF](https://arxiv.org/pdf/2601.11232.pdf)  
**作者**：Javier Carnerero-Cano, Massimiliano Pronesti, Radu Marinescu, Tigran Tchrakian, James Barry, Jasmina Gajcin, Yufang Hou, Alessandra Pascale, Elizabeth Daly  

**一句话要点**：提出FactCorrector，一种基于图的后处理校正方法，用于纠正大语言模型的长文本事实性错误。

**关键词**：事实性校正, 大语言模型, 后处理方法, 图结构, 跨领域适应, 长文本生成

## 3 点简述
- 大语言模型在知识密集型应用中常生成事实错误，需后处理校正。
- FactCorrector利用结构化反馈，无需重训练即可跨领域校正事实性。
- 在VELI5等数据集上实验显示，该方法显著提升事实精度并保持相关性。

## 摘要（原文）

> Large language models (LLMs) are widely used in knowledge-intensive applications but often generate factually incorrect responses. A promising approach to rectify these flaws is correcting LLMs using feedback. Therefore, in this paper, we introduce FactCorrector, a new post-hoc correction method that adapts across domains without retraining and leverages structured feedback about the factuality of the original response to generate a correction. To support rigorous evaluations of factuality correction methods, we also develop the VELI5 benchmark, a novel dataset containing systematically injected factual errors and ground-truth corrections. Experiments on VELI5 and several popular long-form factuality datasets show that the FactCorrector approach significantly improves factual precision while preserving relevance, outperforming strong baselines. We release our code at https://ibm.biz/factcorrector.

