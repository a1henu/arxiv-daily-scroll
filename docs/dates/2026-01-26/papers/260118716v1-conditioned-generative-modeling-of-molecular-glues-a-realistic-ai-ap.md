---
layout: default
title: Conditioned Generative Modeling of Molecular Glues: A Realistic AI Approach for Synthesizable Drug-like Molecules
---

# Conditioned Generative Modeling of Molecular Glues: A Realistic AI Approach for Synthesizable Drug-like Molecules
**arXiv**：[2601.18716v1](https://arxiv.org/abs/2601.18716) · [PDF](https://arxiv.org/pdf/2601.18716.pdf)  
**作者**：Naeyma N. Islam, Thomas R. Caulfield  

**一句话要点**：提出LC-JT-VAE生成模型以设计靶向降解Abeta-42的分子胶水

**关键词**：分子胶水生成, 条件生成模型, 阿尔茨海默病治疗, E3连接酶靶向, JT-VAE

## 3 点简述
- 核心问题：阿尔茨海默病中细胞内Abeta-42积累是早期毒性驱动因素，需靶向降解。
- 方法要点：开发Ligase-Conditioned Junction Tree VAE，结合蛋白序列嵌入和分子图生成E3连接酶特异性小分子。
- 实验或效果：模型生成化学有效、新颖且靶向Abeta-42的分子胶水，促进其通过泛素-蛋白酶体系统降解。

## 摘要（原文）

> Alzheimer's disease (AD) is marked by the pathological accumulation of amyloid beta-42 (Abeta-42), contributing to synaptic dysfunction and neurodegeneration. While extracellular amyloid plaques are well-studied, increasing evidence highlights intracellular Abeta-42 as an early and toxic driver of disease progression. In this study, we present a novel, AI-assisted drug design approach to promote targeted degradation of Abeta-42 via the ubiquitin-proteasome system (UPS), using E3 ligase-directed molecular glues. We systematically evaluated the ternary complex formation potential of Abeta-42 with three E3 ligases: CRBN, VHL, and MDM2, through structure-based modeling, ADMET screening, and docking. We then developed a Ligase-Conditioned Junction Tree Variational Autoencoder (LC-JT-VAE) to generate ligase-specific small molecules, incorporating protein sequence embeddings and torsional angle-aware molecular graphs. Our results demonstrate that this generative model can produce chemically valid, novel, and target-specific molecular glues capable of facilitating Abeta-42 degradation. This integrated approach offers a promising framework for designing UPS-targeted therapies for neurodegenerative diseases.

