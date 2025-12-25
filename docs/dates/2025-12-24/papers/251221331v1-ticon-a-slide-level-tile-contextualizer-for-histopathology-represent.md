---
layout: default
title: TICON: A Slide-Level Tile Contextualizer for Histopathology Representation Learning
---

# TICON: A Slide-Level Tile Contextualizer for Histopathology Representation Learning
**arXiv**：[2512.21331v1](https://arxiv.org/abs/2512.21331) · [PDF](https://arxiv.org/pdf/2512.21331.pdf)  
**作者**：Varun Belagali, Saarthak Kapse, Pierre Marza, Srijan Das, Zilinghan Li, Sofiène Boutaj, Pushpak Pati, Srikar Yellapragada, Tarak Nath Nandi, Ravi K Madduri, Joel Saltz, Prateek Prasanna, Stergios Christodoulidis Maria Vakalopoulou, Dimitris Samaras  

**一句话要点**：提出TICON以解决病理学中切片级瓦片表示缺乏上下文信息的问题

**关键词**：病理学表示学习, 瓦片上下文化, Transformer模型, 掩码建模预训练, 切片级基础模型

## 3 点简述
- 核心问题：标准瓦片编码器剥离上下文，无法建模对局部和全局任务关键的切片级信息
- 方法要点：基于Transformer的瓦片表示上下文化器，通过掩码建模预训练统一和上下文化不同瓦片级基础模型的表示
- 实验或效果：TICON上下文化嵌入显著提升多任务性能，在瓦片级和切片级基准测试中建立新SOTA结果

## 摘要（原文）

> The interpretation of small tiles in large whole slide images (WSI) often needs a larger image context. We introduce TICON, a transformer-based tile representation contextualizer that produces rich, contextualized embeddings for ''any'' application in computational pathology. Standard tile encoder-based pipelines, which extract embeddings of tiles stripped from their context, fail to model the rich slide-level information essential for both local and global tasks. Furthermore, different tile-encoders excel at different downstream tasks. Therefore, a unified model is needed to contextualize embeddings derived from ''any'' tile-level foundation model. TICON addresses this need with a single, shared encoder, pretrained using a masked modeling objective to simultaneously unify and contextualize representations from diverse tile-level pathology foundation models. Our experiments demonstrate that TICON-contextualized embeddings significantly improve performance across many different tasks, establishing new state-of-the-art results on tile-level benchmarks (i.e., HEST-Bench, THUNDER, CATCH) and slide-level benchmarks (i.e., Patho-Bench). Finally, we pretrain an aggregator on TICON to form a slide-level foundation model, using only 11K WSIs, outperforming SoTA slide-level foundation models pretrained with up to 350K WSIs.

