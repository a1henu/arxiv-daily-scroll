---
layout: default
title: Omni-AVSR: Towards Unified Multimodal Speech Recognition with Large Language Models
---

# Omni-AVSR: Towards Unified Multimodal Speech Recognition with Large Language Models
**arXiv**：[2511.07253v1](https://arxiv.org/abs/2511.07253) · [PDF](https://arxiv.org/pdf/2511.07253.pdf)  
**作者**：Umberto Cappellazzo, Xubo Liu, Pingchuan Ma, Stavros Petridis, Maja Pantic  

**一句话要点**：提出Omni-AVSR统一框架以解决多模态语音识别中的独立模型与效率问题

**关键词**：多模态语音识别, 大语言模型, 统一框架, 参数高效适应, 多粒度训练

## 3 点简述
- 当前LLM方法独立处理ASR、VSR和AVSR任务，导致资源浪费和协同缺失
- 采用多粒度训练和LoRA适应策略，实现高效统一模型训练与部署
- 在LRS2和LRS3数据集上，精度可比或优于SOTA，资源使用显著降低

## 摘要（原文）

> Large language models (LLMs) have recently achieved impressive results in
> speech recognition across multiple modalities, including Auditory Speech
> Recognition (ASR), Visual Speech Recognition (VSR), and Audio-Visual Speech
> Recognition (AVSR). Despite this progress, current LLM-based approaches
> typically address each task independently, training separate models that raise
> computational and deployment resource use while missing potential cross-task
> synergies. They also rely on fixed-rate token compression, which restricts
> flexibility in balancing accuracy with efficiency. These limitations highlight
> the need for a unified framework that can support ASR, VSR, and AVSR while
> enabling elastic inference. To this end, we present Omni-AVSR, a unified
> audio-visual LLM that combines efficient multi-granularity training with
> parameter-efficient adaptation. Specifically, we adapt the matryoshka
> representation learning paradigm to efficiently train across multiple audio and
> visual granularities, reducing its inherent training resource use. Furthermore,
> we explore three LoRA-based strategies for adapting the backbone LLM, balancing
> shared and task-specific specialization. Experiments on LRS2 and LRS3 show that
> Omni-AVSR achieves comparable or superior accuracy to state-of-the-art
> baselines while training a single model at substantially lower training and
> deployment resource use. The model also remains robust under acoustic noise,
> and we analyze its scaling behavior as LLM size increases, providing insights
> into the trade-off between performance and efficiency.

