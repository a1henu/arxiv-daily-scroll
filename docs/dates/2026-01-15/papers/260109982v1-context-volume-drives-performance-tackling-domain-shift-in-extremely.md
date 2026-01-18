---
layout: default
title: Context Volume Drives Performance: Tackling Domain Shift in Extremely Low-Resource Translation via RAG
---

# Context Volume Drives Performance: Tackling Domain Shift in Extremely Low-Resource Translation via RAG
**arXiv**：[2601.09982v1](https://arxiv.org/abs/2601.09982) · [PDF](https://arxiv.org/pdf/2601.09982.pdf)  
**作者**：David Samuel Setiawan, Raphaël Merx, Jey Han Lau  

**一句话要点**：提出基于检索增强生成的混合框架，以缓解低资源翻译中的领域偏移问题。

**关键词**：低资源机器翻译, 领域偏移, 检索增强生成, 混合框架, 性能恢复

## 3 点简述
- 核心问题：低资源语言神经机器翻译在领域偏移下性能显著下降，如Dhao语言从新约到旧约翻译时chrF++分数下降9.06。
- 方法要点：结合微调NMT模型生成初稿，再通过LLM和RAG进行精炼，利用检索示例数量驱动性能提升。
- 实验或效果：系统在旧约翻译中恢复8.10 chrF++分数，达到35.21，接近原始领域内质量，LLM作为安全网修复严重错误。

## 摘要（原文）

> Neural Machine Translation (NMT) models for low-resource languages suffer significant performance degradation under domain shift. We quantify this challenge using Dhao, an indigenous language of Eastern Indonesia with no digital footprint beyond the New Testament (NT). When applied to the unseen Old Testament (OT), a standard NMT model fine-tuned on the NT drops from an in-domain score of 36.17 chrF++ to 27.11 chrF++. To recover this loss, we introduce a hybrid framework where a fine-tuned NMT model generates an initial draft, which is then refined by a Large Language Model (LLM) using Retrieval-Augmented Generation (RAG). The final system achieves 35.21 chrF++ (+8.10 recovery), effectively matching the original in-domain quality. Our analysis reveals that this performance is driven primarily by the number of retrieved examples rather than the choice of retrieval algorithm. Qualitative analysis confirms the LLM acts as a robust "safety net," repairing severe failures in zero-shot domains.

