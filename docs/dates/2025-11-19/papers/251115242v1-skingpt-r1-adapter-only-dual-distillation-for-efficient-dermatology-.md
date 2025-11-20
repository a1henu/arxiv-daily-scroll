---
layout: default
title: SkinGPT-R1: Adapter-Only Dual Distillation for Efficient Dermatology Reasoning
---

# SkinGPT-R1: Adapter-Only Dual Distillation for Efficient Dermatology Reasoning
**arXiv**：[2511.15242v1](https://arxiv.org/abs/2511.15242) · [PDF](https://arxiv.org/pdf/2511.15242.pdf)  
**作者**：Yuhao Shen, Jiahe Qian, Zhangtianyi Chen, Yuanhao He, Juexiao Zhou  

**一句话要点**：提出SkinGPT-R1以高效皮肤病推理，通过适配器双蒸馏实现显式链式思维。

**关键词**：皮肤病诊断, 链式思维推理, 视觉语言模型, 适配器蒸馏, DermCoT语料库

## 3 点简述
- 核心问题：皮肤病诊断需显式、可验证的链式思维推理，现有模型缺乏专业支持。
- 方法要点：构建DermCoT语料库，结合适配器双蒸馏提升推理质量和效率。
- 实验效果：在DermBench上排名第一，平均得分4.031/5，准确率稳定提升。

## 摘要（原文）

> We present SkinGPT-R1, a dermatology focused vision language model that makes diagnostic chain of thought reasoning explicit, step by step, and verifiable. To support skin specific reasoning, we build DermCoT, a corpus of standardized dermatologic chain of thought narratives that combines 10,000 DermEval filtered training cases with 3,000 dermatologist scored certified cases, and we define DermEval as a physician aligned six dimensional evaluator and DermBench as the corresponding benchmark for dermatologic chain of thought quality. On DermBench, across 14 general, reasoning, and medical vision language models, SkinGPT-R1 achieves an average score of 4.031 out of 5 over the six clinician defined dimensions, ranks 1st among all systems, and improves the average score over Vision-R1 by about 41%. On three dermatology classification benchmarks, SkinGPT-R1 delivers stable accuracy gains over Vision-R1 and remains competitive among strong vision language models. Ablation results further show that DermCoT based chain of thought supervision provides substantial improvements over the base model and that adding dermatology aware visual distillation yields consistent additional gains in both narrative quality and recognition.

