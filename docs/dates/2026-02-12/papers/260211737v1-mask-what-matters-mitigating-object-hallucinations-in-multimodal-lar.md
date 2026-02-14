---
layout: default
title: Mask What Matters: Mitigating Object Hallucinations in Multimodal Large Language Models with Object-Aligned Visual Contrastive Decoding
---

# Mask What Matters: Mitigating Object Hallucinations in Multimodal Large Language Models with Object-Aligned Visual Contrastive Decoding
**arXiv**：[2602.11737v1](https://arxiv.org/abs/2602.11737) · [PDF](https://arxiv.org/pdf/2602.11737.pdf)  
**作者**：Boqi Chen, Xudong Liu, Jianing Qiu  

**一句话要点**：提出对象对齐视觉对比解码以缓解多模态大语言模型中的对象幻觉问题

**关键词**：对象幻觉, 多模态大语言模型, 视觉对比解码, 自监督视觉Transformer, 对象中心注意力

## 3 点简述
- 核心问题：多模态大语言模型在视觉语言任务中易产生对象幻觉，即生成未在图像中出现的对象描述
- 方法要点：利用自监督视觉Transformer的对象中心注意力，移除最显著视觉证据构建辅助视图，增强对比解码信号
- 实验或效果：在两个对象幻觉基准上对两种MLLM均显示一致性能提升，方法为提示无关、模型无关且计算开销低

## 摘要（原文）

> We study object hallucination in Multimodal Large Language Models (MLLMs) and improve visual contrastive decoding (VCD) by constructing an object-aligned auxiliary view. We leverage object-centric attention in self-supervised Vision Transformers. In particular, we remove the most salient visual evidence to construct an auxiliary view that disrupts unsupported tokens and produces a stronger contrast signal. Our method is prompt-agnostic, model-agnostic, and can be seamlessly plugged into the existing VCD pipeline with little computation overhead, i.e., a single cacheable forward pass. Empirically, our method demonstrates consistent gains on two popular object hallucination benchmarks across two MLLMs.

