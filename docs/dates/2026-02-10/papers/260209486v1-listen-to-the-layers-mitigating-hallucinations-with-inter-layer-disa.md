---
layout: default
title: Listen to the Layers: Mitigating Hallucinations with Inter-Layer Disagreement
---

# Listen to the Layers: Mitigating Hallucinations with Inter-Layer Disagreement
**arXiv**：[2602.09486v1](https://arxiv.org/abs/2602.09486) · [PDF](https://arxiv.org/pdf/2602.09486.pdf)  
**作者**：Koduvayur Subbalakshmi, Sabbir Hossain Ujjal, Venkata Krishna Teja Mangichetty, Nastaran Jamalipour Soofi  

**一句话要点**：提出CoCoA解码器，利用层间不一致性缓解大语言模型幻觉问题

**关键词**：大语言模型, 幻觉缓解, 解码算法, 层间不一致性, 事实正确性

## 3 点简述
- 核心问题：大语言模型易产生流畅但事实错误的幻觉文本，影响可靠性。
- 方法要点：基于层间表示不稳定性设计训练无关解码算法，通过惩罚高混淆输出提升事实性。
- 实验效果：在问答、摘要和代码生成等任务中显著提高多模型的事实正确性。

## 摘要（原文）

> Pretrained Large Language Models (LLMs) are prone to generating fluent yet factually incorrect text-a phenomenon known as hallucinations, undermining their reliability and utility in downstream tasks. We hypothesize that a generated text span's factuality is correlated with its representational instability across the model's internal layers. Based on this, we propose the CoCoA (Confusion and Consistency Aware) decoder, a novel, training-free decoding algorithm that mitigates hallucinations at inference time by listening to these signals in the middle layers. We propose two metrics to quantify this instability in the middle layers, and use it to penalize outputs that exhibit high internal confusion, thereby steering the model towards more internally consistent and factually grounded outputs. We further propose a self-information gated variant, CoCoA-SIG, that dynamically modulates this penalty to selectively target high-surprise, unstable generations. Extensive experiments on diverse tasks, including question-answering, summarization and code generation demonstrate that CoCoA significantly improves factual correctness across multiple model families (e.g., Llama-3, Qwen-2.5, Mistral). By leveraging model-intrinsic signals, CoCoA offers an effective and broadly applicable method for enhancing the trustworthiness of LLMs at inference time, without requiring any model retraining.

