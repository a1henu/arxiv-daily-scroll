---
layout: default
title: Generating readily synthesizable small molecule fluorophore scaffolds with reinforcement learning
---

# Generating readily synthesizable small molecule fluorophore scaffolds with reinforcement learning
**arXiv**：[2601.07145v1](https://arxiv.org/abs/2601.07145) · [PDF](https://arxiv.org/pdf/2601.07145.pdf)  
**作者**：Ruhi Sayana, Kate Callon, Jennifer Xu, Jonathan Deutsch, Steven Chu, James Zou, John Janetzko, Rabindra V. Shivnaraine, Kyle Swanson  

**一句话要点**：提出SyntheFluor-RL模型，利用强化学习生成易合成的小分子荧光团支架

**关键词**：荧光团生成, 强化学习, 图神经网络, 合成可行性, 光物理性质预测, 分子设计

## 3 点简述
- 核心问题：现有生成AI方法常因缺乏反应约束，产生难以合成的荧光分子候选物。
- 方法要点：结合已知反应库和分子构建块，通过强化学习生成候选物，并使用GNN预测光物理性质进行评分。
- 实验或效果：生成11,590个候选分子，筛选出19个，其中14个被合成，13个实验验证，领先化合物显示强荧光等特性。

## 摘要（原文）

> Developing new fluorophores for advanced imaging techniques requires exploring new chemical space. While generative AI approaches have shown promise in designing novel dye scaffolds, prior efforts often produced synthetically intractable candidates due to a lack of reaction constraints. Here, we developed SyntheFluor-RL, a generative AI model that employs known reaction libraries and molecular building blocks to create readily synthesizable fluorescent molecule scaffolds via reinforcement learning. To guide the generation of fluorophores, SyntheFluor-RL employs a scoring function built on multiple graph neural networks (GNNs) that predict key photophysical properties, including photoluminescence quantum yield, absorption, and emission wavelengths. These outputs are dynamically weighted and combined with a computed pi-conjugation score to prioritize candidates with desirable optical characteristics and synthetic feasibility. SyntheFluor-RL generated 11,590 candidate molecules, which were filtered to 19 structures predicted to possess dye-like properties. Of the 19 molecules, 14 were synthesized and 13 were experimentally confirmed. The top three were characterized, with the lead compound featuring a benzothiadiazole chromophore and exhibiting strong fluorescence (PLQY = 0.62), a large Stokes shift (97 nm), and a long excited-state lifetime (11.5 ns). These results demonstrate the effectiveness of SyntheFluor-RL in the identification of synthetically accessible fluorophores for further development.

