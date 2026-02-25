---
layout: default
title: OmniOCR: Generalist OCR for Ethnic Minority Languages
---

# OmniOCR: Generalist OCR for Ethnic Minority Languages
**arXiv**：[2602.21042v1](https://arxiv.org/abs/2602.21042) · [PDF](https://arxiv.org/pdf/2602.21042.pdf)  
**作者**：Bonan Liu, Zeyu Zhang, Bingbing Meng, Han Wang, Hanshuo Zhang, Chengping Wang, Daji Ergu, Ying Cai  

**一句话要点**：提出OmniOCR通用框架，通过动态低秩适应解决少数民族文字OCR低资源泛化问题。

**关键词**：少数民族文字OCR, 动态低秩适应, 稀疏正则化, 低资源泛化, 零样本学习, 参数效率

## 3 点简述
- 核心问题：少数民族文字OCR因书写复杂、标注稀缺和历史现代形式多样，在低资源或零样本场景泛化困难。
- 方法要点：引入动态低秩适应分配模型容量，结合稀疏正则化剪枝冗余更新，实现高效适配且无额外推理成本。
- 实验或效果：在TibetanMNIST、Shui、古彝文和东巴文上超越零样本基础模型和标准后训练，准确率提升39%-66%，参数效率高。

## 摘要（原文）

> Optical character recognition (OCR) has advanced rapidly with deep learning and multimodal models, yet most methods focus on well-resourced scripts such as Latin and Chinese. Ethnic minority languages remain underexplored due to complex writing systems, scarce annotations, and diverse historical and modern forms, making generalization in low-resource or zero-shot settings challenging. To address these challenges, we present OmniOCR, a universal framework for ethnic minority scripts. OmniOCR introduces Dynamic Low-Rank Adaptation (Dynamic LoRA) to allocate model capacity across layers and scripts, enabling effective adaptation while preserving knowledge.A sparsity regularization prunes redundant updates, ensuring compact and efficient adaptation without extra inference cost. Evaluations on TibetanMNIST, Shui, ancient Yi, and Dongba show that OmniOCR outperforms zero-shot foundation models and standard post training, achieving state-of-the-art accuracy with superior parameter efficiency, and compared with the state-of-the-art baseline models, it improves accuracy by 39%-66% on these four datasets. Code: https://github.com/AIGeeksGroup/OmniOCR.

