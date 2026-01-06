---
layout: default
title: DeCode: Decoupling Content and Delivery for Medical QA
---

# DeCode: Decoupling Content and Delivery for Medical QA
**arXiv**：[2601.02123v1](https://arxiv.org/abs/2601.02123) · [PDF](https://arxiv.org/pdf/2601.02123.pdf)  
**作者**：Po-Jen Ko, Chen-Han Tsai, Yu-Shao Peng  

**一句话要点**：提出DeCode框架，以解耦内容与传递，提升大语言模型在临床问答中的个性化响应能力。

**关键词**：医疗问答, 大语言模型, 上下文适应, 模型无关框架, 临床评估

## 3 点简述
- 核心问题：现有大语言模型在医疗问答中常忽略患者个体情境，导致答案临床正确但实用性不足。
- 方法要点：DeCode为无需训练、模型无关的框架，通过解耦内容与传递来适应临床环境，生成上下文化答案。
- 实验或效果：在OpenAI HealthBench基准上，DeCode将最佳性能从28.4%提升至49.8%，相对改进75%。

## 摘要（原文）

> Large language models (LLMs) exhibit strong medical knowledge and can generate factually accurate responses. However, existing models often fail to account for individual patient contexts, producing answers that are clinically correct yet poorly aligned with patients' needs. In this work, we introduce DeCode, a training-free, model-agnostic framework that adapts existing LLMs to produce contextualized answers in clinical settings. We evaluate DeCode on OpenAI HealthBench, a comprehensive and challenging benchmark designed to assess clinical relevance and validity of LLM responses. DeCode improves the previous state of the art from $28.4\%$ to $49.8\%$, corresponding to a $75\%$ relative improvement. Experimental results suggest the effectiveness of DeCode in improving clinical question answering of LLMs.

