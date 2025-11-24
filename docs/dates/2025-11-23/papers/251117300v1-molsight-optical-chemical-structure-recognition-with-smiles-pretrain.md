---
layout: default
title: MolSight: Optical Chemical Structure Recognition with SMILES Pretraining, Multi-Granularity Learning and Reinforcement Learning
---

# MolSight: Optical Chemical Structure Recognition with SMILES Pretraining, Multi-Granularity Learning and Reinforcement Learning
**arXiv**：[2511.17300v1](https://arxiv.org/abs/2511.17300) · [PDF](https://arxiv.org/pdf/2511.17300.pdf)  
**作者**：Wenrui Zhang, Xinggang Wang, Bin Feng, Wenyu Liu  

**一句话要点**：提出MolSight框架以解决光学化学结构识别中立体化学信息准确识别难题

**关键词**：光学化学结构识别, SMILES预训练, 多粒度学习, 强化学习优化, 立体化学识别, 分子表示转换

## 3 点简述
- 核心问题：现有系统难以准确识别立体化学信息，如楔形键和环构象
- 方法要点：采用三阶段训练，包括SMILES预训练、多粒度学习和强化学习优化
- 实验或效果：在多样化数据集上实现最先进性能，尤其在立体分子识别中表现突出

## 摘要（原文）

> Optical Chemical Structure Recognition (OCSR) plays a pivotal role in modern chemical informatics, enabling the automated conversion of chemical structure images from scientific literature, patents, and educational materials into machine-readable molecular representations. This capability is essential for large-scale chemical data mining, drug discovery pipelines, and Large Language Model (LLM) applications in related domains. However, existing OCSR systems face significant challenges in accurately recognizing stereochemical information due to the subtle visual cues that distinguish stereoisomers, such as wedge and dash bonds, ring conformations, and spatial arrangements. To address these challenges, we propose MolSight, a comprehensive learning framework for OCSR that employs a three-stage training paradigm. In the first stage, we conduct pre-training on large-scale but noisy datasets to endow the model with fundamental perception capabilities for chemical structure images. In the second stage, we perform multi-granularity fine-tuning using datasets with richer supervisory signals, systematically exploring how auxiliary tasks-specifically chemical bond classification and atom localization-contribute to molecular formula recognition. Finally, we employ reinforcement learning for post-training optimization and introduce a novel stereochemical structure dataset. Remarkably, we find that even with MolSight's relatively compact parameter size, the Group Relative Policy Optimization (GRPO) algorithm can further enhance the model's performance on stereomolecular. Through extensive experiments across diverse datasets, our results demonstrate that MolSight achieves state-of-the-art performance in (stereo)chemical optical structure recognition.

