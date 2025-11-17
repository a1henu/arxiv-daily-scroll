---
layout: default
title: EmbryoDiff: A Conditional Diffusion Framework with Multi-Focal Feature Fusion for Fine-Grained Embryo Developmental Stage Recognition
---

# EmbryoDiff: A Conditional Diffusion Framework with Multi-Focal Feature Fusion for Fine-Grained Embryo Developmental Stage Recognition
**arXiv**：[2511.11027v1](https://arxiv.org/abs/2511.11027) · [PDF](https://arxiv.org/pdf/2511.11027.pdf)  
**作者**：Yong Sun, Zhengjie Zhang, Junyu Shi, Zhiyuan Zhang, Lijiang Liu, Qiang Nie  

**一句话要点**：提出EmbryoDiff扩散框架，融合多焦特征以识别胚胎发育阶段

**关键词**：胚胎发育识别, 条件扩散模型, 多焦特征融合, 语义边界条件, 体外受精分析

## 3 点简述
- 现有模型未利用胚胎发育分布先验，且单焦信息易受细胞遮挡影响
- 采用两阶段扩散方法，融合多焦特征并注入语义边界条件
- 在基准数据集上达到82.8%和81.3%准确率，优于现有方法

## 摘要（原文）

> Identification of fine-grained embryo developmental stages during In Vitro Fertilization (IVF) is crucial for assessing embryo viability. Although recent deep learning methods have achieved promising accuracy, existing discriminative models fail to utilize the distributional prior of embryonic development to improve accuracy. Moreover, their reliance on single-focal information leads to incomplete embryonic representations, making them susceptible to feature ambiguity under cell occlusions. To address these limitations, we propose EmbryoDiff, a two-stage diffusion-based framework that formulates the task as a conditional sequence denoising process. Specifically, we first train and freeze a frame-level encoder to extract robust multi-focal features. In the second stage, we introduce a Multi-Focal Feature Fusion Strategy that aggregates information across focal planes to construct a 3D-aware morphological representation, effectively alleviating ambiguities arising from cell occlusions. Building on this fused representation, we derive complementary semantic and boundary cues and design a Hybrid Semantic-Boundary Condition Block to inject them into the diffusion-based denoising process, enabling accurate embryonic stage classification. Extensive experiments on two benchmark datasets show that our method achieves state-of-the-art results. Notably, with only a single denoising step, our model obtains the best average test performance, reaching 82.8% and 81.3% accuracy on the two datasets, respectively.

