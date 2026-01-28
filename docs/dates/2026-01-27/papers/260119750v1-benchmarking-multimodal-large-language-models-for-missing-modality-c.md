---
layout: default
title: Benchmarking Multimodal Large Language Models for Missing Modality Completion in Product Catalogues
---

# Benchmarking Multimodal Large Language Models for Missing Modality Completion in Product Catalogues
**arXiv**：[2601.19750v1](https://arxiv.org/abs/2601.19750) · [PDF](https://arxiv.org/pdf/2601.19750.pdf)  
**作者**：Junchen Fu, Wenhao Deng, Kaiwen Zheng, Alexandros Karatzoglou, Ioannis Arapakis, Yu Ye, Yongxin Ni, Joemon M. Jose, Xuri Ge  

**一句话要点**：提出MMPCBench基准以评估MLLMs在电商产品缺失模态补全中的能力。

**关键词**：多模态大语言模型, 缺失模态补全, 电商产品目录, 基准评估, 跨模态生成

## 3 点简述
- 研究MLLMs能否生成电商产品缺失的模态信息，如文本或图像。
- 构建MMPCBench基准，包含内容质量和推荐两个子基准，评估六种MLLMs。
- 实验显示MLLMs在细粒度对齐上表现不佳，性能因类别和模型而异，GRPO仅提升图像到文本任务。

## 摘要（原文）

> Missing-modality information on e-commerce platforms, such as absent product images or textual descriptions, often arises from annotation errors or incomplete metadata, impairing both product presentation and downstream applications such as recommendation systems. Motivated by the multimodal generative capabilities of recent Multimodal Large Language Models (MLLMs), this work investigates a fundamental yet underexplored question: can MLLMs generate missing modalities for products in e-commerce scenarios? We propose the Missing Modality Product Completion Benchmark (MMPCBench), which consists of two sub-benchmarks: a Content Quality Completion Benchmark and a Recommendation Benchmark.
>   We further evaluate six state-of-the-art MLLMs from the Qwen2.5-VL and Gemma-3 model families across nine real-world e-commerce categories, focusing on image-to-text and text-to-image completion tasks. Experimental results show that while MLLMs can capture high-level semantics, they struggle with fine-grained word-level and pixel- or patch-level alignment. In addition, performance varies substantially across product categories and model scales, and we observe no trivial correlation between model size and performance, in contrast to trends commonly reported in mainstream benchmarks. We also explore Group Relative Policy Optimization (GRPO) to better align MLLMs with this task. GRPO improves image-to-text completion but does not yield gains for text-to-image completion. Overall, these findings expose the limitations of current MLLMs in real-world cross-modal generation and represent an early step toward more effective missing-modality product completion.

