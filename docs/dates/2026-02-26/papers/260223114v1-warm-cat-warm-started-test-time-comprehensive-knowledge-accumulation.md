---
layout: default
title: WARM-CAT: : Warm-Started Test-Time Comprehensive Knowledge Accumulation for Compositional Zero-Shot Learning
---

# WARM-CAT: : Warm-Started Test-Time Comprehensive Knowledge Accumulation for Compositional Zero-Shot Learning
**arXiv**：[2602.23114v1](https://arxiv.org/abs/2602.23114) · [PDF](https://arxiv.org/pdf/2602.23114.pdf)  
**作者**：Xudong Yan, Songhe Feng, Jiaxin Wang, Xin Su, Yi Jin  

**一句话要点**：提出WARM-CAT方法，通过测试时知识积累解决组合零样本学习中的分布偏移问题。

**关键词**：组合零样本学习, 测试时适应, 多模态原型, 分布偏移, 动态队列, 基准数据集

## 3 点简述
- 核心问题：组合零样本学习中，测试时包含未见组合导致标签空间分布偏移，性能下降。
- 方法要点：在测试时从无监督数据积累多模态知识，更新原型，并设计自适应权重和动态队列以灵活适应分布变化。
- 实验或效果：在四个基准数据集上，包括新引入的C-Fashion和改进的MIT-States，在封闭和开放世界设置下达到最先进性能。

## 摘要（原文）

> Compositional Zero-Shot Learning (CZSL) aims to recognize novel attribute-object compositions based on the knowledge learned from seen ones. Existing methods suffer from performance degradation caused by the distribution shift of label space at test time, which stems from the inclusion of unseen compositions recombined from attributes and objects. To overcome the challenge, we propose a novel approach that accumulates comprehensive knowledge in both textual and visual modalities from unsupervised data to update multimodal prototypes at test time. Building on this, we further design an adaptive update weight to control the degree of prototype adjustment, enabling the model to flexibly adapt to distribution shift during testing. Moreover, a dynamic priority queue is introduced that stores high-confidence images to acquire visual prototypes from historical images for inference. Since the model tends to favor compositions already stored in the queue during testing, we warm-start the queue by initializing it with training images for visual prototypes of seen compositions and generating unseen visual prototypes using the mapping learned between seen and unseen textual prototypes. Considering the semantic consistency of multimodal knowledge, we align textual and visual prototypes by multimodal collaborative representation learning. To provide a more reliable evaluation for CZSL, we introduce a new benchmark dataset, C-Fashion, and refine the widely used but noisy MIT-States dataset. Extensive experiments indicate that our approach achieves state-of-the-art performance on four benchmark datasets under both closed-world and open-world settings. The source code and datasets are available at https://github.com/xud-yan/WARM-CAT .

