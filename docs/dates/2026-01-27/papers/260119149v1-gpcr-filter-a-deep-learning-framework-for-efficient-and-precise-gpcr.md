---
layout: default
title: GPCR-Filter: a deep learning framework for efficient and precise GPCR modulator discovery
---

# GPCR-Filter: a deep learning framework for efficient and precise GPCR modulator discovery
**arXiv**：[2601.19149v1](https://arxiv.org/abs/2601.19149) · [PDF](https://arxiv.org/pdf/2601.19149.pdf)  
**作者**：Jingjie Ning, Xiangzhen Shen, Li Hou, Shiyi Shen, Jiahao Yang, Junrui Li, Hong Shan, Sanan Wu, Sihan Gao, Huaqiang Eric Xu, Xinheng He  

**一句话要点**：提出GPCR-Filter深度学习框架，以高效精确发现GPCR调节剂。

**关键词**：GPCR调节剂发现, 深度学习框架, 蛋白语言模型, 图神经网络, 注意力机制, 药物开发

## 3 点简述
- 核心问题：GPCR调节剂发现困难，因受体激活常源于复杂变构效应，传统检测方法慢且昂贵。
- 方法要点：整合ESM-3蛋白语言模型和图神经网络，通过注意力机制学习受体-配体功能关系。
- 实验或效果：在多个评估中优于现有模型，成功识别5-HT1A受体的微摩尔级激动剂。

## 摘要（原文）

> G protein-coupled receptors (GPCRs) govern diverse physiological processes and are central to modern pharmacology. Yet discovering GPCR modulators remains challenging because receptor activation often arises from complex allosteric effects rather than direct binding affinity, and conventional assays are slow, costly, and not optimized for capturing these dynamics. Here we present GPCR-Filter, a deep learning framework specifically developed for GPCR modulator discovery. We assembled a high-quality dataset of over 90,000 experimentally validated GPCR-ligand pairs, providing a robust foundation for training and evaluation. GPCR-Filter integrates the ESM-3 protein language model for high-fidelity GPCR sequence representations with graph neural networks that encode ligand structures, coupled through an attention-based fusion mechanism that learns receptor-ligand functional relationships. Across multiple evaluation settings, GPCR-Filter consistently outperforms state-of-the-art compound-protein interaction models and exhibits strong generalization to unseen receptors and ligands. Notably, the model successfully identified micromolar-level agonists of the 5-HT\textsubscript{1A} receptor with distinct chemical frameworks. These results establish GPCR-Filter as a scalable and effective computational approach for GPCR modulator discovery, advancing AI-assisted drug development for complex signaling systems.

