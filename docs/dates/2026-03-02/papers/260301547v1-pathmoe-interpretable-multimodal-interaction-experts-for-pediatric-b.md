---
layout: default
title: PathMoE: Interpretable Multimodal Interaction Experts for Pediatric Brain Tumor Classification
---

# PathMoE: Interpretable Multimodal Interaction Experts for Pediatric Brain Tumor Classification
**arXiv**：[2603.01547v1](https://arxiv.org/abs/2603.01547) · [PDF](https://arxiv.org/pdf/2603.01547.pdf)  
**作者**：Jian Yu, Joakim Nguyen, Jinrui Fang, Awais Naeem, Zeyuan Cao, Sanjay Krishnan, Nicholas Konz, Tianlong Chen, Chandra Krishnan, Hairong Wang, Edward Castillo, Ying Ding, Ankita Shukla  

**一句话要点**：提出PathMoE以解决儿科脑肿瘤分类中多模态信息整合与模型可解释性挑战

**关键词**：多模态学习, 儿科脑肿瘤分类, 专家混合架构, 可解释性, 全切片图像分析, 细胞图

## 3 点简述
- 儿科中枢神经系统肿瘤分类因组织学复杂性和训练数据有限而困难
- PathMoE通过交互感知的专家混合架构整合H&E切片、病理报告和细胞图，动态加权模态交互
- 在内部PBT和外部TCGA数据集上，PathMoE显著提升分类性能，并提供样本级可解释性

## 摘要（原文）

> Accurate classification of pediatric central nervous system tumors remains challenging due to histological complexity and limited training data. While pathology foundation models have advanced whole-slide image (WSI) analysis, they often fail to leverage the rich, complementary information found in clinical text and tissue microarchitecture. To this end, we propose PathMoE, an interpretable multimodal framework that integrates H\&E slides, pathology reports, and nuclei-level cell graphs via an interaction-aware mixture-of-experts architecture built on state-of-the-art foundation models for each modality. By training specialized experts to capture modality uniqueness, redundancy, and synergy, PathMoE employs an input-dependent gating mechanism that dynamically weights these interactions, providing sample-level interpretability. We evaluate our framework on two dataset-specific classification tasks on an internal pediatric brain tumor dataset (PBT) and external TCGA datasets. PathMoE improves macro-F1 from 0.762 to 0.799 (+0.037) on PBT when integrating WSI, text, and graph modalities; on TCGA, augmenting WSI with graph knowledge improves macro-F1 from 0.668 to 0.709 (+0.041). These results demonstrate significant performance gains over state-of-the-art image-only baselines while revealing the specific modality interactions driving individual predictions. This interpretability is particularly critical for rare tumor subtypes, where transparent model reasoning is essential for clinical trust and diagnostic validation.

