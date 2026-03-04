---
layout: default
title: MoD-DPO: Towards Mitigating Cross-modal Hallucinations in Omni LLMs using Modality Decoupled Preference Optimization
---

# MoD-DPO: Towards Mitigating Cross-modal Hallucinations in Omni LLMs using Modality Decoupled Preference Optimization
**arXiv**：[2603.03192v1](https://arxiv.org/abs/2603.03192) · [PDF](https://arxiv.org/pdf/2603.03192.pdf)  
**作者**：Ashutosh Chaubey, Jiacheng Pang, Mohammad Soleymani  

**一句话要点**：提出MoD-DPO以缓解全模态大语言模型中的跨模态幻觉问题

**关键词**：全模态大语言模型, 跨模态幻觉, 偏好优化, 模态对齐, 语言先验去偏

## 3 点简述
- 全模态大语言模型易受虚假相关性和语言先验影响产生跨模态幻觉
- MoD-DPO通过模态感知正则化和语言先验去偏惩罚增强模态对齐
- 实验表明MoD-DPO在多个基准上提升感知准确性和幻觉抵抗能力

## 摘要（原文）

> Omni-modal large language models (omni LLMs) have recently achieved strong performance across audiovisual understanding tasks, yet they remain highly susceptible to cross-modal hallucinations arising from spurious correlations and dominant language priors. In this work, we propose Modality-Decoupled Direct Preference Optimization (MoD-DPO), a simple and effective framework for improving modality grounding in omni LLMs. MoD-DPO introduces modality-aware regularization terms that explicitly enforce invariance to corruptions in irrelevant modalities and sensitivity to perturbations in relevant modalities, thereby reducing unintended cross-modal interactions. To further mitigate over-reliance on textual priors, we incorporate a language-prior debiasing penalty that discourages hallucination-prone text-only responses. Extensive experiments across multiple audiovisual hallucination benchmarks demonstrate that MoD-DPO consistently improves perception accuracy and hallucination resistance, outperforming previous preference optimization baselines under similar training budgets. Our findings underscore the importance of modality-faithful alignment and demonstrate a scalable path toward more reliable and resilient multimodal foundation models.

