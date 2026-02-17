---
layout: default
title: Exploring the limits of pre-trained embeddings in machine-guided protein design: a case study on predicting AAV vector viability
---

# Exploring the limits of pre-trained embeddings in machine-guided protein design: a case study on predicting AAV vector viability
**arXiv**：[2602.14828v1](https://arxiv.org/abs/2602.14828) · [PDF](https://arxiv.org/pdf/2602.14828.pdf)  
**作者**：Ana F. Rodrigues, Lucas Ferraz, Laura Balbi, Pedro Giesteira Cotovio, Catia Pesquita  

**一句话要点**：评估预训练嵌入在蛋白质设计中的极限，通过AAV案例揭示微调对稀疏突变数据集的重要性

**关键词**：蛋白质设计, 预训练嵌入, 序列表示, 生物工程, 微调, AAV病毒

## 3 点简述
- 核心问题：蛋白质生物工程中稀疏或局部突变限制序列表示提取功能信号的能力
- 方法要点：系统比较ProtBERT和ESM2嵌入变体在监督与非监督任务中的表现
- 实验或效果：微调后序列级表示性能最佳，突变幅度需超出常规研究范围

## 摘要（原文）

> Effective representations of protein sequences are widely recognized as a cornerstone of machine learning-based protein design. Yet, protein bioengineering poses unique challenges for sequence representation, as experimental datasets typically feature few mutations, which are either sparsely distributed across the entire sequence or densely concentrated within localized regions. This limits the ability of sequence-level representations to extract functionally meaningful signals. In addition, comprehensive comparative studies remain scarce, despite their crucial role in clarifying which representations best encode relevant information and ultimately support superior predictive performance. In this study, we systematically evaluate multiple ProtBERT and ESM2 embedding variants as sequence representations, using the adeno-associated virus capsid as a case study and prototypical example of bioengineering, where functional optimization is targeted through highly localized sequence variation within an otherwise large protein. Our results reveal that, prior to fine-tuning, amino acid-level embeddings outperform sequence-level representations in supervised predictive tasks, whereas the latter tend to be more effective in unsupervised settings. However, optimal performance is only achieved when embeddings are fine-tuned with task-specific labels, with sequence-level representations providing the best performance. Moreover, our findings indicate that the extent of sequence variation required to produce notable shifts in sequence representations exceeds what is typically explored in bioengineering studies, showing the need for fine-tuning in datasets characterized by sparse or highly localized mutations.

