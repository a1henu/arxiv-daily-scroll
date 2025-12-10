---
layout: default
title: Do Depth-Grown Models Overcome the Curse of Depth? An In-Depth Analysis
---

# Do Depth-Grown Models Overcome the Curse of Depth? An In-Depth Analysis
**arXiv**：[2512.08819v1](https://arxiv.org/abs/2512.08819) · [PDF](https://arxiv.org/pdf/2512.08819.pdf)  
**作者**：Ferdinand Kapl, Emmanouil Angelis, Tobias Höppe, Kaitlin Maile, Johannes von Oswald, Nino Scherrer, Stefan Bauer  

**一句话要点**：分析深度增长模型如何通过中间堆叠克服深度诅咒，提升Transformer推理性能

**关键词**：深度增长模型, Transformer, 深度诅咒, 中间堆叠, 推理性能, 残差流结构

## 3 点简述
- 核心问题：标准Transformer后层贡献低，存在深度诅咒，影响模型深度利用效率
- 方法要点：采用深度增长训练，通过中间堆叠优化残差流结构，形成可置换计算块
- 实验或效果：深度增长模型提升深度利用，改进下游推理基准，提出轻量修改进一步优化

## 摘要（原文）

> Gradually growing the depth of Transformers during training can not only reduce training cost but also lead to improved reasoning performance, as shown by MIDAS (Saunshi et al., 2024). Thus far, however, a mechanistic understanding of these gains has been missing. In this work, we establish a connection to recent work showing that layers in the second half of non-grown, pre-layernorm Transformers contribute much less to the final output distribution than those in the first half - also known as the Curse of Depth (Sun et al., 2025, Csordás et al., 2025). Using depth-wise analyses, we demonstrate that growth via gradual middle stacking yields more effective utilization of model depth, alters the residual stream structure, and facilitates the formation of permutable computational blocks. In addition, we propose a lightweight modification of MIDAS that yields further improvements in downstream reasoning benchmarks. Overall, this work highlights how the gradual growth of model depth can lead to the formation of distinct computational circuits and overcome the limited depth utilization seen in standard non-grown models.

