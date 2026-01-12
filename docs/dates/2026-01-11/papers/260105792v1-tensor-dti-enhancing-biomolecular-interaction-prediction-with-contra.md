---
layout: default
title: Tensor-DTI: Enhancing Biomolecular Interaction Prediction with Contrastive Embedding Learning
---

# Tensor-DTI: Enhancing Biomolecular Interaction Prediction with Contrastive Embedding Learning
**arXiv**：[2601.05792v1](https://arxiv.org/abs/2601.05792) · [PDF](https://arxiv.org/pdf/2601.05792.pdf)  
**作者**：Manel Gil-Sorribes, Júlia Vilalta-Mor, Isaac Filella-Mercè, Robert Soliva, Álvaro Ciudad, Víctor Guallar, Alexis Molina  

**一句话要点**：提出Tensor-DTI对比学习框架，整合多模态嵌入以增强药物-靶标相互作用预测

**关键词**：药物-靶标相互作用预测, 对比学习, 多模态嵌入, 虚拟筛选, 孪生网络, 蛋白质语言模型

## 3 点简述
- 现有DTI预测模型依赖单模态描述符或序列嵌入，代表性有限
- Tensor-DTI采用孪生双编码器架构，整合分子图、蛋白质语言模型和结合位点预测的多模态嵌入
- 在多个DTI基准测试中超越现有模型，并在大规模虚拟筛选中展示化学合理性和竞争力

## 摘要（原文）

> Accurate drug-target interaction (DTI) prediction is essential for computational drug discovery, yet existing models often rely on single-modality predefined molecular descriptors or sequence-based embeddings with limited representativeness. We propose Tensor-DTI, a contrastive learning framework that integrates multimodal embeddings from molecular graphs, protein language models, and binding-site predictions to improve interaction modeling. Tensor-DTI employs a siamese dual-encoder architecture, enabling it to capture both chemical and structural interaction features while distinguishing interacting from non-interacting pairs. Evaluations on multiple DTI benchmarks demonstrate that Tensor-DTI outperforms existing sequence-based and graph-based models. We also conduct large-scale inference experiments on CDK2 across billion-scale chemical libraries, where Tensor-DTI produces chemically plausible hit distributions even when CDK2 is withheld from training. In enrichment studies against Glide docking and Boltz-2 co-folder, Tensor-DTI remains competitive on CDK2 and improves the screening budget required to recover moderate fractions of high-affinity ligands on out-of-family targets under strict family-holdout splits. Additionally, we explore its applicability to protein-RNA and peptide-protein interactions. Our findings highlight the benefits of integrating multimodal information with contrastive objectives to enhance interaction-prediction accuracy and to provide more interpretable and reliability-aware models for virtual screening.

