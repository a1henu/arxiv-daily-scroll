---
layout: default
title: AutoViVQA: A Large-Scale Automatically Constructed Dataset for Vietnamese Visual Question Answering
---

# AutoViVQA: A Large-Scale Automatically Constructed Dataset for Vietnamese Visual Question Answering
**arXiv**：[2603.09689v1](https://arxiv.org/abs/2603.09689) · [PDF](https://arxiv.org/pdf/2603.09689.pdf)  
**作者**：Nguyen Anh Tuong, Phan Ba Duc, Nguyen Trung Quoc, Tran Dac Thinh, Dang Duy Lan, Nguyen Quoc Thinh, Tung Le  

**一句话要点**：提出AutoViVQA数据集以促进越南语视觉问答研究，并基于Transformer架构进行多模态融合与评估比较。

**关键词**：越南语视觉问答, 多模态融合, Transformer架构, 自动评估指标, 低资源学习

## 3 点简述
- 核心问题：越南语视觉问答缺乏大规模自动构建的数据集，影响低资源多模态学习发展。
- 方法要点：利用PhoBERT和Vision Transformers进行文本与视觉预训练，实现多模态融合。
- 实验或效果：系统比较自动评估指标在越南语VQA任务中的表现，未知具体性能提升。

## 摘要（原文）

> Visual Question Answering (VQA) is a fundamental multimodal task that requires models to jointly understand visual and textual information. Early VQA systems relied heavily on language biases, motivating subsequent work to emphasize visual grounding and balanced datasets. With the success of large-scale pre-trained transformers for both text and vision domains -- such as PhoBERT for Vietnamese language understanding and Vision Transformers (ViT) for image representation learning -- multimodal fusion has achieved remarkable progress.
>   For Vietnamese VQA, several datasets have been introduced to promote research in low-resource multimodal learning, including ViVQA, OpenViVQA, and the recently proposed ViTextVQA. These resources enable benchmarking of models that integrate linguistic and visual features in the Vietnamese context.
>   Evaluation of VQA systems often employs automatic metrics originally designed for image captioning or machine translation, such as BLEU, METEOR, CIDEr, Recall, Precision, and F1-score. However, recent research suggests that large language models can further improve the alignment between automatic evaluation and human judgment in VQA tasks.
>   In this work, we explore Vietnamese Visual Question Answering using transformer-based architectures, leveraging both textual and visual pre-training while systematically comparing automatic evaluation metrics under multilingual settings.

