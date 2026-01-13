---
layout: default
title: Advancing Multinational License Plate Recognition Through Synthetic and Real Data Fusion: A Comprehensive Evaluation
---

# Advancing Multinational License Plate Recognition Through Synthetic and Real Data Fusion: A Comprehensive Evaluation
**arXiv**：[2601.07671v1](https://arxiv.org/abs/2601.07671) · [PDF](https://arxiv.org/pdf/2601.07671.pdf)  
**作者**：Rayson Laroca, Valter Estevam, Gladston J. P. Moreira, Rodrigo Minetto, David Menotti  

**一句话要点**：提出融合合成与真实数据方法，提升多国车牌识别性能，通过综合评估验证其有效性。

**关键词**：车牌识别, 合成数据融合, OCR模型评估, 跨数据集性能, 生成对抗网络

## 3 点简述
- 核心问题：现有车牌识别研究在合成数据应用上存在局限，影响跨数据集性能。
- 方法要点：探索三种合成数据生成方法（模板生成、字符排列、GAN），并融合真实数据训练OCR模型。
- 实验或效果：在12个公共数据集上评估16个模型，合成数据显著提升性能，尤其在数据有限时效果突出。

## 摘要（原文）

> Automatic License Plate Recognition is a frequent research topic due to its wide-ranging practical applications. While recent studies use synthetic images to improve License Plate Recognition (LPR) results, there remain several limitations in these efforts. This work addresses these constraints by comprehensively exploring the integration of real and synthetic data to enhance LPR performance. We subject 16 Optical Character Recognition (OCR) models to a benchmarking process involving 12 public datasets acquired from various regions. Several key findings emerge from our investigation. Primarily, the massive incorporation of synthetic data substantially boosts model performance in both intra- and cross-dataset scenarios. We examine three distinct methodologies for generating synthetic data: template-based generation, character permutation, and utilizing a Generative Adversarial Network (GAN) model, each contributing significantly to performance enhancement. The combined use of these methodologies demonstrates a notable synergistic effect, leading to end-to-end results that surpass those reached by state-of-the-art methods and established commercial systems. Our experiments also underscore the efficacy of synthetic data in mitigating challenges posed by limited training data, enabling remarkable results to be achieved even with small fractions of the original training data. Finally, we investigate the trade-off between accuracy and speed among different models, identifying those that strike the optimal balance in each intra-dataset and cross-dataset settings.

