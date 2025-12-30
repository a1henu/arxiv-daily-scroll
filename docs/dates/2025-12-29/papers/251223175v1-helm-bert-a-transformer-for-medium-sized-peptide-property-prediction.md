---
layout: default
title: HELM-BERT: A Transformer for Medium-sized Peptide Property Prediction
---

# HELM-BERT: A Transformer for Medium-sized Peptide Property Prediction
**arXiv**：[2512.23175v1](https://arxiv.org/abs/2512.23175) · [PDF](https://arxiv.org/pdf/2512.23175.pdf)  
**作者**：Seungeon Lee, Takuto Koyama, Itsuki Maeda, Shigeyuki Matsumoto, Yasushi Okuno  

**一句话要点**：提出HELM-BERT以解决治疗性肽性质预测中的表示难题

**关键词**：治疗性肽预测, HELM符号, Transformer模型, 分子语言模型, 数据效率

## 3 点简述
- 核心问题：现有分子语言模型无法准确捕捉肽的化学修饰和拓扑复杂性。
- 方法要点：基于DeBERTa，首次在HELM符号上预训练编码器模型，捕获层次依赖。
- 实验或效果：在膜渗透性和肽-蛋白相互作用预测任务中显著优于SMILES模型。

## 摘要（原文）

> Therapeutic peptides have emerged as a pivotal modality in modern drug discovery, occupying a chemically and topologically rich space. While accurate prediction of their physicochemical properties is essential for accelerating peptide development, existing molecular language models rely on representations that fail to capture this complexity. Atom-level SMILES notation generates long token sequences and obscures cyclic topology, whereas amino-acid-level representations cannot encode the diverse chemical modifications central to modern peptide design. To bridge this representational gap, the Hierarchical Editing Language for Macromolecules (HELM) offers a unified framework enabling precise description of both monomer composition and connectivity, making it a promising foundation for peptide language modeling. Here, we propose HELM-BERT, the first encoder-based peptide language model trained on HELM notation. Based on DeBERTa, HELM-BERT is specifically designed to capture hierarchical dependencies within HELM sequences. The model is pre-trained on a curated corpus of 39,079 chemically diverse peptides spanning linear and cyclic structures. HELM-BERT significantly outperforms state-of-the-art SMILES-based language models in downstream tasks, including cyclic peptide membrane permeability prediction and peptide-protein interaction prediction. These results demonstrate that HELM's explicit monomer- and topology-aware representations offer substantial data-efficiency advantages for modeling therapeutic peptides, bridging a long-standing gap between small-molecule and protein language models.

