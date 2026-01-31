---
layout: default
title: Concise Geometric Description as a Bridge: Unleashing the Potential of LLM for Plane Geometry Problem Solving
---

# Concise Geometric Description as a Bridge: Unleashing the Potential of LLM for Plane Geometry Problem Solving
**arXiv**：[2601.21164v1](https://arxiv.org/abs/2601.21164) · [PDF](https://arxiv.org/pdf/2601.21164.pdf)  
**作者**：Jingyun Wang, Dian Li, Xiaohan Wang, Gang Liu, Jiahong Yan, Guoliang Kang  

**一句话要点**：提出基于简洁几何描述的桥接方法，以释放LLM在平面几何问题求解中的潜力。

**关键词**：平面几何问题求解, 多模态大语言模型, 几何描述生成, 链式思维增强, 奖励优化训练, 数据集构建

## 3 点简述
- 核心问题：LLM无法直接处理视觉图表，现有方法联合优化可能损害其推理能力。
- 方法要点：训练MLLM解释器生成几何描述，利用现成LLM进行推理，采用CDL语言和GRPO训练。
- 实验或效果：在多个数据集上表现优于领先MLLM，仅需5.5k数据微调。

## 摘要（原文）

> Plane Geometry Problem Solving (PGPS) is a multimodal reasoning task that aims to solve a plane geometric problem based on a geometric diagram and problem textual descriptions. Although Large Language Models (LLMs) possess strong reasoning skills, their direct application to PGPS is hindered by their inability to process visual diagrams. Existing works typically fine-tune Multimodal LLMs (MLLMs) end-to-end on large-scale PGPS data to enhance visual understanding and reasoning simultaneously. However, such joint optimization may compromise base LLMs' inherent reasoning capability. In this work, we observe that LLM itself is potentially a powerful PGPS solver when appropriately formulating visual information as textual descriptions. We propose to train a MLLM Interpreter to generate geometric descriptions for the visual diagram, and an off-the-shelf LLM is utilized to perform reasoning. Specifically, we choose Conditional Declaration Language (CDL) as the geometric description as its conciseness eases the MLLM Interpreter training. The MLLM Interpreter is fine-tuned via CoT (Chain-of-Thought)-augmented SFT followed by GRPO to generate CDL. Instead of using a conventional solution-based reward that compares the reasoning result with the ground-truth answer, we design CDL matching rewards to facilitate more effective GRPO training, which provides more direct and denser guidance for CDL generation. To support training, we construct a new dataset, Formalgeo7k-Rec-CoT, by manually reviewing Formalgeo7k v2 and incorporating CoT annotations. Extensive experiments on Formalgeo7k-Rec-CoT, Unigeo, and MathVista show our method (finetuned on only 5.5k data) performs favorably against leading open-source and closed-source MLLMs.

