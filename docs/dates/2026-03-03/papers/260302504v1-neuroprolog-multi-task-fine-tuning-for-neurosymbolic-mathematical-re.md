---
layout: default
title: NeuroProlog: Multi-Task Fine-Tuning for Neurosymbolic Mathematical Reasoning via the Cocktail Effect
---

# NeuroProlog: Multi-Task Fine-Tuning for Neurosymbolic Mathematical Reasoning via the Cocktail Effect
**arXiv**：[2603.02504v1](https://arxiv.org/abs/2603.02504) · [PDF](https://arxiv.org/pdf/2603.02504.pdf)  
**作者**：Pratibha Zunjare, Michael Hsiao  

**一句话要点**：提出NeuroProlog框架，通过多任务鸡尾酒训练解决大语言模型数学推理不可靠问题。

**关键词**：神经符号推理, 数学推理, 多任务训练, 程序合成, 错误修复, 可验证性

## 3 点简述
- 核心问题：大语言模型在数学推理中常生成流畅但逻辑不一致的答案，缺乏可验证性。
- 方法要点：将数学问题编译为可执行的Prolog程序，采用多任务训练联合优化公式翻译、程序合成和答案对齐。
- 实验或效果：在GSM8K数据集上，多任务训练显著提升准确率，并改善错误修复能力，尤其在大型模型中效果更佳。

## 摘要（原文）

> Large Language Models (LLMs) achieve strong performance on natural language tasks but remain unreliable in mathematical reasoning, frequently generating fluent yet logically inconsistent solutions. We present \textbf{NeuroProlog}, a neurosymbolic framework that ensures verifiable reasoning by compiling math word problems into executable Prolog programs with formal verification guarantees. We propose a multi-task Cocktail training strategy that jointly optimizes three synergistic objectives in a unified symbolic representation space: (i) mathematical formula-to-rule translation (KB), (ii) natural language-to-program synthesis (SOLVE), and (iii) program-answer alignment. This joint supervision enables positive transfer, where symbolic grounding in formula translation directly improves compositional reasoning capabilities. At inference, we introduce an execution-guided decoding pipeline with fine-grained error taxonomy that enables iterative program repair and quantifies model self-debugging capacity. Comprehensive evaluation on GSM8K across four model scales (3B--32B parameters) demonstrates consistent improvements: cocktail training achieves significant accuracy gains of +5.23\% (Qwen-32B, $p < 0.01$), +3.43\% (GPT-OSS-20B, $p < 0.01$), and +5.54\% (Llama-3B, $p < 0.05$) over single-task baselines.Systematic error analysis reveals scale-dependent learning dynamics: at 32B scale, cocktail training transforms unfixable type errors (12\% repair rate) into correctable domain errors (96\% repair rate), achieving 92.7\% overall correction; at 8B scale, the same training eliminates syntactic errors but introduces semantic failures, revealing a critical capacity threshold for type-safe symbolic reasoning.

