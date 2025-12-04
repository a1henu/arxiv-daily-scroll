---
layout: default
title: Diminishing Returns in Self-Supervised Learning
---

# Diminishing Returns in Self-Supervised Learning
**arXiv**：[2512.03862v1](https://arxiv.org/abs/2512.03862) · [PDF](https://arxiv.org/pdf/2512.03862.pdf)  
**作者**：Oli Bridge, Huey Sun, Botond Branyicskai-Nagy, Charles D'Ornano, Shomit Basu  

**一句话要点**：探索小规模视觉Transformer在自监督学习中的收益递减与中间微调潜在危害

**关键词**：自监督学习, 视觉Transformer, 收益递减, 中间微调, 小规模模型, 数据选择

## 3 点简述
- 研究小规模ViT在预训练、中间微调和下游任务中的性能边际收益递减现象
- 发现中间微调可能因任务机制差异对下游性能产生负面影响
- 建议针对小规模ViT采用定向预训练和谨慎数据选择以优化计算效率

## 摘要（原文）

> While transformer-based architectures have taken computer vision and NLP by storm, they often require a vast amount of parameters and training data to attain strong performance. In this work, we experiment with three distinct pre-training, intermediate fine-tuning, and downstream datasets and training objectives to explore their marginal benefits on a small 5M-parameter vision transformer. We find that while pre-training and fine-tuning always help our model but have diminishing returns, intermediate fine-tuning can actually show harmful impact on downstream performance, potentially due to dissimilarity in task mechanics. Taken together, our results suggest that small-scale ViTs benefit most from targeted pre-training and careful data selection, while indiscriminate stacking of intermediate tasks can waste compute and even degrade performance.

