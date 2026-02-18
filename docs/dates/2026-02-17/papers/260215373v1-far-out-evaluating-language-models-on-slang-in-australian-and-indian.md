---
layout: default
title: Far Out: Evaluating Language Models on Slang in Australian and Indian English
---

# Far Out: Evaluating Language Models on Slang in Australian and Indian English
**arXiv**：[2602.15373v1](https://arxiv.org/abs/2602.15373) · [PDF](https://arxiv.org/pdf/2602.15373.pdf)  
**作者**：Deniz Kaya Dilsiz, Dipankar Srirag, Aditya Joshi  

**一句话要点**：评估语言模型对澳大利亚和印度英语俚语的理解能力，揭示生成与判别能力的不对称性。

**关键词**：语言模型评估, 俚语理解, 非标准语言变体, 澳大利亚英语, 印度英语, 生成与判别能力

## 3 点简述
- 核心问题：语言模型在处理非标准语言变体（如俚语）时存在性能差距，尤其在澳大利亚和印度英语中。
- 方法要点：构建两个互补数据集（Web和Gen），评估七种先进模型在目标词预测和选择任务上的表现。
- 实验效果：发现模型在判别任务上表现更佳，且对印度英语俚语的理解优于澳大利亚英语，突显生成与判别能力的不对称。

## 摘要（原文）

> Language models exhibit systematic performance gaps when processing text in non-standard language varieties, yet their ability to comprehend variety-specific slang remains underexplored for several languages. We present a comprehensive evaluation of slang awareness in Indian English (en-IN) and Australian English (en-AU) across seven state-of-the-art language models. We construct two complementary datasets: \textsc{web}, containing 377 web-sourced usage examples from Urban Dictionary, and \textsc{gen}, featuring 1,492 synthetically generated usages of these slang terms, across diverse scenarios. We assess language models on three tasks: target word prediction (TWP), guided target word prediction (TWP$^*$) and target word selection (TWS). Our results reveal four key findings: (1) Higher average model performance TWS versus TWP and TWP$^*$, with average accuracy score increasing from 0.03 to 0.49 respectively (2) Stronger average model performance on \textsc{web} versus \textsc{gen} datasets, with average similarity score increasing by 0.03 and 0.05 across TWP and TWP$^*$ tasks respectively (3) en-IN tasks outperform en-AU when averaged across all models and datasets, with TWS demonstrating the largest disparity, increasing average accuracy from 0.44 to 0.54. These findings underscore fundamental asymmetries between generative and discriminative competencies for variety-specific language, particularly in the context of slang expressions despite being in a technologically rich language such as English.

