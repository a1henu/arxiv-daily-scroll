---
layout: default
title: Distilling to Hybrid Attention Models via KL-Guided Layer Selection
---

# Distilling to Hybrid Attention Models via KL-Guided Layer Selection
**arXiv**：[2512.20569v1](https://arxiv.org/abs/2512.20569) · [PDF](https://arxiv.org/pdf/2512.20569.pdf)  
**作者**：Yanhong Li, Songlin Yang, Shawn Tan, Mayank Mishra, Rameswar Panda, Jiawei Zhou, Yoon Kim  

**一句话要点**：提出基于KL引导层选择的蒸馏方法，将预训练Transformer转换为混合注意力模型以提高推理效率

**关键词**：注意力蒸馏, 混合注意力模型, 层选择, 推理效率, KL散度, Transformer优化

## 3 点简述
- 核心问题：如何高效选择Transformer层转换为线性注意力，以构建混合架构
- 方法要点：使用通用文本数据训练获取层重要性分数，指导层选择，结合RADLADS蒸馏流程
- 实验或效果：相比均匀插层和专用数据集方法，本方法在层选择上更有效

## 摘要（原文）

> Distilling pretrained softmax attention Transformers into more efficient hybrid architectures that interleave softmax and linear attention layers is a promising approach for improving the inference efficiency of LLMs without requiring expensive pretraining from scratch. A critical factor in the conversion process is layer selection, i.e., deciding on which layers to convert to linear attention variants. This paper describes a simple and efficient recipe for layer selection that uses layer importance scores derived from a small amount of training on generic text data. Once the layers have been selected we use a recent pipeline for the distillation process itself \citep[RADLADS;][]{goldstein2025radlads}, which consists of attention weight transfer, hidden state alignment, KL-based distribution matching, followed by a small amount of finetuning. We find that this approach is more effective than existing approaches for layer selection, including heuristics that uniformly interleave linear attentions based on a fixed ratio, as well as more involved approaches that rely on specialized diagnostic datasets.

