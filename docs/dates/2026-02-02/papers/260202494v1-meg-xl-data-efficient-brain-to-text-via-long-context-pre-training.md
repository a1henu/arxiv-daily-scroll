---
layout: default
title: MEG-XL: Data-Efficient Brain-to-Text via Long-Context Pre-Training
---

# MEG-XL: Data-Efficient Brain-to-Text via Long-Context Pre-Training
**arXiv**：[2602.02494v1](https://arxiv.org/abs/2602.02494) · [PDF](https://arxiv.org/pdf/2602.02494.pdf)  
**作者**：Dulhan Jayalath, Oiwi Parker Jones  

**一句话要点**：提出MEG-XL模型，通过长上下文预训练提升脑到文本接口的数据效率。

**关键词**：脑到文本接口, 长上下文预训练, 数据效率, MEG解码, 神经表示学习, 临床应用

## 3 点简述
- 核心问题：临床脑到文本接口需在有限训练数据下实现高效泛化，但现有方法上下文短，丢弃了扩展神经上下文。
- 方法要点：MEG-XL预训练使用每样本2.5分钟MEG上下文，比先前工作长5-300倍，以捕获扩展神经统计先验。
- 实验或效果：微调后，MEG-XL在单词解码任务中，用少量数据（如1小时）匹配监督性能，并优于脑基础模型。

## 摘要（原文）

> Clinical brain-to-text interfaces are designed for paralysed patients who cannot provide extensive training recordings. Pre-training improves data-efficient generalisation by learning statistical priors across subjects, but these priors critically depend on context. While natural speech might unfold gradually over minutes, most methods pre-train with only a few seconds of context. Thus, we propose MEG-XL, a model pre-trained with 2.5 minutes of MEG context per sample, 5-300x longer than prior work, and equivalent to 191k tokens, capturing extended neural context. Fine-tuning on the task of word decoding from brain data, MEG-XL matches supervised performance with a fraction of the data (e.g. 1hr vs 50hrs) and outperforms brain foundation models. We find that models pre-trained with longer contexts learn representations that transfer better to word decoding. Our results indicate that long-context pre-training helps exploit extended neural context that other methods unnecessarily discard. Code, model weights, and instructions are available at https://github.com/neural-processing-lab/MEG-XL .

