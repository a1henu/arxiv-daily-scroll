---
layout: default
title: Bayesian Integration of Nonlinear Incomplete Clinical Data
---

# Bayesian Integration of Nonlinear Incomplete Clinical Data
**arXiv**：[2602.01924v1](https://arxiv.org/abs/2602.01924) · [PDF](https://arxiv.org/pdf/2602.01924.pdf)  
**作者**：Lucía González-Zamorano, Nuria Balbás-Esteban, Vanessa Gómez-Verdejo, Albert Belenguer-Llorens, Carlos Sevilla-Salcedo  

**一句话要点**：提出BIONIC框架以解决多模态临床数据高维异构与缺失下的集成与预测问题

**关键词**：多模态数据集成, 贝叶斯建模, 临床预测, 缺失数据处理, 潜变量架构

## 3 点简述
- 核心问题：多模态临床数据高维异构、结构化缺失，阻碍预测建模与可解释性
- 方法要点：基于贝叶斯生成-判别潜架构，集成预训练嵌入与结构化变量，显式建模缺失
- 实验或效果：在三个数据集上验证，缺失场景下性能优于基线，提供潜结构可解释性

## 摘要（原文）

> Multimodal clinical data are characterized by high dimensionality, heterogeneous representations, and structured missingness, posing significant challenges for predictive modeling, data integration, and interpretability. We propose BIONIC (Bayesian Integration of Nonlinear Incomplete Clinical data), a unified probabilistic framework that integrates heterogeneous multimodal data under missingness through a joint generative-discriminative latent architecture. BIONIC uses pretrained embeddings for complex modalities such as medical images and clinical text, while incorporating structured clinical variables directly within a Bayesian multimodal formulation. The proposed framework enables robust learning in partially observed and semi-supervised settings by explicitly modeling modality-level and variable-level missingness, as well as missing labels. We evaluate BIONIC on three multimodal clinical and biomedical datasets, demonstrating strong and consistent discriminative performance compared to representative multimodal baselines, particularly under incomplete data scenarios. Beyond predictive accuracy, BIONIC provides intrinsic interpretability through its latent structure, enabling population-level analysis of modality relevance and supporting clinically meaningful insight.

