---
layout: default
title: Order Matters in Retrosynthesis: Structure-aware Generation via Reaction-Center-Guided Discrete Flow Matching
---

# Order Matters in Retrosynthesis: Structure-aware Generation via Reaction-Center-Guided Discrete Flow Matching
**arXiv**：[2602.13136v1](https://arxiv.org/abs/2602.13136) · [PDF](https://arxiv.org/pdf/2602.13136.pdf)  
**作者**：Chenguang Wang, Zihan Zhou, Lei Bai, Tianshu Yu  

**一句话要点**：提出基于反应中心引导离散流匹配的结构感知逆合成方法，以解决原子顺序在神经表示中的重要性问题。

**关键词**：逆合成预测, 结构感知生成, 离散流匹配, 反应中心引导, 图变换器, 位置编码

## 3 点简述
- 核心问题：传统无模板方法学习效率低，半模板方法泛化受限，原子顺序在逆合成中未被充分利用。
- 方法要点：通过将反应中心原子置于序列头部，编码化学反应的两阶段特性作为位置归纳偏置，结合RetroDiT骨干网络和离散流匹配。
- 实验或效果：在USPTO-50k和USPTO-Full上达到SOTA性能，生成步骤减少至20-50步，结构先验优于暴力缩放。

## 摘要（原文）

> Template-free retrosynthesis methods treat the task as black-box sequence generation, limiting learning efficiency, while semi-template approaches rely on rigid reaction libraries that constrain generalization. We address this gap with a key insight: atom ordering in neural representations matters. Building on this insight, we propose a structure-aware template-free framework that encodes the two-stage nature of chemical reactions as a positional inductive bias. By placing reaction center atoms at the sequence head, our method transforms implicit chemical knowledge into explicit positional patterns that the model can readily capture. The proposed RetroDiT backbone, a graph transformer with rotary position embeddings, exploits this ordering to prioritize chemically critical regions. Combined with discrete flow matching, our approach decouples training from sampling and enables generation in 20--50 steps versus 500 for prior diffusion methods. Our method achieves state-of-the-art performance on both USPTO-50k (61.2% top-1) and the large-scale USPTO-Full (51.3% top-1) with predicted reaction centers. With oracle centers, performance reaches 71.1% and 63.4% respectively, surpassing foundation models trained on 10 billion reactions while using orders of magnitude less data. Ablation studies further reveal that structural priors outperform brute-force scaling: a 280K-parameter model with proper ordering matches a 65M-parameter model without it.

