---
layout: default
title: EPAS: Efficient Training with Progressive Activation Sharing
---

# EPAS: Efficient Training with Progressive Activation Sharing
**arXiv**：[2601.19089v1](https://arxiv.org/abs/2601.19089) · [PDF](https://arxiv.org/pdf/2601.19089.pdf)  
**作者**：Rezaul Karim, Maryam Dialameh, Yang Liu, Boxing Chen, Walid Ahmed  

**一句话要点**：提出EPAS方法，通过渐进激活共享提升Transformer训练和推理效率

**关键词**：渐进训练, 激活共享, Transformer优化, 高效推理, 模型压缩

## 3 点简述
- 核心问题：Transformer深层存在冗余QK或KV激活，导致计算浪费
- 方法要点：训练中渐进切换解码层至激活共享模式，从深层向浅层扩展共享区域
- 实验或效果：在LLaMA模型上实现最高11.1%训练和29%推理吞吐提升，损失曲线接近基线

## 摘要（原文）

> We present a novel method for Efficient training with Progressive Activation Sharing (EPAS). This method bridges progressive training paradigm with the phenomenon of redundant QK (or KV ) activations across deeper layers of transformers. EPAS gradually grows a sharing region during training by switching decoder layers to activation sharing mode. This results in throughput increase due to reduced compute. To utilize deeper layer redundancy, the sharing region starts from the deep end of the model and grows towards the shallow end. The EPAS trained models allow for variable region lengths of activation sharing for different compute budgets during inference. Empirical evaluations with QK activation sharing in LLaMA models ranging from 125M to 7B parameters show up to an 11.1% improvement in training throughput and up to a 29% improvement in inference throughput while maintaining similar loss curve to the baseline models. Furthermore, applying EPAS in continual pretraining to transform TinyLLaMA into an attention-sharing model yields up to a 10% improvement in average accuracy over state-of-the-art methods, emphasizing the significance of progressive training in cross layer activation sharing models.

