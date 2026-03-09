---
layout: default
title: Addressing the Ecological Fallacy in Larger LMs with Human Context
---

# Addressing the Ecological Fallacy in Larger LMs with Human Context
**arXiv**：[2603.05928v1](https://arxiv.org/abs/2603.05928) · [PDF](https://arxiv.org/pdf/2603.05928.pdf)  
**作者**：Nikita Soni, Dhruv Vijay Kunjadiya, Pratham Piyush Shah, Dikshya Mohanty, H. Andrew Schwartz, Niranjan Balasubramanian  

**一句话要点**：提出HuLM和HuFT方法，通过建模作者语言上下文解决大型语言模型中的生态谬误问题。

**关键词**：生态谬误, 作者上下文建模, HuLM预训练, HuFT微调, QLoRA优化, 大型语言模型

## 3 点简述
- 核心问题：语言模型训练忽略同一作者文本间的依赖关系，导致生态谬误。
- 方法要点：使用HuLM目标进行预训练，并在微调中引入作者上下文（HuFT），结合QLoRA优化。
- 实验或效果：在8B Llama模型上，HuFT提升性能，HuLM预训练模型在八个下游任务中表现更优。

## 摘要（原文）

> Language model training and inference ignore a fundamental linguistic fact -- there is a dependence between multiple sequences of text written by the same person. Prior work has shown that addressing this form of \textit{ecological fallacy} can greatly improve the performance of multiple smaller (~124M) GPT-based models. In this work, we ask if addressing the ecological fallacy by modeling the author's language context with a specific LM task (called HuLM) can provide similar benefits for a larger-scale model, an 8B Llama model. To this end, we explore variants that process an author's language in the context of their other temporally ordered texts. We study the effect of pre-training with this author context using the HuLM objective, as well as using it during fine-tuning with author context (\textit{HuFT:Human-aware Fine-Tuning}). Empirical comparisons show that addressing the ecological fallacy during fine-tuning alone using QLoRA improves the performance of the larger 8B model over standard fine-tuning. Additionally, QLoRA-based continued HuLM pre-training results in a human-aware model generalizable for improved performance over eight downstream tasks with linear task classifier training alone. These results indicate the utility and importance of modeling language in the context of its original generators, the authors.

