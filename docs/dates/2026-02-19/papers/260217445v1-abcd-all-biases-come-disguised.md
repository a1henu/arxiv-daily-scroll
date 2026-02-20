---
layout: default
title: ABCD: All Biases Come Disguised
---

# ABCD: All Biases Come Disguised
**arXiv**：[2602.17445v1](https://arxiv.org/abs/2602.17445) · [PDF](https://arxiv.org/pdf/2602.17445.pdf)  
**作者**：Mateusz Nowak, Xavier Cadet, Peter Chin  

**一句话要点**：提出无偏评估协议以减少LLM在多项选择题中的标签位置和少样本提示偏差

**关键词**：多项选择题评估, 偏差减少, 句子相似度模型, 无偏评估协议, LLM稳健性

## 3 点简述
- 核心问题：LLM在多项选择题评估中受标签位置、少样本提示分布等偏差影响，导致评估结果不稳健
- 方法要点：使用均匀无序标签替换原标签，结合句子相似度模型，减少评估中的提示和标签依赖
- 实验或效果：在多个基准和模型上，该方法显著降低答案排列的方差，平均性能下降最小

## 摘要（原文）

> Multiple-choice question (MCQ) benchmarks have been a standard evaluation practice for measuring LLMs' ability to reason and answer knowledge-based questions. Through a synthetic NonsenseQA benchmark, we observe that different LLMs exhibit varying degrees of label-position-few-shot-prompt bias, where the model either uses the answer position, the label in front of the answer, the distributions of correct answers present in the few-shot prompt, or a combination of all to answer each MCQ question. We propose a simple bias-reduced evaluation protocol that replaces the labels of each question with uniform, unordered labels and prompts the LLM to use the whole answer presented. With a simple sentence similarity model, we demonstrate improved robustness and lower standard deviation between different permutations of answers with a minimal drop in LLM's performance, exposing the LLM's capabilities under reduced evaluation artifacts, without any help from the prompt examples or the option labels. Across multiple benchmarks and models, this protocol substantially improves the robustness to answer permutations, reducing mean accuracy variance $3\times$ with only a minimal decrease in the mean model's performance. Through ablation studies on various embedding models and similarity functions, we show that the method is more robust than the standard ones.

