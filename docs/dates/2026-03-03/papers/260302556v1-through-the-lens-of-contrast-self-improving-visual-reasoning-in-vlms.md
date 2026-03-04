---
layout: default
title: Through the Lens of Contrast: Self-Improving Visual Reasoning in VLMs
---

# Through the Lens of Contrast: Self-Improving Visual Reasoning in VLMs
**arXiv**：[2603.02556v1](https://arxiv.org/abs/2603.02556) · [PDF](https://arxiv.org/pdf/2603.02556.pdf)  
**作者**：Zhiyu Pan, Yizheng Wu, Jiashen Hua, Junyi Feng, Shaotian Yan, Bing Deng, Zhiguo Cao, Jieping Ye  

**一句话要点**：提出VC-STaR框架，利用视觉对比缓解VLMs中的幻觉问题以增强视觉推理能力。

**关键词**：视觉语言模型, 自改进学习, 视觉推理, 对比学习, 幻觉缓解, 数据集构建

## 3 点简述
- 核心问题：视觉语言模型在推理路径中易产生视觉幻觉，难以验证或纠正。
- 方法要点：通过构建对比性VQA对，利用视觉相似性引导模型生成更精确的理性解释。
- 实验或效果：VC-STaR超越现有自改进方法，并在多个VLM上通过VisCoR-55K数据集提升推理性能。

## 摘要（原文）

> Reasoning has emerged as a key capability of large language models. In linguistic tasks, this capability can be enhanced by self-improving techniques that refine reasoning paths for subsequent finetuning. However, extending these language-based self-improving approaches to vision language models (VLMs) presents a unique challenge:~visual hallucinations in reasoning paths cannot be effectively verified or rectified. Our solution starts with a key observation about visual contrast: when presented with a contrastive VQA pair, i.e., two visually similar images with synonymous questions, VLMs identify relevant visual cues more precisely. Motivated by this observation, we propose Visual Contrastive Self-Taught Reasoner (VC-STaR), a novel self-improving framework that leverages visual contrast to mitigate hallucinations in model-generated rationales. We collect a diverse suite of VQA datasets, curate contrastive pairs according to multi-modal similarity, and generate rationales using VC-STaR. Consequently, we obtain a new visual reasoning dataset, VisCoR-55K, which is then used to boost the reasoning capability of various VLMs through supervised finetuning. Extensive experiments show that VC-STaR not only outperforms existing self-improving approaches but also surpasses models finetuned on the SoTA visual reasoning datasets, demonstrating that the inherent contrastive ability of VLMs can bootstrap their own visual reasoning. Project at: https://github.com/zhiyupan42/VC-STaR.

