---
layout: default
title: RhythmBERT: A Self-Supervised Language Model Based on Latent Representations of ECG Waveforms for Heart Disease Detection
---

# RhythmBERT: A Self-Supervised Language Model Based on Latent Representations of ECG Waveforms for Heart Disease Detection
**arXiv**：[2602.23060v1](https://arxiv.org/abs/2602.23060) · [PDF](https://arxiv.org/pdf/2602.23060.pdf)  
**作者**：Xin Wang, Burcu Ozek, Aruna Mohan, Amirhossein Ravari, Or Zilbershot, Fatemeh Afghah  

**一句话要点**：提出RhythmBERT，基于ECG波形潜在表示的自监督语言模型，用于心脏病检测。

**关键词**：心电图分析, 自监督学习, 语言模型, 心脏病检测, 潜在表示, 节律语义

## 3 点简述
- 核心问题：现有自监督方法将ECG视为通用时间序列，忽略生理语义和节律结构，对比方法扭曲形态，生成方法分割窗口错位心搏周期。
- 方法要点：将ECG编码为P、QRS、T段的符号令牌，结合连续嵌入，通过掩码预测目标预训练，学习上下文表示。
- 实验或效果：在约80万无标签ECG记录上预训练，单导联性能媲美或优于12导联基线，泛化至心房颤动、ST-T异常和心肌梗死等病例。

## 摘要（原文）

> Electrocardiogram (ECG) analysis is crucial for diagnosing heart disease, but most self-supervised learning methods treat ECG as a generic time series, overlooking physiologic semantics and rhythm-level structure. Existing contrastive methods utilize augmentations that distort morphology, whereas generative approaches employ fixed-window segmentation, which misaligns cardiac cycles. To address these limitations, we propose RhythmBERT, a generative ECG language model that considers ECG as a language paradigm by encoding P, QRS, and T segments into symbolic tokens via autoencoder-based latent representations. These discrete tokens capture rhythm semantics, while complementary continuous embeddings retain fine-grained morphology, enabling a unified view of waveform structure and rhythm. RhythmBERT is pretrained on approximately 800,000 unlabeled ECG recordings with a masked prediction objective, allowing it to learn contextual representations in a label-efficient manner. Evaluations show that despite using only a single lead, RhythmBERT achieves comparable or superior performance to strong 12-lead baselines. This generalization extends from prevalent conditions such as atrial fibrillation to clinically challenging cases such as subtle ST-T abnormalities and myocardial infarction. Our results suggest that considering ECG as structured language offers a scalable and physiologically aligned pathway for advancing cardiac analysis.

