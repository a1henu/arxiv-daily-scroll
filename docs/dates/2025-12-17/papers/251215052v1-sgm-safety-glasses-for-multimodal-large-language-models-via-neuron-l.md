---
layout: default
title: SGM: Safety Glasses for Multimodal Large Language Models via Neuron-Level Detoxification
---

# SGM: Safety Glasses for Multimodal Large Language Models via Neuron-Level Detoxification
**arXiv**：[2512.15052v1](https://arxiv.org/abs/2512.15052) · [PDF](https://arxiv.org/pdf/2512.15052.pdf)  
**作者**：Hongbo Wang, MaungMaung AprilPyone, Isao Echizen  

**一句话要点**：提出SGM方法，通过神经元级干预解决多模态大语言模型中的毒性问题

**关键词**：多模态大语言模型, 神经元级去毒, 白盒干预, 毒性评估框架, 对抗性安全, 软抑制技术

## 3 点简述
- 多模态大语言模型从弱监督预训练数据中继承毒性信号，现有训练无关的去毒方法难以应对对抗性触发
- SGM采用白盒神经元级干预，通过专家权重软抑制选择性重新校准毒性专家神经元，无需参数更新
- 实验表明SGM在标准与对抗条件下显著降低毒性，有害率从48.2%降至2.5%，同时保持流畅性和多模态推理能力

## 摘要（原文）

> Disclaimer: Samples in this paper may be harmful and cause discomfort.
>   Multimodal large language models (MLLMs) enable multimodal generation but inherit toxic, biased, and NSFW signals from weakly curated pretraining corpora, causing safety risks, especially under adversarial triggers that late, opaque training-free detoxification methods struggle to handle. We propose SGM, a white-box neuron-level multimodal intervention that acts like safety glasses for toxic neurons: it selectively recalibrates a small set of toxic expert neurons via expertise-weighted soft suppression, neutralizing harmful cross-modal activations without any parameter updates. We establish MM-TOXIC-QA, a multimodal toxicity evaluation framework, and compare SGM with existing detoxification techniques. Experiments on open-source MLLMs show that SGM mitigates toxicity in standard and adversarial conditions, cutting harmful rates from 48.2\% to 2.5\% while preserving fluency and multimodal reasoning. SGM is extensible, and its combined defenses, denoted as SGM*, integrate with existing detoxification methods for stronger safety performance, providing an interpretable, low-cost solution for toxicity-controlled multimodal generation.

